"""Checks the bank builds cleanly: python3 -m unittest discover -s motion-studio/refbank/tools -p 'test_*.py'"""
import io, json, os, sys, unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import refbank


class BankBuild(unittest.TestCase):
    def test_build_has_no_warnings(self):
        out = io.StringIO()
        with redirect_stdout(out):
            code = refbank.build()
        self.assertEqual(code, 0, out.getvalue())
        self.assertNotIn('WARN', out.getvalue())

    def test_index_matches_cards(self):
        cards = refbank.load_cards()
        index = json.load(open(refbank.INDEX))
        self.assertEqual(index['count'], len(cards))
        self.assertEqual(len({c['id'] for c in cards}), len(cards))

    def test_file_name_is_id(self):
        for c in refbank.load_cards():
            self.assertEqual(c['file'], f"cards/{c['id']}.md")


class YouTubeProof(unittest.TestCase):
    """yt- cards are proven by a breakout over their own channel's median (ORGANIC-OS outlier logic)."""

    def test_median_and_multiple(self):
        yt = [c for c in refbank.load_cards() if c['id'].startswith('yt-')]
        self.assertTrue(yt)
        for c in yt:
            self.assertEqual(c['platform'], 'youtube', c['id'])
            self.assertGreater(c.get('channel_median_views') or 0, 0, c['id'])
            self.assertGreaterEqual(c.get('x_median') or 0, 3, c['id'])
            self.assertAlmostEqual(c['plays'] / c['channel_median_views'], c['x_median'], delta=0.05, msg=c['id'])


if __name__ == '__main__':
    unittest.main()
