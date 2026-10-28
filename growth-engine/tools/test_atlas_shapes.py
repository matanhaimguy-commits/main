"""The owner's Atlas entries as they stand in standards.json, on 9:16 and 4:5 work (S1, plan of 28 Oct): each
command line goes through the wrapper's parser (atlas_gate.decide) and the gate (pipeline.check_call), in process.
Nothing reaches Atlas. Runs with test_atlas_gate (it imports this class) or alone:

    python3 -m unittest test_atlas_shapes      (from growth-engine/tools)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "atlas"))
import atlas_gate as G  # noqa: E402
import pipeline as P  # noqa: E402
import test_pipeline as TP  # noqa: E402

SLUG, POST = TP.SLUG, TP.POST
REPO = HERE.parents[1]
I2V, R2V = "minimax/h3-developer/image-to-video", "minimax/h3-developer/reference-to-video"
T2I, EDIT, STT = "openai/gpt-image-2/text-to-image", "openai/gpt-image-2/edit", "xai/stt-v1"
SHOT, FRAME_URL, VO_URL = "S40-SEQ01-SH1", "https://cdn.example.com/acme/sf-01.png", "https://cdn.example.com/acme/vo.mp3"
CLIP_PROMPT = "She lifts the phone and reads the message; slow push in; warm desk lamp."
STILL_PROMPT = "Vertical 9:16 still: a founder at a desk at night, phone face up, warm lamp."
SLIDE_PROMPT = "Instagram slide, 4:5 frame inside a 2:3 canvas. TEXT: 'MISSED DMs' ..."
H3 = ("--param", "resolution=768P", "--param", "prompt_expansion=false")


class Shapes(TP.Base):
    def setUp(self):
        super().setUp()
        self._allowed = P.STANDARDS["models"]["atlas"]["allowed"]
        std = json.loads((REPO / "growth-engine/production/standards.json").read_text())
        P.STANDARDS["models"]["atlas"]["allowed"] = std["models"]["atlas"]["allowed"]

    def tearDown(self):
        P.STANDARDS["models"]["atlas"]["allowed"] = self._allowed
        super().tearDown()

    def gate(self, *argv):
        return P.check_call("atlas_generate", G.decide(list(argv)).tool_input())

    def spec(self, shot, aspect, fmt):
        TP.write(P.spec_path(SLUG, POST, shot), {**TP.SLIDE, "shot_id": shot, "format": fmt, "hero": False,
                                                 "camera": {**TP.SLIDE["camera"], "aspect": aspect}})
        P.spec_check(SLUG, POST)
        P.record_report(SLUG, POST, self.report(gate="G-SPEC", shot_id=shot, checks=[],
                                                spec_sha256=P.sha_file(P.spec_path(SLUG, POST, shot))))

    def asset(self, aid, atype, shots, prompt, medias, gate):
        P.new_asset(SLUG, POST, aid, atype, shots)
        a = P.set_prompt(SLUG, POST, aid, prompt, medias)
        P.record_report(SLUG, POST, self.report(gate=gate, asset_id=aid, version=a["version"],
                                                prompt_sha256=a["prompt_sha256"], checks=self.checks("prompt")))

    def clip_run(self, role="image"):
        """A 9:16 shot with its reviewed start frame and a reviewed clip prompt that uses it."""
        P.init_run(SLUG, POST, "reel_animation_short")
        self.spec(SHOT, "9:16", "animation_3d")
        P.new_asset(SLUG, POST, "SB-SEQ01", "storyboard", [SHOT])
        P.add_media(SLUG, POST, "SB-SEQ01@v1", ids=[FRAME_URL])
        P.record_gate(SLUG, POST, "G-VIS-BOARD", "OVERRIDE", "Matan", asset="SB-SEQ01@v1", note="test")
        P.record_gate(SLUG, POST, "G-CONTINUITY", "OVERRIDE", "Matan", note="test", covers=["SB-SEQ01@v1"])
        self.asset("SEQ01-video", "video_clip", [SHOT], CLIP_PROMPT, [{"value": FRAME_URL, "role": role}],
                   "G-PROMPT-VID")
        P.budget(SLUG, POST, planned=1, balance=8)
        led = P.load_ledger(SLUG, POST)
        led["steps"]["9"] = {"status": "done", "at": P.stamp()}
        P.save_ledger(led)

    def still_run(self, shot, aspect, atype, prompt, medias=(), family="carousel_mistakes", fmt="carousel_slide"):
        P.init_run(SLUG, POST, family)
        self.spec(shot, aspect, fmt)
        self.asset(atype.upper(), atype, [shot], prompt, list(medias), "G-PROMPT-IMG")
        P.budget(SLUG, POST, planned=1, balance=8)

    # ---- pass ----

    def test_h3_image_to_video_9x16_clip_follows_its_start_frame(self):
        self.clip_run()
        ok, why = self.gate("generate", "video", I2V, "-p", CLIP_PROMPT, "--image", FRAME_URL, "--duration", "6", *H3)
        self.assertTrue(ok, why)

    def test_h3_reference_to_video_9x16_by_ratio(self):
        self.clip_run(role="refers")
        args = ("generate", "video", R2V, "-p", CLIP_PROMPT, "--param", f'refers=[{{"url": "{FRAME_URL}"}}]', "--duration", "6",
                *H3)
        for bad, needle in (("adaptive", "ratio must be one of"), ("1:1", "ratio 1:1 differs from the Shot Spec (9:16)")):
            ok, why = self.gate(*args, "--ratio", bad)
            self.assertFalse(ok)
            self.assertIn(needle, " ".join(why))
        ok, why = self.gate(*args, "--ratio", "9:16")
        self.assertTrue(ok, why)

    def test_gpt_image_2_9x16_still_by_size(self):
        self.still_run("ST01", "9:16", "still", STILL_PROMPT, family="reel_animation_short", fmt="animation_3d")
        args = ("generate", "image", T2I, "-p", STILL_PROMPT, "--param", "quality=medium")
        ok, why = self.gate(*args, "--size", "1024x1536")
        self.assertIn("size 1024x1536 differs from the Shot Spec (9:16)", " ".join(why))
        ok, why = self.gate(*args, "--size", "1152x2048")
        self.assertTrue(ok, why)

    def test_gpt_image_2_4x5_slide_at_its_named_size(self):
        self.lib_with_style()
        P.add_media(SLUG, TP.LIB, "STYLE@v1", ids=["https://cdn.example.com/acme/style-v1.png"])
        style = "https://cdn.example.com/acme/style-v1.png"
        self.still_run("SL01", "4:5", "slide", SLIDE_PROMPT, [{"value": style, "role": "image_references"}])
        args = ("generate", "image", EDIT, "-p", SLIDE_PROMPT, "--images", style, "--param", "quality=medium")
        ok, why = self.gate(*args, "--size", "1152x2048")
        self.assertIn("this model makes 4:5 at 1024x1536", " ".join(why))
        ok, why = self.gate(*args, "--size", "1024x1536")
        self.assertTrue(ok, why)

    # ---- stays denied ----

    def test_wrong_model_is_denied_first(self):
        self.clip_run()
        ok, why = self.gate("generate", "video", "bytedance/seedance-2.0/image-to-video", "-p", CLIP_PROMPT, "--image",
                            FRAME_URL, "--duration", "6")
        self.assertFalse(ok)
        self.assertIn("is not on the owner's list", why[0])

    def test_duration_outside_the_limits_is_denied(self):
        self.clip_run()
        for d in ("3", "16"):
            ok, why = self.gate("generate", "video", I2V, "-p", CLIP_PROMPT, "--image", FRAME_URL, "--duration", d, *H3)
            self.assertFalse(ok)
            self.assertIn("outside 4 to 15 s", " ".join(why))

    def test_a_prompt_on_stt_is_denied(self):
        P.init_run(SLUG, POST, "reel_quote_broll")
        P.new_asset(SLUG, POST, "VO", "voice")
        P.add_media(SLUG, POST, "VO@v1", ids=[VO_URL])
        ok, why = self.gate("generate", "audio", STT, "--audio", VO_URL, "--param", "language=en", "-p", "hello")
        self.assertFalse(ok)
        self.assertIn("takes no prompt", " ".join(why))
