import unittest

import numpy as np

from helpers import EXAMPLE
from kit import align


def tone_with_gaps(spans, sr=align.SR, total=3.0):
    x = np.zeros(int(total * sr), np.float32)
    for a, b in spans:
        t = np.arange(int((b - a) * sr)) / sr
        x[int(a * sr): int(a * sr) + len(t)] = 0.3 * np.sin(2 * np.pi * 220 * t)
    return x


class AlignTest(unittest.TestCase):
    def test_voiced_finds_stretches(self):
        segs = align.voiced(tone_with_gaps([(0.2, 1.0), (1.5, 2.5)]))
        self.assertEqual(len(segs), 2)
        self.assertAlmostEqual(segs[0][0], 0.2, delta=0.02)
        self.assertAlmostEqual(segs[1][1], 2.5, delta=0.02)

    def test_short_pauses_merge(self):
        self.assertEqual(len(align.voiced(tone_with_gaps([(0.2, 1.0), (1.08, 2.0)]))), 1)

    def test_phrases_map_to_stretches(self):
        words = align.align("One two, three four.", [(0.0, 1.0), (2.0, 3.0)])
        self.assertEqual(words[0]["s"], 0.0)
        self.assertEqual(words[2]["s"], 2.0)
        self.assertEqual(words[-1]["e"], 3.0)

    def test_no_phrase_straddles_a_pause(self):
        words = align.align("a b, c d, e f.", [(0.0, 1.0), (2.0, 3.0)])
        for w in words:
            self.assertFalse(w["s"] < 1.0 < w["e"] or w["s"] < 2.0 < w["e"], w)

    def test_words_are_in_order(self):
        words = align.align("a bb ccc, dddd.", [(0.0, 2.0)])
        starts = [w["s"] for w in words]
        self.assertEqual(starts, sorted(starts))

    def test_real_voice(self):
        text = (EXAMPLE / "script.txt").read_text()
        r = align.run(EXAMPLE / "media" / "vo.mp3", text)
        self.assertEqual(len(r["words"]), len(text.split()))
        # the take's documented pauses: 2.26, 4.20, 5.72, 7.16 s
        self.assertAlmostEqual(r["segments"][1][1], 4.20, delta=0.05)
        self.assertIn("estimated", r["source"])

    def test_no_audio_raises(self):
        with self.assertRaises(ValueError):
            align.align("a b", [])


if __name__ == "__main__":
    unittest.main()
