"""Tests for gate_auth.py (who may record a gate by hand). Run from growth-engine/tools: python3 -m unittest test_gate_auth"""
import json
import tempfile
import unittest
from pathlib import Path

import gate_auth as A

STD = json.loads((Path(__file__).resolve().parents[1] / "production" / "standards.json").read_text())
HC, HUMANS = STD["human_checkpoints"], STD["humans"]
D = "claude (delegated by Matan, plan 28 Oct)"
NOTE = "clients/acme/runs/X/reviews/look.v1.review.json: PASS"


class Checkpoints(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        rep = self.root / NOTE.split(":")[0]
        rep.parent.mkdir(parents=True)
        rep.write_text("{}")

    def tearDown(self):
        self.tmp.cleanup()

    def why(self, gate, by, note=NOTE):
        return A.checkpoint_problem(gate, HC[gate], by, note, HUMANS, self.root)

    def test_look_and_hookboard_take_the_delegate_with_a_report(self):
        for gate in ("G-HUMAN-LOOK", "G-HUMAN-HOOKBOARD"):
            self.assertIsNone(self.why(gate, D))
            self.assertIsNone(self.why(gate, "Matan", "approved in chat"))
            self.assertIn("names the fresh evaluator's report", self.why(gate, D, "looks good"))
            for note in ("reviews/nope.review.json: PASS", "../outside.review.json: PASS", "/etc/passwd.json"):
                self.assertIn("is not a file in the repo", self.why(gate, D, note))
            self.assertIn("is a human checkpoint", self.why(gate, "claude"))
            self.assertTrue(A.is_delegated(HC[gate], D, HUMANS))
            self.assertFalse(A.is_delegated(HC[gate], "Matan", HUMANS))

    def test_voice_song_final_stay_matan_only(self):
        for gate in ("G-HUMAN-VOICE", "G-HUMAN-SONG", "G-HUMAN-FINAL"):
            self.assertNotIn("delegate", HC[gate])
            for by in (D, "claude (delegated)", "claude"):
                self.assertIn("is a human checkpoint", self.why(gate, by))
            self.assertIsNone(self.why(gate, "Matan", "listened on the Studio page"))

    def test_spine_and_director_unchanged(self):
        self.assertIsNone(self.why("G-HUMAN-SPINE", "claude (delegated)", "spine B"))
        self.assertIn("the owner's call", self.why("G-HUMAN-SPINE", "claude", "spine B"))
        self.assertIn("say what was decided", self.why("G-HUMAN-SPINE", "claude (delegated)", None))
        self.assertIsNone(self.why("G-FALLBACK", "organic-director", "one shot"))


class Budget(unittest.TestCase):
    DATA = {"unit": "usd", "planned": 2, "with_buffer": 2.5, "balance": 6.9, "month_spent": 10, "cap": 100,
            "el_planned": 0, "source": "budget_usd"}

    def test_pass_needs_budget_usds_data(self):
        self.assertIsNone(A.budget_problem(self.DATA))
        for bad, needle in ((None, "not budget_usd's"), ({**self.DATA, "source": "hand"}, "not budget_usd's"),
                            ({k: v for k, v in self.DATA.items() if k != "source"}, "not budget_usd's"),
                            ({**self.DATA, "unit": "credits"}, "not budget_usd's"),
                            ({**self.DATA, "cap": None}, "non-negative cap"), ({**self.DATA, "planned": True}, "planned"),
                            ({**self.DATA, "cap": float("nan")}, "cap"), ({**self.DATA, "balance": float("inf")}, "balance"),
                            ({**self.DATA, "month_spent": -50}, "month_spent"),
                            ({**self.DATA, "with_buffer": 1}, "below planned"),
                            ({**self.DATA, "month_spent": 98}, "over the cap"), ({**self.DATA, "balance": 1}, "over the balance")):
            with self.subTest(bad=bad):
                self.assertIn(needle, A.budget_problem(bad))

    def test_no_pass_by_hand(self):
        self.assertIn("written only by pipeline.py budget", A.hand_budget_problem("PASS"))
        self.assertIsNone(A.hand_budget_problem("FAIL"))
        self.assertIsNone(A.hand_budget_problem("OVERRIDE"))

    def test_budget_ok(self):
        self.assertTrue(A.budget_ok({"status": "PASS", "data": self.DATA}))
        self.assertTrue(A.budget_ok({"status": "OVERRIDE", "by": "Matan"}))
        for rec in (None, {"status": "PASS"}, {"status": "FAIL", "data": self.DATA},
                    {"status": "PASS", "data": {**self.DATA, "source": None}}):
            self.assertFalse(A.budget_ok(rec))


if __name__ == "__main__":
    unittest.main()
