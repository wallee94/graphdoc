import re
import unicodedata

from markdown2 import Markdown
import graphql
from .utilities import unwrap_field_type

markdowner = Markdown()


def gql_group(value) -> str:
    value = unwrap_field_type(value)
    if graphql.is_object_type(value):
        return 'objects'
    elif graphql.is_scalar_type(value):
        return 'scalars'
    elif graphql.is_interface_type(value):
        return 'interfaces'
    elif graphql.is_union_type(value):
        return 'unions'
    elif graphql.is_enum_type(value):
        return 'enums'
    elif graphql.is_input_object_type(value):
        return 'input-objects'
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
