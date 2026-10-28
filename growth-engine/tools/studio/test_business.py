"""Tests for studio/business.py (the hub business a client folder posts to)."""
import json

from .business import REPO, business_for
from .testbase import StudioCase


class BusinessFor(StudioCase):
    def brain(self, slug, data):
        d = self.root / "clients" / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "brain.json").write_text(json.dumps(data) if not isinstance(data, str) else data)

    def test_the_brain_names_the_business(self):
        self.brain("acme-en", {"hub": {"business": "acme"}})
        self.assertEqual(business_for("acme-en", self.root), "acme")

    def test_falls_back_to_the_slug(self):
        self.assertEqual(business_for("nobody", self.root), "nobody")
        for data in ({}, {"hub": None}, {"hub": {"business": ""}}, {"hub": "acme"}, "not json"):
            with self.subTest(data=data):
                self.brain("acme-x", data)
                self.assertEqual(business_for("acme-x", self.root), "acme-x")

    def test_given_wins(self):
        self.brain("acme-en", {"hub": {"business": "acme"}})
        self.assertEqual(business_for("acme-en", self.root, given="other"), "other")

    def test_the_english_account_posts_through_straightscale(self):
        self.assertEqual(business_for("straightscale-en", REPO), "straightscale")
