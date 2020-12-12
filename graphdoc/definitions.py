from dataclasses import dataclass, field
from typing import List, Any

import graphql


class GraphQLField:
    """Composition to add unwrapped_field to graphql.GraphQLField. GraphQLField uses
    slots, so we cannot just set the attr """
    unwrapped_type: graphql.GraphQLObjectType = None
    _graphql_field: graphql.GraphQLField

    def __init__(self, g_field) -> None:
        self._graphql_field = g_field

    def __getattr__(self, name: str) -> Any:
        return getattr(self._graphql_field, name)


@dataclass
class TypeMapReference:
    """Stores the different types found in a schema"""
    query: graphql.GraphQLObjectType = None
    mutation: graphql.GraphQLObjectType = None

    objects: List[graphql.GraphQLObjectType] = field(default_factory=list)
    interfaces: List[graphql.GraphQLInterfaceType] = field(default_factory=list)
    unions: List[graphql.GraphQLUnionType] = field(default_factory=list)
    scalars: List[graphql.GraphQLScalarType] = field(default_factory=list)
    input_objects: List[graphql.GraphQLInputObjectType] = field(default_factory=list)
    enums: List[graphql.GraphQLEnumType] = field(default_factory=list)
