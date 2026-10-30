"""Funnel stage: the default from the job, and card-check's warning. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

import organic_os as o
from organic_os.funnel import default_stage, funnel_issues, stage_of
from organic_os.testbase import BRAIN, DEMAND, MAP, card, codes


class FunnelTest(unittest.TestCase):
    def test_default_follows_the_job(self):
        self.assertEqual([default_stage(j) for j in ("reach", "trust", "convert", None)], ["TOF", "MOF", "BOF", None])
        self.assertEqual(stage_of({"job": "trust"}), "MOF")
        self.assertEqual(stage_of({"job": "trust", "funnel_stage": "BOF"}), "BOF")

    def test_missing_or_disagreeing_stage_warns(self):
        self.assertIn("defaults to TOF", funnel_issues({"job": "reach"})[0]["msg"])
        self.assertIn("usually MOF", funnel_issues({"job": "trust", "funnel_stage": "TOF"})[0]["msg"])
        self.assertEqual(funnel_issues({"job": "convert", "funnel_stage": "BOF"}), [])

    def test_card_check_takes_the_field_and_warns(self):
        good = o.card_check(card(funnel_stage="TOF"), BRAIN, MAP, DEMAND)
        self.assertNotIn("funnel", codes(good, o.WARN))
        self.assertIn("funnel", codes(o.card_check(card(funnel_stage="BOF"), BRAIN, MAP, DEMAND), o.WARN))
        self.assertIn("schema", codes(o.card_check(card(funnel_stage="TOP"), BRAIN, MAP, DEMAND), o.ERROR))

    def test_card_takes_a_project(self):
        c = card(funnel_stage="TOF", project="motion-studio/projects/acme-01")
        self.assertEqual(codes(o.card_check(c, BRAIN, MAP, DEMAND), o.ERROR), [])


if __name__ == "__main__":
    unittest.main()
