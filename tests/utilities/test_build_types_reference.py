from unittest import TestCase

with open('sw-schema.graphql', 'r') as f:
    SCHEMA = f.read()


class BuildTypesReference(TestCase):
    def test_finds_query(self):
        pass

    def test_finds_mutation(self):
        pass

    def test_finds_objects_without_query_nor_mutation(self):
        pass

    def test_finds_enums(self):
        pass

    def test_finds_interfaces(self):
        pass

    def test_finds_unions(self):
        pass

    def test_finds_scalars(self):
        pass

    def test_finds_input_objects(self):
        pass
