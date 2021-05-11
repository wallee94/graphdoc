import re
import unicodedata

import graphql
from markdown2 import Markdown

from .utilities import unwrap_field_type

markdowner = Markdown()


def gql_group(value) -> str:
    value = unwrap_field_type(value)
    if isinstance(value, graphql.GraphQLObjectType):
        return 'objects'
    elif isinstance(value, graphql.GraphQLScalarType):
        return 'scalars'
    elif isinstance(value, graphql.GraphQLInterfaceType):
        return 'interfaces'
    elif isinstance(value, graphql.GraphQLUnionType):
        return 'unions'
    elif isinstance(value, graphql.GraphQLEnumType):
        return 'enums'
    elif isinstance(value, graphql.GraphQLInputObjectType):
        return 'io'
    return ''


def markdown(value):
    return markdowner.convert(value)


def slugify(value):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    value = str(value)
    value = unicodedata.normalize('NFKD', value)
    value = value.encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)
