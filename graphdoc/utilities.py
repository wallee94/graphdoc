from collections import defaultdict
from typing import Union

import graphql

from . import definitions


def unwrap_field_type(
        field_type: graphql.GraphQLOutputType
) -> graphql.GraphQLOutputType:
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
        schema = graphql.utilities.build_ast_schema(document_ast)

    type_map = {
        k: v for k, v in sorted(schema.type_map.items(), key=lambda t: t[1].name)
        if not k.startswith('__')
    }

    # separate the different type definitions in the schema
    reference = definitions.TypeMapReference()
    reference.query = schema.query_type
    reference.mutation = schema.mutation_type
    if reference.mutation:
        for name, field in reference.mutation.fields.items():
            setattr(field, 'unwrapped_type', unwrap_field_type(field.type))

    implemented_by = defaultdict(list)
    for name, obj in type_map.items():
        # This is a long if-elif chain, but graphql has only 6 different
        # types in the specs, so it won't grow bigger soon
        if graphql.is_object_type(obj):
            if obj != reference.query and obj != reference.mutation:
                reference.objects.append(obj)
                for interface in obj.interfaces:
                    implemented_by[interface.name].append(obj)

        elif graphql.is_scalar_type(obj):
            reference.scalars.append(obj)

        elif graphql.is_interface_type(obj):
            reference.interfaces.append(obj)

        elif graphql.is_union_type(obj):
            reference.unions.append(obj)

        elif graphql.is_enum_type(obj):
            reference.enums.append(obj)

        elif graphql.is_input_object_type(obj):
            reference.input_objects.append(obj)

    for interface in reference.interfaces:
        setattr(interface, 'implemented_by', implemented_by[interface.name])

    return reference
