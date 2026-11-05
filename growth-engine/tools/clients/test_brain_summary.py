"""Tests for clients/brain_summary.py."""
import unittest

from clients import brain_summary
from clients.testbase import SLUG, ClientsCase


class BrainSummary(ClientsCase):
    def test_summary_keeps_the_dashboard_fields_and_open_decisions_only(self):
        s = brain_summary.summary(brain_summary.load(self.root, SLUG))
        self.assertEqual(s["offer"]["keyword"], "AUDIT")
        self.assertEqual(s["avatars"], [{"id": "AV-01", "name": "Ana", "role": "owner"}])
        self.assertEqual(s["awareness"], {"stage": "problem_aware", "sophistication": "S3"})
        self.assertEqual(s["voice"], {"adjectives": ["calm"], "banned": ["hype"]})
        self.assertEqual(s["package"]["monthly_usd_cap"], 50)
        self.assertNotIn("monthly_credit_cap", s["package"])
        self.assertEqual(s["decisions_open"], [{"id": "E1", "question": "Name the method?", "interim": "unnamed"}])

    def test_no_brain_is_an_empty_summary(self):
        self.assertEqual(brain_summary.summary(brain_summary.load(self.root, "nobody"))["avatars"], [])


if __name__ == "__main__":
    unittest.main()
