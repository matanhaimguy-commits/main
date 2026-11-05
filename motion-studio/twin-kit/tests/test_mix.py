import re
import subprocess
import tempfile
import unittest
from pathlib import Path

from kit import mix, sfx

LOUDNORM_OUT = """[Parsed_loudnorm_0 @ 0x1]
{
	"input_i" : "-23.10",
	"input_tp" : "-6.20",
	"input_lra" : "4.00",
	"input_thresh" : "-33.40",
	"output_i" : "-14.00",
	"output_tp" : "-2.00",
	"output_lra" : "3.10",
	"output_thresh" : "-24.30",
	"normalization_type" : "linear",
	"target_offset" : "0.10"
}
"""


def tone(path, freq, dur, vol):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"sine=frequency={freq}:duration={dur}",
                    "-af", f"volume={vol}", str(path)], check=True)


def lufs(path):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", "ebur128", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", err)[-1])


class MixTest(unittest.TestCase):
    def test_parse_loudnorm(self):
        m = mix.parse_loudnorm("noise\n" + LOUDNORM_OUT)
        self.assertEqual(m["input_i"], "-23.10")

    def test_pass_two_filter_uses_measured_values(self):
        f = mix.loudnorm_filter(mix.parse_loudnorm(LOUDNORM_OUT))
        self.assertIn("measured_I=-23.10", f)
        self.assertIn("linear=true", f)
        self.assertIn("I=-14.0", f)

    def test_graph_has_ducking_and_every_cue(self):
        cues = [sfx.cue(1.0, "pop", "a", "hero"), sfx.cue(2.5, "whoosh", "b", "cut")]
        _, g = mix.premix_graph(cues, 0.3, {"src": "m.mp3", "gain_db": -15}, 6.0)
        self.assertIn("sidechaincompress", g)
        self.assertIn("adelay=300:all=1", g)            # voice delayed to its start
        self.assertIn("adelay=2500:all=1", g)
        self.assertIn("amix=inputs=4", g)               # voice, music, two cues
        self.assertIn("[mstem]", g)

    def test_graph_without_music(self):
        _, g = mix.premix_graph([], 0.0, None, 3.0)
        self.assertNotIn("sidechaincompress", g)
        self.assertIn("amix=inputs=1", g)

    def test_end_to_end_lands_on_target(self):
        with tempfile.TemporaryDirectory() as d:
            d = Path(d)
            tone(d / "vo.wav", 300, 4, 0.05)
            tone(d / "m.wav", 90, 6, 0.4)
            cues = [sfx.cue(1.0, "pop", "a", "hero")]
            mix.premix(d / "vo.wav", 0.5, {"src": str(d / "m.wav"), "gain_db": -12}, cues, 5.0,
                       d / "pre.wav", d / "vo-stem.wav", d / "m-stem.wav")
            for f in ("pre.wav", "vo-stem.wav", "m-stem.wav"):
                self.assertTrue((d / f).stat().st_size > 1000, f)
            measured, final = mix.master(d / "pre.wav", d / "out.wav")
            self.assertAlmostEqual(lufs(d / "out.wav"), -14.0, delta=1.0)
            self.assertLessEqual(float(final["output_tp"]), -1.5)


if __name__ == "__main__":
    unittest.main()
