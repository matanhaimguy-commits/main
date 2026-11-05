"""The intake question set: schema, stable unique ids, required fields, brain.json paths that exist.
Run: python3 -m unittest discover -s growth-engine/onboarding -p 'test_*.py'"""
import json
import unittest
from pathlib import Path

import jsonschema

HERE = Path(__file__).resolve().parent
SET = json.loads((HERE / "intake-questions.json").read_text(encoding="utf-8"))
SCHEMA = json.loads((HERE / "intake-questions.schema.json").read_text(encoding="utf-8"))
BRAIN = json.loads((HERE.parent / "schemas" / "brain.schema.json").read_text(encoding="utf-8"))
FOUNDATION_IDS = [f"{s}{n}" for s, k in zip("ABCDEF", (7, 5, 5, 6, 2, 5)) for n in range(1, k + 1)]


class IntakeQuestions(unittest.TestCase):
    def test_matches_its_schema(self):
        jsonschema.validate(SET, SCHEMA)

    def test_ids_are_unique_and_every_section_exists(self):
        ids = [q["id"] for q in SET["questions"]]
        self.assertEqual(len(ids), len(set(ids)))
        sections = {s["id"] for s in SET["sections"]}
        self.assertTrue({q["section"] for q in SET["questions"]} <= sections)
        self.assertTrue(all(q["id"].startswith(q["section"]) for q in SET["questions"]))

    def test_keeps_all_30_foundation_questions_with_their_ids(self):
        ids = {q["id"] for q in SET["questions"]}
        self.assertEqual(len(FOUNDATION_IDS), 30)
        self.assertEqual(set(FOUNDATION_IDS) - ids, set())

    def test_has_the_research_and_consent_inputs(self):
        text = " ".join(q["label"].lower() + " " + " ".join(q.get("fields", [])) for q in SET["questions"])
        for word in ("website", "instagram", "competitors", "offer economics", "ai-made", "proof", "trustpilot"):
            self.assertIn(word, text)

    def test_required_fields_are_marked_and_choices_have_options(self):
        req = {q["id"] for q in SET["questions"] if q["required"]}
        self.assertTrue({"A1", "A3", "A4", "G1", "H1", "H2", "D5"} <= req)
        for q in SET["questions"]:
            if q["type"] in ("choice", "multichoice"):
                self.assertGreaterEqual(len(q.get("options", [])), 2, q["id"])
            if q.get("required_any"):
                self.assertTrue(set(q["required_any"]) <= set(q["fields"]), q["id"])

    def test_maps_to_paths_exist_in_the_brain_schema(self):
        def exists(path: str) -> bool:
            node = BRAIN
            for part in path.replace("[]", "").split("."):
                node = node.get("items", node)
                node = node.get("properties", {}).get(part)
                if node is None:
                    return False
            return True
        bad = [(q["id"], p) for q in SET["questions"] for p in q["maps_to"]
               if not exists(p.replace("[]", "").replace("proof_bank[].", "proof_bank."))]
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
