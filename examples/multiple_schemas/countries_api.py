import graphene


class Query(graphene.ObjectType):
    countries = graphene.List(graphene.String)

    def resolve_countries(self, info):
        return ['Canada', 'France', 'Mexico']


schema = graphene.Schema(query=Query)
