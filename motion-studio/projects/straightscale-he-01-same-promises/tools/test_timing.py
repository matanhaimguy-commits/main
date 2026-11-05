#!/usr/bin/env python3
"""Tests for the timing tools (run: python3 tools/test_timing.py)."""
import unittest

from retime import fill, match
from timing_scratch import spread
from timing_lib import script_lines


class TimingTools(unittest.TestCase):
    def test_script_has_twelve_lines_and_91_words(self):
        lines = script_lines()
        self.assertEqual(len(lines), 12)
        self.assertEqual(sum(len(text.split()) for _, text, _, _ in lines), 91)

    def test_spread_stays_inside_its_line(self):
        words = spread("רק שואלים אתכם מחיר? זה כנראה מתחיל כבר במודעה.", 0.0, 3.8)
        self.assertEqual(words[0]["s"], 0.0)
        self.assertLess(words[-1]["e"], 3.8)
        self.assertTrue(all(a["s"] < b["s"] for a, b in zip(words, words[1:])))

    def test_match_ignores_punctuation_and_skips_extra_words(self):
        script = ["רק", "שואלים", "מחיר?"]
        voice = [{"w": "רק"}, {"w": "אממ"}, {"w": "שואלים"}, {"w": "מחיר"}]
        self.assertEqual(match(script, voice), [0, 2, 3])

    def test_fill_interpolates_a_missing_word(self):
        out = fill([(0.0, 0.3), None, (1.0, 1.2)])
        self.assertTrue(0.3 <= out[1][0] < 1.0)


if __name__ == "__main__":
    unittest.main()
