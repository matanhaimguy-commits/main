#!/usr/bin/env python3
"""Phone-size contact sheet: frames scaled to 360 px wide (a phone's width), labelled with their time.

    python3 tools/contact.py out.png frame1.png frame2.png ... [--cols 4] [--width 360] [--labels "a|b|c"]
"""
import argparse
import re

from PIL import Image, ImageDraw, ImageFont


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("frames", nargs="+")
    ap.add_argument("--cols", type=int, default=4)
    ap.add_argument("--width", type=int, default=360)
    ap.add_argument("--labels", default="")
    a = ap.parse_args()
    labels = a.labels.split("|") if a.labels else []
    w = a.width
    h = round(w * 1920 / 1080)
    rows = (len(a.frames) + a.cols - 1) // a.cols
    sheet = Image.new("RGB", (a.cols * (w + 12) + 12, rows * (h + 44) + 12), (40, 40, 40))
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 18)
    except OSError:
        font = ImageFont.load_default()
    for i, f in enumerate(a.frames):
        im = Image.open(f).convert("RGB").resize((w, h), Image.LANCZOS)
        x, y = 12 + (i % a.cols) * (w + 12), 12 + (i // a.cols) * (h + 44)
        sheet.paste(im, (x, y))
        m = re.search(r"at-([\d.]+)s", f)
        label = labels[i] if i < len(labels) else (m.group(1) + " s" if m else f.rsplit("/", 1)[-1])
        draw.text((x, y + h + 8), label, fill=(235, 235, 235), font=font)
    sheet.save(a.out)
    print(a.out, sheet.size)


if __name__ == "__main__":
    main()
