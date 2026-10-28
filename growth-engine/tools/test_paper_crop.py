import tempfile
import unittest
from pathlib import Path

from PIL import Image

import paper_crop


class PaperCropTest(unittest.TestCase):
    def test_crop_scales_and_reports_mean(self):
        with tempfile.TemporaryDirectory() as d:
            src, out = Path(d) / "s.png", Path(d) / "o.png"
            im = Image.new("RGB", (100, 100), (10, 10, 10))
            im.paste((246, 232, 210), (20, 20, 60, 60))
            im.save(src)
            rgb = paper_crop.crop_paper(str(src), str(out), (20, 20, 60, 60), size=64)
            self.assertEqual(rgb, (246, 232, 210))
            self.assertEqual(Image.open(out).size, (64, 64))
            self.assertEqual(paper_crop.hex_rgb(rgb), "#f6e8d2")


if __name__ == "__main__":
    unittest.main()
