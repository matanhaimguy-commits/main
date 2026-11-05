#!/usr/bin/env python3
"""Static charcoal ground for straightscale-06: brand charcoal #1F1F1F, a soft warm vignette and seeded grain
(the grain dithers the vignette so H.264 does not band it). One image per format, rebuilt the same every time.
    python3 tools/make_bg.py   ->  film/assets/bg-9x16.jpg, film/assets/bg-4x5.jpg"""
import os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'film', 'assets')
for name, (w, h) in {'9x16': (1080, 1920), '4x5': (1080, 1350)}.items():
    rng = np.random.default_rng(6)                      # seeded: same file every build
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    # elliptical distance from a centre a little above the middle (where the chart sits)
    d = np.sqrt(((x - w * 0.5) / (w * 0.75)) ** 2 + ((y - h * 0.47) / (h * 0.62)) ** 2)
    vig = np.clip(d - 0.35, 0, None) ** 1.6 * 9.0          # up to ~ -7 levels in the corners
    base = np.array([31.0, 31.0, 31.0])                    # #1F1F1F
    warm = np.array([1.2, 0.6, 0.0])                       # a breath of warmth in the centre (marble side)
    centre = np.clip(0.9 - d, 0, 1)[..., None]
    img = base[None, None, :] + warm[None, None, :] * centre - vig[..., None]
    img += rng.normal(0, 1.6, (h, w, 1))                   # monochrome grain
    Image.fromarray(np.clip(np.round(img), 0, 255).astype(np.uint8)).save(
        os.path.join(OUT, f'bg-{name}.jpg'), quality=93, subsampling=0)
    print(name, img.mean().round(2), img.min().round(1), img.max().round(1))
