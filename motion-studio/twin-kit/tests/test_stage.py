import unittest

from helpers import FACE, small_edl
from kit import stage


class StageTest(unittest.TestCase):
    def test_off_has_no_placement(self):
        self.assertIsNone(stage.placement(small_edl(), "off", 1080))
        self.assertIsNone(stage.face_on_frame(small_edl(), "off", FACE))

    def test_stage_is_centred_and_low(self):
        s, left, top = stage.placement(small_edl(), "stage", 1080)
        self.assertAlmostEqual(left, (1080 - 1080 * s) / 2)
        head = stage.head_on_frame(small_edl(), "stage", FACE)
        self.assertGreater(head[1], 1920 * 0.55)        # the head starts below the middle: the set is above

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
