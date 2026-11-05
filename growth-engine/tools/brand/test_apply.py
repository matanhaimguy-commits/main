"""Tests for brand/apply.py: the field mapping, sources, and what is refused."""
import unittest

from brainio import paths, validate
from brainio.testbase import BrainCase
from brand import apply as ap

DAY = "2026-10-29"
SRC = "Matan (Brand card, 2026-10-29)"
ALL = {"offer": "Bread subscription", "icp": "Busy families near the shop", "promise": "Fresh loaf at your door every week",
       "mechanism": "The 48-hour sourdough", "voice": "warm, direct", "never_say": "no health claims\nno discounts",
       "proof_bank": ["500 loaves a week"], "cta_keyword": "LOAF", "monthly_cap_usd": 90, "cadence": 4}


class Apply(BrainCase):
    def test_every_field_lands_at_its_path_with_a_source(self):
        new, changes, problems = ap.apply(self.brain(), ALL, DAY)
        self.assertEqual(problems, [])
        self.assertEqual(len(changes), 10)
        for path, want in (("offer.main_offer", "Bread subscription"), ("avatars[0].situation", "Busy families near the shop"),
                           ("offer.delivers", "Fresh loaf at your door every week"), ("mechanism.ums", "The 48-hour sourdough"),
                           ("voice.adjectives", ["warm", "direct"]), ("constraints.cannot_say", ["no health claims", "no discounts"]),
                           ("offer.keyword", "LOAF"), ("package.monthly_usd_cap", 90), ("package.posts_per_week", 4)):
            self.assertEqual(paths.get(new, path), want, path)
            self.assertEqual(new["field_sources"][path], SRC, path)
        self.assertEqual(new["proof_bank"][0]["source"], SRC)
        self.assertEqual(new["field_sources"]["proof_bank"], SRC)
        self.assertEqual(new["updated"], DAY)
        self.assertEqual(validate.errors(new), [])

    def test_the_input_brain_is_not_changed(self):
        b = self.brain()
        ap.apply(b, ALL, DAY)
        self.assertEqual(b, self.brain())

    def test_same_values_again_change_nothing(self):
        once, _, _ = ap.apply(self.brain(), ALL, DAY)
        twice, changes, _ = ap.apply(once, ALL, "2026-11-02")
        self.assertEqual(changes, [])
        self.assertEqual(twice["updated"], DAY)

    def test_only_the_fields_sent_change(self):
        new, changes, _ = ap.apply(self.brain(), {"cadence": 3}, DAY)
        self.assertEqual([c["field"] for c in changes], ["cadence"])
        self.assertEqual(new["offer"], self.brain()["offer"])

    def test_unknown_field_and_bad_values_are_problems(self):
        _, _, problems = ap.apply(self.brain(), {"colour": "red", "cadence": 0, "monthly_cap_usd": -3}, DAY)
        self.assertEqual(len(problems), 3)
        self.assertTrue(any("colour: not a Brand card field" in p for p in problems))

    def test_icp_creates_the_first_avatar_when_there_is_none(self):
        b = self.brain()
        b["avatars"] = []
        new, _, problems = ap.apply(b, {"icp": "Office managers"}, DAY)
        self.assertEqual(problems, [])
        self.assertEqual(new["avatars"][0]["id"], "AV-01")
        self.assertEqual(validate.errors(new), [])

    def test_cap_can_be_cleared(self):
        b = self.brain()
        b["package"]["monthly_usd_cap"] = 50
        new, _, _ = ap.apply(b, {"monthly_cap_usd": None}, DAY)
        self.assertIsNone(new["package"]["monthly_usd_cap"])
