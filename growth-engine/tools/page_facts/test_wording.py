"""Tests for wording.py: the shared phrases."""
import unittest

import testbase  # noqa: F401
from page_facts.wording import page_read, plural, quote, where_read


class Wording(unittest.TestCase):
    def test_phrases(self):
        self.assertEqual((plural(1, "URL"), plural(0, "URL")), ("1 URL", "0 URLs"))
        self.assertEqual((quote(None), quote("ab"), quote("abcdef", 4)), ("missing", '"ab"', '"abc…"'))
        self.assertEqual((where_read({"mode": "static"}), page_read({"mode": "rendered"})), ("the page's HTML", "the rendered page"))


if __name__ == "__main__":
    unittest.main()
