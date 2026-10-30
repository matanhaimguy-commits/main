"""Tests for budget_heygen.py and G-BUDGET with HeyGen credits (pipeline.py budget --heygen).
Run from growth-engine/tools: python3 -m unittest test_budget_heygen"""
import json
import unittest

import budget_heygen as H
import gate_auth
import pipeline as P
import test_pipeline as TP

SLUG, POST = TP.SLUG, TP.POST


class Check(unittest.TestCase):
    def test_no_cap_warns_and_passes(self):
        r = H.check(None, 0, 100, None, 0.25)
        self.assertEqual(r["notes"], [])
        self.assertIn("monthly_heygen_credit_cap", r["warnings"][0])
        self.assertEqual(r["data"]["heygen_with_buffer"], 125)

    def test_cap_and_balance(self):
        self.assertEqual(H.check(1000, 800, 100, None, 0.25)["notes"], [])
        self.assertIn("month cap", H.check(1000, 900, 100, None, 0.25)["notes"][0])
        self.assertIn("balance", H.check(None, 0, 100, 120, 0.25)["notes"][0])
        self.assertEqual(H.check(None, 0, 0, None, 0.25)["warnings"], [])   # no credits planned: nothing to warn

    def test_data_problem(self):
        good = H.check(1000, 0, 100, 3694, 0.25)["data"]
        self.assertIsNone(H.data_problem(good))
        self.assertIsNone(H.data_problem({"planned": 1}))   # no HeyGen numbers: an Atlas-only piece
        self.assertIn("over the credit cap", H.data_problem({**good, "heygen_month_spent": 950}))
        self.assertIn("heygen_planned", H.data_problem({**good, "heygen_planned": -1}))
        self.assertIn("below", H.data_problem({**good, "heygen_with_buffer": 50}))
        self.assertIn("balance", H.data_problem({**good, "heygen_balance": 10}))
        self.assertTrue(H.priced(good))
        self.assertFalse(H.priced({"heygen_planned": 0}))
        self.assertFalse(H.priced(None))


class Run(TP.Base):
    def setUp(self):
        super().setUp()
        P.init_run(SLUG, POST, "carousel_mistakes")

    def brain(self, **pkg):
        p = self.root / "clients" / SLUG / "brain.json"
        b = json.loads(p.read_text())
        b["package"].update(pkg)
        p.write_text(json.dumps(b))

    def test_budget_records_credits_and_warns_with_no_cap(self):
        r = P.budget(SLUG, POST, planned=1, balance=8, heygen=200)
        self.assertEqual(r["status"], "PASS")
        self.assertEqual(r["heygen_with_buffer"], 250)
        rec = P.latest(P.load_ledger(SLUG, POST)["run_gates"]["G-BUDGET"])
        self.assertIn("warning: no monthly HeyGen credit cap", rec["note"])
        self.assertTrue(gate_auth.budget_ok(rec))

    def test_credit_cap_counts_the_ledger(self):
        self.brain(monthly_heygen_credit_cap=500)
        month = P.now().strftime("%Y-%m")
        led = self.root / "clients" / SLUG / "ledger.csv"
        led.write_text("date,post_id,format,tier,atlas_usd,heygen_credits,higgsfield_credits,elevenlabs_credits,"
                       f"minutes,note\n{month}-01,X,reel_motion,C,1,300,,,0,\n")
        self.assertEqual(P.budget(SLUG, POST, planned=1, balance=8, heygen=100)["status"], "PASS")
        r = P.budget(SLUG, POST, planned=1, balance=8, heygen=200)
        self.assertEqual(r["status"], "FAIL")
        self.assertIn("HeyGen month cap", r["notes"][0])
        self.assertEqual(P.budget(SLUG, POST, planned=1, balance=8, heygen=100, heygen_balance=50)["status"], "FAIL")

    def test_a_hand_pass_with_heygen_numbers_over_the_cap_does_not_count(self):
        r = P.budget(SLUG, POST, planned=1, balance=8, heygen=100)
        rec = {"status": "PASS", "data": {k: r[k] for k in r if k not in ("status", "notes", "warnings")}}
        self.assertTrue(gate_auth.budget_ok(rec))
        rec["data"]["heygen_cap"] = 10
        self.assertFalse(gate_auth.budget_ok(rec))

    def test_the_cli_prints_the_credits(self):
        import contextlib
        import io
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = P.main(["budget", SLUG, POST, "--planned", "1", "--balance", "8", "--heygen", "200"])
        self.assertEqual(code, 0)
        self.assertIn("HeyGen: planned 200 credits", out.getvalue())
        self.assertIn("warning: no monthly HeyGen credit cap", out.getvalue())


if __name__ == "__main__":
    unittest.main()
