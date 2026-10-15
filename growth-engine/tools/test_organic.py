"""Tests for organic.py. Run: python3 -m unittest growth-engine/tools/test_organic.py"""
import copy
import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import organic as o  # noqa: E402

BRAIN = {
    "client": "acme", "updated": "2026-10-15",
    "business_model": {"sells": "audits", "sales_process": "call", "capacity": "unknown"},
    "offer": {"main_offer": "free audit", "next_step": "comment AUDIT", "keyword": "AUDIT", "delivers": "a 30-minute audit"},
    "avatars": [{"id": "AV-01", "name": "Ana", "role": "owner", "situation": "busy", "words": ["x"], "fears": ["y"], "desires": ["z"]}],
    "awareness": {"stage": "problem_aware", "sophistication": "3"},
    "mechanism": {"ump": "Patchwork", "ums": "System", "steps": ["Find", "Own"]},
    "belief_ladder": [{"id": f"B{i}", "statement": "s", "state": "unknown"} for i in range(1, 9)],
    "contrarian_vault": [{"id": "C1", "position": "p", "source": "owner"}],
    "proof_bank": [{"id": "P1", "type": "result", "text": "t", "source": "s", "permission": "yes"},
                   {"id": "P2", "type": "result", "text": "t", "source": "s", "permission": "pending"}],
    "lead_magnets": [{"keyword": "AUDIT", "resource": "audit", "delivers": "30 min", "live": True},
                     {"keyword": "TEST", "resource": "quiz", "live": False}],
    "voice": {"adjectives": ["calm"], "samples": [], "banned": ["hype"], "language": "sq", "register": "ti"},
    "visual": {"colors": {}, "fonts": [], "logo_files": [], "face": "ai_character", "ai_label": "unknown", "real_footage": False},
    "market": {"language": "sq", "country": "AL"},
    "constraints": {"cannot_say": ["prices"]},
    "baseline": {"followers": None, "as_of": None},
    "package": {"posts_per_week": 7, "account_stage": "new", "monthly_credit_cap": 1200},
}
MAP = {"pillars": [{"name": "Find"}, {"name": "Convert"}], "series": [{"name": "The Build", "pillar": "Convert"}, {"name": "One Step", "pillar": "Find"}],
       "buyer_formats": []}
DEMAND = [{"phrase": "na shkruajne po nuk blejne", "tag": "direct"}, {"phrase": "off topic", "tag": "off_map"}]


def card(**kw):
    c = {"post_id": "AC-2026-10-W3-01", "client": "acme", "account_language": "sq", "slot": "2026-10-19 19:30",
         "pillar": "Find", "series": None, "episode": None, "job": "reach", "belief": "B1", "avatar": "AV-01",
         "awareness": "problem_aware", "demand_phrase": "na shkruajne po nuk blejne", "idea_source": "outlier",
         "source_ref": "@x 3.4x", "narrow_product": "the exact first reply to send", "format": "reel_quote_broll",
         "format_tier": "C", "angle_proven": False, "credit_budget": 30, "length_target_s": 30, "hook_type": "contrarian",
         "emotion": "surprise", "cta_type": "send", "cta_keyword": None, "lead_magnet": None, "proof_used": [],
         "hypothesis": "contrarian line gets more sends", "success_metric": "sends_per_reach", "target": ">= median x1.5",
         "status": "planned"}
    c.update(kw)
    return c


def codes(issues, level=None):
    return [i["code"] for i in issues if level is None or i["level"] == level]


class BrainTest(unittest.TestCase):
    def test_complete_enough_brain_has_no_blockers_but_lists_gaps(self):
        issues, gaps = o.brain_check(BRAIN, DEMAND)
        self.assertEqual(codes(issues, o.ERROR), [])
        fields = [g["field"] for g in gaps]
        for f in ("business_model.capacity", "demand_map", "contrarian_vault", "visual.ai_label", "baseline", "lead_magnets[TEST]"):
            self.assertIn(f, fields)

    def test_missing_offer_blocks(self):
        b = copy.deepcopy(BRAIN)
        b["offer"]["main_offer"] = "TBD"
        issues, _ = o.brain_check(b, DEMAND)
        self.assertIn("blocking", codes(issues, o.ERROR))


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


class WeekTest(unittest.TestCase):
    def week(self):
        days = ["2026-10-19", "2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25"]
        spec = [("reel_quote_broll", "reach", "B1", "send", "contrarian"), ("carousel_framework", "trust", "B4", "save", "teaching"),
                ("reel_quote_broll", "reach", "B2", "comment", "hidden_cause"), ("carousel_self_check", "convert", "B3", "keyword", "self_check"),
                ("reel_strategist_prop", "reach", "B1", "send", "myth"), ("image_question", "trust", "B7", "comment", "question"),
                ("carousel_mistakes", "reach", "B1", "save", "list")]
        return [card(slot=f"{d} 19:30", format=f, job=j, belief=b, cta_type=cta, hook_type=h, cta_keyword="AUDIT" if cta == "keyword" else None)
                for d, (f, j, b, cta, h) in zip(days, spec)]

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


class RouteTest(unittest.TestCase):
    def test_reach_prefers_reels_and_skips_tier_a_and_real_footage(self):
        opts = o.route(card(job="reach", belief="B1"), BRAIN, MAP)
        fams = [x["family"] for x in opts]
        self.assertEqual(fams[0], "reel")
        self.assertNotIn("A", [x["tier"] for x in opts])
        self.assertNotIn("reel_bts_real", [x["format"] for x in opts])

    def test_proven_angle_unlocks_tier_a_and_budget_and_rotation_filter(self):
        opts = o.route(card(job="reach", belief="B1", angle_proven=True), BRAIN, MAP)
        self.assertIn("A", [x["tier"] for x in opts])
        tight = o.route(card(job="reach", belief="B1", angle_proven=True), BRAIN, MAP, spent=1150)
        self.assertTrue(all(x["credits"][1] <= 50 for x in tight))
        no_reels = o.route(card(job="reach", belief="B1"), BRAIN, MAP, prev_family="reel")
        self.assertNotIn("reel", [x["family"] for x in no_reels])


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
