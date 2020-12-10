from dataclasses import dataclass, field
from typing import List

import graphql


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
