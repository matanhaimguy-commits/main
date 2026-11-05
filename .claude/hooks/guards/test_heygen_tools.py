"""The HeyGen connector catch-all. Run: python3 -m unittest discover -s .claude/hooks/guards -p 'test_*.py'"""
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guards.heygen_tools import bare_name, deny_reason, read_only  # noqa: E402

HOOKS = Path(__file__).resolve().parents[1]
REPO = HOOKS.parents[1]
STANDARDS = json.loads((REPO / "growth-engine" / "production" / "standards.json").read_text())
CONNECTOR = "mcp__49562e34-e2bd-4bfe-95e6-8f2f8287878e__"
LOCKED = {"create_speech", "create_video_from_avatar"}
# every tool the HeyGen connector exposes in this environment (read 30 Oct 2026)
TOOLS = """bulk_asset_statuses bulk_lipsync_statuses bulk_video_statuses bulk_video_translation_statuses cancel_subscription
clone_voice complete_asset_batch complete_asset_upload continue_subscription_cancellation convert_model_speech
create_ai_clipping create_asset_upload create_asset_upload_batch create_avatar_consent create_brand_glossary
create_brand_kit create_digital_twin create_filler_word_removal create_folder create_image_generation
create_instant_audio_voice create_lipsync create_lipsync_batch create_look_pack_looks create_model_audio_voice
create_photo_avatar create_prompt_avatar create_speech create_speech_without_player create_template
create_template_looks create_video_agent create_video_batch create_video_from_avatar
create_video_from_cinematic_avatar create_video_from_image create_video_from_studio create_video_translation
create_video_translation_batch delete_ai_clipping delete_asset delete_avatar_group delete_avatar_look
delete_brand_glossary delete_brand_kit delete_lipsync delete_model_audio_voice delete_template delete_video
delete_video_translation delete_voice design_voice generate_from_template get_ai_clipping get_asset get_asset_batch
get_avatar_creation_status get_avatar_group get_avatar_look get_brand_glossary get_brand_kit get_current_user
get_filler_word_removal get_folder get_image_generation get_lipsync get_lipsync_batch get_model_audio_voice
get_model_video get_template get_video get_video_agent_resource get_video_agent_session get_video_batch
get_video_scenes get_video_translation get_video_translation_batch get_voice image_to_video list_ai_clipping
list_assets list_avatar_groups list_avatar_looks list_brand_glossaries list_brand_kits list_lipsyncs
list_look_templates list_model_audio_voices list_templates list_video_agent_session_videos list_video_agent_sessions
list_video_agent_styles list_video_translation_languages list_video_translations list_videos list_voices lookup_videos
reference_to_video search_audio_sounds send_video_agent_message set_template_variables show_subscription_action
stop_video_agent_session submit_feedback text_to_video track_skill_activation update_avatar_group update_avatar_look
update_brand_glossary update_brand_kit update_lipsync update_template update_video_translation""".split()


def generation_gate(tool, ti):
    r = subprocess.run([sys.executable, str(HOOKS / "generation_gate.py")], capture_output=True, text=True,
                       input=json.dumps({"tool_name": tool, "tool_input": ti}))
    return json.loads(r.stdout)["hookSpecificOutput"]["permissionDecisionReason"] if r.stdout else ""


def tools_gate(tool):
    r = subprocess.run([sys.executable, str(HOOKS / "heygen_tools_gate.py")], capture_output=True, text=True,
                       input=json.dumps({"tool_name": tool, "tool_input": {}}))
    return json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"] if r.stdout else "allow"


class CatchAll(unittest.TestCase):
    def test_every_heygen_tool_is_locked_read_only_or_denied(self):
        self.assertEqual(len(TOOLS), 113)
        for name in TOOLS:
            for tool in (CONNECTOR + name, "mcp__HeyGen__" + name, "mcp__heygen__" + name):
                with self.subTest(tool=tool):
                    if name in LOCKED:
                        self.assertIsNone(deny_reason(tool, STANDARDS))   # the generation gate checks these
                    elif read_only(name, STANDARDS):
                        self.assertIsNone(deny_reason(tool, STANDARDS))
                    elif "mcp__HeyGen__" + name in STANDARDS["gated_tools"]:
                        # a generation tool in gated_tools: the generation gate refuses it, service off
                        self.assertEqual(STANDARDS["gated_tools"]["mcp__HeyGen__" + name]["service"], "heygen")
                        self.assertIsNone(deny_reason(tool, STANDARDS))
                    else:
                        self.assertIn("HeyGen", deny_reason(tool, STANDARDS) or "")

    def test_reads_are_only_list_get_lookup_and_bulk_statuses(self):
        reads = {n for n in TOOLS if read_only(n, STANDARDS)}
        self.assertTrue(all(re.match(r"(list_|get_|lookup_)|bulk_\w+_statuses$", n) for n in reads), reads)
        for write in ("cancel_subscription", "delete_video", "create_brand_kit", "create_asset_upload",
                      "complete_asset_upload", "update_avatar_look", "submit_feedback", "search_audio_sounds",
                      "show_subscription_action", "track_skill_activation", "set_template_variables"):
            with self.subTest(write=write):
                self.assertNotIn(write, reads)
                self.assertEqual(tools_gate(CONNECTOR + write), "deny")

    def test_the_hook_lets_reads_and_the_locked_tools_through_to_their_gates(self):
        for name in ("list_avatar_looks", "get_video", "lookup_videos", "bulk_video_statuses", "create_speech",
                     "create_video_from_avatar"):
            with self.subTest(name=name):
                self.assertEqual(tools_gate(CONNECTOR + name), "allow")
        self.assertIn("GENERATION BLOCKED", generation_gate(CONNECTOR + "create_speech", {"text": "x"}))

    def test_other_servers_are_not_heygen(self):
        for tool in ("mcp__Higgs__get_video", "mcp__6f1c2a9e-3b4d-4e5f-8a7b-0c1d2e3f4a5b__delete_video", "Bash"):
            self.assertIsNone(bare_name(tool, STANDARDS))

    def test_settings_send_every_heygen_tool_to_the_hook(self):
        hooks = json.loads((REPO / ".claude/settings.json").read_text())["hooks"]["PreToolUse"]
        e = next(e for e in hooks if any("heygen_tools_gate.py" in h["command"] for h in e["hooks"]))
        self.assertEqual(e["hooks"][0]["onFailure"], "block")
        m = re.compile(e["matcher"])
        for name in TOOLS:
            for tool in (CONNECTOR + name, "mcp__HeyGen__" + name, "mcp__heygen__" + name):
                with self.subTest(tool=tool):
                    self.assertTrue(m.fullmatch(tool))
        self.assertIsNone(m.fullmatch("mcp__Higgs__generate_video"))

    def test_unreadable_input_fails_closed(self):
        r = subprocess.run([sys.executable, str(HOOKS / "heygen_tools_gate.py")], input="not json",
                           capture_output=True, text=True)
        self.assertEqual(json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"], "deny")


if __name__ == "__main__":
    unittest.main()
