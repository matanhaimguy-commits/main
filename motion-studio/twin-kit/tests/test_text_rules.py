import unittest

from helpers import FACE, small_edl, example_edl
from kit import rules, stage, text_rules, zones


def names(e):
    return [r for lv, r, _ in rules.check(e, FACE) if lv == "FAIL"]


class TextRulesTest(unittest.TestCase):
    def test_behind_word_on_the_hair_fails(self):
        e = example_edl()
        e["beats"][4]["hero"]["vars"].update(y=480, size=280)      # hair over the letters
        self.assertIn("head", names(e))

    def test_behind_word_clear_of_the_head_passes(self):
        self.assertNotIn("head", names(example_edl()))

    def test_behind_word_beside_the_head_is_fine(self):
        e = small_edl()
        e["beats"][0]["twin"] = "stage"
        hv = {"text": "HI", "y": 700, "size": 100}
        hv_box = zones.move_box("behind-word", hv)
        head = stage.head_on_frame(e, "stage", FACE)
        self.assertTrue(stage.overlaps(hv_box, head))               # sanity: this one does reach the head
        self.assertTrue(text_rules.head_clear_findings(e, e["beats"][0], hv, FACE))

    def test_orbit_lanes_never_overlap(self):
        lanes = zones.orbit_lanes({"words": "A|BB|CCC|DDDD", "size": 60, "ry": 16})
        for i in range(len(lanes)):
            for j in range(i + 1, len(lanes)):
                self.assertFalse(stage.overlaps(lanes[i], lanes[j]))

    def test_scaled_orbit_size_is_checked(self):
        e = example_edl()
        e["beats"][3]["hero"]["vars"]["min_scale"] = 0.6           # 60 px words shrink to 36 px
        self.assertIn("size", names(e))

    def test_ui_scene_floor(self):
        self.assertEqual(text_rules.scene_findings({"move": "ui-chat", "vars": {"messages": "[]"}}), [])
        self.assertGreaterEqual(zones.SCENE_TEXT["ui-notification"], zones.MIN_TEXT)

    def test_overlapping_text_layers_fail(self):
        e = small_edl(captions={"y": 1130, "size": 88})
        e["beats"][1]["scene"] = {"move": "ui-prompt", "vars": {"y": 880}}   # prompt box runs into the captions
        self.assertIn("overlap", names(e))

    def test_overlap_can_be_marked(self):
        e = small_edl(captions={"y": 1130, "size": 88})
        e["beats"][1]["scene"] = {"move": "ui-prompt", "vars": {"y": 880}, "overlap_ok": True}
        self.assertNotIn("overlap", names(e))

    def test_pop3d_is_disabled(self):
        from kit import edl
        e = small_edl()
        e["beats"][2]["hero"] = {"move": "pop3d", "vars": {}}
        with self.assertRaises(edl.EDLError):
            edl.validate(e)

    def test_example_has_no_overlap(self):
        self.assertNotIn("overlap", names(example_edl()))

    def test_overshoot_stays_inside_the_margins(self):
        box = zones.move_box("behind-word", {"text": "A VERY LONG WORD HERE", "size": 300, "y": 600})
        self.assertGreaterEqual(box[0], zones.SIDE)
        self.assertLessEqual(box[2], zones.W - zones.SIDE)


if __name__ == "__main__":
    unittest.main()
