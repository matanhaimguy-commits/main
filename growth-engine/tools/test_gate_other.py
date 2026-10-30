"""Tests for gate_other.py (an owner's one-off test call on a gated tool of kind other) and gate_budget.py.
Run from growth-engine/tools: python3 -m unittest test_gate_other"""
import json
import unittest

import pipeline as P
import test_pipeline as TP

SLUG = TP.SLUG
TEST_RUN = "AC-TEST-HIGGS"
TOOL = "mcp__Higgs__execute_preset"


class OtherTest(TP.Base):
    def setUp(self):
        super().setUp()
        P.init_run(SLUG, TEST_RUN, "carousel_mistakes")
        P.new_asset(SLUG, TEST_RUN, "T1", "test", tool=TOOL)
        P.record_gate(SLUG, TEST_RUN, "G-HUMAN-TEST", "PASS", "Matan", asset="T1@v1", note="try the preset once")

    def age_budget(self, hours):
        led = P.load_ledger(SLUG, TEST_RUN)
        b = P.latest(led["run_gates"]["G-BUDGET"])
        b["at"] = (P.parse_ts(b["at"]) - P.dt.timedelta(hours=hours)).isoformat()
        P.save_ledger(led)

    def test_one_call_with_a_fresh_budget(self):
        P.budget(SLUG, TEST_RUN, planned=1, balance=8)
        self.assertEqual(P.check_call(TOOL, {}), (True, []))
        ok, why = P.check_call(TOOL, {})
        self.assertFalse(ok, "a test is one call")

    def test_a_budget_older_than_24_hours_is_refused(self):
        P.budget(SLUG, TEST_RUN, planned=1, balance=8)
        self.age_budget(25)
        ok, why = P.check_call(TOOL, {})
        self.assertFalse(ok)
        self.assertIn("older than 24 h", why[0])

    def test_no_budget_and_no_log_on_a_dry_check(self):
        ok, why = P.check_call(TOOL, {})
        self.assertFalse(ok)
        self.assertIn("no G-BUDGET PASS", why[0])
        P.budget(SLUG, TEST_RUN, planned=1, balance=8)
        self.assertTrue(P.check_call(TOOL, {}, log=False)[0])
        self.assertTrue(P.check_call(TOOL, {})[0], "the dry check did not count as the call")
        log = [json.loads(x) for x in (P.run_dir(SLUG, TEST_RUN) / "calls.jsonl").read_text().splitlines()]
        self.assertEqual([e["decision"] for e in log], ["ALLOW"])


if __name__ == "__main__":
    unittest.main()
