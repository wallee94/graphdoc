from functools import lru_cache
from typing import Union

import graphql
from jinja2 import (
    Environment,
    ChoiceLoader,
    FileSystemLoader,
    PackageLoader,
    select_autoescape
)

from . import filters
from . import utilities

_jinja_env = Environment(
    loader=PackageLoader('graphdoc', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
)
_jinja_env.filters['slugify'] = filters.slugify
_jinja_env.filters['markdown'] = filters.markdown
_jinja_env.filters['gql_group'] = filters.gql_group


@lru_cache(maxsize=50)
def _to_doc(schema, templates_path=None) -> str:
    if templates_path is not None:
        _jinja_env.loader = ChoiceLoader([
            FileSystemLoader(templates_path),
            _jinja_env.loader
        ])

    reference = utilities.build_types_reference(schema)
    return _jinja_env.get_template('index.html').render(reference=reference)


def to_doc(
        schema: Union[str, graphql.GraphQLSchema],
        templates_path: str = None,
        use_cache=True
) -> str:
    """
    Returns an html with the documentation from the schema
    """
    if use_cache is True:
        return _to_doc(schema, templates_path)
    return _to_doc.__wrapped__(schema, templates_path)
