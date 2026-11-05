"""Tests for the twin route in the generation gate (heygen_gate.py, check_explain.py; D-T4, Twin reel machine plan T1).

    python3 -m unittest test_heygen_gate      (from growth-engine/tools)

A temp ledger (PIPELINE_ROOT) with a twin_host card, the brain's real host block and the steps before each call. The
calls use the tool names this cloud session really exposes (mcp__<connector id>__create_speech); nothing reaches HeyGen.
"""
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

import pipeline as P
import test_pipeline as TP

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
SLUG, POST = TP.SLUG, TP.POST
HOST = json.loads((REPO / "clients" / "straightscale-en" / "brain.json").read_text())["host"]
PORTRAIT, LANDSCAPE = "0295627e7d5e497980c0e20c50bb2db7", "fb4c6f11e09e4fd2863bcf77eaa00c2c"
VOICE = "8646763dcd2e4f97934ca00402817e4b"
CONNECTOR = "mcp__49562e34-e2bd-4bfe-95e6-8f2f8287878e__"   # the HeyGen connector's id in this environment
SPEECH, VIDEO = "mcp__HeyGen__create_speech", "mcp__HeyGen__create_video_from_avatar"
SCRIPT = "Referrals aren't your problem. The timing is. Ask on the day they thank you. Comment TIMING for the script."
AUDIO_URL = "https://files.example/speech/vo-1.mp3"
CARD = f"clients/{SLUG}/cards/2026-11-W1/{POST}.yaml"


def speech_call(**kw):
    return {"voiceId": VOICE, "text": SCRIPT, **kw}


def video_call(**kw):
    return {"avatarId": LANDSCAPE, "aspectRatio": "9:16", "fit": "cover", "audioUrl": AUDIO_URL, **kw}


class Twin(TP.Base):
    def setUp(self):
        super().setUp()
        cd = self.root / "clients" / SLUG
        brain = json.loads((cd / "brain.json").read_text())
        (cd / "brain.json").write_text(json.dumps({**brain, "host": HOST}))
        self.card(True)
        P.init_run(SLUG, POST, "reel_whiteboard", CARD)

    def card(self, twin):
        p = self.root / CARD
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f"post_id: {POST}\nformat: reel_whiteboard\ntwin_host: {str(twin).lower()}\n")

    def ready_for_speech(self, budget=True, heygen=200):
        P.record_gate(SLUG, POST, "G-SCRIPT", "PASS", "script-lab gate", score=88,
                      data={"script_sha256": P.sha_text(SCRIPT)})
        if budget:
            P.budget(SLUG, POST, planned=1, balance=8, heygen=heygen)
        P.new_asset(SLUG, POST, "VO", "voice", tool=SPEECH)
        P.set_prompt(SLUG, POST, "VO", SCRIPT, [])

    def ready_for_video(self, audio_pass=True, step9=True):
        self.ready_for_speech()
        self.assertEqual(P.check_call(SPEECH, speech_call()), (True, []))
        P.add_media(SLUG, POST, "VO@v1", ids=[AUDIO_URL])
        if audio_pass:
            P.record_gate(SLUG, POST, "G-AUDIO", "PASS", "take check", asset="VO@v1", data={"seconds": 31.2})
        P.new_asset(SLUG, POST, "AROLL", "video_clip", ["S01"], tool=VIDEO)
        P.set_prompt(SLUG, POST, "AROLL", "Twin A-roll, the whole script, driven by VO@v1.",
                     P.parse_media([f"{AUDIO_URL}:audio"]))
        if step9:
            led = P.load_ledger(SLUG, POST)
            led["steps"]["9"]["status"] = "done"
            P.save_ledger(led)

    def denied(self, tool, ti, *needles):
        ok, why = P.check_call(tool, ti)
        self.assertFalse(ok)
        for n in needles:
            self.assertIn(n, " ".join(why))
        return why


class Speech(Twin):
    def test_the_locked_speech_call_passes_once(self):
        self.ready_for_speech()
        self.assertEqual(P.check_call(SPEECH, speech_call()), (True, []))
        self.denied(SPEECH, speech_call(), "already generated")
        log = [json.loads(x) for x in (P.run_dir(SLUG, POST) / "calls.jsonl").read_text().splitlines()]
        self.assertEqual([(e["decision"], e["asset"]) for e in log], [("ALLOW", "VO@v1"), ("DENY", "VO@v1")])

    def test_another_voice_is_refused(self):
        self.ready_for_speech()
        self.denied(SPEECH, speech_call(voiceId="stock-voice"), "not one of the twin's voices")

    def test_text_that_is_not_the_released_script_is_refused(self):
        self.ready_for_speech()
        self.denied(SPEECH, speech_call(text=SCRIPT + " Also buy now."), "not registered on a voice asset")
        P.set_prompt(SLUG, POST, "VO", SCRIPT + " Also buy now.", [])
        self.denied(SPEECH, speech_call(text=SCRIPT + " Also buy now."), "not the released script")

    def test_a_card_without_twin_host_is_refused(self):
        self.card(False)
        self.ready_for_speech()
        self.denied(SPEECH, speech_call(), "not marked twin_host")

    def test_the_budget_must_price_heygen_credits_and_be_fresh(self):
        self.ready_for_speech(heygen=0)
        self.denied(SPEECH, speech_call(), "no HeyGen credits planned")
        P.budget(SLUG, POST, planned=1, balance=8, heygen=200)
        led = P.load_ledger(SLUG, POST)
        b = P.latest(led["run_gates"]["G-BUDGET"])
        b["at"] = (P.parse_ts(b["at"]) - P.dt.timedelta(hours=25)).isoformat()
        P.save_ledger(led)
        self.denied(SPEECH, speech_call(), "older than 24 h")

    def test_a_voice_asset_for_another_tool_does_not_count(self):
        P.record_gate(SLUG, POST, "G-SCRIPT", "PASS", "script-lab gate", score=88,
                      data={"script_sha256": P.sha_text(SCRIPT)})
        P.budget(SLUG, POST, planned=1, balance=8, heygen=200)
        P.new_asset(SLUG, POST, "VO", "voice")
        P.set_prompt(SLUG, POST, "VO", SCRIPT, [])
        self.denied(SPEECH, speech_call(), "not registered on a voice asset for mcp__HeyGen__create_speech")


class Video(Twin):
    def test_the_locked_video_call_passes(self):
        self.ready_for_video()
        self.assertEqual(P.check_call(VIDEO, video_call()), (True, []))
        self.denied(VIDEO, video_call(), "already generated")

    def test_the_portrait_look_with_an_asset_id(self):
        self.ready_for_video()
        P.add_media(SLUG, POST, "VO@v1", ids=["asset-77"])
        P.new_asset(SLUG, POST, "AROLL2", "video_clip", ["S01"], tool=VIDEO)
        P.set_prompt(SLUG, POST, "AROLL2", "Twin A-roll, portrait look.", [{"value": "asset-77", "role": "audio"}])
        ok, why = P.check_call(VIDEO, {"avatarId": PORTRAIT, "aspectRatio": "9:16", "audioAssetId": "asset-77"})
        self.assertTrue(ok, why)

    def test_refusals(self):
        self.ready_for_video()
        self.denied(VIDEO, video_call(avatarId="stock-presenter"), "not one of the twin's looks")
        self.denied(VIDEO, video_call(aspectRatio="16:9"), "a reel is 9:16")
        self.denied(VIDEO, video_call(fit="contain"), "never contain")
        self.denied(VIDEO, video_call(audioUrl=None, script=SCRIPT, voiceId=VOICE), "script, voiceId",
                    "exactly one audio source")
        self.denied(VIDEO, video_call(audioUrl="https://elsewhere.example/a.mp3"), "not registered on a voice asset")

    def test_the_voice_needs_its_take_check(self):
        self.ready_for_video(audio_pass=False)
        self.denied(VIDEO, video_call(), "no G-AUDIO PASS")

    def test_the_voice_must_be_the_twins_own(self):
        self.ready_for_video()
        P.new_asset(SLUG, POST, "VO-ATLAS", "voice")
        P.add_media(SLUG, POST, "VO-ATLAS@v1", ids=["https://files.example/other.mp3"])
        P.record_gate(SLUG, POST, "G-AUDIO", "PASS", "take check", asset="VO-ATLAS@v1")
        self.denied(VIDEO, video_call(audioUrl="https://files.example/other.mp3"), "his own cloned voice")

    def test_step_9_closes_before_the_first_video(self):
        self.ready_for_video(step9=False)
        self.denied(VIDEO, video_call(), "step 9")


class Explain(Twin):
    """pipeline.py check-call --explain, as a subprocess, with the real connector names; writes nothing."""

    def explain(self, name, ti):
        f = self.root / "call.json"
        f.write_text(json.dumps(ti))
        r = subprocess.run([sys.executable, str(HERE / "pipeline.py"), "check-call", "--explain", name, str(f)],
                           capture_output=True, text=True, env={**os.environ, "PIPELINE_ROOT": str(self.root)})
        return r.returncode, r.stdout

    def test_the_two_locked_calls_are_allowed(self):
        self.ready_for_speech()
        code, out = self.explain(CONNECTOR + "create_speech", speech_call())
        self.assertEqual(code, 0, out)
        self.assertIn("gated as mcp__HeyGen__create_speech", out)
        self.assertIn("service heygen_twin, kind heygen_speech", out)
        self.assertFalse((P.run_dir(SLUG, POST) / "calls.jsonl").exists(), "--explain writes no call")
        self.ready_for_video_after_speech()
        code, out = self.explain(CONNECTOR + "create_video_from_avatar", video_call())
        self.assertEqual((code, out.splitlines()[-1]), (0, "ALLOW"), out)

    def ready_for_video_after_speech(self):
        self.assertTrue(P.check_call(SPEECH, speech_call())[0])
        P.add_media(SLUG, POST, "VO@v1", ids=[AUDIO_URL])
        P.record_gate(SLUG, POST, "G-AUDIO", "PASS", "take check", asset="VO@v1")
        P.new_asset(SLUG, POST, "AROLL", "video_clip", ["S01"], tool=VIDEO)
        P.set_prompt(SLUG, POST, "AROLL", "Twin A-roll.", [{"value": AUDIO_URL, "role": "audio"}])
        led = P.load_ledger(SLUG, POST)
        led["steps"]["9"]["status"] = "done"
        P.save_ledger(led)

    def test_wrong_look_landscape_size_script_driven_and_missing_audio_are_refused(self):
        self.ready_for_video()
        for needle, ti in (("not one of the twin's looks", video_call(avatarId="stock-presenter")),
                           ("a reel is 9:16", video_call(aspectRatio="16:9")),
                           ("no script text", video_call(audioUrl=None, script=SCRIPT)),
                           ("exactly one audio source", video_call(audioUrl=None))):
            with self.subTest(needle=needle):
                code, out = self.explain(CONNECTOR + "create_video_from_avatar", ti)
                self.assertEqual(code, 1, out)
                self.assertIn("DENY", out)
                self.assertIn(needle, out)

    def test_every_other_heygen_tool_is_refused(self):
        for name in ("create_speech_without_player", "create_video_agent", "text_to_video", "create_lipsync",
                     "create_video_from_image", "clone_voice", "create_digital_twin", "generate_from_template"):
            with self.subTest(name=name):
                code, out = self.explain(CONNECTOR + name, {"text": SCRIPT, "voiceId": VOICE})
                self.assertEqual(code, 1, out)
                self.assertIn("SERVICE OFF", out)
        for name in ("cancel_subscription", "delete_video", "create_asset_upload", "create_brand_kit"):
            with self.subTest(name=name):
                code, out = self.explain(CONNECTOR + name, {})
                self.assertEqual(code, 1, out)
                self.assertIn("HEYGEN TOOL OFF", out)
        code, out = self.explain(CONNECTOR + "list_avatar_looks", {})
        self.assertEqual((code, out.splitlines()[-1]), (0, "ALLOW"))


if __name__ == "__main__":
    unittest.main()
