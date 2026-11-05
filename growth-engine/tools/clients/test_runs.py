"""Tests for clients/runs.py."""
import json
import unittest

from clients import runs
from clients.cards import load
from clients.testbase import SLUG, ClientsCase


class Runs(ClientsCase):
    def entries(self):
        return {e["card"]["post_id"]: e for e in load(self.root, SLUG)}

    def test_run_by_post_id_and_its_facts(self):
        found = runs.find(self.root, SLUG, self.entries()["AC-2026-11-W1-01"])
        f = runs.facts(self.root, found)
        self.assertEqual(f["run"], "clients/acme/runs/AC-2026-11-W1-01")
        self.assertEqual((f["steps_done"], f["steps_total"], f["current_step"]), (2, 3, 2))
        self.assertEqual(f["waiting_on_owner"], ["G-HUMAN-SPINE"])
        self.assertEqual([(g["gate"], g["status"], g["score"]) for g in f["gates"]], [("G-SCRIPT", "PASS", 88)])

    def test_run_named_by_the_card_the_ledger_or_the_project(self):
        e = self.entries()["AC-2026-11-W1-02"]
        self.assertIsNone(runs.find(self.root, SLUG, e))
        other = self.root / "clients" / "other" / "runs" / "X-1" / "ledger.json"
        self.write(other, json.dumps({"post_id": "X-1", "card": e["path"]}))
        self.assertEqual(runs.find(self.root, SLUG, e), other)
        e["card"]["run"] = "clients/other/runs/X-1/"
        self.assertEqual(runs.find(self.root, SLUG, e), other)
        proj = self.root / "motion-studio" / "projects" / "p2"
        self.write(proj / "PROJECT.md", "Pipeline run `clients/other/runs/X-1` (steps 0 to 3)")
        self.assertEqual(runs.by_project(self.root, "motion-studio/projects/p2"), other)
        self.assertIsNone(runs.by_project(self.root, None))


if __name__ == "__main__":
    unittest.main()
