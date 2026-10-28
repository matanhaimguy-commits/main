"""Format router. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

import organic_os as o
from organic_os.testbase import BRAIN, MAP, card


class RouteTest(unittest.TestCase):
    def test_reach_prefers_reels_and_skips_tier_a_and_real_footage(self):
        opts = o.route(card(job="reach", belief="B1"), BRAIN, MAP)
        fams = [x["family"] for x in opts]
        self.assertEqual(fams[0], "reel")
        self.assertNotIn("A", [x["tier"] for x in opts])
        self.assertNotIn("reel_bts_real", [x["format"] for x in opts])

    def test_proven_angle_unlocks_tier_a_and_budget_and_rotation_filter(self):
        opts = o.route(card(job="reach", belief="B1", angle_proven=True), BRAIN, MAP)
        self.assertIn("A", [x["tier"] for x in opts])
        tight = o.route(card(job="reach", belief="B1", angle_proven=True), BRAIN, MAP, spent=58)
        self.assertTrue(tight)
        self.assertTrue(all(x["usd"][1] <= 2 for x in tight))
        no_reels = o.route(card(job="reach", belief="B1"), BRAIN, MAP, prev_family="reel")
        self.assertNotIn("reel", [x["family"] for x in no_reels])

    def test_budget_is_usd_and_no_cap_routes_only_free_formats(self):
        opts = o.route(card(job="reach", belief="B1", angle_proven=True), BRAIN, MAP, spent=0)
        self.assertTrue(all(x["usd"][1] <= 60 for x in opts))
        no_cap = {**BRAIN, "package": {"posts_per_week": 7, "account_stage": "new", "monthly_credit_cap": 1200}}
        free = o.route(card(job="reach", belief="B1", angle_proven=True), no_cap, MAP)
        self.assertTrue(all(x["usd"][1] == 0 for x in free))


if __name__ == "__main__":
    unittest.main()
