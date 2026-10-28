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

    def test_decided_questions_leave_the_owners_list(self):
        b = copy.deepcopy(BRAIN)
        b["decisions_open"] = [{"id": "E1", "question": "Name the method?", "interim": "unnamed"},
                               {"id": "E4", "question": "Prices?", "decided": {"answer": "No prices.", "by": "Matan"}}]
        b["hub"] = {"business": "acme"}
        b["package"]["schedule"] = {"days": ["Mon", "Fri"], "time": "12:00", "timezone": "America/New_York"}
        issues, gaps = o.brain_check(b, DEMAND)
        self.assertEqual(codes(issues, o.ERROR), [])
        report = o.brain_report("acme", b, issues, gaps)
        owner, decided = report.split("## Decided")
        self.assertIn("**E1** Name the method?", owner)
        self.assertNotIn("E4", owner)
        self.assertIn("**E4** No prices. (Matan)", decided)
        for bad in ({"decided": {"answer": "x"}}, {"hub": {"business": ""}},
                    {"schedule": {"days": ["Monday"], "time": "12:00", "timezone": "X"}},
                    {"schedule": {"days": ["Mon"], "time": "25:00", "timezone": "X"}}):
            c = copy.deepcopy(b)
            if "decided" in bad:
                c["decisions_open"][1]["decided"] = bad["decided"]
            elif "hub" in bad:
                c["hub"] = bad["hub"]
            else:
                c["package"]["schedule"] = bad["schedule"]
            with self.subTest(bad=bad):
                self.assertIn("schema", codes(o.brain_check(c, DEMAND)[0], o.ERROR))


if __name__ == "__main__":
    unittest.main()
