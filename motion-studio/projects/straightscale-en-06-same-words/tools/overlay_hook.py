"""overlay.py <in.png> <out.png> "<text hook>": set the text hook in the top third (frame 1 as the edit shows it)."""
import sys
from PIL import Image, ImageDraw, ImageFont
src, out, text = sys.argv[1:4]
im = Image.open(src).convert("RGB"); W, H = im.size
font = ImageFont.truetype("/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf", int(W * 0.082))
d = ImageDraw.Draw(im); words = text.split(); lines, cur = [], ""
for w in words:
    t = (cur + " " + w).strip()
    if d.textlength(t, font=font) > W * 0.84 and cur: lines.append(cur); cur = w
    else: cur = t
lines.append(cur)
lh = int(font.size * 1.18); y = int(H * 0.09)
for ln in lines:
    x = (W - d.textlength(ln, font=font)) / 2
    d.text((x, y), ln, font=font, fill="#2B2A33"); y += lh
im.save(out); print(out, len(lines), "lines")
