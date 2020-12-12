from typing import Union

import graphql
from jinja2 import Environment, PackageLoader, select_autoescape

from . import filters
from . import utilities
from .configs import default_config

_template_name = 'graphql-docs.html'
_jinja_env = Environment(
    loader=PackageLoader('graphdoc', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
)
_jinja_env.filters['slugify'] = filters.slugify
_jinja_env.filters['markdown'] = filters.markdown
_jinja_env.filters['gql_group'] = filters.gql_group


def to_doc(
        schema: Union[str, graphql.GraphQLSchema],
        **configs
) -> str:
    """
    Returns an html with the documentation from the schema
    """
    configs = {**default_config, **configs}
    reference = utilities.build_types_reference(schema)
    html = _jinja_env.get_template(_template_name).render(
        reference=reference,
        configs=configs
    )
    return html
