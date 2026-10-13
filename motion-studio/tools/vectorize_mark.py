#!/usr/bin/env python3
"""Trace a flat-colour logo PNG into an SVG, one <path> per brand colour, so the real mark can be shown
sharp at any zoom (macro shots). This is a faithful trace of the client's file, not a redraw: the script
reports the IoU of every colour against the source and refuses to write below --min-iou.

usage: vectorize_mark.py symbol.png out.svg --color red=#BE0F18 --color gold=#DD9A10 [--tol 18] [--min-iou 0.995]
"""
import argparse, sys
import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter
from skimage import measure, draw

ap = argparse.ArgumentParser()
ap.add_argument('png'); ap.add_argument('svg')
ap.add_argument('--color', action='append', required=True, help='name=#hex (repeatable)')
ap.add_argument('--tol', type=float, default=60, help='max RGB distance to count a pixel as this colour')
ap.add_argument('--simplify', type=float, default=0.35, help='polygon tolerance in source px')
ap.add_argument('--min-iou', type=float, default=0.995)
a = ap.parse_args()

im = np.asarray(Image.open(a.png).convert('RGBA')).astype(np.float32)
H, W = im.shape[:2]
rgb, alpha = im[..., :3], im[..., 3] / 255
out, ok = [], True
for spec in a.color:
    name, hx = spec.split('=')
    c = np.array([int(hx[i:i + 2], 16) for i in (1, 3, 5)], np.float32)
    dist = np.linalg.norm(rgb - c, axis=2)
    # soft coverage: alpha times closeness to the colour (keeps antialiased edges as sub-pixel information)
    cov = alpha * np.clip(1.5 - dist / a.tol, 0, 1)
    cov = gaussian_filter(cov, 0.7)
    src = cov > 0.5
    contours = measure.find_contours(np.pad(cov, 1), 0.5)
    d, test = [], np.zeros_like(src)
    for cnt in contours:
        cnt = measure.approximate_polygon(cnt - 1, a.simplify)
        if len(cnt) < 4: continue
        area = 0.5 * np.sum(cnt[:-1, 1] * cnt[1:, 0] - cnt[1:, 1] * cnt[:-1, 0])
        if abs(area) < 40: continue  # specks
        rr, cc = draw.polygon(cnt[:, 0], cnt[:, 1], (H, W))
        test[rr, cc] ^= True
        # contour coordinates are pixel indices (pixel centres); SVG/canvas pixel centres sit at +0.5
        d.append('M' + ' L'.join(f'{x + 0.5:.2f},{y + 0.5:.2f}' for y, x in cnt[:-1]) + 'Z')
    iou = (src & test).sum() / max(1, (src | test).sum())
    ok &= iou >= a.min_iou
    print(f'{name}: {len(d)} contours, {sum(p.count("L") + 1 for p in d)} points, IoU {iou:.4f}')
    out.append(f'<path id="{name}" fill="{hx}" fill-rule="evenodd" d="{" ".join(d)}"/>')

if not ok:
    sys.exit(f'IoU below {a.min_iou}: not written')
open(a.svg, 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">\n'
                       + '\n'.join(out) + '\n</svg>\n')
print('wrote', a.svg)
