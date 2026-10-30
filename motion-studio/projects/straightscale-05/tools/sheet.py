#!/usr/bin/env python3
"""Phone-size contact sheet from a rendered video, one frame per beat, each labelled with its time.
  python3 tools/sheet.py video.mp4 out.png t1,t2,... [--w 360] [--cols 6]"""
import subprocess, sys, tempfile, os
from PIL import Image, ImageDraw
v, out, ts = sys.argv[1], sys.argv[2], [float(x) for x in sys.argv[3].split(',')]
W = int(sys.argv[sys.argv.index('--w') + 1]) if '--w' in sys.argv else 360
COLS = int(sys.argv[sys.argv.index('--cols') + 1]) if '--cols' in sys.argv else 6
tiles = []
with tempfile.TemporaryDirectory() as d:
    for i, t in enumerate(ts):
        p = os.path.join(d, f'{i}.png')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', v, '-frames:v', '1', '-vf', f'scale={W}:-1', p], check=True)
        im = Image.open(p).convert('RGB'); ImageDraw.Draw(im).text((6, 4), f'{t:.2f}s', fill=(0, 230, 255)); tiles.append(im)
w, h = tiles[0].size; rows = (len(tiles) + COLS - 1) // COLS
sheet = Image.new('RGB', (COLS * (w + 6), rows * (h + 6)), (255, 255, 255))
for i, im in enumerate(tiles): sheet.paste(im, ((i % COLS) * (w + 6), (i // COLS) * (h + 6)))
sheet.save(out); print(out, sheet.size)
