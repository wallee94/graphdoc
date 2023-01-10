import os

import graphql

SCHEMA = None
graphql_version = 3
path = os.path.join(os.path.dirname(__file__), '../files')
for filename in ['sw-schema-3.graphql', 'sw-schema-2.graphql']:
    with open(os.path.join(path, filename), 'r') as _f:
        SCHEMA = _f.read()
        try:
            graphql.parse(SCHEMA)
            break
        except graphql.error.syntax_error.GraphQLSyntaxError:
            graphql_version = 2
            continue

if SCHEMA is None:
    raise ValueError("Couldn't find a valid schema file")
