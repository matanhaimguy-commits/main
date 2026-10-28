"""L19 fit (organic_os/l19.py). Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

import organic_os as o
from organic_os import l19


class L19Test(unittest.TestCase):
    def test_every_format_has_six_properties_a_family_and_a_funnel(self):
        for fid, f in o.CONFIG["formats"].items():
            with self.subTest(fid=fid):
                self.assertEqual(set(f["l19"]), set(l19.PROPERTIES))
                self.assertTrue(all(v in (0, 1, 2) for v in f["l19"].values()))
                self.assertTrue(f["format_family"])
                self.assertTrue(set(f["funnel"]) <= {"TOF", "MOF", "BOF"} and f["funnel"])

    def test_fit_is_weighted_and_scaled_to_five(self):
        f = o.CONFIG["formats"]
        self.assertEqual(l19.fit(f["reel_animation"], "mechanism"), 5.0)
        self.assertEqual(l19.fit(f["reel_whiteboard"], "mechanism"), round(5 * 10 / 12, 2))  # invisible 2x3 + order 2x1 + attention 1 + person 1 of 12
        self.assertGreater(l19.fit(f["reel_podcast"], "proof"), l19.fit(f["reel_animation"], "proof"))
        self.assertGreater(l19.fit(f["reel_animation"], "mechanism"), l19.fit(f["reel_ugc_talking"], "mechanism"))
        self.assertEqual(l19.fit(f["reel_motion"], None), 0.0)
        with self.assertRaises(ValueError):
            l19.fit(f["reel_motion"], "vibes")

    def test_motion_takes_only_list_data_and_type(self):
        self.assertEqual([b for b in l19.beats() if l19.motion_allowed_beat(b)], ["list", "data", "type"])
        self.assertFalse(l19.motion_allowed_beat(None))


if __name__ == "__main__":
    unittest.main()
