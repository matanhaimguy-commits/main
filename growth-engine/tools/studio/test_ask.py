"""Tests for studio/ask.py: studio-ask."""
import json
import tempfile
import unittest
from pathlib import Path

from studio.ask import ask
from studio.testbase import Recorder


class Ask(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.hub = Recorder()
        self.hub.replies[("POST", "decisions")] = lambda body: {"decision": {"id": 3, "run_id": 7, "key": "GATE-4"}, "updated": False}

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, data):
        p = self.dir / name
        p.write_text(json.dumps(data) if not isinstance(data, str) else data, encoding="utf-8")
        return str(p)

    def test_reads_the_context_file_and_names_the_run(self):
        (self.dir / "why.md").write_text("## Writer's recommendation\n\nRelease the O30.", encoding="utf-8")
        path = self.write("q.json", {"checkpoint": "GATE-4", "question": "Which spine?", "context_file": "why.md",
                                     "options": [{"label": "A", "description": "Maya's quilt"}, {"label": "B"}]})
        ask("acme", "AC-1", path, call=self.hub.call, business="acme-app")
        body = self.hub.calls[0]["body"]
        self.assertEqual((body["business"], body["post_id"], body["checkpoint"]), ("acme-app", "AC-1", "GATE-4"))
        self.assertEqual(body["context"], "## Writer's recommendation\n\nRelease the O30.")
        self.assertNotIn("context_file", body)
        self.assertEqual(self.hub.calls[0]["api"], "studio")

    def test_a_question_needs_a_checkpoint_and_readable_files(self):
        for data, why in (({"question": "no checkpoint"}, "BAD_DECISION"),
                          ("{not json", "BAD_DECISION"),
                          ({"checkpoint": "X", "question": "?", "context_file": "missing.md"}, "NO_FILE")):
            with self.assertRaises(SystemExit) as e:
                ask("acme", "AC-1", self.write("bad.json", data), call=self.hub.call)
            self.assertIn(why, str(e.exception))
        self.assertEqual(self.hub.calls, [])


if __name__ == "__main__":
    unittest.main()
