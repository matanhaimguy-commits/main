import unittest

import numpy as np

from helpers import EXAMPLE
from kit import face


def silhouette():
    """A head (ellipse) on a neck on wide shoulders, 270 x 472 like the analysis frames."""
    m = np.zeros((472, 270), bool)
    yy, xx = np.mgrid[0:472, 0:270]
    m |= ((xx - 135) / 60.0) ** 2 + ((yy - 120) / 80.0) ** 2 <= 1      # head 40..200
    m[195:240, 110:160] = True                                           # neck
    m[240:, 20:250] = True                                               # shoulders
    return m


class FaceTest(unittest.TestCase):
    def test_head_box_on_a_silhouette(self):
        x0, y0, x1, y1 = face.head_box(silhouette())
        self.assertAlmostEqual(y0, 40, delta=2)
        self.assertTrue(190 <= y1 <= 240, y1)          # the neck, above the shoulders
        self.assertTrue(70 <= x0 <= 80 and 190 <= x1 <= 200)

    def test_empty_mask(self):
        self.assertIsNone(face.head_box(np.zeros((10, 10), bool)))

    def test_face_band_is_inside_the_head_span(self):
        f = face.face_from_head([0, 100, 50, 200])
        self.assertAlmostEqual(f[1], 128)
        self.assertAlmostEqual(f[3], 208)

    def test_union(self):
        self.assertEqual(face.union([[0, 0, 5, 5], [2, -1, 9, 3]]), [0, -1, 9, 5])

    def test_real_cutout(self):
        r = face.run(EXAMPLE / "media" / "twin-cut.webm", every=2.0)
        self.assertEqual((r["src_w"], r["src_h"]), (1080, 1890))
        hx0, hy0, hx1, hy1 = r["head"]
        self.assertTrue(150 < hy0 < 260 and 900 < hy1 < 1100, r)


if __name__ == "__main__":
    unittest.main()
