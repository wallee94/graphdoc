from collections import defaultdict, namedtuple
from typing import Union

import graphql

try:
    # graphql-core>=3.1.0,<4
    from graphql.utilities import build_ast_schema
except ImportError:
    # graphql-core>=2.1.0,<3
    from graphql.utils.build_ast_schema import build_ast_schema

from . import definitions

GraphQLEnumValue = namedtuple('GraphQLEnumValue', ('name', 'values'))


def unwrap_field_type(
        field_type: graphql.type.definition.GraphQLOutputType
) -> graphql.type.definition.GraphQLOutputType:
    """
    Unwraps field type from NonNull and List GraphQL type wrappers
    """
    while isinstance(field_type, (graphql.GraphQLNonNull, graphql.GraphQLList)):
        field_type = field_type.of_type
    return field_type


def build_types_reference(
        schema: Union[str, graphql.GraphQLSchema]
) -> definitions.TypeMapReference:
    """
    Parse schema string to a TypeMapReference instance with definition from the schema
    :param schema: GraphQL API schema
    :return: definitions.TypeMapReference: map with definitions from schema
    """
    # parse schema to ast obj and filter out native graphql types
    if isinstance(schema, str):
        document_ast = graphql.parse(schema)
        schema = build_ast_schema(document_ast)

    # graphql-core>=3.1.0,<4 has a type_map attr, but graphql-core>=2.1.0,<3
    # uses get_type_map
    type_map = schema.type_map if hasattr(schema, 'type_map') else schema.get_type_map()
    type_map = {
        k: v for k, v in sorted(type_map.items(), key=lambda t: t[1].name)
        if not k.startswith('__')
    }

    # separate the different type definitions in the schema
    reference = definitions.TypeMapReference()
    if hasattr(schema, 'query_type') and hasattr(schema, 'mutation_type'):
        # graphql-core>=3.1.0,<4
        reference.query = schema.query_type
        reference.mutation = schema.mutation_type
    else:
        # graphql-core>=2.1.0,<3
        reference.query = schema.get_query_type()
        reference.mutation = schema.get_mutation_type()

    if reference.mutation:
        for name, field in reference.mutation.fields.items():
            # Wrap all mutation fields to set the unwrapped_type attr
            unwrapped_type = unwrap_field_type(field.type)
            wrapper = definitions.GraphQLField(field)
            wrapper.unwrapped_type = unwrapped_type
            reference.mutation.fields[name] = wrapper

    implemented_by = defaultdict(list)
    for name, obj in type_map.items():
        # This is a long if-elif chain, but graphql has only 6 different
        # types in the specs, so it won't grow bigger soon
        if isinstance(obj, graphql.GraphQLObjectType):
            if obj != reference.query and obj != reference.mutation:
                reference.objects.append(obj)
                for interface in obj.interfaces:
                    implemented_by[interface.name].append(obj)

        elif isinstance(obj, graphql.GraphQLScalarType):
            reference.scalars.append(obj)

        elif isinstance(obj, graphql.GraphQLInterfaceType):
            reference.interfaces.append(obj)

        elif isinstance(obj, graphql.GraphQLUnionType):
            reference.unions.append(obj)

        elif isinstance(obj, graphql.GraphQLEnumType):
            if isinstance(obj.values, list):
                # graphql-core>=2.1.0,<3
                obj = GraphQLEnumValue(obj.name, {v.name: v for v in obj.values})
            reference.enums.append(obj)

        elif isinstance(obj, graphql.GraphQLInputObjectType):
            reference.input_objects.append(obj)

    for interface in reference.interfaces:
        setattr(interface, 'implemented_by', implemented_by[interface.name])

    return reference
