"""Tests for clients/project.py."""
import unittest

from clients import project
from clients.testbase import ClientsCase


class Project(ClientsCase):
    def test_stage_score_master_hook_and_hub_key(self):
        f = project.facts(self.root, {"project": "motion-studio/projects/acme-01", "source_ref": "hooks v2 master AC-B"})
        self.assertEqual(f["project"], "motion-studio/projects/acme-01")
        self.assertEqual((f["stage"], f["gate_score"]), ("script (gate 88/100)", 88))
        self.assertEqual(f["hook"], {"id": "AC-B", "text": "second", "spoken": "two", "source": "docs/hooks.json"})
        self.assertEqual(f["content_external_key"], "AC-2026-11-W1-01")

    def test_first_hook_when_no_master_is_named(self):
        f = project.facts(self.root, {"project": "motion-studio/projects/acme-01", "source_ref": ""})
        self.assertEqual(f["hook"]["id"], "AC-A")

    def test_hook_from_the_card_notes_and_a_missing_project(self):
        f = project.facts(self.root, {"project": "motion-studio/projects/gone",
                                      "notes": "Text hook: 'Nothing filled April. Why?' CTA: 'Follow.'"})
        self.assertIsNone(f["project"])
        self.assertEqual(f["hook"], {"id": None, "text": "Nothing filled April. Why?", "source": "card notes"})
        spoken = project.hook(None, {"notes": "Spoken hook (draft), asked off camera: 'Here's one test.' More"})
        self.assertEqual(spoken["spoken"], "Here's one test.")
        self.assertIsNone(project.hook(None, {"notes": "no hook here"}))


if __name__ == "__main__":
    unittest.main()
