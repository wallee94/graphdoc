from typing import Union

import graphql

import definitions


def build_types_reference(
        schema: Union[str, graphql.GraphQLSchema]
) -> definitions.TypeMapReference:
    """
    Parse schema string to a TypeMapReference instance with definition from the schema
    :param schema: GraphQL API schema
    :return: definitions.TypeMapReference: map with definitions from schema
    """
    # parse schema to ast obj and filter out native graphql types
    document_ast = graphql.parse(schema)
    defs = [definition.name.value for definition in document_ast.definitions]
    if isinstance(schema, str):
        schema = graphql.utilities.build_ast_schema(document_ast)

    type_map = {k: v for k, v in schema.type_map.items() if k in defs}

    # parse the different type definitions in the schema
    reference = definitions.TypeMapReference()
    for name, obj in type_map.items():
        # This is a long if-elif chain, but graphql has only 6 different
        # types in the specs, so it won't grow bigger soon
        if isinstance(obj, graphql.GraphQLObjectType):
            if name == 'Query':
                reference.query = obj
            elif name == 'Mutation':
                reference.mutation = obj
            else:
                reference.objects.append(obj)

        elif isinstance(obj, graphql.GraphQLScalarType):
            reference.scalars.append(obj)

        elif isinstance(obj, graphql.GraphQLInterfaceType):
            reference.interfaces.append(obj)

        elif isinstance(obj, graphql.GraphQLUnionType):
            reference.unions.append(obj)

        elif isinstance(obj, graphql.GraphQLEnumType):
            reference.enums.append(obj)

        elif isinstance(obj, graphql.GraphQLInputObjectType):
            reference.input_objects.append(obj)

    return reference
