"""Post Card check. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -p 'test_*.py'"""
import unittest

import organic_os as o
from organic_os.testbase import BRAIN, DEMAND, MAP, card, codes


class CardTest(unittest.TestCase):
    def check(self, **kw):
        return o.card_check(card(**kw), BRAIN, MAP, DEMAND)

    def test_good_card_passes(self):
        self.assertEqual(codes(self.check(), o.ERROR), [])

    def test_off_map_pillar_and_language(self):
        errs = codes(self.check(pillar="Lifestyle", account_language="en"), o.ERROR)
        self.assertIn("map", errs)
        self.assertIn("language", errs)

    def test_keyword_needs_a_live_flow(self):
        self.assertIn("conversion", codes(self.check(job="trust", belief="B3", cta_type="keyword", cta_keyword="TEST",
                                                     format="carousel_self_check", credit_budget=10), o.ERROR))
        self.assertEqual(codes(self.check(job="trust", belief="B3", cta_type="keyword", cta_keyword="AUDIT",
                                          format="carousel_self_check", credit_budget=10), o.ERROR), [])

    def test_cta_must_fit_the_job(self):
        self.assertIn("cta", codes(self.check(cta_type="book"), o.ERROR))

    def test_tier_a_needs_a_proven_angle_or_the_wildcard(self):
        self.assertIn("spend", codes(self.check(format="reel_song", format_tier="A", credit_budget=250), o.ERROR))
        self.assertNotIn("spend", codes(self.check(format="reel_song", format_tier="A", credit_budget=250, wildcard=True), o.ERROR))

    def test_b6_needs_permitted_proof_or_the_build(self):
        base = dict(job="convert", belief="B6", awareness="product_aware", format="reel_strategist_prop", format_tier="B",
                    credit_budget=100, cta_type="keyword", cta_keyword="AUDIT", pillar="Convert")
        self.assertIn("truth", codes(self.check(**base), o.ERROR))
        self.assertIn("truth", codes(self.check(**base, proof_used=["P2"]), o.ERROR))
        self.assertEqual(codes(self.check(**base, proof_used=["P1"]), o.ERROR), [])
        self.assertEqual(codes(self.check(**base, series="The Build"), o.ERROR), [])

    def test_real_footage_formats_need_real_people(self):
        self.assertIn("format", codes(self.check(job="trust", belief="B7", format="carousel_bts", cta_type="follow"), o.ERROR))

    def test_story_template_and_style_must_fit_the_format(self):
        c = card(format="reel_animation_short", format_tier="B", credit_budget=90, story_template="pov_day",
                 animation_style="claymation", job="reach", belief="B1")
        self.assertEqual(codes(o.card_check(c, BRAIN, MAP, DEMAND), o.ERROR), [])
        bad = dict(c, story_template="podcast_disagreement", animation_style="anime")
        self.assertEqual(codes(o.card_check(bad, BRAIN, MAP, DEMAND), o.ERROR).count("story"), 1)
        self.assertIn("style", codes(o.card_check(bad, BRAIN, MAP, DEMAND), o.ERROR))
        self.assertIn("style", codes(o.card_check(dict(c, animation_style=None), BRAIN, MAP, DEMAND), o.ERROR))

    def test_story_card_routes_only_to_story_formats(self):
        r = o.route(card(story_template="pov_day", job="reach", belief="B1"), BRAIN, MAP)
        fmts = [x["format"] for x in r]
        self.assertTrue(fmts)
        for f in fmts:
            self.assertIn("pov_day", o.CONFIG["formats"][f]["story_templates"])
        self.assertNotIn("reel_drama_pov", fmts)  # tier A needs a proven angle or the wildcard
        r = o.route(card(story_template="pov_day", job="reach", belief="B1", animation_style="crochet", wildcard=True), BRAIN, MAP)
        self.assertEqual({x["format"] for x in r}, {"reel_animation", "reel_animation_short"})

    def test_off_map_demand_phrase_kills_the_idea(self):
        self.assertIn("demand", codes(self.check(demand_phrase="off topic"), o.ERROR))
        self.assertIn("demand", codes(self.check(demand_phrase="something new"), o.WARN))

    def test_schema_rejects_unknown_fields_and_bad_ids(self):
        self.assertIn("schema", codes(self.check(post_id="bad"), o.ERROR))


if __name__ == "__main__":
    unittest.main()
