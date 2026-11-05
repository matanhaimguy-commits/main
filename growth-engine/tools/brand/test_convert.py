"""Tests for brand/convert.py and mapping.py."""
import unittest

from brand import convert
from brand.mapping import FIELDS


class Convert(unittest.TestCase):
    def test_every_field_has_a_converter_or_is_proof(self):
        for field, (path, kind) in FIELDS.items():
            self.assertTrue(kind == "proof" or kind in convert.CONVERTERS, field)
        self.assertEqual(set(FIELDS), {"offer", "icp", "promise", "mechanism", "voice", "never_say", "proof_bank",
                                       "cta_keyword", "monthly_cap_usd", "cadence"})

    def test_lists(self):
        self.assertEqual(convert.list_commas("warm, direct\n- plain"), ["warm", "direct", "plain"])
        self.assertEqual(convert.list_lines("no prices, ever\n* no medical claims"), ["no prices, ever", "no medical claims"])
        self.assertEqual(convert.list_lines(["a", " b "]), ["a", "b"])
        with self.assertRaises(ValueError):
            convert.list_lines("  \n ")
        with self.assertRaises(ValueError):
            convert.list_lines([1])

    def test_numbers(self):
        self.assertEqual(convert.usd("120"), 120.0)
        self.assertEqual(convert.usd(80), 80)
        self.assertIsNone(convert.usd(None))
        for bad in (-1, True, "lots"):
            with self.assertRaises(ValueError):
                convert.usd(bad)
        self.assertEqual(convert.count("4"), 4)
        for bad in (0, 30, 2.5, "4 a week", True):
            with self.assertRaises(ValueError):
                convert.count(bad)

    def test_text_and_keyword(self):
        self.assertEqual(convert.text("  x "), "x")
        with self.assertRaises(ValueError):
            convert.text("")
        self.assertEqual(convert.keyword("LOAF"), "LOAF")
        with self.assertRaises(ValueError):
            convert.keyword("two words")
