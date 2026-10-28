"""Tests for clients/spend.py."""
import unittest

from clients import spend
from clients.testbase import SLUG, ClientsCase


class Spend(ClientsCase):
    def test_month_against_the_cap(self):
        s = spend.month(self.root, SLUG, "2026-10", 50)
        self.assertEqual((s["usd"], s["cap_usd"], s["left_usd"], s["pieces"], s["has_ledger"]), (1.25, 50, 48.75, 1, True))
        self.assertEqual(s["by_format"], {"reel_motion": {"pieces": 1, "usd": 1.25}})

    def test_no_ledger_and_no_cap(self):
        s = spend.month(self.root, "nobody", "2026-10", None)
        self.assertEqual((s["usd"], s["left_usd"], s["has_ledger"]), (0, None, False))

    def test_spend_per_post(self):
        self.assertEqual(spend.by_post(spend.rows(self.root, SLUG)), {"AC-2026-11-W1-01": 1.25, "AC-OLD": 9.0})


if __name__ == "__main__":
    unittest.main()
