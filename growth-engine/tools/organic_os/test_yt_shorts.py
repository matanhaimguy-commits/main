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


if __name__ == "__main__":
    unittest.main()
