from functools import lru_cache
from typing import Optional, Union

import graphql
from jinja2 import (
    ChoiceLoader,
    Environment,
    FileSystemLoader,
    PackageLoader,
    select_autoescape
)

from . import filters, utilities

_jinja_env = Environment(
    loader=PackageLoader('graphdoc', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
)
_jinja_env.filters['slugify'] = filters.slugify
_jinja_env.filters['markdown'] = filters.markdown
_jinja_env.filters['gql_group'] = filters.gql_group


@lru_cache(maxsize=50)
def _to_doc(schema, templates_path=None, context=None) -> str:
    if templates_path is not None:
        _jinja_env.loader = ChoiceLoader([
            FileSystemLoader(templates_path),
            _jinja_env.loader
        ])

    context = context or {}
    reference = utilities.build_types_reference(schema)
    return _jinja_env.get_template('index.html').render(reference=reference, **context)


def to_doc(
        schema: Union[str, graphql.GraphQLSchema],
        templates_path: str = None,
        context: Optional[dict] = None,
        use_cache=True
) -> str:
    """
    Returns an html with the documentation from the schema
    """
    if context is not None and use_cache:
        raise ValueError('use_cache must be False if context is not None')
    if use_cache is True:
        return _to_doc(schema, templates_path, context)
    return _to_doc.__wrapped__(schema, templates_path, context)
