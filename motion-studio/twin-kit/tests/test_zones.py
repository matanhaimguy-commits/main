import unittest

from kit import zones


class ZonesTest(unittest.TestCase):
    def test_inside(self):
        self.assertEqual(zones.breaches([100, 300, 900, 900]), [])

    def test_each_edge(self):
        self.assertIn("top", zones.breaches([100, 200, 900, 400])[0])
        self.assertIn("bottom", zones.breaches([100, 1200, 800, 1300])[0])
        self.assertIn("left", zones.breaches([40, 300, 800, 400])[0])
        self.assertIn("right", zones.breaches([100, 300, 1040, 400])[0])

    def test_right_strip_only_in_the_lower_half(self):
        self.assertEqual(zones.breaches([100, 300, 900, 700]), [])
        self.assertIn("lower half", zones.breaches([100, 1000, 900, 1100])[0])

    def test_face_band(self):
        self.assertIsNone(zones.face_band_breach([0, 400, 10, 990]))
        self.assertIn("chin", zones.face_band_breach([0, 400, 10, 1010]))
        self.assertIsNotNone(zones.face_band_breach([0, 250, 10, 1000]))
        self.assertIsNotNone(zones.face_band_breach([0, 400, 10, 1100]))

    def test_caption_box_keeps_out_of_the_right_strip(self):
        box = zones.caption_box({"y": 1130, "size": 88})
        self.assertEqual(zones.breaches(box), [])
        self.assertLessEqual(box[2], 1080 - 227)

    def test_behind_word_is_capped_to_the_margins(self):
        box = zones.move_box("behind-word", {"text": "A VERY LONG WORD", "size": 300, "y": 560})
        self.assertGreaterEqual(box[0], 65)

    def test_two_tone_sizes(self):
        self.assertEqual(zones.text_sizes("two-tone", {"size": 100}), [("two-tone lead", 42.0)])


if __name__ == "__main__":
    unittest.main()
