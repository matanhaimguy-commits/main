#!/usr/bin/env python3
"""Phone-size contact sheet from a folder of stills (f_<time>.png) or from a video at given times.
  python3 tools/sheet.py <dir-of-pngs | video.mp4> out.jpg [t1,t2,...] [--w 360] [--cols 6] [--labels a,b,...]"""
import glob, os, subprocess, sys, tempfile
from PIL import Image, ImageDraw
src, out = sys.argv[1], sys.argv[2]
opt = lambda k, d: sys.argv[sys.argv.index('--' + k) + 1] if '--' + k in sys.argv else d
W, COLS = int(opt('w', 360)), int(opt('cols', 6))
labels = opt('labels', '').split(',') if opt('labels', '') else []
tiles = []
with tempfile.TemporaryDirectory() as d:
    if os.path.isdir(src):
        files = sorted(glob.glob(os.path.join(src, 'f_*.png')))
        items = [(f, os.path.basename(f)[2:-4].lstrip('0') or '0') for f in files]
    else:
        ts = [float(x) for x in sys.argv[3].split(',')]
        items = []
        for i, t in enumerate(ts):
            p = os.path.join(d, f'{i}.png')
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.3f}', '-i', src, '-frames:v', '1', p], check=True)
            items.append((p, f'{t:.2f}'))
    for i, (f, t) in enumerate(items):
        im = Image.open(f).convert('RGB'); im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
        dr = ImageDraw.Draw(im); txt = f'{t}s' + (f'  {labels[i]}' if i < len(labels) else '')
        dr.rectangle([0, 0, 8 + 7 * len(txt), 16], fill=(0, 0, 0)); dr.text((4, 2), txt, fill=(0, 230, 255))
        tiles.append(im)
w, h = tiles[0].size; rows = (len(tiles) + COLS - 1) // COLS
sheet = Image.new('RGB', (COLS * (w + 6) + 6, rows * (h + 6) + 6), (90, 90, 90))
for i, im in enumerate(tiles): sheet.paste(im, (6 + (i % COLS) * (w + 6), 6 + (i // COLS) * (h + 6)))
sheet.save(out, quality=88); print(out, sheet.size)
