"""The templates' pure functions, run under node exactly as written in the HTML (between kit:<name> markers)."""
import json
import re
import shutil
import subprocess
import unittest

from helpers import KIT

TEMPLATES = KIT / "templates"


def extract(template, name):
    text = (TEMPLATES / template).read_text()
    m = re.search(rf"// kit:{name} start.*?\n(.*?)// kit:{name} end", text, re.S)
    if not m:
        raise AssertionError(f"{template}: no kit:{name} block")
    return m.group(1)


def run_js(code):
    out = subprocess.run(["node", "-e", code], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


@unittest.skipUnless(shutil.which("node"), "node is needed to run the template code")
class TemplateLogicTest(unittest.TestCase):
    def schedule(self, groups, hide):
        return run_js(extract("captions.html", "schedule") +
                      f"\nconsole.log(JSON.stringify(schedule({json.dumps(groups)}, {json.dumps(hide)})));")

    def test_card_inside_a_whip_keeps_all_its_words(self):
        # v4 review: "RUNNING ADS" started 0.02 s before the whip window and showed only "ADS"
        groups = [[{"w": "content,", "s": 1.2, "e": 1.6}],
                  [{"w": "running", "s": 1.623, "e": 2.04}, {"w": "ads,", "s": 2.04, "e": 2.3}],
                  [{"w": "and", "s": 2.87, "e": 3.0}]]
        when = self.schedule(groups, [[1.64, 2.02]])
        self.assertIsNotNone(when[1])                       # the card is shown, whole
        self.assertAlmostEqual(when[1]["start"], 2.02)      # after the whip
        self.assertGreaterEqual(when[1]["end"] - when[1]["start"], 0.4)
        self.assertLessEqual(when[0]["end"], 1.64 - 0.08 + 1e-9)   # the card before leaves before the whip

    def test_two_cards_pushed_by_one_whip_do_not_collide(self):
        groups = [[{"w": "a", "s": 1.7, "e": 1.8}], [{"w": "b", "s": 1.9, "e": 2.0}], [{"w": "c", "s": 3.0, "e": 3.2}]]
        when = self.schedule(groups, [[1.64, 2.02]])
        self.assertTrue(all(when))
        self.assertLess(when[0]["end"], when[1]["start"] + 1e-9)
        self.assertGreater(when[1]["start"], when[0]["start"])

    def test_card_in_the_end_card_range_is_dropped(self):
        when = self.schedule([[{"w": "late", "s": 9.0, "e": 9.2}]], [[8.5, 10.6]])
        self.assertEqual(when, [None])

    def test_card_leaves_after_its_last_word(self):
        when = self.schedule([[{"w": "a", "s": 1.0, "e": 1.2}], [{"w": "b", "s": 3.0, "e": 3.2}]], [])
        self.assertAlmostEqual(when[0]["end"], 1.55)

    def test_behind_word_fits_inside_the_margins_at_its_slam_scale(self):
        # v4 review: OWNER reached x 1019 at the 1.06 slam
        fit = extract("move-behind.html", "fit")
        for width in (700, 900, 960, 1200):
            px = run_js(fit + f"\nconsole.log(JSON.stringify(fitPx(240, {width}, 890, 1.06, 65)));")
            drawn = width * px / 240 * 1.06
            self.assertLessEqual(540 + drawn / 2, 1015, (width, px))
            self.assertGreaterEqual(540 - drawn / 2, 65, (width, px))

    def test_orbit_word_stays_inside_the_margins(self):
        # v4 review: NO AGENCY reached x 1016
        clamp = extract("move-orbit.html", "clamp")
        for x, w in ((827, 380), (253, 380), (540, 200), (1000, 100)):
            cx = run_js(clamp + f"\nconsole.log(JSON.stringify(clampX({x}, {w}, 65, 1015)));")
            self.assertGreaterEqual(cx - w / 2, 65 - 1e-9)
            self.assertLessEqual(cx + w / 2, 1015 + 1e-9)


if __name__ == "__main__":
    unittest.main()
