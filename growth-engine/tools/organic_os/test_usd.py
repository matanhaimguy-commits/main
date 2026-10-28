"""Atlas USD per format (organic_os/usd.py). Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

import organic_os as o
from organic_os import usd

PRICES = {"image": 0.05, "video_s": 0.02, "omni_s": 0.1, "tts_1k_chars": 0.1, "song": 0.2, "stt_min": 0.0,
          "chars_per_word": 6}


class UsdTest(unittest.TestCase):
    def test_units_times_prices_plus_the_retake_buffer(self):
        self.assertEqual(usd.piece_usd({"images": [2, 4], "video_s": [10, 20]}, 0, PRICES, 0.25), 0.38)
        self.assertEqual(usd.piece_usd({"images": [2, 4], "video_s": [10, 20]}, 1, PRICES, 0.25), 0.75)
        self.assertEqual(usd.piece_usd({"omni_s": [10, 10], "songs": [1, 1]}, 0, PRICES, 0), 1.2)
        self.assertEqual(usd.piece_usd({}, 1, PRICES, 0.25), 0)
        with self.assertRaises(ValueError):
            usd.piece_usd({"credits": [1, 2]}, 0, PRICES, 0.25)

    def test_voice_is_every_take_of_the_words_at_standards_pace(self):
        # 60 s at 2.5 words/s, 6 chars a word, 4 takes = 3,600 chars at $0.10 per 1,000
        self.assertAlmostEqual(usd.voice_usd(60, PRICES, {"takes_per_beat": 4, "pace_words_per_s_default": 2.5}), 0.36)

    def test_every_format_has_units_and_its_usd_matches_the_prices(self):
        for fid, f in o.CONFIG["formats"].items():
            with self.subTest(fid=fid):
                self.assertIn("atlas_units", f)
                self.assertEqual(f["usd"], usd.format_usd(f), "re-run the usd computation after a price change")
                self.assertLessEqual(f["usd"][0], f["usd"][1])
                self.assertIn("credits", f)  # kept for the ledger's history

    def test_prices_are_dated_in_standards(self):
        p = o.STANDARDS["atlas_prices"]
        self.assertEqual(p["as_of"], "2026-10-28")
        self.assertEqual((p["image"], p["video_s"], p["omni_s"], p["tts_1k_chars"], p["song"]),
                         (0.059, 0.024, 0.0896, 0.10, 0.132))


if __name__ == "__main__":
    unittest.main()
