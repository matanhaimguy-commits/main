"""Outlier mining (the four checks). Run: python3 -m unittest discover -s growth-engine/tools/organic_os -p 'test_*.py'"""
import datetime as dt
import unittest

import organic_os as o


class OutlierTest(unittest.TestCase):
    def test_four_checks(self):
        now = dt.datetime(2026, 10, 15, tzinfo=dt.timezone.utc)
        base = [{"ownerUsername": "eri", "url": f"u{i}", "videoViewCount": 1000, "likesCount": 40, "commentsCount": 2,
                 "timestamp": "2026-10-01T10:00:00Z"} for i in range(6)]
        hit = {"ownerUsername": "eri", "url": "hit", "videoViewCount": 5000, "likesCount": 220, "commentsCount": 30, "timestamp": "2026-10-02T10:00:00Z"}
        boosted = {"ownerUsername": "eri", "url": "boost", "videoViewCount": 9000, "likesCount": 20, "commentsCount": 1, "timestamp": "2026-10-03T10:00:00Z"}
        old = {"ownerUsername": "eri", "url": "old", "videoViewCount": 90000, "likesCount": 5000, "commentsCount": 900, "timestamp": "2026-01-01T10:00:00Z"}
        rows = {r["url"]: r for r in o.outliers(base + [hit, boosted, old], days=90, now=now)}
        self.assertTrue(rows["hit"]["trusted"])
        self.assertFalse(rows["boost"]["trusted"])  # big views, no engagement: paid boost pattern
        self.assertNotIn("old", rows)

    def test_carousels_without_views_are_partial(self):
        items = [{"ownerUsername": "a", "url": f"c{i}", "likesCount": 10} for i in range(5)] + [{"ownerUsername": "a", "url": "big", "likesCount": 60}]
        rows = {r["url"]: r for r in o.outliers(items, days=None)}
        self.assertEqual(rows["big"]["basis"], "likes_only")
        self.assertTrue(rows["big"]["partial_outlier"])
        self.assertFalse(rows["big"]["trusted"])

    def test_hidden_likes_are_unknown_not_zero(self):
        base = [{"ownerUsername": "eri", "url": f"u{i}", "videoViewCount": 1000, "likesCount": 40, "commentsCount": 2} for i in range(6)]
        hidden = {"ownerUsername": "eri", "url": "hid", "videoViewCount": 5000, "likesCount": -1, "commentsCount": 30}
        rows = {r["url"]: r for r in o.outliers(base + [hidden], days=None)}
        r = rows["hid"]
        self.assertTrue(r["likes_hidden"])
        self.assertIsNone(r["likes"])
        self.assertIsNone(r["likes_in_proportion"])  # can't be checked, so not failed either
        self.assertTrue(r["views_3x"] and r["comments_above_rate"])
        self.assertFalse(r["trusted"])  # all four must pass (5.1)
        self.assertTrue(r["partial_outlier"])  # check it by hand
        self.assertEqual(rows["u0"]["likes_in_proportion"], True)

    def test_hidden_likes_stay_out_of_the_medians(self):
        items = [{"ownerUsername": "a", "url": f"c{i}", "likesCount": 10} for i in range(3)]
        items += [{"ownerUsername": "a", "url": f"h{i}", "likesCount": -1} for i in range(4)]
        items += [{"ownerUsername": "a", "url": "big", "likesCount": 60}]
        rows = {r["url"]: r for r in o.outliers(items, days=None)}
        self.assertEqual(rows["big"]["x_median"], 6.0)  # 60 against the median of the shown likes (10), not 5
        self.assertIsNone(rows["h0"]["x_median"])
        self.assertFalse(rows["h0"]["partial_outlier"])


if __name__ == "__main__":
    unittest.main()
