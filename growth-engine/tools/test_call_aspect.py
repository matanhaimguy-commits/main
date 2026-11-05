"""Tests for call_aspect.py: python3 -m unittest test_call_aspect (from growth-engine/tools)."""
import unittest
from fractions import Fraction

from call_aspect import mismatch, ratio

GPT_SIZES = {"9:16": ["1152x2048"], "4:5": ["1024x1536"], "1:1": ["1024x1024"]}


class Ratio(unittest.TestCase):
    def test_reads_colon_and_size(self):
        self.assertEqual(ratio("9:16"), Fraction(9, 16))
        self.assertEqual(ratio("1152x2048"), Fraction(9, 16))
        self.assertEqual(ratio("1080X1350"), Fraction(4, 5))

    def test_anything_else_is_none(self):
        for v in ("adaptive", None, 916, "0:16", "9:16:1", ""):
            self.assertIsNone(ratio(v), v)


class Mismatch(unittest.TestCase):
    def test_ratio_and_aspect_ratio_match_by_value(self):
        self.assertEqual(mismatch({"ratio": "9:16"}, "9:16"), [])
        self.assertEqual(mismatch({"aspect_ratio": "4:5"}, "4:5"), [])
        self.assertIn("ratio 1:1 differs", mismatch({"ratio": "1:1"}, "9:16")[0])
        self.assertIn("ratio adaptive differs", mismatch({"ratio": "adaptive"}, "9:16")[0])

    def test_size_compares_its_ratio(self):
        self.assertEqual(mismatch({"size": "1152x2048"}, "9:16"), [])
        self.assertIn("size 1024x1024 differs", mismatch({"size": "1024x1024"}, "9:16")[0])

    def test_size_for_aspect_names_the_sizes(self):
        self.assertEqual(mismatch({"size": "1024x1536"}, "4:5", GPT_SIZES), [])
        self.assertEqual(mismatch({"size": "1152x2048"}, "9:16", GPT_SIZES), [])
        self.assertIn("makes 4:5 at 1024x1536", mismatch({"size": "1152x2048"}, "4:5", GPT_SIZES)[0])
        self.assertIn("no size", mismatch({"size": "1024x1536"}, "3:4", GPT_SIZES)[0])

    def test_every_shape_key_given_must_match(self):
        self.assertEqual(len(mismatch({"ratio": "9:16", "aspect_ratio": "1:1"}, "9:16")), 1)

    def test_no_shape_key(self):
        self.assertIn("no aspect_ratio, ratio or size", mismatch({}, "9:16")[0])


if __name__ == "__main__":
    unittest.main()
