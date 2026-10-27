"""Scorecard and diagnosis. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -p 'test_*.py'"""
import unittest

import organic_os as o


class ScoreTest(unittest.TestCase):
    def rows(self):
        r = []
        for i in range(5):
            r.append({"post_id": f"p{i}", "job": "trust", "reach": "1000", "views": "1500", "likes": "30", "comments": "3", "saves": "10",
                      "sends": "5", "profile_visits": "20", "follows": "2", "avg_watch_s": "8", "skip_rate": "0.5"})
        r.append({"post_id": "win", "job": "trust", "reach": "1000", "views": "6000", "likes": "200", "comments": "40", "saves": "40",
                  "sends": "20", "profile_visits": "60", "follows": "12", "avg_watch_s": "12", "skip_rate": "0.3"})
        r.append({"post_id": "flat", "job": "trust", "reach": "1000", "views": "1500", "likes": "30", "comments": "3", "saves": "2",
                  "sends": "1", "profile_visits": "20", "follows": "2", "avg_watch_s": "10", "skip_rate": "0.5"})
        r.append({"post_id": "lead", "job": "convert", "reach": "800", "views": "1000", "dms": "3", "qualified_dms": "2", "booked": "1"})
        return r

    def test_flags_and_diagnosis(self):
        res = {s["post_id"]: s for s in o.score(self.rows())}
        self.assertEqual(res["win"]["flag"], "template")
        self.assertEqual(res["lead"]["flag"], "template")  # any booked analysis promotes
        self.assertIn("value not unique", res["flat"]["diagnosis"])
        self.assertEqual(res["p0"]["flag"], "")


if __name__ == "__main__":
    unittest.main()
