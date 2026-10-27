"""The card's ask: lead-magnet checks and keywords on reach posts. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import copy
import unittest

import organic_os as o
from organic_os.testbase import BRAIN, DEMAND, MAP, card, codes

ALL_PASS = {"main_pain": True, "one_thing": True, "quick_win": True, "leads_to_offer": True, "low_friction": True}


def brain_with(checks=None, delivers="a 30-minute audit with a written list of the three biggest leaks"):
    b = copy.deepcopy(BRAIN)
    b["lead_magnets"][0].update({"delivers": delivers, **({"checks": checks} if checks is not None else {})})
    return b


def keyword_card(job="trust"):
    return card(job=job, cta_type="keyword", cta_keyword="AUDIT", belief="B4")


class CardCtaTest(unittest.TestCase):
    def issues(self, brain, c=None):
        return o.card_check(c or keyword_card(), brain, MAP, DEMAND)

    def test_checked_magnet_passes(self):
        iss = self.issues(brain_with(ALL_PASS))
        self.assertNotIn("conversion", codes(iss))

    def test_unchecked_magnet_warns(self):
        iss = self.issues(brain_with())
        self.assertIn("conversion", codes(iss, o.WARN))
        self.assertNotIn("conversion", codes(iss, o.ERROR))

    def test_failed_check_blocks(self):
        iss = self.issues(brain_with({**ALL_PASS, "quick_win": False}))
        self.assertIn("conversion", codes(iss, o.ERROR))

    def test_unwritten_delivers_warns(self):
        iss = self.issues(brain_with(ALL_PASS, delivers="unknown: not written"))
        self.assertEqual(codes(iss, o.WARN).count("conversion"), 1)

    def test_keyword_on_a_reach_post_warns(self):
        self.assertIn("reach", codes(self.issues(brain_with(ALL_PASS), keyword_card("reach")), o.WARN))
        self.assertNotIn("reach", codes(self.issues(brain_with(ALL_PASS), keyword_card("trust"))))

    def test_schema_takes_checks_and_messaging(self):
        b = brain_with(ALL_PASS)
        b["messaging"] = {"status": "draft", "one_liner": "x", "value_props": ["a", "b", "c"]}
        self.assertEqual(o.brain_check(b, DEMAND)[0], [])


if __name__ == "__main__":
    unittest.main()
