"""Step 5 line table, line times and slices (song_timeline/). Run from growth-engine/tools:
python3 -m unittest test_song_timeline"""
import unittest

from song_timeline import lines, lyrics

MD = """| Id | Section | Words |
|---|---|---|
| O30-L01 | Verse | Lumpy months? It was never |
| O30-L02 | Chorus | That's patchwork, buyers' words. |
| O60-L01 | Verse | Not this one |
"""


class SongTimeline(unittest.TestCase):
    def test_read_lines_keeps_apostrophes_and_prefix(self):
        rows = lyrics.read_lines(MD, "O30")
        self.assertEqual([r["id"] for r in rows], ["O30-L01", "O30-L02"])
        self.assertEqual(rows[1]["tokens"], ["that's", "patchwork", "buyers", "words"])

    def test_line_times_consume_words_in_order(self):
        rows = lyrics.read_lines(MD, "O30")
        words = [{"word": t, "start": i, "end": i + 0.5} for i, t in enumerate(rows[0]["tokens"] + rows[1]["tokens"])]
        timed = lines.line_times(rows, words)
        self.assertEqual((timed[0]["start"], timed[0]["end"]), (0, 4.5))
        self.assertEqual((timed[1]["start"], timed[1]["end"]), (5, 8.5))

    def test_snap_prefers_a_beat_in_the_gap(self):
        self.assertEqual(lines.snap(10.0, 11.0, [9.0, 10.4, 10.6, 12.0]), 10.4)
        self.assertEqual(lines.snap(10.0, 11.0, [12.0]), 10.5)

    def test_slices_stay_within_5_to_15_seconds(self):
        timed = [{"id": f"L{i}", "start": i * 3.0, "end": i * 3.0 + 2.8} for i in range(10)]
        plan = lines.slices(timed, [], 30.0, "O30")
        self.assertTrue(all(5 <= s["length"] <= 15 for s in plan), plan)
        self.assertEqual(sum(len(s["lines"]) for s in plan), 10)
        self.assertEqual((plan[0]["start"], plan[-1]["end"]), (0.0, 30.0))


if __name__ == "__main__":
    unittest.main()
