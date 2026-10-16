#!/usr/bin/env python3
"""Replace a logo the image model drew in the bottom-left corner with the client's real logo file (FL-13).

  fix_drawn_logo.py <in> <out> <logo.png> [--width 0.27]

The brand kit says "Logo: real files only": a model-drawn logo is a defect (V24). New prompts leave the bottom-left
corner calm and empty and the real logo goes on with brand_overlay.py. This tool repairs images made before that rule:
it finds the drawn wordmark (white letters) and the drawn mark (red and gold shapes) in the bottom-left zone, inpaints
exactly those pixels (OpenCV Telea), then pastes the real logo at 27% of the width where the drawn one was.

Needs OpenCV (`pip install opencv-python-headless`); the Higgsfield sandbox has it. Run it where the image bytes are
(send this script with a heredoc; it is code, not file bytes). The output is a new asset version: it gets its own
visual review (V24 crop of the logo zone) before it replaces anything in the hub. Prints a JSON report; exit 1 when no
drawn logo is found (nothing to fix: use brand_overlay.py instead).
"""
from __future__ import annotations

import argparse
import json
import sys

import numpy as np
import cv2
from PIL import Image


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inp"); ap.add_argument("out"); ap.add_argument("logo")
    ap.add_argument("--width", type=float, default=0.27, help="logo width as a share of the image width")
    a = ap.parse_args(argv)

    img = cv2.imread(a.inp)
    if img is None:
        print(json.dumps({"ok": False, "error": f"cannot read {a.inp}"}))
        return 1
    H, W = img.shape[:2]
    b, g, r = [img[:, :, i].astype(int) for i in range(3)]
    zone = np.zeros((H, W), bool)
    zone[int(H * 0.875):int(H * 0.99), int(W * 0.02):int(W * 0.50)] = True
    spread = np.maximum(np.maximum(r, g), b) - np.minimum(np.minimum(r, g), b)
    white = zone & (r > 200) & (g > 200) & (b > 190) & (spread < 40)
    ys, xs = np.nonzero(white)
    if len(xs) < 50:
        print(json.dumps({"ok": False, "error": "no drawn wordmark found in the bottom-left zone"}))
        return 1
    tx0, tx1, ty0, ty1 = xs.min(), xs.max(), ys.min(), ys.max()
    near = np.zeros((H, W), bool)
    near[max(0, ty0 - int(H * 0.04)):min(H, ty1 + int(H * 0.02)), max(0, tx0 - int(W * 0.12)):min(W, tx1 + 8)] = True
    red = near & (r > 120) & (r > 2 * g) & (r > 2 * b)
    gold = near & (r > 160) & (g > 90) & (g < 210) & (b < 100) & (r > b + 80)
    mask = (white | red | gold) & near
    mask = cv2.dilate(mask.astype(np.uint8) * 255, np.ones((7, 7), np.uint8), iterations=2)
    ys2, xs2 = np.nonzero(mask)
    clean = cv2.inpaint(img, mask, 9, cv2.INPAINT_TELEA)

    im = Image.fromarray(cv2.cvtColor(clean, cv2.COLOR_BGR2RGB)).convert("RGBA")
    logo = Image.open(a.logo).convert("RGBA")
    logo = logo.crop(logo.getbbox())
    lw = int(W * a.width)
    lh = int(logo.height * lw / logo.width)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    x0 = int(xs2.min()) + 4
    cy = (int(ys2.min()) + int(ys2.max())) // 2
    im.alpha_composite(logo, (x0, cy - lh // 2))
    out = im.convert("RGB")
    out.save(a.out, quality=93) if a.out.lower().endswith((".jpg", ".jpeg")) else out.save(a.out)
    print(json.dumps({"ok": True, "masked_px": int((mask > 0).sum()),
                      "drawn_box": [int(xs2.min()), int(ys2.min()), int(xs2.max()), int(ys2.max())],
                      "logo_box": [x0, cy - lh // 2, x0 + lw, cy - lh // 2 + lh], "written": a.out}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
