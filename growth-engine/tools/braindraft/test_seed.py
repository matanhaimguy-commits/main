"""Tests for braindraft/seed.py: the slim intake's facts, with sources, never over a filled value."""
import json
import unittest

from brainio import validate
from brainio.testbase import BrainCase
from braindraft import seed
from intake import slim
from intake.test_slim import slim_row


class Seed(BrainCase):
    def slim(self):
        return slim.normalize(slim_row())

    def test_seeds_the_typed_facts_with_sources(self):
        new, seeds = seed.seed(self.brain(), self.slim(), "acme")
        self.assertEqual(new["client"], "Sample Bakery")
        self.assertEqual(new["account"], "@sample_bakery (Instagram) https://sample-bakery.example")
        self.assertEqual(new["offer"]["main_offer"], "Sourdough bread subscription, 30 USD a month")
        self.assertEqual(new["visual"]["face"], "faceless")
        self.assertEqual(new["hub"]["business"], "sample-bakery")
        for p in ("client", "account", "offer.main_offer", "visual.face"):
            self.assertTrue(new["field_sources"][p].startswith("client intake"), p)
        self.assertEqual(validate.errors(new), [])
        self.assertEqual(seeds["competitors"], ["Corner Loaf", "https://rival-bakery.example"])
        self.assertEqual(seeds["consents"], {"ai_people": False, "proof": True})

    def test_never_overwrites_a_filled_field(self):
        b = self.brain()
        b["offer"]["main_offer"] = "Already drafted from the brand guide"
        new, _ = seed.seed(b, self.slim(), "acme")
        self.assertEqual(new["offer"]["main_offer"], "Already drafted from the brand guide")
        self.assertNotIn("offer.main_offer", new["field_sources"])

    def test_ai_consent_yes_or_unknown_leaves_the_face_alone(self):
        for v in (True, None):
            s = self.slim()
            s["consents"]["ai_people"] = v
            new, _ = seed.seed(self.brain(), s, "acme")
            self.assertEqual(new["visual"]["face"], "faceless")  # the template default is kept, no source claimed
            self.assertNotIn("visual.face", new["field_sources"])

    def test_handle_forms(self):
        self.assertEqual(seed.handle("@sample_bakery"), "@sample_bakery")
        self.assertEqual(seed.handle("https://www.instagram.com/sample.bakery/?hl=en"), "@sample.bakery")
        self.assertEqual(seed.handle(""), "")
