import os
from unittest import TestCase, mock

import graphdoc

path = os.path.join(os.path.dirname(__file__), 'files', 'sw-schema.graphql')
with open(path, 'r') as f:
    SCHEMA = f.read()


class ToDocTest(TestCase):
    def test_pass_context_with_cache(self):
        context = {
            'custom': 'key',
            'list': [1, 2, 3]
        }
        with self.assertRaises(ValueError):
            graphdoc.to_doc(SCHEMA, context=context)

    @mock.patch('graphdoc.render._jinja_env')
    def test_pass_context_to_template(self, mock_jinja_env):
        context = {
            'custom': 'key',
            'list': [1, 2, 3]
        }
        graphdoc.to_doc(SCHEMA, use_cache=False, context=context)

        m_get_template = mock_jinja_env.get_template.return_value
        kw = m_get_template.render.call_args.kwargs
        self.assertIn('reference', kw)

        self.assertEqual(kw['custom'], context['custom'])
        self.assertEqual(kw['list'], context['list'])
