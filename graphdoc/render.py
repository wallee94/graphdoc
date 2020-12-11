from typing import Union, Optional

import graphql
from jinja2 import Environment, PackageLoader, select_autoescape

from . import filters
from . import utilities

_template_name = 'graphql-docs.html'
about_description_default = """
### About GraphQL

The [GraphQL](https://graphql.github.io/) data query language is:

- **A [specification](http://spec.graphql.org/June2018/)**. The spec determines the 
validity of the schema on the API server. The schema determines the validity of 
client calls.

- **Strongly typed**. The schema defines an API's type system and all object relationships.

- **Introspective**. A client can query the schema for details about the schema.

- **Hierarchical**. The shape of a GraphQL call mirrors the shape of the JSON data it
returns. Nested fields let you query for and receive only the data you specify in a
single round trip.

- **An application layer**. GraphQL is not a storage model or a database query language. 
The graph refers to graph structures defined in the schema, where nodes define objects 
and edges define relationships between objects. The API traverses and returns 
application data based on the schema definitions, independent of how the data is stored.
"""
_jinja_env = Environment(
    loader=PackageLoader('graphdoc', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=True
)
_jinja_env.filters['slugify'] = filters.slugify
_jinja_env.filters['markdown'] = filters.markdown
_jinja_env.filters['gql_group'] = filters.gql_group


def to_doc(
        schema: Union[str, graphql.GraphQLSchema],
        html_title: str = 'GraphQL API Documentation',
        api_about: Optional[str] = None
) -> str:
    """
    Returns an html with the documentation from the schema
    """
    reference = utilities.build_types_reference(schema)
    html = _jinja_env.get_template(_template_name).render(
        reference=reference,
        title=html_title,
        about_description=api_about,
        about_description_default=about_description_default,
    )
    return html


async def to_doc_async(
        schema: Union[str, graphql.GraphQLSchema],
        html_title: str = 'GraphQL API Documentation',
        api_about: Optional[str] = None
) -> str:
    """
    Returns an html with the documentation from the schema using
    jinja's asyncio implementation
    """
    reference = utilities.build_types_reference(schema)
    html = await _jinja_env.get_template(_template_name).render_async(
        reference=reference,
        title=html_title,
        about_description=api_about,
        about_description_default=about_description_default,
    )
    return html
