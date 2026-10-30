"""Lay the text hook on a 9:16 concept frame, as the viewer sees frame 1 (top third, safe zone, phone-size type).

python3 text_hook_overlay.py frame.png "Text hook words" out.png [--phone out_360.png]
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

FONT = Path(__file__).resolve().parents[2] / "straightscale-en-01/assets/fonts/Montserrat/montserrat-latin-800-normal.woff2"
W, H = 1080, 1920
TOP, SIDE, RIGHT = 269, 65, 65       # STANDARDS 6 reels safe zone: top 269 px, 6% sides (text sits in the upper half)
SIZE = 80                            # display type; 3 lines end by y 557 (29%)
MAX_W = W - SIDE - RIGHT


def wrap(draw: ImageDraw.ImageDraw, text: str, font) -> list[str]:
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=font) <= MAX_W:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    return lines + [cur] if cur else lines


def compose(frame: Path, text: str) -> Image.Image:
    img = Image.open(frame).convert("RGB").resize((W, H), Image.LANCZOS)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(str(FONT), SIZE)
    y = TOP
    for line in wrap(draw, text, font):
        draw.text((SIDE, y), line, font=font, fill="white", stroke_width=6, stroke_fill="black")
        y += int(SIZE * 1.2)
    return img


def main() -> None:
    a = argparse.ArgumentParser()
    a.add_argument("frame"), a.add_argument("text"), a.add_argument("out")
    a.add_argument("--phone", help="also write a 360 px wide copy (the phone-size check)")
    args = a.parse_args()
    img = compose(Path(args.frame), args.text)
    img.save(args.out)
    if args.phone:
        img.resize((360, 640), Image.LANCZOS).save(args.phone)


if __name__ == "__main__":
    main()
