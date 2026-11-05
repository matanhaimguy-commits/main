"""Format router. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

import organic_os as o
from organic_os.testbase import BRAIN, MAP, card


def fmts(opts):
    return [x["format"] for x in opts]


class RouteTest(unittest.TestCase):
    def test_mechanism_beat_ranks_formats_that_show_the_invisible(self):
        opts = o.route(card(job="reach", belief="B1", load_bearing_beat="mechanism"), BRAIN, MAP)
        self.assertIn(opts[0]["format_family"], ("animation", "presenter"))
        self.assertNotIn("A", [x["tier"] for x in opts])
        self.assertNotIn("reel_bts_real", fmts(opts))

    def test_proof_beat_ranks_a_face(self):
        opts = o.route(card(job="trust", belief="B3", load_bearing_beat="proof"), BRAIN, MAP)
        self.assertEqual(o.CONFIG["formats"][opts[0]["format"]]["l19"]["face"], 2)

    def test_motion_only_for_list_data_or_type(self):
        for beat in ("mechanism", "proof", "offer", None):
            self.assertNotIn("reel_motion", fmts(o.route(card(job="trust", belief="B4", load_bearing_beat=beat), BRAIN, MAP)))
        self.assertIn("reel_motion", fmts(o.route(card(job="trust", belief="B4", load_bearing_beat="list"), BRAIN, MAP)))

    def test_cost_never_ranks(self):
        c = card(job="trust", belief="B4", load_bearing_beat="mechanism")
        rich = o.route(c, {**BRAIN, "package": {**BRAIN["package"], "monthly_usd_cap": 1e9}}, MAP)
        self.assertEqual(fmts(o.route(c, BRAIN, MAP)), fmts(rich))
        self.assertTrue(all("cheap" not in x["why"] for x in rich))

    def test_budget_filters_and_rotation(self):
        opts = o.route(card(job="reach", belief="B1", angle_proven=True), BRAIN, MAP)
        self.assertIn("A", [x["tier"] for x in opts])
        tight = o.route(card(job="reach", belief="B1", angle_proven=True), BRAIN, MAP, spent=58)
        self.assertTrue(tight)
        self.assertTrue(all(x["usd"][1] <= 2 for x in tight))
        self.assertNotIn("reel", [x["family"] for x in o.route(card(job="reach", belief="B1"), BRAIN, MAP, prev_family="reel")])
        self.assertNotIn("animation", [x["format_family"] for x in
                                      o.route(card(job="reach", belief="B1"), BRAIN, MAP, prev_family="animation")])

    def test_plan_variety_and_blocked_formats(self):
        plan = [card(post_id="P1", slot="2026-10-19 12:00", format="reel_animation_short"),
                card(post_id="P2", slot="2026-10-21 12:00", format="reel_talking_object")]
        c = card(slot="2026-10-23 12:00", job="reach", belief="B1")
        self.assertNotIn("animation", [x["format_family"] for x in o.route(c, BRAIN, MAP, plan=plan)])
        self.assertNotIn("reel_whiteboard", fmts(o.route(card(job="trust", belief="B4"), BRAIN, {**MAP, "blocked_formats": ["reel_whiteboard"]})))
        reels_only = {**MAP, "formats_per_week": {"reel": 3, "carousel": 0, "image": 0}}
        self.assertEqual({x["family"] for x in o.route(card(job="trust", belief="B4"), BRAIN, reels_only)}, {"reel"})

    def test_no_cap_routes_without_a_filter_and_warns(self):
        no_cap = {**BRAIN, "package": {"posts_per_week": 7, "account_stage": "new", "monthly_credit_cap": 1200}}
        routed = o.route(card(job="reach", belief="B1", angle_proven=True), no_cap, MAP, spent=10_000)
        self.assertTrue(any(x["usd"][1] > 5 for x in routed))
        self.assertEqual(o.route_issues(BRAIN), [])
        self.assertEqual([(w["level"], w["code"]) for w in o.route_issues(no_cap)], [(o.WARN, "budget")])


if __name__ == "__main__":
    unittest.main()
