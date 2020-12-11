import os
from unittest import TestCase

from graphdoc.utilities import build_types_reference

with open(os.path.join(os.path.dirname(__file__), 'sw-schema.graphql'), 'r') as f:
    SCHEMA = f.read()


class BuildTypesReference(TestCase):
    def test_finds_query(self):
        ref = build_types_reference(SCHEMA)
        self.assertNotEqual(None, ref.query)
        self.assertEqual('Root', ref.query.name)

    def test_finds_objects_without_query_nor_mutation(self):
        ref = build_types_reference(SCHEMA)
        self.assertEqual(53, len(ref.objects))

    def test_finds_enums(self):
        ref = build_types_reference(SCHEMA)
        self.assertEqual(1, len(ref.enums))

    def test_finds_interfaces(self):
        ref = build_types_reference(SCHEMA)
        self.assertEqual(1, len(ref.interfaces))

    def test_finds_unions(self):
        ref = build_types_reference(SCHEMA)
        self.assertEqual(1, len(ref.unions))

    def test_finds_scalars(self):
        ref = build_types_reference(SCHEMA)
        self.assertEqual(7, len(ref.scalars))

    def test_finds_input_objects(self):
        ref = build_types_reference(SCHEMA)
        self.assertEqual(1, len(ref.input_objects))
