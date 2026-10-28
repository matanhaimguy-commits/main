"""Plain-paper crop from a locked look-bible sheet: the World reference for shots without a set sheet.

Cuts a box of plain paper out of a sheet, scales it up and reports its mean colour, so the reference is made in
code and costs nothing. Usage:
  python3 growth-engine/tools/paper_crop.py SRC.png OUT.png --box X0 Y0 X1 Y1 [--size 512]
"""
from __future__ import annotations

import argparse
import sys

from PIL import Image, ImageStat


def crop_paper(src: str, out: str, box: tuple[int, int, int, int], size: int = 512) -> tuple[int, int, int]:
    """Crop `box` from `src`, scale it to `size` square with Lanczos, save to `out`; return the mean RGB."""
    im = Image.open(src).convert("RGB").crop(box)
    im = im.resize((size, size), Image.LANCZOS)
    im.save(out)
    return tuple(round(c) for c in ImageStat.Stat(im).mean)


def hex_rgb(rgb: tuple[int, int, int]) -> str:
    return "#" + "".join(f"{c:02x}" for c in rgb)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--box", type=int, nargs=4, required=True, metavar=("X0", "Y0", "X1", "Y1"))
    ap.add_argument("--size", type=int, default=512)
    a = ap.parse_args(argv)
    rgb = crop_paper(a.src, a.out, tuple(a.box), a.size)
    print(f"{a.out}: {a.size}x{a.size}, mean {hex_rgb(rgb)} {rgb}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
