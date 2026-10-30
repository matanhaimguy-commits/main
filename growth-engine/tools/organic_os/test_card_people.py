"""The owner only as his twin, only on twin_host cards (organic_os/card_people.py, D-T1). Run: python3 -m unittest
discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

import organic_os as o
from organic_os.card_people import AI_PEOPLE, people_issues, twin_issues
from organic_os.testbase import BRAIN, DEMAND, MAP, card, codes

HOST = {"engine": "heygen", "looks": [{"id": "L1"}], "voices": [{"id": "V1"}]}
UGC = dict(format="reel_ugc_talking", usd_budget=2.0, credit_budget=None)


class TwinHostTest(unittest.TestCase):
    def check(self, brain=BRAIN, **kw):
        c = card(**kw)
        if c.get("usd_budget") is not None:
            c.pop("credit_budget", None)
        return o.card_check(c, brain, MAP, DEMAND)

    def test_the_review_gaps_are_on_camera_formats(self):
        self.assertTrue({"reel_strategist_prop", "reel_talking_head_real"} <= AI_PEOPLE)
        for fmt in ("reel_strategist_prop", "reel_talking_head_real"):
            with self.subTest(fmt=fmt):
                self.assertEqual(codes(people_issues({"format": fmt, "notes": "a real client tells it"}), o.ERROR),
                                 ["ai_person"])

    def test_the_twin_as_the_owner_needs_twin_host(self):
        for text in ("Matan's twin explains the fix", "the HeyGen twin hosts", "the avatar plays the founder",
                     "speaks as Matan"):
            with self.subTest(text=text):
                self.assertIn("ai_person", codes(self.check(**UGC, notes=text), o.ERROR))
                self.assertIn("ai_person", codes(self.check(notes=text), o.ERROR))   # any format
                self.assertNotIn("ai_person", codes(self.check(brain={**BRAIN, "host": HOST}, **UGC, notes=text,
                                                               twin_host=True)))

    def test_twin_host_never_allows_a_client_or_customer(self):
        iss = self.check(brain={**BRAIN, "host": HOST}, **UGC, twin_host=True, notes="the twin plays a happy client")
        self.assertIn("ai_person", codes(iss, o.ERROR))

    def test_twin_host_needs_a_host_block(self):
        self.assertIn("twin_host", codes(self.check(**UGC, twin_host=True), o.ERROR))
        self.assertEqual(twin_issues({"twin_host": True}, {"host": HOST}), [])
        self.assertEqual(twin_issues({"twin_host": False}, {}), [])

    def test_twin_host_must_be_a_boolean(self):
        self.assertIn("schema", codes(self.check(twin_host="yes"), o.ERROR))


if __name__ == "__main__":
    unittest.main()
