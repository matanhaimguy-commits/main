"""Tests for hook_packet.py. Run from growth-engine/tools: python3 -m unittest test_hook_packet"""
import tempfile
import unittest
from pathlib import Path

import hook_anchors
import hook_packet
import hook_rule

HOOK = {"id": "H1", "buyer": "Owners of small service businesses.", "text": "Likes, no bookings? Fix the page.",
        "spoken": "Your post asks about slow months. Your page never answers it.", "frame": None}


class Packet(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name) / "packet"
        self.key = hook_packet.build(self.dir, [HOOK], seed=3)
        self.stacks = (self.dir / "stacks.md").read_text()

    def tearDown(self):
        self.tmp.cleanup()

    def test_every_run_carries_both_anchors_and_the_hook(self):
        self.assertEqual(sorted(self.key.values()), sorted(["H1"] + hook_anchors.anchor_ids()))
        for a in hook_anchors.load():
            self.assertIn(a["spoken"], self.stacks)
        self.assertIn(HOOK["spoken"], self.stacks)

    def test_graders_see_neutral_labels_only(self):
        self.assertNotIn("ANCHOR", self.stacks)
        self.assertNotIn("H1", self.stacks)

    def test_packet_v2_files_ride_along(self):
        self.assertIn("Hook grading rubric", (self.dir / "rubric.md").read_text())
        self.assertIn("Return \"visual\"", (self.dir / "instructions.md").read_text())

    def test_frame_line_only_when_a_frame_exists(self):
        k = hook_packet.build(self.dir, [dict(HOOK, frame="f.png")], seed=3, root=self.dir)
        self.assertIn("FRAME:", (self.dir / "stacks.md").read_text())
        self.assertEqual((self.dir / "stacks.md").read_text().count("FRAME:"), 1)
        self.assertEqual(len(k), 3)

    def test_graders_output_becomes_a_run_the_rule_judges(self):
        top = {"visual": "A", "text": "A", "spoken": "A", "gates_failed": []}
        out = {"stacks": [dict(top, id=label) for label in self.key]}
        r = hook_rule.judge(hook_packet.to_run(self.key, "H1", [out, out]))
        self.assertTrue(r["pass"], r["why"])
        low = {"stacks": [dict(top, id=label, text="C") if v == "H1" else dict(top, id=label)
                          for label, v in self.key.items()]}
        self.assertFalse(hook_rule.judge(hook_packet.to_run(self.key, "H1", [out, low]))["pass"])


if __name__ == "__main__":
    unittest.main()
