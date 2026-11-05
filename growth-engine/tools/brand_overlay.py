#!/usr/bin/env python3
"""Paste a client's real logo file onto a generated image (models never draw logos: brand-kit "real files only").

  brand_overlay.py <in> <out> (--client <slug> [--logo wordmark-white] | --logo-file PATH) [--pos bottom-left]
                   [--width 0.27] [--margin-x 0.065] [--margin-y 0.04] [--check-only]

In the Higgsfield sandbox (no repo there), fetch the logo from the URL in clients/<slug>/brand/brand.json and pass
--logo-file; send this script with a heredoc (it is code, not file bytes).

The logo files live in clients/<slug>/brand/. Before pasting, it checks the area the logo will cover: it must be calm
(low detail) and give the logo enough contrast (4.5:1 for a white wordmark on its mean colour). A busy or bright area
fails with exit code 1: regenerate with the area left empty ("leave the bottom-left corner calm, dark and empty: no
logo, no text there") rather than pasting over clutter. Prints a JSON report.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageStat

ROOT = Path(__file__).resolve().parents[2]


def rel_lum(rgb) -> float:
    def ch(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb[:3]
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast(a, b) -> float:
    la, lb = sorted((rel_lum(a), rel_lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def place(img_size, logo_size, pos, width, mx, my):
    W, H = img_size
    lw = int(W * width)
    lh = int(logo_size[1] * lw / logo_size[0])
    x = int(W * mx) if "left" in pos else W - int(W * mx) - lw
    y = H - int(H * my) - lh if "bottom" in pos else int(H * my)
    return x, y, lw, lh


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inp"); ap.add_argument("out")
    ap.add_argument("--client")
    ap.add_argument("--logo-file", help="a logo PNG path (sandbox use)")
    ap.add_argument("--logo", default="wordmark-white")
    ap.add_argument("--pos", default="bottom-left", choices=["bottom-left", "bottom-right", "top-left", "top-right"])
    ap.add_argument("--width", type=float, default=0.27, help="logo width as a share of the image width")
    ap.add_argument("--margin-x", type=float, default=0.065)
    ap.add_argument("--margin-y", type=float, default=0.04)
    ap.add_argument("--max-detail", type=float, default=22.0, help="max std-dev of the area's luminance (calm area)")
    ap.add_argument("--check-only", action="store_true")
    a = ap.parse_args(argv)

    if a.logo_file:
        logo_p = Path(a.logo_file)
    elif a.client:
        logo_p = ROOT / "clients" / a.client / "brand" / f"{a.logo}.png"
    else:
        ap.error("give --client or --logo-file")
    if not logo_p.exists():
        print(json.dumps({"ok": False, "error": f"no logo file {logo_p}"}))
        return 1
    img = Image.open(a.inp).convert("RGB")
    logo = Image.open(logo_p).convert("RGBA")
    logo = logo.crop(logo.getbbox())
    x, y, lw, lh = place(img.size, logo.size, a.pos, a.width, a.margin_x, a.margin_y)
    pad = int(lh * 0.35)
    area = img.crop((max(0, x - pad), max(0, y - pad), min(img.width, x + lw + pad), min(img.height, y + lh + pad)))
    stat = ImageStat.Stat(area.convert("L"))
    mean_rgb = tuple(int(v) for v in ImageStat.Stat(area).mean)
    detail = stat.stddev[0]
    light_logo = a.logo.endswith("white") or "light" in logo_p.name or "white" in logo_p.name
    ratio = contrast((248, 246, 239) if light_logo else (31, 31, 31), mean_rgb)
    problems = []
    if detail > a.max_detail:
        problems.append(f"the area is busy (detail {detail:.1f} > {a.max_detail}): leave it calm and empty in the prompt")
    if ratio < 4.5:
        problems.append(f"contrast {ratio:.1f}:1 is under 4.5:1 for this logo on the area's mean colour {mean_rgb}")
    rep = {"ok": not problems, "logo": str(logo_p), "box": [x, y, x + lw, y + lh], "detail": round(detail, 1),
           "contrast": round(ratio, 2), "problems": problems}
    if problems or a.check_only:
        print(json.dumps(rep, indent=2))
        return 0 if (a.check_only and not problems) else (1 if problems else 0)
    out = img.convert("RGBA")
    out.alpha_composite(logo.resize((lw, lh), Image.LANCZOS), (x, y))
    out_p = Path(a.out)
    out.convert("RGB").save(out_p, quality=92) if out_p.suffix.lower() in (".jpg", ".jpeg") else out.convert("RGB").save(out_p)
    rep["written"] = str(out_p)
    print(json.dumps(rep, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
