"""Tests for intake/required.py: O1's gate."""
import unittest

from intake import questions, required
from intake.testbase import sample

QS = questions.load()


class Required(unittest.TestCase):
    def ids(self, answers, files=None):
        return [m["id"] for m in required.missing(answers, QS, files)]

    def test_the_sample_is_complete(self):
        s = sample()
        self.assertEqual(self.ids(s["answers"], s["files"]), [])

    def test_empty_intake_misses_every_required_answer(self):
        got = self.ids({})
        self.assertTrue({"A1", "A3", "A4", "B2", "G1", "H1", "H2", "D5"} <= set(got))

    def test_i_dont_know_passes_only_where_allowed(self):
        a = {**sample()["answers"], "B2": "I don't know", "A4": "I don't know"}
        self.assertEqual(self.ids(a), ["A4"])

    def test_links_need_a_website_or_an_instagram(self):
        a = {**sample()["answers"], "A3": {"website": "", "facebook": "https://fb.example/x"}}
        self.assertEqual(self.ids(a), ["A3"])

    def test_empty_values_do_not_count(self):
        a = {**sample()["answers"], "H2": [], "A1": "  "}
        self.assertEqual(sorted(self.ids(a)), ["A1", "H2"])


if __name__ == "__main__":
    unittest.main()
