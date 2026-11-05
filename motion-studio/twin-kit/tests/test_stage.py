import unittest

from helpers import FACE, small_edl
from kit import stage


class StageTest(unittest.TestCase):
    def test_off_has_no_placement(self):
        self.assertIsNone(stage.placement(small_edl(), "off", 1080))
        self.assertIsNone(stage.face_on_frame(small_edl(), "off", FACE))

    def test_every_mode_puts_the_face_in_the_band(self):
        s, left, top = stage.placement(small_edl(), "stage", 1080)
        self.assertAlmostEqual(left, (1080 - 1080 * s) / 2)
        for mode in ("stage", "full"):
            f = stage.face_on_frame(small_edl(), mode, FACE)
            self.assertTrue(1920 * 0.15 <= f[1] and f[3] <= 1920 * 0.55, (mode, f))

    def test_orbit_ring_sits_on_the_head(self):
        e = small_edl()
        v = stage.orbit_geometry(e, {"twin": "stage"}, {"words": "A"}, FACE)
        head = stage.head_on_frame(e, "stage", FACE)
        self.assertTrue(head[1] < v["cy"] < head[3])
        self.assertEqual(len(v["head"].split(",")), 4)
        self.assertEqual(stage.orbit_geometry(e, {"twin": "stage"}, {"cx": 9}, FACE)["cx"], 9)

    def test_edl_can_tune_a_mode(self):
        e = small_edl(twin={"src": "x", "modes": {"stage": {"top": 1200}}})
        self.assertEqual(stage.placement(e, "stage", 1080)[2], 1200)

    def test_to_frame(self):
        self.assertEqual(stage.to_frame([0, 0, 10, 10], (2, 5, 7)), [5, 7, 25, 27])

    def test_overlaps(self):
        self.assertTrue(stage.overlaps([0, 0, 10, 10], [5, 5, 20, 20]))
        self.assertFalse(stage.overlaps([0, 0, 10, 10], [10, 0, 20, 10]))


if __name__ == "__main__":
    unittest.main()
