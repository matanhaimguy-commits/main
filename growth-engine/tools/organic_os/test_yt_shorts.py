"""YouTube Shorts import. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

import organic_os as o
from organic_os.yt_shorts import parse_views, to_items

PAGE = {"content": {"results": [
    {"videoId": "a1", "title": "Stop pricing your work based on what you'd pay for it.", "viewCountText": "42K views"},
    {"videoId": "a2", "title": "Big one", "viewCountText": "1.2M views"},
    {"videoId": "a3", "title": "Members", "viewCountText": None, "members_only": True},
    {"videoId": "a4", "title": "Small", "viewCountText": "4,800 views"},
]}}


class YtShortsTest(unittest.TestCase):
    def test_parse_views(self):
        self.assertEqual(parse_views("42K views"), 42_000)
        self.assertEqual(parse_views("1.2M views"), 1_200_000)
        self.assertEqual(parse_views("4,800 views"), 4_800)
        self.assertIsNone(parse_views("No views"))
        self.assertIsNone(parse_views(None))

    def test_to_items_skips_hidden_and_feeds_outliers(self):
        items = to_items([PAGE], "@AlexHormozi")
        self.assertEqual([i["url"][-2:] for i in items], ["a1", "a2", "a4"])
        self.assertEqual(items[0]["ownerUsername"], "AlexHormozi")
        rows = {r["url"][-2:]: r for r in o.outliers(items, days=None)}
        self.assertEqual(rows["a2"]["x_median"], round(1_200_000 / 42_000, 2))

    def test_shorts_are_views_only_without_comment_counts(self):
        items = to_items([PAGE], "@AlexHormozi")
        self.assertTrue(all(i["views_only"] for i in items))
        rows = {r["url"][-2:]: r for r in o.outliers(items, days=None)}
        big = rows["a2"]
        self.assertEqual(big["basis"], "views_only")
        self.assertFalse(big["trusted"])
        self.assertTrue(big["views_3x"] and big["partial_outlier"])
        self.assertIn("comment counts", big["skipped"])

    def test_counts_file_gives_a_short_the_full_check(self):
        counts = {"a1": {"comments": 40, "likes": 900}, "a2": {"comments": 6000, "likes": 50000}, "a4": {"comments": 10, "likes": 200}}
        items = to_items([PAGE], "@AlexHormozi", counts)
        self.assertFalse(any(i.get("views_only") for i in items))
        rows = {r["url"][-2:]: r for r in o.outliers(items, days=None)}
        self.assertEqual(rows["a2"]["basis"], "views")
        self.assertNotIn("skipped", rows["a2"])
        self.assertTrue(rows["a2"]["trusted"])

    def test_mixed_account_comment_rate_ignores_views_only_posts(self):
        items = to_items([PAGE], "@AlexHormozi", {"a1": {"comments": 40, "likes": 900}})
        rows = {r["url"][-2:]: r for r in o.outliers(items, days=None)}
        self.assertEqual(rows["a1"]["account_comments_per_1k"], round(40 / 42000 * 1000, 2))
        self.assertEqual(rows["a4"]["basis"], "views_only")


if __name__ == "__main__":
    unittest.main()
