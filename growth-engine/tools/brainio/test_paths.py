"""Tests for brainio/paths.py and unknown.py."""
import unittest

from brainio import paths
from brainio.unknown import is_placeholder, is_unknown


class Paths(unittest.TestCase):
    def test_get_nested_and_indexed(self):
        b = {"offer": {"main_offer": "x"}, "avatars": [{"situation": "s"}]}
        self.assertEqual(paths.get(b, "offer.main_offer"), "x")
        self.assertEqual(paths.get(b, "avatars[0].situation"), "s")
        self.assertIsNone(paths.get(b, "avatars[1].situation"))
        self.assertIsNone(paths.get(b, "voice.language"))

    def test_set_creates_dicts_and_the_next_list_item(self):
        b = {}
        paths.set_(b, "package.posts_per_week", 4)
        paths.set_(b, "avatars[0].situation", "s")
        self.assertEqual(b, {"package": {"posts_per_week": 4}, "avatars": [{"situation": "s"}]})
        with self.assertRaises(ValueError):
            paths.set_(b, "avatars[5].situation", "s")

    def test_bad_path(self):
        with self.assertRaises(ValueError):
            paths.steps("a..b")

    def test_unknown_convention(self):
        self.assertTrue(is_unknown("unknown: the price"))
        self.assertTrue(is_unknown(None) and is_unknown("") and is_unknown([]))
        self.assertFalse(is_unknown("a bakery"))
        self.assertTrue(is_placeholder(["unknown: a", "unknown: b"]))
        self.assertFalse(is_placeholder(["unknown: a", "real"]))
