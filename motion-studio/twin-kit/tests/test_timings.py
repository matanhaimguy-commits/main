import json
import tempfile
import unittest
from pathlib import Path

from helpers import EXAMPLE
from kit import timings

W = [{"w": "Two", "s": 0.0, "e": 0.2}, {"w": "years,", "s": 0.2, "e": 0.5},
     {"w": "We", "s": 1.0, "e": 1.1}, {"w": "didn't.", "s": 1.1, "e": 1.4}, {"w": "Go", "s": 1.45, "e": 1.6}]


class TimingsTest(unittest.TestCase):
    def test_example_words_load(self):
        data = timings.load(EXAMPLE / "words.json")
        self.assertEqual(len(data["words"]), 24)

    def test_rejects_out_of_order(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "w.json"
            p.write_text(json.dumps({"words": [{"w": "a", "s": 1, "e": 2}, {"w": "b", "s": 0.5, "e": 0.6}]}))
            with self.assertRaises(ValueError):
                timings.load(p)

    def test_find_ignores_case_and_punctuation(self):
        self.assertEqual(timings.find(W, "YEARS")["s"], 0.2)
        self.assertEqual(timings.find(W, "DIDN'T")["s"], 1.1)

    def test_find_after(self):
        with self.assertRaises(KeyError):
            timings.find(W, "two", after=0.1)

    def test_shift(self):
        self.assertEqual(timings.shift(W, 0.3)[0], {"w": "Two", "s": 0.3, "e": 0.5})

    def test_phrases_split_at_pauses_and_full_stops(self):
        self.assertEqual([[w["w"] for w in p] for p in timings.phrases(W)], [["Two", "years,"], ["We", "didn't."], ["Go"]])


if __name__ == "__main__":
    unittest.main()
