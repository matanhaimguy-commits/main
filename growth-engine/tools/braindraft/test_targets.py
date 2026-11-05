"""Tests for braindraft/targets.py and checklist.py: all 38 questions are on the checklist, none is asked of the client."""
import json
import unittest

from brainio import paths
from brainio.testbase import BrainCase
from braindraft import checklist
from braindraft.targets import TARGETS


class Targets(BrainCase):
    def test_every_question_has_a_line_and_no_stale_ones(self):
        ids = {q["id"] for q in json.loads(checklist.QUESTIONS.read_text())["questions"]}
        self.assertEqual(ids, set(TARGETS))
        self.assertEqual(len(ids), 38)

    def test_every_target_is_a_valid_path_or_a_research_file(self):
        for qid, (targets, where) in TARGETS.items():
            self.assertTrue(targets and where, qid)
            for t in targets:
                if not t.startswith("research/"):
                    paths.steps(t)

    def test_checklist_states(self):
        b = self.brain()
        b["offer"]["main_offer"] = "Bread subscription"
        b["field_sources"] = {"offer.main_offer": "brand-guide.pdf p.2"}
        rows = {r["id"]: r for r in checklist.build(b)}
        self.assertEqual(rows["B2"]["targets"], {"offer.main_offer": "sourced"})
        self.assertEqual(rows["A4"]["targets"]["business_model.sells"], "open")
        self.assertEqual(rows["E1"]["targets"], {"research/competitors.csv": "file"})
        b["offer"]["main_offer"] = "Bread"
        b["field_sources"] = {}
        self.assertEqual(checklist.state(b, "offer.main_offer"), "no source")
        self.assertIn("B2", checklist.render(checklist.build(b)))
