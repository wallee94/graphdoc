from unittest import TestCase

import graphene

from graphdoc.utilities import build_types_reference


class Options(graphene.Enum):
    ONE = '1'
    TWO = '2'


class Query(graphene.ObjectType):
    all_data = graphene.List(Options)

    def resolve_all_data(self, info, **kwargs):
        return []


schema = graphene.Schema(query=Query)


class UtilitiesTest(TestCase):
    def test_build_types_reference(self):
        res = build_types_reference(schema)
        self.assertEqual(len(res.scalars), 2)

        self.assertEqual(len(res.enums), 1)
        self.assertEqual(res.enums[0].name, 'Options')
        self.assertTrue(isinstance(res.enums[0].values, dict))
        self.assertIn('ONE', res.enums[0].values)
        self.assertIn('TWO', res.enums[0].values)

        self.assertTrue(isinstance(res.query.fields, dict))
        self.assertIn('allData', res.query.fields)
