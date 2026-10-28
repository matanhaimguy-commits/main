"""First spoken sentence. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

from organic_os.testbase import BRAIN  # noqa: F401  (puts tools/ on the path)
from organic_os.first_line import add_hooks, first_sentence, hook_of


class FirstLineTest(unittest.TestCase):
    def test_first_sentence_of_transcript(self):
        h = hook_of({"transcript": "Cold email?  Most people get it wrong. Here's why.", "caption": "Ranking channels"})
        self.assertEqual(h, {"hook": "Cold email?", "hook_source": "transcript"})

    def test_segments(self):
        h = hook_of({"transcript": [{"text": "Sales."}, {"text": "The worst job."}]})
        self.assertEqual(h["hook"], "Sales.")

    def test_caption_fallback_is_marked(self):
        h = hook_of({"caption": "\n  Ranking jobs by damage\nmore text"})
        self.assertEqual(h, {"hook": "Ranking jobs by damage", "hook_source": "caption"})
        self.assertEqual(hook_of({})["hook_source"], "none")

    def test_join_by_url_or_shortcode(self):
        rows = add_hooks([{"url": "u1"}, {"url": "SC2"}], [{"url": "u1", "transcript": "A. B."}, {"shortCode": "SC2", "caption": "Cap"}])
        self.assertEqual([r["hook"] for r in rows], ["A.", "Cap"])

    def test_no_text(self):
        self.assertEqual(first_sentence("   "), "")


if __name__ == "__main__":
    unittest.main()
