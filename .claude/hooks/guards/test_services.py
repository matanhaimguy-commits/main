"""Switched-off services. Run: python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'"""
import json
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guards.services import off_reason  # noqa: E402

HOOKS = Path(__file__).resolve().parents[1]
STANDARDS = json.loads((HOOKS.parents[1] / "growth-engine" / "production" / "standards.json").read_text())
ID = "mcp__6f1c2a9e-3b4d-4e5f-8a7b-0c1d2e3f4a5b__"


def gate(tool: str, tool_input: dict | None = None) -> str:
    r = subprocess.run([sys.executable, str(HOOKS / "generation_gate.py")], capture_output=True, text=True,
                       input=json.dumps({"tool_name": tool, "tool_input": tool_input or {}}))
    return json.loads(r.stdout)["hookSpecificOutput"]["permissionDecisionReason"] if r.stdout else ""


class ServicesTest(unittest.TestCase):
    def test_every_higgsfield_elevenlabs_and_heygen_tool_is_off(self):
        tools = [k for k in STANDARDS["gated_tools"] if k.startswith(("mcp__Higgs__", "mcp__ElevenLabs__", "mcp__HeyGen__"))]
        self.assertGreaterEqual(len(tools), 70)
        for t in tools:
            with self.subTest(tool=t):
                self.assertIn("Atlas", off_reason(t, STANDARDS))

    def test_the_tools_that_were_missed_are_gated(self):
        for name in ("generate_3d", "upscale_image", "upscale_video", "remove_background", "reframe", "create_voice",
                     "voice_change", "dubbing", "apps_invoke", "sandbox_exec", "scene_builder_3d_generate_video",
                     "scene_builder_3d_generate_angles", "video_analysis_create"):
            with self.subTest(name=name):
                self.assertEqual(STANDARDS["gated_tools"]["mcp__Higgs__" + name]["service"], "higgs")

    def test_the_hook_refuses_them_under_any_server_name(self):
        for tool in ("mcp__Higgs__upscale_video", ID + "upscale_video", ID + "sandbox_exec", ID + "generate_3d",
                     "mcp__ElevenLabs__creative_generate_speech", ID + "creative_generate_speech",
                     ID + "creative_design_voice", ID + "creative_transcribe_audio", ID + "text_to_video",
                     ID + "create_video_from_avatar", ID + "create_speech", ID + "create_photo_avatar",
                     ID + "create_lipsync", "mcp__heygen__create_video_agent"):
            with self.subTest(tool=tool):
                self.assertIn("SERVICE OFF", gate(tool, {"prompt": "x"}))

    def test_atlas_stays_on(self):
        self.assertIsNone(off_reason("atlas_generate", STANDARDS))
        self.assertIsNone(off_reason("Bash", STANDARDS))
        for free in (ID + "balance", ID + "list_avatar_looks", ID + "get_video", ID + "creative_list_voices"):
            self.assertEqual(gate(free), "", f"{free}: a free read is not gated")


if __name__ == "__main__":
    unittest.main()
