"""Tests for jsonld.py: @type values, @graph and nested items, and invalid blocks counted."""
import unittest

from testbase import doc
from page_facts.htmldoc import parse
from page_facts.jsonld import types


class JsonLd(unittest.TestCase):
    def test_types_from_graph_nested_and_lists(self):
        self.assertEqual(types(doc("pixel_gtm_form.html")),
                         {"types": ["Plumber", "PostalAddress", "WebSite", "Thing"], "blocks": 2, "invalid_blocks": 1})

    def test_no_blocks_and_other_script_types(self):
        self.assertEqual(types(parse('<script type="application/json">{"@type": "X"}</script>')),
                         {"types": [], "blocks": 0, "invalid_blocks": 0})
        self.assertEqual(types(parse('<script type="Application/LD+JSON; charset=utf-8">[{"@type": "Organization"}]</script>'))["types"],
                         ["Organization"])


if __name__ == "__main__":
    unittest.main()
