import os
from unittest import TestCase, mock

import graphdoc
from . import SCHEMA, path, graphql_version


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

    def test_html_result(self):
        with open(os.path.join(path, f"expected-{graphql_version}.html"), "r") as f:
            want = f.read()
        got = graphdoc.to_doc(SCHEMA, use_cache=False)
        self.assertEqual(got, want)

    def test_md_result(self):
        with open(os.path.join(path, f"expected-{graphql_version}.md"), "r") as f:
            want = f.read()
        got = graphdoc.to_md(SCHEMA, use_cache=False)
        self.assertEqual(got, want)
