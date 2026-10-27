"""Tests for studio/gates.py: ledger records, computed gates and per-asset gates."""
import unittest

from studio.gates import asset_gates, computed_gate, gate_entry, run_gates
from studio.testbase import POST, SLUG, P, StudioCase


class GateEntry(unittest.TestCase):
    def test_keeps_what_the_page_shows_and_nothing_else(self):
        rec = {"at": "2026-10-27T10:00:00+00:00", "status": "PASS", "by": "fresh cold reader", "score": 86,
               "note": "n" * 5000, "data": {"x": 1}}
        e = gate_entry("G-SCRIPT", rec)
        self.assertEqual({k: v for k, v in e.items() if k != "note"},
                         {"gate": "G-SCRIPT", "label": "Script Lab", "status": "PASS", "by": "fresh cold reader", "score": 86,
                          "at": "2026-10-27T10:00:00+00:00"})
        self.assertEqual(len(e["note"]), 4000)
        self.assertEqual(gate_entry("G-NEW", {"status": "WEIRD", "score": True}), {"gate": "G-NEW", "label": "G-NEW", "status": "PENDING"})
        self.assertEqual(gate_entry("G-VIS", {"status": "FAIL"}, "SB@v2")["asset"], "SB@v2")


class Computed(StudioCase):
    def test_open_gates_say_what_is_missing_and_no_takes_is_not_a_pass(self):
        led = self.song_run()
        self.assertEqual(computed_gate(P, led, "G-SPEC"), {"gate": "G-SPEC", "label": "Shot Specs", "status": "PENDING",
                                                          "note": "no Shot Specs written"})
        self.assertEqual(computed_gate(P, led, "G-ASSETS"), {"gate": "G-ASSETS", "label": "Every take passed",
                                                            "status": "PENDING", "note": "No takes yet."})
        self.assertNotIn("note", computed_gate(P, led, "G-PLAN"))  # "has no PASS" says nothing new

    def test_recorded_gates_list_every_record_in_order(self):
        self.song_run()
        P.record_gate(SLUG, POST, "G-IDEA", "PASS", "organic-director", note="second try")
        led = P.load_ledger(SLUG, POST)
        self.assertEqual([g["status"] for g in run_gates(P, led, 1)], ["FAIL", "PASS"])

    def test_assets_show_under_their_step_with_their_open_gates(self):
        P.init_run(SLUG, POST, "carousel_mistakes")
        led = P.load_ledger(SLUG, POST)
        led["assets"] += [
            {"asset_id": "SL01", "version": 1, "type": "slide", "gates": {"G-PROMPT-IMG": [{"status": "FAIL"}]}},
            {"asset_id": "SL01", "version": 2, "type": "slide", "gates": {"G-PROMPT-IMG": [{"status": "PASS", "by": "prompt-reviewer"}]}},
        ]
        self.assertEqual([(g["gate"], g.get("asset"), g["status"]) for g in asset_gates(P, led, 10)],
                         [("G-PROMPT-IMG", "SL01@v2", "PASS"), ("G-VIS-SLIDE", "SL01@v2", "PENDING")])
        self.assertEqual(asset_gates(P, led, 7), [])


if __name__ == "__main__":
    unittest.main()
