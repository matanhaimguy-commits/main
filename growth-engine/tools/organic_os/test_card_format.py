"""A card's format against its beat (organic_os/card_format.py). Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import unittest

import organic_os as o
from organic_os.testbase import BRAIN, DEMAND, MAP, card, codes

MOTION = dict(format="reel_motion", format_tier="C", job="trust", belief="B4", usd_budget=1.0, credit_budget=None)


class CardFormatTest(unittest.TestCase):
    def check(self, cmap=MAP, **kw):
        c = card(**kw)
        if c.get("usd_budget") is not None:
            c.pop("credit_budget", None)
        return o.card_check(c, BRAIN, cmap, DEMAND)

    def test_motion_needs_a_list_data_or_type_beat(self):
        self.assertIn("beat", codes(self.check(**MOTION, load_bearing_beat="mechanism"), o.ERROR))
        self.assertIn("beat", codes(self.check(**MOTION, load_bearing_beat=None), o.ERROR))
        self.assertNotIn("beat", codes(self.check(**MOTION, load_bearing_beat="list")))
        self.assertNotIn("beat", codes(self.check(**MOTION, load_bearing_beat="mechanism", status="killed")))

    def test_missing_beat_warns_and_unknown_beat_fails_the_schema(self):
        self.assertIn("beat", codes(self.check(load_bearing_beat=None), o.WARN))
        self.assertIn("schema", codes(self.check(load_bearing_beat="vibes"), o.ERROR))

    def test_blocked_format_fails(self):
        iss = self.check(cmap={**MAP, "blocked_formats": ["reel_quote_broll"]})
        self.assertIn("format", codes(iss, o.ERROR))

    def test_ai_people_are_staged_never_clients_or_the_owner(self):
        ugc = dict(format="reel_ugc_talking", usd_budget=2.0, credit_budget=None)
        self.assertNotIn("ai_person", codes(self.check(**ugc, notes="staged UGC creator, AI label on")))
        for bad in ("a real client tells her story", "Testimonial from the creator", "the host plays the owner",
                    "Matan's twin explains"):
            with self.subTest(bad=bad):
                self.assertIn("ai_person", codes(self.check(**ugc, notes=bad), o.ERROR))
        self.assertNotIn("ai_person", codes(self.check(notes="a real client review on screen")))
        # naming the owner is not casting him (the F1 re-route notes cite his 28 Oct decision)
        for ok in ("the fallback Matan asked us to stop (28 Oct)", "Matan approved the format"):
            with self.subTest(ok=ok):
                self.assertNotIn("ai_person", codes(self.check(**ugc, notes=ok)))
        self.assertIn("ai_person", codes(self.check(**ugc, notes="the host plays Matan"), o.ERROR))


if __name__ == "__main__":
    unittest.main()
