"""The 16 Oct decisions: CTA types, hard offers, B8, confession, styles, lengths, credits. Run: python3 -m unittest discover -s growth-engine/tools/organic_os -t growth-engine/tools"""
import copy
import unittest

import organic_os as o
from organic_os.testbase import BRAIN, DEMAND, MAP, card, codes, week_cards


class Decisions1016Test(unittest.TestCase):
    """Orchestrator decisions of 16 Oct 2026: CTAs (D-c), AI people (D-d), style ids (D-g), lengths (D-i), credits (STANDARDS 10)."""

    def check(self, brain=BRAIN, **kw):
        return o.card_check(card(**kw), brain, MAP, DEMAND)

    def convert(self, **kw):
        base = dict(job="convert", belief="B5", awareness="solution_aware", format="carousel_comparison", credit_budget=20,
                    pillar="Convert", hook_type="comparison")
        base.update(kw)
        return self.check(**base)

    def test_book_is_a_convert_cta_said_as_the_keyword_path(self):
        errs = [i for i in self.check(cta_type="book") if i["level"] == o.ERROR]
        self.assertTrue(any(i["code"] == "cta" and "convert posts only" in i["msg"] for i in errs))
        self.assertEqual(codes(self.convert(cta_type="book"), o.ERROR), [])
        self.assertEqual(codes(self.convert(cta_type="book", cta_keyword="AUDIT"), o.ERROR), [])
        self.assertIn("conversion", codes(self.convert(cta_type="book", cta_keyword="TEST"), o.ERROR))

    def test_comment_is_an_answer_not_a_keyword(self):
        self.assertIn("comment", o.CONFIG["jobs"]["reach"]["ctas"])
        self.assertIn("answer to a question", o.CONFIG["cta_types"]["comment"])
        self.assertEqual(codes(self.check(cta_type="comment"), o.WARN), [])
        self.assertIn("cta", codes(self.check(cta_type="comment", cta_keyword="AUDIT"), o.WARN))

    def test_hard_offer_is_a_convert_post_with_a_monthly_cap(self):
        self.assertIn("note", o.CONFIG["stage_mix"])
        self.assertIn("offer", codes(self.check(hard_offer=True), o.ERROR))
        self.assertNotIn("offer", codes(self.convert(cta_type="keyword", cta_keyword="AUDIT", hard_offer=True), o.ERROR))
        growing = copy.deepcopy(BRAIN)
        growing["package"]["account_stage"] = "growing"
        self.assertEqual(o.hard_offer_cap(o.CONFIG["stage_mix"]["growing"], growing), 1)
        w = week_cards()
        w[3]["hard_offer"] = True
        self.assertNotIn("offer", codes(o.week_check(w, growing)[0], o.ERROR))
        w[4]["hard_offer"] = True
        self.assertIn("offer", codes(o.week_check(w, growing)[0], o.ERROR))

    def test_b8_waits_for_the_offer_contents(self):
        b = copy.deepcopy(BRAIN)
        b["offer"]["delivers"] = "unknown: not written down"
        self.assertIn("truth", codes(self.convert(brain=b, belief="B8", awareness="most_aware", format="reel_podcast", format_tier="B",
                                                  credit_budget=250, cta_type="dm", story_template="podcast_disagreement",
                                                  length_target_s=40), o.WARN))

    def test_confession_needs_real_footage_and_no_ai_format_renders_it(self):
        for f in ("reel_ugc_pov", "reel_drama_pov"):
            self.assertNotIn("confession_pov", o.CONFIG["formats"][f]["story_templates"])
        self.assertTrue(o.CONFIG["story_templates"]["confession_pov"]["needs_real_footage"])
        iss = self.check(job="trust", belief="B3", format="reel_ugc_pov", format_tier="B", credit_budget=120,
                         story_template="confession_pov", cta_type="save")
        self.assertIn("truth", codes(iss, o.ERROR))
        self.assertIn("story", codes(iss, o.ERROR))

    def test_style_ids_name_no_studio(self):
        styles = set(o.CONFIG["animation_styles"]) - {"_doc"}
        self.assertEqual(styles, {"claymation", "crochet", "family_film_3d", "storybook_2d", "skeleton_xray", "anime_2d"})
        c = card(format="reel_animation_short", format_tier="B", credit_budget=90, story_template="pov_day", job="reach", belief="B1")
        self.assertEqual(codes(o.card_check(dict(c, animation_style="family_film_3d"), BRAIN, MAP, DEMAND), o.ERROR), [])
        self.assertIn("style", codes(o.card_check(dict(c, animation_style="pixar_style_3d"), BRAIN, MAP, DEMAND), o.ERROR))

    def test_lengths_come_from_standards_8(self):
        self.assertEqual(codes(self.check(length_target_s=20), o.WARN), [])
        self.assertIn("length", codes(self.check(length_target_s=120), o.ERROR))
        self.assertIn("length", codes(self.check(length_target_s=40), o.WARN))
        pod = dict(job="trust", belief="B4", awareness="solution_aware", format="reel_podcast", format_tier="B", credit_budget=250,
                   cta_type="save", story_template="podcast_disagreement")
        self.assertNotIn("length", codes(self.check(**pod, length_target_s=40)))
        self.assertIn("length", codes(self.check(**pod, length_target_s=60), o.WARN))

    def test_credit_ranges_follow_standards_10_and_the_adapters(self):
        fmts = o.CONFIG["formats"]
        carousel = o.STANDARDS["credits"]["carousel_7_to_12_slides"]
        for fid, f in fmts.items():
            if f["family"] == "carousel" and f["production"] == "still":
                self.assertEqual(f["credits"], carousel, fid)
        self.assertEqual(fmts["reel_podcast"]["credits"], [220, 320])
        self.assertEqual(fmts["reel_drama_pov"]["credits"], [180, 495])
        self.assertEqual(fmts["reel_song"]["credits"], [140, 355])
        self.assertEqual(fmts["reel_song"]["production"], "song")


if __name__ == "__main__":
    unittest.main()
