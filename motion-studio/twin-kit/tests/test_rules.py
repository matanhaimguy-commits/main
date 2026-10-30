import unittest

from helpers import FACE, small_edl, example_edl
from kit import rules


def rule_names(edl, face=FACE, level="FAIL"):
    return [r for lv, r, _ in rules.check(edl, face) if lv == level]


class RulesTest(unittest.TestCase):
    def test_example_passes(self):
        self.assertEqual(rule_names(example_edl()), [])

    def test_small_passes(self):
        self.assertEqual(rule_names(small_edl()), [])

    def test_two_heroes_fail(self):
        e = small_edl()
        e["beats"][0]["hero"] = [e["beats"][0]["hero"], e["beats"][2]["hero"]]
        self.assertIn("one-hero", rule_names(e))

    def test_missing_sound_fails(self):
        e = small_edl()
        e["beats"][0]["hero"]["sfx"] = "no-such-sound"
        self.assertIn("sound", rule_names(e))

    def test_long_hero_text_fails(self):
        e = small_edl()
        e["beats"][0]["hero"]["vars"]["text"] = "far too many words here now"
        self.assertIn("readable", rule_names(e))

    def test_two_tone_counts_both_lines(self):
        e = small_edl()
        e["beats"][2]["hero"]["vars"].update(lead="a b c", key="d e")
        self.assertIn("readable", rule_names(e))

    def test_short_hero_fails(self):
        e = small_edl()
        e["beats"][0]["hero"]["vars"]["at"] = 1.5
        self.assertIn("readable", rule_names(e))

    def test_long_orbit_item_fails(self):
        e = small_edl()
        e["beats"][0]["hero"] = {"move": "orbit", "vars": {"words": "ONE|TWO THREE FOUR"}}
        self.assertIn("readable", rule_names(e))

    def test_gap_over_three_seconds_fails(self):
        e = small_edl()
        e["beats"].pop()
        e["beats"][2]["end"] = 8.0
        self.assertIn("pacing", rule_names(e))

    def test_twin_over_half_fails(self):
        e = small_edl()
        e["beats"][1]["twin"] = "stage"
        self.assertIn("twin-share", rule_names(e))

    def test_front_text_on_face_fails(self):
        e = small_edl()
        e["beats"][2]["hero"]["vars"].update(y=900, size=120)   # stage mode face is about 723-1050
        self.assertIn("face", rule_names(e))

    def test_behind_word_may_cross_the_face(self):
        e = small_edl()
        e["beats"][0]["hero"]["vars"]["y"] = 700        # behind the twin: the twin covers it
        self.assertNotIn("face", rule_names(e))

    def test_captions_on_the_chin_fail(self):
        e = example_edl()
        e["captions"]["y"] = 1040                      # stage mode chin reaches about 1050
        self.assertIn("face", rule_names(e))

    def test_captions_outside_safe_zone_fail(self):
        e = small_edl(captions={"y": 1600})
        self.assertIn("safe-zone", rule_names(e))

    def test_captions_size_band(self):
        self.assertIn("size", rule_names(small_edl(captions={"y": 1130, "size": 64})))
        self.assertNotIn("size", rule_names(small_edl(captions={"y": 1130, "size": 88})))

    def test_face_outside_the_band_fails(self):
        e = small_edl(twin={"src": "x", "modes": {"stage": {"top": 1060}}})
        self.assertIn("face-band", rule_names(e))

    def test_behind_word_is_held_to_the_safe_zone(self):
        e = small_edl()
        e["beats"][0]["hero"]["vars"]["y"] = 280       # behind the twin, but in the top 269 px
        self.assertIn("safe-zone", rule_names(e))

    def test_ui_scene_is_held_to_the_safe_zone(self):
        e = small_edl()
        e["beats"][1]["scene"] = {"move": "ui-notification", "vars": {"y": 120, "items": "[{}]"}}
        self.assertIn("safe-zone", rule_names(e))

    def test_small_text_fails(self):
        e = small_edl()
        e["beats"][0]["hero"] = {"move": "orbit", "vars": {"words": "A|B", "size": 36}}
        self.assertIn("size", rule_names(e))

    def test_no_face_data_warns(self):
        self.assertIn("face", rule_names(small_edl(), face=None, level="WARN"))

    def test_summary(self):
        s = rules.summary(small_edl())
        self.assertEqual(s["beats"], 4)
        self.assertAlmostEqual(s["twin_share"], 4 / 8, places=3)


if __name__ == "__main__":
    unittest.main()
