"""Tests for pipeline.py (runs, Shot Specs, gate ledger, the generation gate) and vqa_crops.py.

    python3 -m unittest growth-engine/tools/test_pipeline.py
"""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import pipeline as P  # noqa: E402
import vqa_crops as V  # noqa: E402

SLUG, POST, LIB = "acme", "AC-2026-10-W3-01", "AC-LIB-STYLE"
REF = "11111111-2222-3333-4444-555555555555"

SLIDE = {
    "shot_id": "SL01", "post_id": POST, "format": "carousel_slide", "script_lines": ["S1"],
    "line_text": "3 gabime që të vrasin DM-të", "story_purpose": "Cover: stop the owner who loses leads in DMs",
    "must_read_in_1s": "Three mistakes kill your DMs", "subjects": [
        {"id": "PR-PHONE", "state": "on a dark desk, screen lit", "pose": "lying flat, slight angle", "expression": ""}],
    "hands": "none visible",
    "props": [{"id": "PR-PHONE", "story_critical": True, "ref": "LIB-PHONE@v1", "state": "screen on",
               "content": "a chat screen with two grey and two green bubbles holding short grey text lines, contact circle at top"}],
    "text_in_image": [{"string": "3 GABIME", "surface": "dark upper area", "must_be_exact": True,
                       "occlusion": "nothing covers any letter"}],
    "action_physics": [], "static": True,
    "setting": {"details": "dark wooden desk at night, warm lamp", "background_rule": "no frames, screens or signs besides the phone"},
    "camera": {"framing": "top-down medium", "angle": "overhead", "aspect": "4:5", "safe_zones": "top 8% and bottom 12% free"},
    "continuity": {"previous_shot": None}, "style": "photoreal film still, as the style reference",
    "must_not": ["no text on walls", "no logos other than ours"], "hero": True,
    "regions": [{"name": "headline", "kind": "text", "box": [0.05, 0.05, 0.95, 0.3]},
                {"name": "phone", "kind": "prop", "box": [0.3, 0.4, 0.7, 0.9]}],
}


def write(p: Path, data):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump(data, allow_unicode=True) if p.suffix == ".yaml" else json.dumps(data))


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self._root, self._out = P.ROOT, P.OUT
        P.ROOT, P.OUT = self.root, self.root / "growth-engine" / "production"
        cd = self.root / "clients" / SLUG
        cd.mkdir(parents=True)
        (cd / "brain.json").write_text(json.dumps({"package": {"monthly_credit_cap": 1300}}))
        (cd / "ledger.csv").write_text("date,post_id,format,higgsfield_credits,elevenlabs_credits,minutes,note\n")

    def tearDown(self):
        P.ROOT, P.OUT = self._root, self._out
        self.tmp.cleanup()

    # helpers
    def report(self, **kw):
        base = {"independent": True, "reviewer": "visual-reviewer (fresh agent)", "status": "PASS"}
        base.update(kw)
        return base

    def checks(self, kind, fail=None):
        fail = fail or {}
        return [{"id": i, "result": "FAIL" if i in fail else "PASS", "severity": fail.get(i, ""), "evidence": "e"}
                for i in P.CHECK_IDS[kind]]

    def lib_with_style(self):
        P.init_run(SLUG, LIB, "carousel_mistakes")
        write(P.spec_path(SLUG, LIB, "SHEET-STYLE"), {**copy.deepcopy(SLIDE), "shot_id": "SHEET-STYLE", "post_id": LIB,
                                                       "format": "character_sheet", "script_lines": [], "line_text": ""})
        P.new_asset(SLUG, LIB, "STYLE", "style_ref", ["SHEET-STYLE"])
        P.add_media(SLUG, LIB, "STYLE@v1", ids=[REF])
        P.record_gate(SLUG, LIB, "G-VIS-SHEET", "OVERRIDE", "Matan", asset="STYLE@v1",
                      note="the live 15 Oct cover; owner approved it by asking to post it")
        P.record_gate(SLUG, LIB, "G-HUMAN-LOOK", "PASS", "Matan", note="approved the look on 15 Oct")

    def slide_run(self):
        P.init_run(SLUG, POST, "carousel_mistakes")
        write(P.spec_path(SLUG, POST, "SL01"), SLIDE)
        led, res = P.spec_check(SLUG, POST)
        self.assertFalse([i for i in res["SL01"] if i["level"] == "error"], res)
        sha = P.sha_file(P.spec_path(SLUG, POST, "SL01"))
        P.record_report(SLUG, POST, self.report(gate="G-SPEC", shot_id="SL01", spec_sha256=sha, checks=[]))
        P.new_asset(SLUG, POST, "COVER", "cover", ["SL01"])
        a = P.set_prompt(SLUG, POST, "COVER", "Instagram post, portrait 4:5. TEXT: '3 GABIME' ...",
                         [{"value": REF, "role": "image_references"}])
        return a

    def call(self, prompt, medias=None, **params):
        p = {"model": "gpt_image_2_5", "prompt": prompt, "aspect_ratio": "4:5", "resolution": "2k",
             "medias": medias if medias is not None else [{"value": REF, "role": "image_references"}]}
        p.update(params)
        return P.check_call("mcp__Higgs__generate_image", {"params": p})


class SpecLint(Base):
    def test_good_slide_passes(self):
        issues = P.spec_lint(copy.deepcopy(SLIDE), "SL01", POST)
        self.assertFalse([i for i in issues if i["level"] == "error"], issues)

    def test_blanket_no_text_with_story_prop_fails(self):
        s = copy.deepcopy(SLIDE)
        s["must_not"] = ["no text"]
        codes = [i["code"] for i in P.spec_lint(s, "SL01", POST) if i["level"] == "error"]
        self.assertIn("FL-04", codes)

    def test_story_prop_without_content_fails(self):
        s = copy.deepcopy(SLIDE)
        s["props"][0]["content"] = "a phone"
        self.assertIn("FL-04", [i["code"] for i in P.spec_lint(s, "SL01", POST) if i["level"] == "error"])

    def test_realistic_scene_needs_background_action(self):
        s = copy.deepcopy(SLIDE)
        s.update(format="ugc", camera={**s["camera"], "aspect": "9:16"})
        self.assertIn("FL-09", [i["code"] for i in P.spec_lint(s, "SL01", POST) if i["level"] == "error"])

    def test_action_shot_needs_contact_points(self):
        s = copy.deepcopy(SLIDE)
        s["static"] = False
        self.assertIn("action", [i["code"] for i in P.spec_lint(s, "SL01", POST) if i["level"] == "error"])

    def test_hero_needs_region_boxes(self):
        s = copy.deepcopy(SLIDE)
        s["regions"] = []
        self.assertIn("regions", [i["code"] for i in P.spec_lint(s, "SL01", POST) if i["level"] == "error"])


class Gate(Base):
    def test_unregistered_prompt_is_blocked(self):
        ok, why = self.call("a nice picture")
        self.assertFalse(ok)
        self.assertIn("not registered", why[0])

    def test_non_gated_tool_passes(self):
        self.assertTrue(P.check_call("mcp__Higgs__balance", {})[0])

    def test_cost_preflight_passes(self):
        self.assertTrue(self.call("anything", get_cost=True)[0])

    def test_full_still_flow(self):
        self.lib_with_style()
        a = self.slide_run()
        ok, why = self.call("Instagram post, portrait 4:5. TEXT: '3 GABIME' ...")
        self.assertFalse(ok)
        text = " ".join(why)
        self.assertIn("G-BUDGET", text)
        self.assertIn("G-PROMPT-IMG", text)
        self.assertEqual(P.budget(SLUG, POST, planned=10, balance=500)["status"], "PASS")
        st, _ = P.record_report(SLUG, POST, self.report(gate="G-PROMPT-IMG", asset_id="COVER", version=1,
                                                        prompt_sha256=a["prompt_sha256"], checks=self.checks("prompt")))
        self.assertEqual(st, "PASS")
        # whitespace differences don't matter, wording does
        ok, why = self.call("Instagram post,  portrait 4:5.\nTEXT: '3 GABIME' ...")
        self.assertTrue(ok, why)
        ok, why = self.call("Instagram post, portrait 4:5. TEXT: '3 GABIME' ...")
        self.assertFalse(ok)
        self.assertIn("already generated", " ".join(why))

    def test_reference_order_and_aspect_are_checked(self):
        self.lib_with_style()
        a = self.slide_run()
        P.budget(SLUG, POST, planned=10, balance=500)
        P.record_report(SLUG, POST, self.report(gate="G-PROMPT-IMG", asset_id="COVER", version=1,
                                                prompt_sha256=a["prompt_sha256"], checks=self.checks("prompt")))
        ok, why = self.call("Instagram post, portrait 4:5. TEXT: '3 GABIME' ...", medias=[], aspect_ratio="1:1")
        self.assertFalse(ok)
        text = " ".join(why)
        self.assertIn("reference map", text)
        self.assertIn("aspect_ratio", text)

    def test_changed_spec_needs_new_review(self):
        self.lib_with_style()
        a = self.slide_run()
        P.budget(SLUG, POST, planned=10, balance=500)
        P.record_report(SLUG, POST, self.report(gate="G-PROMPT-IMG", asset_id="COVER", version=1,
                                                prompt_sha256=a["prompt_sha256"], checks=self.checks("prompt")))
        s = copy.deepcopy(SLIDE)
        s["story_purpose"] = "Cover, changed after review"
        write(P.spec_path(SLUG, POST, "SL01"), s)
        ok, why = self.call("Instagram post, portrait 4:5. TEXT: '3 GABIME' ...")
        self.assertFalse(ok)
        self.assertIn("SL01", " ".join(why))

    def test_talking_clip_without_storyboard_is_blocked(self):
        P.init_run(SLUG, "AC-2026-10-W3-02", "reel_story_narrated")
        post = "AC-2026-10-W3-02"
        v = copy.deepcopy(SLIDE)
        v.update(shot_id="S60-SEQ01-SH1", post_id=post, format="animation_3d",
                 camera={**v["camera"], "aspect": "9:16"}, hero=False)
        write(P.spec_path(SLUG, post, "S60-SEQ01-SH1"), v)
        P.spec_check(SLUG, post)
        P.record_report(SLUG, post, self.report(gate="G-SPEC", shot_id="S60-SEQ01-SH1",
                                                spec_sha256=P.sha_file(P.spec_path(SLUG, post, "S60-SEQ01-SH1")), checks=[]))
        P.new_asset(SLUG, post, "CH-ARTA", "character_sheet", ["S60-SEQ01-SH1"])
        P.add_media(SLUG, post, "CH-ARTA@v1", ids=["img-1"])
        P.record_gate(SLUG, post, "G-VIS-SHEET", "OVERRIDE", "Matan", asset="CH-ARTA@v1", note="test")
        P.record_gate(SLUG, post, "G-HUMAN-LOOK", "PASS", "Matan", note="test")
        P.new_asset(SLUG, post, "SLICE-SEQ01", "audio_slice")
        P.add_media(SLUG, post, "SLICE-SEQ01@v1", ids=["aud-1"])
        P.new_asset(SLUG, post, "SEQ01-video", "video_clip", ["S60-SEQ01-SH1"])
        medias = [{"value": "img-1", "role": "image_references"}, {"value": "aud-1", "role": "audio_references"}]
        a = P.set_prompt(SLUG, post, "SEQ01-video", "Pixar-style 3D. <<<image_1>>> is Arta ...", medias)
        ok, why = P.check_call("mcp__Higgs__generate_video", {"params": {
            "model": "minimax_h3", "prompt": "Pixar-style 3D. <<<image_1>>> is Arta ...", "medias": medias,
            "duration": 4, "aspect_ratio": "9:16"}})
        self.assertFalse(ok)
        text = " ".join(why)
        for needle in ("storyboard as image 1", "declined_preset_id", "resolution", "duration", "G-AUDIO",
                       "G-PROMPT-VID"):
            self.assertIn(needle, text)

    def test_banned_video_model_is_blocked(self):
        self.lib_with_style()
        a = self.slide_run()
        P.new_asset(SLUG, POST, "CLIP", "video_clip", ["SL01"])
        P.set_prompt(SLUG, POST, "CLIP", "a seedance clip", [])
        ok, why = P.check_call("mcp__Higgs__generate_video", {"params": {"model": "seedance_2_5", "prompt": "a seedance clip"}})
        self.assertFalse(ok)
        self.assertIn("banned", " ".join(why))

    def test_audio_needs_released_script(self):
        P.init_run(SLUG, "AC-2026-10-W3-03", "reel_quote_broll")
        post = "AC-2026-10-W3-03"
        P.new_asset(SLUG, post, "VO", "voice")
        P.set_prompt(SLUG, post, "VO", "Ti humb klientë çdo ditë.", [])
        P.budget(SLUG, post, planned=30, balance=500)
        ti = {"prompt": "Ti humb klientë çdo ditë.", "model_id": "eleven_v4", "voice_id": "x", "context": "vo"}
        ok, why = P.check_call("mcp__ElevenLabs__creative_generate_speech", ti)
        self.assertFalse(ok)
        self.assertIn("G-SCRIPT", " ".join(why))
        with self.assertRaises(P.PipelineError):
            P.record_gate(SLUG, post, "G-SCRIPT", "PASS", "script-lab", score=80)
        P.record_gate(SLUG, post, "G-SCRIPT", "PASS", "script-lab gate", score=88)
        self.assertTrue(P.check_call("mcp__ElevenLabs__creative_generate_speech", ti)[0])
        ti2 = dict(ti, model_id="eleven_multilingual_v2")
        P.new_asset(SLUG, post, "VO", "voice")
        P.set_prompt(SLUG, post, "VO", "Ti humb klientë çdo ditë.", [])
        ok, why = P.check_call("mcp__ElevenLabs__creative_generate_speech", ti2)
        self.assertFalse(ok)
        self.assertIn("eleven_multilingual_v2", " ".join(why))

    def test_other_generators_need_an_approved_test(self):
        ok, why = P.check_call("mcp__Higgs__execute_preset", {"preset_id": "x"})
        self.assertFalse(ok)
        self.assertIn("G-HUMAN-TEST", why[0])


class Records(Base):
    def make_vis(self, hero):
        self.lib_with_style()
        a = self.slide_run()
        if not hero:
            led = P.load_ledger(SLUG, POST)
            P.get_asset(led, "COVER@v1")["hero"] = False
            P.save_ledger(led)
        img = self.root / "cover.png"
        Image.new("RGB", (400, 500), (30, 30, 30)).save(img)
        V.main(["image", str(img), "--out", str(P.run_dir(SLUG, POST) / "qa" / "crops" / "COVER.v1"),
                "--spec", str(P.spec_path(SLUG, POST, "SL01"))])
        man = json.loads((P.run_dir(SLUG, POST) / "qa" / "crops" / "COVER.v1" / "manifest.json").read_text())
        return man

    def test_hero_fails_on_one_minor(self):
        man = self.make_vis(hero=True)
        rep = self.report(gate="G-VIS-SLIDE", asset_id="COVER", version=1, checks=self.checks("visual", {"V23": "minor"}),
                          files_opened=man["must_open"])
        st, notes = P.record_report(SLUG, POST, rep)
        self.assertEqual(st, "FAIL")
        self.assertIn("hero", notes[-1])
        self.assertTrue((P.OUT / "failure-log.csv").exists())

    def test_non_hero_passes_with_two_minors(self):
        man = self.make_vis(hero=False)
        rep = self.report(gate="G-VIS-SLIDE", asset_id="COVER", version=1,
                          checks=self.checks("visual", {"V23": "minor", "V21": "minor"}), files_opened=man["must_open"])
        self.assertEqual(P.record_report(SLUG, POST, rep)[0], "PASS")

    def test_review_without_opened_crops_is_invalid(self):
        self.make_vis(hero=False)
        rep = self.report(gate="G-VIS-SLIDE", asset_id="COVER", version=1, checks=self.checks("visual"),
                          files_opened=["full.png"])
        st, notes = P.record_report(SLUG, POST, rep)
        self.assertEqual(st, "FAIL")
        self.assertIn("did not open", " ".join(notes))

    def test_reports_must_be_independent(self):
        self.make_vis(hero=False)
        with self.assertRaises(P.PipelineError):
            P.record_report(SLUG, POST, {"gate": "G-VIS-SLIDE", "asset_id": "COVER", "version": 1, "status": "PASS"})

    def test_human_checkpoints_need_a_human(self):
        P.init_run(SLUG, POST, "carousel_mistakes")
        with self.assertRaises(P.PipelineError):
            P.record_gate(SLUG, POST, "G-HUMAN-HOOKBOARD", "PASS", "claude", note="looks fine")
        with self.assertRaises(P.PipelineError):
            P.record_gate(SLUG, POST, "G-VIS-SLIDE", "PASS", "claude")
        P.record_gate(SLUG, POST, "G-HUMAN-SPINE", "PASS", "claude (delegated)", note="picked spine B: strongest seam")
        text, n = P.queue_report(SLUG)
        self.assertIn("FYI", text)

    def test_steps_close_in_order_with_their_gates(self):
        P.init_run(SLUG, POST, "carousel_mistakes")
        with self.assertRaises(P.PipelineError):
            P.close_step(SLUG, POST, 1, "done")
        P.record_gate(SLUG, POST, "G-BRIEF", "PASS", "claude", note="brain-check clean")
        P.close_step(SLUG, POST, 0, "done")
        P.record_gate(SLUG, POST, "G-IDEA", "PASS", "idea-agent")
        P.close_step(SLUG, POST, 1, "done")
        with self.assertRaises(P.PipelineError):
            P.close_step(SLUG, POST, 3, "done")
        self.assertEqual(P.load_ledger(SLUG, POST)["steps"]["4"]["status"], "na")


class Crops(unittest.TestCase):
    def test_storyboard_panels_and_regions(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            im = Image.new("RGB", (1600, 900), (255, 255, 255))
            d = ImageDraw.Draw(im)
            for i, x in enumerate((20, 550, 1080)):
                d.rectangle((x, 20, x + 500, 880), fill=(40 + 60 * i, 90, 120))
            p = t / "board.png"
            im.save(p)
            spec = {"shot_id": "SH1", "format": "storyboard_panel",
                    "regions": [{"name": "hand", "kind": "hand", "box": [0.1, 0.1, 0.4, 0.4], "panel": 2}]}
            (t / "s.json").write_text(json.dumps(spec))
            V.main(["image", str(p), "--out", str(t / "out"), "--spec", str(t / "s.json"), "--panels", "auto"])
            man = json.loads((t / "out" / "manifest.json").read_text())
            self.assertEqual(man["panels"], 3)
            self.assertIn("region_SH1_hand.png", man["must_open"])
            self.assertEqual(sum(1 for f in man["files"] if f.startswith("tile_")), 9)
            tile = Image.open(t / "out" / "tile_r1c1.png")
            self.assertEqual(tile.size, (1600 // 3 * 2, 900 // 3 * 2))


class Hook(unittest.TestCase):
    def test_hook_blocks_unregistered_generation_and_ignores_other_tools(self):
        hook = HERE.parents[1] / ".claude" / "hooks" / "generation_gate.py"
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / "clients").mkdir()
            env = {"PIPELINE_ROOT": t, "PATH": "/usr/bin:/bin"}
            inp = {"tool_name": "mcp__Higgs__generate_image",
                   "tool_input": {"params": {"model": "gpt_image_2_5", "prompt": "unregistered"}}}
            r = subprocess.run([sys.executable, str(hook)], input=json.dumps(inp), capture_output=True, text=True, env=env)
            self.assertEqual(r.returncode, 0)
            out = json.loads(r.stdout)
            self.assertEqual(out["hookSpecificOutput"]["permissionDecision"], "deny")
            self.assertIn("not registered", out["hookSpecificOutput"]["permissionDecisionReason"])
            r = subprocess.run([sys.executable, str(hook)], input=json.dumps({"tool_name": "Bash", "tool_input": {}}),
                               capture_output=True, text=True, env=env)
            self.assertEqual((r.returncode, r.stdout), (0, ""))
            r = subprocess.run([sys.executable, str(hook)], input=json.dumps(
                {"tool_name": "mcp__Higgs__generate_image", "tool_input": {"params": {"model": "x", "get_cost": True}}}),
                capture_output=True, text=True, env=env)
            self.assertEqual((r.returncode, r.stdout), (0, ""))


if __name__ == "__main__":
    unittest.main()
