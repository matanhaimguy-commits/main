"""Gated tool names under id-named connectors. Run: python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'"""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guards.tool_names import canonical  # noqa: E402

GATED = json.loads((Path(__file__).resolve().parents[3] / "growth-engine" / "production" / "standards.json").read_text())["gated_tools"]
ID = "mcp__6f1c2a9e-3b4d-4e5f-8a7b-0c1d2e3f4a5b__"


class ToolNamesTest(unittest.TestCase):
    def test_id_named_connectors_map_to_the_gated_tool(self):
        self.assertEqual(canonical(ID + "generate_image", GATED), "mcp__Higgs__generate_image")
        self.assertEqual(canonical(ID + "creative_generate_speech", GATED), "mcp__ElevenLabs__creative_generate_speech")

    def test_a_named_server_matches_without_case(self):
        self.assertEqual(canonical("mcp__heygen__create_speech", GATED), "mcp__HeyGen__create_speech")
        self.assertEqual(canonical("mcp__higgs__upscale_video", GATED), "mcp__Higgs__upscale_video")

    def test_named_and_unrelated_tools_keep_their_name(self):
        for t in ["mcp__Higgs__generate_image", "mcp__Figma__generate_image", ID + "list_projects", "Bash"]:
            self.assertEqual(canonical(t, GATED), t)

    def test_every_gated_ending_is_unique(self):
        ends = [k.split("__", 2)[2] for k in GATED if k.startswith("mcp__")]
        self.assertEqual(len(ends), len(set(ends)))


if __name__ == "__main__":
    unittest.main()
