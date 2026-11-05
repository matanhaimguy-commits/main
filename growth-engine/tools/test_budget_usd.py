"""G-BUDGET in Atlas USD (budget_usd.py). Run from growth-engine/tools: python3 -m unittest test_budget_usd"""
import unittest

import budget_usd as B


class BudgetUsd(unittest.TestCase):
    def test_pass_within_cap_and_balance(self):
        r = B.check(cap=40, month_spent=10, planned=4, balance=8.3, buffer=0.25)
        self.assertEqual(r["status"], "PASS", r["notes"])
        self.assertEqual(r["data"], {"unit": "usd", "planned": 4, "with_buffer": 5.0, "balance": 8.3,
                                     "month_spent": 10, "cap": 40})

    def test_cap_balance_and_missing_cap_fail(self):
        over = B.check(cap=40, month_spent=36, planned=4, balance=100, buffer=0.25)
        self.assertEqual(over["status"], "FAIL")
        self.assertIn("month cap $40.00", over["notes"][0])
        poor = B.check(cap=40, month_spent=0, planned=8, balance=8.3, buffer=0.25)
        self.assertIn("balance $8.30 can't cover $10.00", poor["notes"][0])
        none = B.check(cap=None, month_spent=0, planned=1, balance=100, buffer=0.25)
        self.assertEqual(none["status"], "FAIL")
        self.assertIn("monthly_usd_cap", none["notes"][0])
        self.assertEqual(B.check(cap=0, month_spent=0, planned=0, balance=0, buffer=0.25)["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
