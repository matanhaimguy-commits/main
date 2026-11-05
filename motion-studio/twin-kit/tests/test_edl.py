import copy
import unittest

from helpers import small_edl, example_edl
from kit import edl


class EDLTest(unittest.TestCase):
    def test_small_edl_is_valid(self):
        self.assertTrue(edl.validate(small_edl()))

    def test_example_loads(self):
        e = example_edl()
        self.assertEqual(e["beats"][-1]["hero"]["move"], "end-card")

    def bad(self, mutate, word):
        e = small_edl()
        mutate(e)
        with self.assertRaises(edl.EDLError) as ctx:
            edl.validate(e)
        self.assertIn(word, str(ctx.exception))

    def test_beats_must_tile(self):
        self.bad(lambda e: e["beats"][1].update(start=2.5), "tile")

    def test_beats_must_reach_the_end(self):
        self.bad(lambda e: e.update(duration=9.0), "film is")

    def test_unknown_move(self):
        self.bad(lambda e: e["beats"][0]["hero"].update(move="spin"), "unknown hero")

    def test_unknown_twin_mode(self):
        self.bad(lambda e: e["beats"][0].update(twin="huge"), "twin must be")

    def test_unknown_cut(self):
        self.bad(lambda e: e["beats"][1].update(cut_in="dissolve"), "cut_in")

    def test_repeated_id(self):
        self.bad(lambda e: e["beats"][1].update(id="a"), "repeated")

    def test_grade_only_bw_grain(self):
        self.bad(lambda e: e["beats"][0].update(grade={"move": "orbit"}), "grade")

    def test_missing_key(self):
        e = small_edl()
        del e["voice"]
        with self.assertRaises(edl.EDLError):
            edl.validate(e)

    def test_resolve_is_relative_to_the_edl(self):
        e = small_edl()
        self.assertTrue(str(edl.resolve(e, "media/vo.mp3")).endswith("test-clip/media/vo.mp3"))
        self.assertEqual(str(edl.resolve(e, "/abs/x")), "/abs/x")


if __name__ == "__main__":
    unittest.main()
