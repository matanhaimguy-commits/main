import unittest

from helpers import small_edl, example_edl
from kit import sfx
from kit.moves import MOVES, SCENES, CUTS


class SfxTest(unittest.TestCase):
    def test_every_kit_sound_exists(self):
        for table in (MOVES, SCENES, CUTS):
            for name, spec in table.items():
                self.assertTrue(sfx.exists(spec["sfx"]), f"{name}: {spec['sfx']}")

    def test_every_move_in_the_example_gets_a_cue(self):
        e = example_edl()
        cues = sfx.cues(e)
        made = {(c["beat"], c["for"].split(":")[0]) for c in cues}
        for b in e["beats"]:
            for key in ("hero", "scene", "grade"):
                if b.get(key):
                    self.assertIn((b["id"], key), made)
            if b.get("cut_in"):
                self.assertIn((b["id"], "cut"), made)

    def test_cue_times_follow_the_moves(self):
        cues = sfx.cues(small_edl())
        whip = next(c for c in cues if c["for"] == "cut:whip")
        self.assertAlmostEqual(whip["t"], 2.0 + CUTS["whip"]["sfx_at"])
        self.assertEqual([c["t"] for c in cues], sorted(c["t"] for c in cues))

    def test_override_and_gain(self):
        e = small_edl()
        e["beats"][0]["hero"]["sfx"] = "chime"
        c = next(c for c in sfx.cues(e) if c["beat"] == "a")
        self.assertEqual(c["name"], "chime")
        self.assertEqual(c["gain_db"], sfx.GAIN_DB["chime"])

    def test_never_negative(self):
        e = small_edl()
        e["beats"][0]["cut_in"] = "whip"
        self.assertTrue(all(c["t"] >= 0 for c in sfx.cues(e)))


if __name__ == "__main__":
    unittest.main()
