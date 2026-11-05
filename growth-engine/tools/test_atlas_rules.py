"""The owner's Atlas entries as pure rules (atlas_rules.py): OmniHuman's audio-led length and prop-only subjects, and
xai/stt-v1 as an analysis call. Run from growth-engine/tools: python3 -m unittest test_atlas_rules"""
import json
import unittest
from pathlib import Path

import atlas_rules as R

STD = json.loads((Path(__file__).resolve().parents[1] / "production" / "standards.json").read_text())
ALLOWED = STD["models"]["atlas"]["allowed"]
OMNI, STT = "bytedance/avatar-omni-human-v2.0", "xai/stt-v1"
SLICE, FRAME = "https://cdn.example.com/acme/slice-01.mp3", "https://cdn.example.com/acme/sb-01.png"
OBJECT_SPEC = {"shot_id": "S30-SEQ01-SH1", "subjects": [{"id": "PR-PHONE"}]}


def entry(model):
    return next(e for e in ALLOWED if e["id"] == model)


def omni_req(params=None, medias=None):
    return {"kind": "video", "model": OMNI, "prompt": "the phone talks", "params": params or {}, "atlas": entry(OMNI),
            "medias": medias if medias is not None else [{"value": FRAME, "role": "image"},
                                                         {"value": SLICE, "role": "audio"}]}


class Entries(unittest.TestCase):
    def test_the_owners_list_reads_and_names_both_models(self):
        self.assertEqual([R.entry_problem(e) for e in ALLOWED], [None] * len(ALLOWED))
        self.assertEqual(R.find_entry(ALLOWED, OMNI, "video")[1], [])
        self.assertEqual(R.find_entry(ALLOWED, STT, "audio")[1], [])
        self.assertTrue(entry(STT)["analysis"])
        self.assertEqual(entry(STT)["params"], {"language": "en"})

    def test_new_keys_are_checked(self):
        for bad in ({"id": "m", "kind": "video", "min_s": 4, "max_s": 15, "duration_from": "prompt"},
                    {"id": "m", "kind": "video", "min_s": 4, "max_s": 15, "aspect_from": "spec"},
                    {"id": "m", "kind": "audio", "duration_from": "audio"},
                    {"id": "m", "kind": "video", "min_s": 4, "max_s": 15, "prop_subjects_only": "yes"},
                    {"id": "m", "kind": "audio", "analysis": True},
                    {"id": "m", "kind": "image", "analysis": True, "reads": ["voice"]},
                    {"id": "m", "kind": "audio", "analysis": True, "reads": ["voice"], "use": ["voice"]},
                    {"id": "m", "kind": "audio", "analysis": True, "reads": ["voice"], "text_fields": ["x"]},
                    {"id": "m", "kind": "audio", "reads": ["voice"]}):
            with self.subTest(bad=bad):
                self.assertIsNotNone(R.entry_problem(bad))


class Shapes(unittest.TestCase):
    """size_for_aspect (gpt-image-2) and reference objects (H3 reference-to-video refers)."""

    def test_size_for_aspect_is_checked(self):
        base = {"id": "m/x", "kind": "image"}
        self.assertIsNone(R.entry_problem({**base, "size_for_aspect": {"4:5": ["1024x1536"]}}))
        for bad in ({"4:5": "1024x1536"}, ["4:5"], {"4:5": [1024]}):
            self.assertIn("size_for_aspect maps", R.entry_problem({**base, "size_for_aspect": bad}))
        self.assertIn("don't mix", R.entry_problem({**base, "size_for_aspect": {"4:5": ["1x1"]}, "aspect_from": "image"}))

    def test_reference_objects_are_structure_not_text(self):
        e = entry("minimax/h3-developer/reference-to-video")
        req = {"model": e["id"], "medias": [{"value": FRAME, "role": "refers"}],
               "params": {"resolution": "768P", "prompt_expansion": False, "ratio": "9:16"}}
        for refers, loose in (([{"url": FRAME}], None), ([{"url": FRAME, "type": "image"}], None),
                              ([{"url": "https://elsewhere/x.png"}], "url"), ([{"url": FRAME, "type": "a cat"}], "type"),
                              ([{"url": FRAME, "caption": "a cat"}], "caption")):
            with self.subTest(refers=refers):
                why = R.param_checks({**req, "params": {**req["params"], "refers": refers}}, e)
                self.assertEqual(why, []) if loose is None else self.assertIn("refers carries text", why[0])


class OmniHuman(unittest.TestCase):
    def why(self, req, seconds=9.4, specs=(OBJECT_SPEC,), atype="video_clip"):
        return " | ".join(R.entry_checks(req, {"type": atype}, list(specs), lambda v: seconds if v == SLICE else None))

    def test_a_talking_object_clip_with_a_measured_slice_passes(self):
        self.assertEqual(self.why(omni_req()), "")
        self.assertEqual(self.why(omni_req({"watermark": False})), "")

    def test_length_comes_from_the_audio(self):
        self.assertIn("has no duration setting", self.why(omni_req({"duration": 10})))
        self.assertIn("has no measured length", self.why(omni_req(), seconds=None))
        self.assertIn("the audio is 22 s", self.why(omni_req(), seconds=22))
        self.assertIn("the audio is 3.5 s", self.why(omni_req(), seconds=3.5))
        self.assertIn("exactly one audio reference (0", self.why(omni_req(medias=[{"value": FRAME, "role": "image"}])))

    def test_only_props_talk(self):
        person = {"shot_id": "S30-SEQ01-SH2", "subjects": [{"id": "PR-PHONE"}, {"id": "CH-ARTA"}]}
        self.assertIn("talking-object clips only: shot S30-SEQ01-SH2", self.why(omni_req(), specs=[OBJECT_SPEC, person]))
        self.assertIn("subjects none", self.why(omni_req(), specs=[{"shot_id": "X", "subjects": []}]))
        self.assertIn("serves no Shot Spec", self.why(omni_req(), specs=[]))

    def test_other_rules_still_apply(self):
        self.assertIn("watermark must be one of [False]", self.why(omni_req({"watermark": True})))
        self.assertIn("seed carries text", self.why(omni_req({"seed": "x"})))
        self.assertIn("not a cover", self.why(omni_req(), atype="cover"))


class Stt(unittest.TestCase):
    def why(self, prompt="", medias=None, params=None, types=None):
        req = {"kind": "audio", "model": STT, "prompt": prompt, "params": {"language": "en", **(params or {})},
               "medias": medias if medias is not None else [{"value": SLICE, "role": "audio"}]}
        known = types if types is not None else {SLICE: "audio_slice"}
        return " | ".join(R.analysis_checks(req, entry(STT), known.get))

    def test_english_word_timings_on_our_own_file_pass(self):
        self.assertEqual(self.why(), "")
        self.assertEqual(self.why(params={"diarize": True, "filler_words": False}), "")
        self.assertEqual(self.why(types={SLICE: "final"}), "")

    def test_no_prompt_one_registered_file_english_only(self):
        self.assertIn("takes no prompt", self.why(prompt="transcribe this"))
        self.assertIn("not registered on any asset", self.why(types={}))
        self.assertIn("not a cover", self.why(types={SLICE: "cover"}))
        self.assertIn("exactly one reference", self.why(medias=[]))
        self.assertIn("exactly one reference", self.why(medias=[{"value": SLICE, "role": "audio"}] * 2))
        self.assertIn("pass language: 'en'", self.why(params={"language": "fr"}))
        self.assertIn("keyterm carries text", self.why(params={"keyterm": ["StraightScale"]}))
        self.assertIn("audio_format must be one of ['auto']", self.why(params={"audio_format": "pcm"}))


class Conditions(unittest.TestCase):
    """Matan's 28 Oct names (FORMATS.md 5): 1440p-sr for faces, gpt-image-2 high for realistic people, instrumental
    music-3.0 beds, and the test-only models of the F1 and F6 comparisons."""
    DEV = "minimax/h3-developer/reference-to-video"
    FACE = {"shot_id": "S30-SEQ01-SH1", "format": "talking_head", "regions": [{"name": "face", "kind": "face"}]}
    MOUTH = {"shot_id": "S30-SEQ01-SH2", "format": "ugc", "regions": [{"name": "mouth-close", "kind": "other"}]}
    BROLL = {"shot_id": "S30-SEQ02-SH1", "format": "realistic_photo", "regions": [{"name": "desk", "kind": "prop"}]}
    SHEET = {"shot_id": "SHEET-CH-MAYA", "format": "character_sheet", "regions": [{"name": "face", "kind": "face"}]}
    CLAY = {"shot_id": "S30-SEQ03-SH1", "format": "claymation"}

    def why(self, model, params, atype, specs, kind="video"):
        e = entry(model)
        req = {"kind": kind, "model": model, "prompt": "p", "params": params, "atlas": e, "medias": []}
        return " | ".join(R.entry_checks(req, {"type": atype}, list(specs), lambda v: None))

    def h3(self, res, specs):
        return self.why(self.DEV, {"resolution": res, "prompt_expansion": False, "ratio": "9:16", "duration": 10},
                        "video_clip", specs)

    def test_1440p_sr_only_for_a_face_or_mouth(self):
        self.assertEqual(self.h3("768P", [self.BROLL]), "")
        self.assertEqual(self.h3("1440p-sr", [self.FACE]), "")
        self.assertEqual(self.h3("1440p-sr", [self.BROLL, self.MOUTH]), "")
        self.assertIn("1440p-sr' is only for face or mouth", self.h3("1440p-sr", [self.BROLL]))
        self.assertIn("1440p-sr' is only for face or mouth", self.h3("1440p-sr", []))
        self.assertIn("one of ['768P', '1440p-sr']", self.h3("4k-sr", [self.FACE]))
        i2v = entry("minimax/h3-developer/image-to-video")
        self.assertEqual(i2v["params_when"], {"resolution": {"1440p-sr": "face_or_mouth"}})

    def gpt(self, quality, atype, specs):
        return self.why("openai/gpt-image-2/edit", {"quality": quality, "size": "1152x2048"}, atype, specs, "image")

    def test_gpt_image_2_high_only_for_realistic_people(self):
        self.assertEqual(self.gpt("medium", "slide", [self.CLAY]), "")
        self.assertEqual(self.gpt("high", "start_frame", [self.FACE]), "")
        self.assertEqual(self.gpt("high", "still", [self.MOUTH]), "")
        self.assertEqual(self.gpt("high", "character_sheet", [self.SHEET, self.FACE]), "")
        self.assertIn("serves no such shot", self.gpt("high", "character_sheet", [self.SHEET]))
        self.assertIn("S30-SEQ03-SH1 (claymation)", self.gpt("high", "start_frame", [self.FACE, self.CLAY]))
        self.assertIn("a slide is not a realistic-people asset", self.gpt("high", "slide", [self.FACE]))
        self.assertIn("one of ['medium', 'high']", self.gpt("low", "slide", [self.CLAY]))
        t2i = entry("openai/gpt-image-2/text-to-image")
        self.assertEqual(t2i["params"], {"quality": "medium"}, "text-to-image stays at medium (F5 named /edit)")

    def test_music_3_beds_are_instrumental(self):
        m = "minimax/music-3.0"
        ok = {"is_instrumental": True, "lyrics_optimizer": False}
        self.assertEqual(self.why(m, ok, "music", [], "audio"), "")
        self.assertEqual(self.why(m, {**ok, "format": "wav", "sample_rate": 44100}, "music", [], "audio"), "")
        self.assertIn("pass is_instrumental: True", self.why(m, {**ok, "is_instrumental": False}, "music", [], "audio"))
        self.assertIn("lyrics carries text", self.why(m, {**ok, "lyrics": "la la"}, "music", [], "audio"))
        self.assertIn("pass lyrics_optimizer: False", self.why(m, {"is_instrumental": True}, "music", [], "audio"))
        self.assertIn("not a song", self.why(m, ok, "song", [], "audio"))

    def test_test_only_models_make_test_assets_only(self):
        nb = {"resolution": "2k", "aspect_ratio": "9:16"}
        self.assertIn("G-HUMAN-TEST comparison only, not a character_sheet",
                      self.why("google/nano-banana-2/edit", nb, "character_sheet", [], "image"))
        h3 = {"resolution": "2K", "prompt_expansion": False, "ratio": "9:16", "duration": 10}
        self.assertIn("comparison only, not a video_clip", self.why("minimax/h3/reference-to-video", h3, "video_clip",
                                                                     [self.FACE]))
        self.assertEqual(R.C.test_only_checks(entry("google/nano-banana-2/edit"), {"type": "test"}), [])

    def test_new_keys_are_read_strictly(self):
        base = {"id": "m", "kind": "image", "params_one_of": {"quality": ["medium", "high"]}}
        self.assertIsNone(R.entry_problem({**base, "params_when": {"quality": {"high": "realistic_people"}}}))
        for bad, needle in (({"quality": "high"}, "maps a parameter"), ({"quality": {"high": "vip"}}, "not vip"),
                            ({"quality": {"ultra": "realistic_people"}}, "also in params_one_of")):
            self.assertIn(needle, R.entry_problem({**base, "params_when": bad}))
        self.assertIn("test_only is true or false", R.entry_problem({**base, "test_only": "yes"}))


if __name__ == "__main__":
    unittest.main()
