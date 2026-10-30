import tempfile
import unittest
from pathlib import Path

from helpers import FACE, example_edl
from kit import project


class ProjectTest(unittest.TestCase):
    def test_build_writes_a_self_contained_project(self):
        if not (project.STUDIO / "vendor" / "gsap.min.js").is_file():
            self.skipTest("run bash motion-studio/setup.sh first (vendored GSAP)")
        with tempfile.TemporaryDirectory() as d:
            out = project.build(example_edl(), FACE, Path(d) / "build")
            for f in ("index.html", "assets/vendor/gsap.min.js", "assets/vendor/motion-blur.js",
                      "compositions/move-orbit.html", "assets/media/twin-cut.webm", "assets/media/wordmark-white.png"):
                self.assertTrue((out / f).is_file(), f)
            self.assertEqual(len(list((out / "assets" / "fonts").glob("*.woff2"))), 5)
            html = (out / "index.html").read_text()
            self.assertIn("assets/media/wordmark-white.png", html)   # media variables rewritten to local copies

    def test_templates_load_no_cdn(self):
        for t in (project.KIT / "templates").glob("*.html"):
            self.assertNotIn("cdn.jsdelivr", t.read_text(), t.name)
            self.assertNotIn("font:", t.read_text().replace("font: ", "font:"), t.name)

    def test_templates_use_fromto_only(self):
        # a .to() records its start state at whatever time first renders it, so the frame depends on seek order
        for t in (project.KIT / "templates").glob("*.html"):
            self.assertNotIn("tl.to(", t.read_text(), t.name)


if __name__ == "__main__":
    unittest.main()
