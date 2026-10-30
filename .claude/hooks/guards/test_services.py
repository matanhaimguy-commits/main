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
TWIN = ("mcp__HeyGen__create_speech", "mcp__HeyGen__create_video_from_avatar")   # D-T4: the twin route, gated by checks


def gate(tool: str, tool_input: dict | None = None) -> str:
    r = subprocess.run([sys.executable, str(HOOKS / "generation_gate.py")], capture_output=True, text=True,
                       input=json.dumps({"tool_name": tool, "tool_input": tool_input or {}}))
    return json.loads(r.stdout)["hookSpecificOutput"]["permissionDecisionReason"] if r.stdout else ""


class ServicesTest(unittest.TestCase):
    def test_every_higgsfield_elevenlabs_and_heygen_tool_is_off_but_the_twin_route(self):
        tools = [k for k in STANDARDS["gated_tools"] if k.startswith(("mcp__Higgs__", "mcp__ElevenLabs__", "mcp__HeyGen__"))
                 and k not in TWIN]
        self.assertGreaterEqual(len(tools), 69)
        for t in tools:
            with self.subTest(tool=t):
                self.assertIn("Atlas", off_reason(t, STANDARDS))

    def test_only_the_two_twin_tools_are_open(self):
        heygen = {k: v for k, v in STANDARDS["gated_tools"].items() if k.startswith("mcp__HeyGen__")}
        self.assertEqual(sorted(k for k, v in heygen.items() if off_reason(k, STANDARDS) is None), sorted(TWIN))
        self.assertEqual({heygen[t]["service"] for t in TWIN}, {"heygen_twin"})
        self.assertNotIn("other", {heygen[t]["kind"] for t in TWIN})

    def test_the_twin_tools_are_checked_not_waved_through(self):
        for tool in (ID + "create_speech", ID + "create_video_from_avatar", "mcp__heygen__create_speech"):
            with self.subTest(tool=tool):
                why = gate(tool, {"text": "x", "voiceId": "v", "avatarId": "a"})
                self.assertIn("GENERATION BLOCKED", why)
                self.assertNotIn("SERVICE OFF", why)

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
                     ID + "create_speech_without_player", ID + "create_photo_avatar",
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
