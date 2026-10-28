"""Tests for clients/plan.py."""
import unittest

from clients import plan
from clients.testbase import SLUG, ClientsCase


class Plan(ClientsCase):
    def test_plan_summary(self):
        p = plan.summary(plan.load(self.root, SLUG))
        self.assertEqual((p["month"], p["theme"], p["approved_by"]), ("2026-11 (all of November)", "steady months", "owner"))
        self.assertEqual(p["pillars"], ["Find"])
        self.assertEqual(p["series"], [{"name": "Parts", "kind": "hard", "format": None, "job": "reach",
                                        "target_episodes": 3, "status": None}])
        self.assertNotIn("rules", p)


if __name__ == "__main__":
    unittest.main()
