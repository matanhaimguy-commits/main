"""Format variety (organic_os/variety.py). Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

import organic_os as o
from organic_os import variety as v
from organic_os.testbase import card, codes

NOV = ["2026-11-02", "2026-11-04", "2026-11-06", "2026-11-09", "2026-11-11", "2026-11-13"]


def month(formats):
    return [card(post_id=f"AC-{i}", slot=f"{d} 12:00", format=f) for i, (d, f) in enumerate(zip(NOV, formats))]


class VarietyTest(unittest.TestCase):
    def test_families_and_weeks(self):
        self.assertEqual(v.format_family("reel_animation_short"), "animation")
        self.assertEqual(v.format_family({"format": "carousel_framework"}), "carousel")
        self.assertEqual(v.week_key("2026-11-02 12:00"), v.week_key("2026-11-08 09:00"))
        self.assertNotEqual(v.week_key("2026-11-08 09:00"), v.week_key("2026-11-09 09:00"))

    def test_motion_cap_is_one_in_six_and_one_in_a_small_set(self):
        self.assertEqual([v.motion_cap(n) for n in (1, 3, 6, 11, 12, 13)], [1, 1, 1, 1, 2, 2])

    def test_three_of_a_family_in_a_week_fails(self):
        iss = v.variety_issues(month(["reel_animation_short", "reel_talking_object", "reel_animation_short"]))
        self.assertEqual(codes(iss, o.ERROR), ["variety"])
        self.assertIn("3 animation posts", iss[0]["msg"])

    def test_two_motion_in_six_and_three_families_fail(self):
        msgs = [i["msg"] for i in v.variety_issues(month(["reel_motion", "reel_song", "reel_motion",
                                                           "reel_song", "reel_whiteboard", "reel_whiteboard"]))]
        self.assertTrue(any("2 reel_motion of 6" in m for m in msgs))
        self.assertTrue(any("3 format families" in m for m in msgs))

    def test_a_varied_month_passes(self):
        self.assertEqual(v.variety_issues(month(["reel_song", "reel_whiteboard", "reel_animation_short",
                                                 "reel_story_narrated", "reel_motion", "reel_podcast"])), [])

    def test_plan_blocks_a_third_in_the_week_and_a_second_motion(self):
        plan = month(["reel_animation_short", "reel_talking_object"])
        self.assertIn("animation already 2x", v.blocked_by_plan("reel_animation", "2026-11-06 12:00", plan))
        self.assertIsNone(v.blocked_by_plan("reel_animation", "2026-11-09 12:00", plan))
        plan = month(["reel_motion", "reel_song", "reel_podcast"])
        self.assertIn("reel_motion already 1", v.blocked_by_plan("reel_motion", "2026-11-11 12:00", plan))

    def test_unused_family_scores_up(self):
        plan = month(["reel_song"])
        self.assertEqual(v.month_bonus("reel_podcast", "2026-11-04 12:00", plan)[0], 1.0)
        self.assertEqual(v.month_bonus("reel_song", "2026-11-04 12:00", plan)[0], -1.0)


if __name__ == "__main__":
    unittest.main()
