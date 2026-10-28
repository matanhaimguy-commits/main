"""Client Brain check. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import copy
import unittest

import organic_os as o
from organic_os.testbase import BRAIN, DEMAND, codes


class BrainTest(unittest.TestCase):
    def test_complete_enough_brain_has_no_blockers_but_lists_gaps(self):
        issues, gaps = o.brain_check(BRAIN, DEMAND)
        self.assertEqual(codes(issues, o.ERROR), [])
        fields = [g["field"] for g in gaps]
        for f in ("business_model.capacity", "demand_map", "contrarian_vault", "visual.ai_label", "baseline", "lead_magnets[TEST]"):
            self.assertIn(f, fields)

    def test_missing_offer_blocks(self):
        b = copy.deepcopy(BRAIN)
        b["offer"]["main_offer"] = "TBD"
        issues, _ = o.brain_check(b, DEMAND)
        self.assertIn("blocking", codes(issues, o.ERROR))

    def test_usd_cap_is_a_gap_until_the_owner_sets_it(self):
        _, gaps = o.brain_check(BRAIN, DEMAND)
        self.assertNotIn("package.monthly_usd_cap", [g["field"] for g in gaps])
        for pkg in ({"monthly_credit_cap": 1200}, {"monthly_usd_cap": None}):
            b = copy.deepcopy(BRAIN)
            b["package"] = {"posts_per_week": 7, "account_stage": "new", **pkg}
            issues, gaps = o.brain_check(b, DEMAND)
            self.assertEqual(codes(issues, o.ERROR), [])
            self.assertIn("package.monthly_usd_cap", [g["field"] for g in gaps])
        b = copy.deepcopy(BRAIN)
        b["package"]["monthly_usd_cap"] = -5
        self.assertIn("schema", codes(o.brain_check(b, DEMAND)[0], o.ERROR))


if __name__ == "__main__":
    unittest.main()
