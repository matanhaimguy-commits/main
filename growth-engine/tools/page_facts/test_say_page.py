"""Tests for say_page.py: page basics and JSON-LD lines, "missing" when absent."""
import unittest

import testbase  # noqa: F401
from page_facts.say_page import section

EMPTY = {"title": None, "meta_description": None, "h1": [], "canonical": None, "lang": None, "viewport": None, "og": {}}


class SayPage(unittest.TestCase):
    def test_missing_values_say_missing(self):
        self.assertEqual(section({"basics": EMPTY, "jsonld": {"types": [], "blocks": 0, "invalid_blocks": 0}}), [
            "## Page basics", "- Title: missing", "- Meta description: missing", "- H1: none", "- Canonical: missing",
            "- Language (html lang): missing", "- Viewport: missing", "- Open Graph: none", "- JSON-LD: none"])

    def test_present_values(self):
        basics = dict(EMPTY, title="Acme", h1=["One", ""], og={"og:title": "A", "og:image": "i.jpg"})
        lines = section({"basics": basics, "jsonld": {"types": ["Plumber"], "blocks": 2, "invalid_blocks": 1}})
        self.assertEqual((lines[1], lines[3], lines[7], lines[8]), ('- Title: "Acme"', '- H1 (2): "One"; (empty)',
                                                                    "- Open Graph: og:title, og:image",
                                                                    "- JSON-LD types: Plumber (2 blocks, 1 not valid JSON)"))


if __name__ == "__main__":
    unittest.main()
