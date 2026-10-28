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


if __name__ == "__main__":
    unittest.main()
