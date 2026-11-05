"""Builds the act 1 hero layers from the gated masters (run in the Higgsfield sandbox, which can reach the CDN).

Inputs: WEB-HERO-D.v2/src.png (desk master, G-VIS PASS) and WEB-CUP.v<n>/src.png (cup, G-VIS PASS).
Outputs (hero/): hero-d-poster.webp, hero-d-plate.webp (window glass keyed to alpha), hero-far.webp (the master's own
window view with sky added above), hero-cup.webp (matte + defocus), hero-p-poster.webp (9:16 crop around the phone),
boxes.json (far and cup boxes as fractions of the desktop frame). See hero-manifest.json for the published ids.
"""
import json, os
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
from scipy import ndimage

CUP_SRC = os.environ.get("CUP_SRC", "WEB-CUP.v2/src.png")
O = os.environ.get("OUT", "hero/")
rng = np.random.default_rng(7)
D = Image.open('WEB-HERO-D.v2/src.png').convert('RGB'); W, H = D.size
GX0, GX1, GY0, GY1 = 0.614, 0.981, 0.0, 0.563          # window glass, fractions of the frame

# far layer: the window view itself, with sky added above (scroll lag) and a few px on the other sides (pointer)
gx0, gx1, gy1 = round(GX0 * W), round(GX1 * W), round(GY1 * H)
glass = np.asarray(D.crop((gx0, 0, gx1, gy1))).astype(np.float32)
gw, gh = gx1 - gx0, gy1
pt, ps, pb = round(0.16 * gh), round(0.02 * gw), round(0.03 * gh)
far = np.zeros((gh + pt + pb, gw + 2 * ps, 3), np.float32)
far[pt:pt + gh, ps:ps + gw] = glass
top = glass[:6].mean(axis=0)
for y in range(pt):
    far[y, ps:ps + gw] = top * (0.92 + 0.08 * y / pt)
far[pt + gh:, ps:ps + gw] = glass[-1]
far[:, :ps] = far[:, ps:ps + 1]; far[:, ps + gw:] = far[:, ps + gw - 1:ps + gw]
sky = Image.fromarray(far[:pt + 8].clip(0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(10))
far[:pt] = np.asarray(sky).astype(np.float32)[:pt]
noise = rng.normal(0, 2.2, far.shape[:2])[..., None]
far[:pt] += noise[:pt]; far[:, :ps] += noise[:, :ps]; far[:, ps + gw:] += noise[:, ps + gw:]; far[pt + gh:] += noise[pt + gh:]
farI = Image.fromarray(far.clip(0, 255).astype(np.uint8))
far_box = [(gx0 - ps) / W, (0 - pt) / H, (gx1 + ps) / W, (gy1 + pb) / H]

# plate: the master with the window glass keyed to alpha (1 px feather)
mask = Image.new('L', (W, H), 255); ImageDraw.Draw(mask).rectangle([gx0 + 1, -2, gx1 - 2, gy1 - 2], fill=0)
mask = mask.filter(ImageFilter.GaussianBlur(0.8))
plate = D.copy(); plate.putalpha(mask)

# cup: matte from the white porcelain; every hole filled except the handle loop; exposure 0.9; then defocus
C = Image.open(CUP_SRC).convert('RGB'); cw, ch = C.size
c = np.asarray(C).astype(np.float32); L = c.mean(axis=2)
bg = np.median(np.concatenate([L[:50].ravel(), L[-50:].ravel()]))
a = np.clip((L - (bg + 18)) / 40, 0, 1)
solid = a > 0.5
filled = ndimage.binary_fill_holes(solid)
holes, n = ndimage.label(filled & ~solid)
sizes = ndimage.sum(np.ones_like(L), holes, range(1, n + 1)) if n else []
keep = np.zeros_like(solid)
if n:
    cms = ndimage.center_of_mass(np.ones_like(L), holes, range(1, n + 1))
    for i, (cy, cx) in enumerate(cms, 1):
        if not (cx / cw > 0.70 and sizes[i - 1] > 2000):
            keep |= holes == i
alpha = ndimage.gaussian_filter(np.maximum(a, keep.astype(np.float32)), 0.7)
ys, xs = np.where(alpha > 0.05)
bx0, by0, bx1, by1 = xs.min(), ys.min(), xs.max(), ys.max()
cup = Image.fromarray(np.dstack([c * 0.9, alpha * 255]).clip(0, 255).astype(np.uint8), 'RGBA')
m = 40
cup = cup.crop((bx0 - m, by0 - m, bx1 + m, by1 + m))
tw = 0.17 * W; s = tw / (bx1 - bx0)                    # cup + handle about 0.17 of the frame wide
cupS = cup.resize((round(cup.width * s), round(cup.height * s)), Image.LANCZOS)
blur = 9
r, g, b, al = cupS.split()
premul = Image.merge('RGB', [Image.fromarray((np.asarray(ch_).astype(np.float32) * np.asarray(al) / 255).astype(np.uint8)) for ch_ in (r, g, b)])
pa = np.asarray(premul.filter(ImageFilter.GaussianBlur(blur))).astype(np.float32)
aa = np.asarray(al.filter(ImageFilter.GaussianBlur(blur))).astype(np.float32)
un = np.where(aa[..., None] > 0, pa * 255 / np.maximum(aa[..., None], 1), 0)
cupB = Image.fromarray(np.dstack([un, aa]).clip(0, 255).astype(np.uint8), 'RGBA')
cx1 = 0.995 * W                                        # handle side near the right edge, foot below the bottom edge
left = cx1 - (m * s) - (bx1 - bx0) * s
top_ = 0.80 * H - m * s
cup_box = [left / W, top_ / H, (left + cupB.width) / W, (top_ + cupB.height) / H]

# posters: the live page at rest
comp = Image.new('RGBA', (W, H), (0, 0, 0, 255))
comp.alpha_composite(farI.convert('RGBA'), (round(far_box[0] * W), round(far_box[1] * H)))
comp.alpha_composite(plate)
comp.alpha_composite(cupB, (round(left), round(top_)))
comp = comp.convert('RGB')
os.makedirs(O, exist_ok=True)
def webp(img, name, w, q):
    im2 = img.resize((w, round(img.height * w / img.width)), Image.LANCZOS) if img.width != w else img
    im2.save(O + name, 'WEBP', quality=q, method=6)
webp(comp, 'hero-d-poster.webp', 2400, 74)
webp(plate, 'hero-d-plate.webp', 2400, 74)
webp(farI, 'hero-far.webp', round(farI.width * 2400 / W), 72)
webp(cupB, 'hero-cup.webp', round(cupB.width * 2400 / W), 78)
px0 = 0.436; pw = (H * 9 / 16) / W                     # portrait poster: 9:16 crop around the phone
P = comp.crop((round(px0 * W), 0, round((px0 + pw) * W), H)); webp(P, 'hero-p-poster.webp', P.width, 74)
json.dump({'far_box': far_box, 'cup_box': cup_box, 'glass': [GX0, GY0, GX1, GY1], 'portrait_x': [px0, px0 + pw]}, open(O + 'boxes.json', 'w'))
