"""Weekly rules. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -p 'test_*.py'"""
import unittest

import organic_os as o
from organic_os.testbase import BRAIN, codes, week_cards


class WeekTest(unittest.TestCase):
    def week(self):
        return week_cards()

    def test_good_week(self):
        issues, summary = o.week_check(self.week(), BRAIN)
        self.assertEqual(codes(issues, o.ERROR), [])
        self.assertEqual(summary["families"], {"reel": 3, "carousel": 3, "image": 1})

    def test_same_format_two_days_in_a_row_fails(self):
        w = self.week()
        w[1]["format"] = "reel_motion"
        self.assertIn("rotation", codes(o.week_check(w, BRAIN)[0], o.ERROR))

    def test_missing_b7_and_contrarian_are_flagged(self):
        w = self.week()
        w[0]["hook_type"] = "myth"
        w[5]["belief"] = "B3"
        warns = [i["msg"] for i in o.week_check(w, BRAIN)[0]]
        self.assertTrue(any("contrarian" in m for m in warns))
        self.assertTrue(any("B7" in m for m in warns))

    def test_two_hard_offers_in_a_month_fail_for_new_accounts(self):
        w = self.week()
        w[3]["hard_offer"] = True
        w[4]["hard_offer"] = True
        self.assertIn("offer", codes(o.week_check(w, BRAIN)[0], o.ERROR))


if __name__ == "__main__":
    unittest.main()
