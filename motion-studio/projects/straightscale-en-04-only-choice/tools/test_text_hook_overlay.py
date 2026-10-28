import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

import text_hook_overlay as t


class OverlayTest(unittest.TestCase):
    def test_lines_fit_the_safe_width(self):
        d = ImageDraw.Draw(Image.new("RGB", (t.W, t.H)))
        font = ImageFont.truetype(str(t.FONT), t.SIZE)
        lines = t.wrap(d, "Lost a client to someone cheaper? It wasn't your price.", font)
        self.assertTrue(all(d.textlength(x, font=font) <= t.MAX_W for x in lines))
        self.assertEqual(" ".join(lines), "Lost a client to someone cheaper? It wasn't your price.")

    def test_compose_is_1080x1920(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = Path(tmp) / "f.png"
            Image.new("RGB", (1152, 2048), "grey").save(f)
            self.assertEqual(t.compose(f, "Four words go here").size, (1080, 1920))


if __name__ == "__main__":
    unittest.main()
