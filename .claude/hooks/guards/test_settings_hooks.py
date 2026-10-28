"""The hooks in .claude/settings.json cover what they must. Run: python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'"""
import json
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SETTINGS = json.loads((REPO / ".claude" / "settings.json").read_text())["hooks"]["PreToolUse"]
GATED = json.loads((REPO / "growth-engine" / "production" / "standards.json").read_text())["gated_tools"]
ID = "mcp__6f1c2a9e-3b4d-4e5f-8a7b-0c1d2e3f4a5b__"


def entry(script: str) -> dict:
    return next(e for e in SETTINGS if any(script in h["command"] for h in e["hooks"]))


class SettingsHooksTest(unittest.TestCase):
    def test_every_gated_connector_tool_reaches_the_generation_gate(self):
        m = re.compile(entry("generation_gate.py")["matcher"])
        for tool in (k for k in GATED if k.startswith("mcp__")):
            for name in (tool, ID + tool.split("__", 2)[2]):
                with self.subTest(name=name):
                    self.assertTrue(m.fullmatch(name))

    def test_free_reads_are_not_matched(self):
        m = re.compile(entry("generation_gate.py")["matcher"])
        for name in ("mcp__Higgs__balance", ID + "show_generations", ID + "creative_list_voices", ID + "jobs_wait"):
            with self.subTest(name=name):
                self.assertIsNone(m.fullmatch(name))

    def test_the_atlas_bash_guard_runs_on_bash_and_blocks_on_failure(self):
        e = entry("atlas_bash_guard.py")
        self.assertTrue(re.fullmatch(e["matcher"], "Bash"))
        self.assertEqual(e["hooks"][0]["onFailure"], "block")
        self.assertEqual(entry("generation_gate.py")["hooks"][0]["onFailure"], "block")


if __name__ == "__main__":
    unittest.main()
