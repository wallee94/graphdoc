import graphene


class Query(graphene.ObjectType):
    cities = graphene.List(graphene.String)

    def resolve_cities(self, info):
        return ['Mexico City', 'New York', 'San Francisco']


schema = graphene.Schema(query=Query)
