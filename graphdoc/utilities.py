from typing import Union

import graphql
from jinja2 import Environment, PackageLoader, select_autoescape

from . import definitions

_template_name = 'graphql-docs.html'
_jinja_env = Environment(
    loader=PackageLoader('graphdoc', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=True
)


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
    defs = [
        definition.name.value
        for definition in document_ast.definitions
        if not isinstance(definition, graphql.SchemaDefinitionNode)
    ]
    if isinstance(schema, str):
        schema = graphql.utilities.build_ast_schema(document_ast)

    type_map = {k: v for k, v in schema.type_map.items() if k in defs}

    # parse the different type definitions in the schema
    reference = definitions.TypeMapReference()
    reference.query = schema.query_type
    reference.mutation = schema.mutation_type
    for name, obj in type_map.items():
        # This is a long if-elif chain, but graphql has only 6 different
        # types in the specs, so it won't grow bigger soon
        if isinstance(obj, graphql.GraphQLObjectType):
            if obj != reference.query and obj != reference.mutation:
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


def to_doc(schema: Union[str, graphql.GraphQLSchema]) -> str:
    """
    Returns an html with the documentation from the schema
    """
    reference = build_types_reference(schema)
    html = _jinja_env.get_template(_template_name).render(reference=reference)
    return html


async def to_doc_async(schema: Union[str, graphql.GraphQLSchema]) -> str:
    """
    Returns an html with the documentation from the schema using
    jinja's asyncio implementation
    """
    reference = build_types_reference(schema)
    html = await _jinja_env.get_template(_template_name).render_async(
        reference=reference
    )
    return html
