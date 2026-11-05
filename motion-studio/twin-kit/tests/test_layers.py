import re
import unittest

from helpers import FACE, small_edl, example_edl
from kit import layers
from kit.moves import LAYERS, MOVES, SCENES, FIXED


class LayersTest(unittest.TestCase):
    def test_every_template_has_a_unique_composition_id(self):
        ids = [layers.comp_id(s["template"]) for t in (MOVES, SCENES, FIXED) for s in t.values() if s["template"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_layer_order(self):
        order = ["set", "scene", "grade", "words-back", "twin", "words-front", "captions", "end", "flash"]
        self.assertEqual([LAYERS[k] for k in order], sorted(LAYERS[k] for k in order))

    def test_orbit_is_mounted_behind_and_in_front(self):
        clips = layers.clips(example_edl(), FACE)
        orbit = [(z, h) for z, h in clips if 'id="b4-hero-' in h]
        self.assertEqual(sorted(z for z, _ in orbit), [LAYERS["words-back"], LAYERS["words-front"]])
        self.assertTrue(all("&quot;head&quot;" in h for _, h in orbit))

    def test_clip_times_follow_the_edl(self):
        html = dict((h.split('"')[1], h) for _, h in layers.clips(example_edl(), FACE))
        self.assertIn('data-start="0.000"', html["b1-hero"])     # the hook is on frame 0
        self.assertIn('data-duration="1.800"', html["b1-hero"])
        self.assertIn('data-start="8.450"', html["b7-flash"])

    def test_captions_hide_the_end_card(self):
        cap = next(h for _, h in layers.clips(example_edl(), FACE) if 'id="captions"' in h)
        hide = cap.replace("&quot;", '"').replace('\\"', '"')
        self.assertIn("[8.5, 10.6]", hide)                         # the end card
        self.assertIn("[1.64, 2.02]", hide)                        # the whip into b2 (out 0.16 s, in 0.22 s)

    def test_twin_track_sets_each_beat(self):
        e = small_edl()
        e["beats"][0]["twin"] = "full"
        lines = layers.twin_track(e, FACE)
        self.assertEqual(len(lines), 4)
        self.assertIn("opacity: 0", lines[1])
        self.assertIn("scale: 1.0000", lines[0])
        self.assertIn('"--fx": "0.0%"', lines[0])                 # full frame: no soft edge
        self.assertIn('"--fx": "16.0%"', lines[2])                # stage: the clip's box edges fade out

    def test_whip_alternates_direction(self):
        e = small_edl()
        e["beats"][2]["cut_in"] = "whip"
        xs = [re.findall(r"x: (-?\d+), scale", l)[1] for l in layers.whip_track(e) if '"power3.in"' in l]
        self.assertEqual(len(xs), 2)
        self.assertNotEqual(xs[0], xs[1])

    def test_index_html(self):
        html = layers.index_html(example_edl(), FACE, "assets/media/twin.webm",
                                 [{"family": "X", "src": "assets/fonts/x.woff2", "weight": 900}])
        self.assertIn('window.__timelines["main"]', html)
        self.assertIn('src="assets/media/twin.webm"', html)
        self.assertIn('font-family: "X"', html)
        self.assertNotIn("cdn.jsdelivr", html)


if __name__ == "__main__":
    unittest.main()
