"""Tests for heygen_rules.py (the twin route's pure call checks). Run from growth-engine/tools:
python3 -m unittest test_heygen_rules"""
import json
import unittest
from pathlib import Path

import heygen_rules as R

HERE = Path(__file__).resolve().parent
RULES = json.loads((HERE.parent / "production" / "standards.json").read_text())["models"]["heygen"]
HOST = json.loads((HERE.parents[1] / "clients" / "straightscale-en" / "brain.json").read_text())["host"]
PORTRAIT, LANDSCAPE = "0295627e7d5e497980c0e20c50bb2db7", "fb4c6f11e09e4fd2863bcf77eaa00c2c"
VOICE = "8646763dcd2e4f97934ca00402817e4b"


def video(**kw):
    return {"avatarId": LANDSCAPE, "aspectRatio": "9:16", "fit": "cover", "audioUrl": "https://f.example/vo.mp3", **kw}


class Speech(unittest.TestCase):
    def test_the_brains_voices_only(self):
        self.assertEqual(R.speech_checks({"voiceId": VOICE, "text": "Hi."}, HOST, RULES["speech"]), [])
        self.assertIn("not one of the twin's voices",
                      R.speech_checks({"voiceId": "someone-else", "text": "Hi."}, HOST, RULES["speech"])[0])

    def test_no_unplanned_credits(self):
        base = {"voiceId": VOICE, "text": "Hi."}
        for k, v in (("forceRegenerate", True), ("engine", "elevenlabs"), ("engine", "heygen_voice"),
                     ("settings", {"model_id": "eleven_v4"})):
            with self.subTest(k=k, v=v):
                self.assertIn(k, " ".join(R.speech_checks({**base, k: v}, HOST, RULES["speech"])))
        self.assertEqual(R.speech_checks({**base, "forceRegenerate": False, "engine": None, "speed": 1}, HOST,
                                         RULES["speech"]), [])

    def test_plain_text_only(self):
        self.assertIn("no text", R.speech_checks({"voiceId": VOICE, "text": " "}, HOST, RULES["speech"])[0])
        self.assertIn("inputType", R.speech_checks({"voiceId": VOICE, "text": "<speak>x</speak>", "inputType": "ssml"},
                                                   HOST, RULES["speech"])[0])


class Video(unittest.TestCase):
    def test_the_locked_calls_pass(self):
        self.assertEqual(R.video_checks(video(), HOST, RULES["avatar_video"]), ([], "https://f.example/vo.mp3"))
        self.assertEqual(R.video_checks(video(avatarId=PORTRAIT, fit=None, audioUrl=None, audioAssetId="A1"), HOST,
                                        RULES["avatar_video"]), ([], "A1"))
        self.assertEqual(R.video_checks(video(resolution="1080p", removeBackground=False, outputFormat="mp4"), HOST,
                                        RULES["avatar_video"])[0], [])

    def test_refusals(self):
        cases = {
            "not one of the twin's looks": video(avatarId="stock-presenter"),
            "aspectRatio '16:9'": video(aspectRatio="16:9"),
            "aspectRatio 'auto'": video(aspectRatio="auto"),
            "never contain": video(fit="contain"),
            "fit None for the landscape": video(fit=None),
            "script, voiceId": video(script="Say this.", voiceId=VOICE),
            "motionPrompt": video(motionPrompt="wave"),
            "exactly one audio source": video(audioUrl=None),
            "caption.style": video(caption={"style": "default"}),
            "outputFormat": video(outputFormat="mov"),
            "reference_look_id": video(engine={"type": "avatar_v", "reference_look_id": "someone-else"}),
            "resolution '4k'": video(resolution="4k"),
            "background": video(background={"type": "color", "value": "#000000"}),
            "removeBackground": video(removeBackground=True),
            "outputFormat 'webm'": video(outputFormat="webm"),
        }
        for needle, ti in cases.items():
            with self.subTest(needle=needle):
                why, _ = R.video_checks(ti, HOST, RULES["avatar_video"])
                self.assertIn(needle, " ".join(why))
        why, value = R.video_checks(video(audioAssetId="A1"), HOST, RULES["avatar_video"])
        self.assertIn("exactly one audio source", " ".join(why))
        self.assertIsNone(value)

    def test_host_problem(self):
        self.assertIsNone(R.host_problem(HOST))
        self.assertIn("no HeyGen host", R.host_problem(None))
        self.assertIn("no looks", R.host_problem({"engine": "heygen", "looks": [], "voices": [{"id": "v"}]}))


if __name__ == "__main__":
    unittest.main()
