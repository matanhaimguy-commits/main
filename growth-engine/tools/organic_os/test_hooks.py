"""Hook checks. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import tempfile
import unittest
from pathlib import Path

from organic_os.cmd_hooks import check_stacks
from organic_os.hook_plain import plain_issues
from organic_os.hook_sources import library, phrases

LIB = """- `HF-01` · Channel verdict · danielpriestley · 12.5x · spoken: "Cold email?"
- `HF-02` · Small lift · someone · 2.1x · spoken: "x"
- `HA-01` · Some coach ads · 45 days, 33 copies, image, active
- `HA-02` · New ad · 12 days, 1 copy
- `HL-01` · Accusation · takimoore · 0.18x · spoken: "You don't make content."
  - formula: as `HA-01`, with no days on this line
"""
PH = """- `Q-R-0054` "linkedin ... it's lumpy" · r/agency
- `Q-R-0058` "some months we'd sign 3 clients other months literally nothing" · reddit
"""
GOOD = {"id": "good", "format_id": "HF-01", "voc_ids": ["Q-R-0058"], "text": "Some months clients, some months nothing",
        "spoken": "Some months you sign clients, other months nothing. Here's why."}


class HookCheckTest(unittest.TestCase):
    def setUp(self):
        d = Path(tempfile.mkdtemp())
        (d / "lib.md").write_text(LIB); (d / "ph.md").write_text(PH)
        self.lib, self.ph = library(d / "lib.md"), phrases(d / "ph.md")

    def check(self, **change):
        return check_stacks([{**GOOD, **change}], self.lib, self.ph)["good"]

    def test_parses_ids_and_breakouts(self):
        self.assertEqual(self.lib["HF-01"], 12.5)
        self.assertIn("lumpy", self.ph["Q-R-0054"])

    def test_good_stack_passes(self):
        self.assertEqual(self.check(), [])

    def test_needs_a_proven_format(self):
        self.assertTrue(any("no proven format" in i for i in self.check(format_id=None)))
        self.assertTrue(any("under the 3.0x" in i for i in self.check(format_id="HF-02")))
        self.assertTrue(any("loser" in i for i in self.check(format_id="HL-01")))
        self.assertTrue(any("not in the Hook Library" in i for i in self.check(format_id="HF-99")))

    def test_long_running_ads_count_as_proof(self):
        self.assertEqual(self.lib["HA-01"], 45)
        self.assertEqual(self.check(format_id="HA-01"), [])
        self.assertTrue(any("30-day bar" in i for i in self.check(format_id="HA-02")))

    def test_needs_the_buyers_words(self):
        self.assertTrue(any("no buyer phrase" in i for i in self.check(voc_ids=[])))
        out = self.check(spoken="Your pipeline breaks when you stop. Here's why.", text="Why your calendar empties")
        self.assertTrue(any("none of the cited buyers' words" in i for i in out))

    def test_form(self):
        long = "You lost to someone cheaper, and it was decided before you ever quoted."
        out = self.check(spoken=long)
        self.assertTrue(any("13 words" in i for i in out))
        self.assertTrue(any("'quoted'" in i for i in out))

    def test_plain_english_allows_buyer_words(self):
        self.assertTrue(plain_issues("Solutions for growth", set()))
        self.assertEqual(plain_issues("Solutions for growth", {"solutions", "growth"}), [])
        self.assertTrue(any("teaser" in i for i in plain_issues("Watch this before you post", set())))


if __name__ == "__main__":
    unittest.main()
