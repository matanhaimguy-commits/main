"""Tests for hook_record.py and the G-HOOK PASS rule in pipeline.record_gate.
Run from growth-engine/tools: python3 -m unittest test_hook_record"""
import unittest

import hook_anchors
import hook_record
import pipeline as P
from test_pipeline import POST, SLUG, Base

IDS = hook_anchors.anchor_ids()


def read(v, t, s, gates=()):
    return {"visual": v, "text": t, "spoken": s, "gates_failed": list(gates)}


def run(hook=("A", "A", "A"), anchors=("B+", "B+", "B+"), gates=()):
    g = {"hook": read(*hook, gates=gates), "anchors": {i: read(*anchors) for i in IDS}}
    g2 = {"hook": read(*hook, gates=gates), "anchors": {i: read("B+", "B+", "B") for i in IDS}}  # a second, different read
    return {"packet": "packet-v2", "graders": [g, g2]}


class Data(unittest.TestCase):
    def test_pass_run_stores_the_grades_and_the_anchors(self):
        d = hook_record.make(run())
        self.assertEqual((d["source"], d["verdict"], d["anchors"], d["packet"]), ("hook_rule", "pass", IDS, "packet-v2"))
        self.assertEqual(len(d["graders"]), 2)
        self.assertIsNone(hook_record.pass_problem(d))

    def test_below_an_anchor_stores_a_fail(self):
        d = hook_record.make(run(hook=("A", "B", "A")))
        self.assertEqual(d["verdict"], "fail")
        self.assertIn("text", d["why"][0])
        self.assertIn("below an anchor", hook_record.pass_problem(d))

    def test_a_forged_verdict_is_recomputed(self):
        d = hook_record.make(run(hook=("A", "B", "A")))
        d["verdict"], d["why"] = "pass", []
        self.assertIsNotNone(hook_record.pass_problem(d))

    def test_missing_or_foreign_data(self):
        for d in (None, {}, {"source": "hook_rule", "anchors": ["x", "y"]}):
            self.assertIsNotNone(hook_record.pass_problem(d))

    def test_a_failed_check_is_a_fail(self):
        self.assertIsNotNone(hook_record.pass_problem(hook_record.make(run(gates=[3]))))


class Gate(Base):
    def test_g_hook_pass_needs_a_passing_twin_run(self):
        P.init_run(SLUG, POST, "carousel_mistakes")
        for d in (None, hook_record.make(run(hook=("A", "A", "B"))), hook_record.make(run(hook=("n/a", "A", "A")))):
            with self.assertRaises(P.PipelineError):
                P.record_gate(SLUG, POST, "G-HOOK", "PASS", "hook-lab + fresh grader", note="m", data=d)
        rec = P.record_gate(SLUG, POST, "G-HOOK", "PASS", "hook-lab + fresh grader", note="m", data=hook_record.make(run()))
        self.assertEqual(rec["data"]["verdict"], "pass")
        stored = P.latest(P.load_ledger(SLUG, POST)["run_gates"]["G-HOOK"])
        self.assertEqual(stored["data"]["anchors"], IDS)

    def test_a_fail_needs_no_data(self):
        P.init_run(SLUG, POST, "carousel_mistakes")
        self.assertEqual(P.record_gate(SLUG, POST, "G-HOOK", "FAIL", "hook-lab", note="below anchor")["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
