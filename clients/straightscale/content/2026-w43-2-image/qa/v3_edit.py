#!/usr/bin/env python3
"""IMG-W43-2 (2026-w43-2-image) v3 = v2 + three local code fixes. No image generation.

Run in the Higgsfield sandbox:
    python3 v3_edit.py            # writes /home/user/drafts/fixed/be2672d8_v3.jpg (1080x1350, q93)

Inputs
  ORIG  model output with the drawn logo   /home/user/drafts/be2672d8-7527-434c-8be5-8fe201468af1.jpg
  V2    drawn logo inpainted + real logo    /home/user/drafts/fixed/be2672d8.jpg   (base for v3)
  LOGO  real logo                           /home/user/brand/straightscale-logo-light.png

Fixes (VISUAL-QA 5.5 route: paint-out / local edit)
  V23  restore the table-edge highlight beads that the v2 inpaint wiped (copy ORIG back, box x120-185 y1150-1196,
       only where the pixel is not drawn logo; under the real logo's soft edge re-composite over the ORIG background).
  V21  recolour the crimson box behind "sistem." (#A00911 -> flat #B31217) by colour unmixing; letters untouched.
  V11  flatten the tiny pseudo-word day headers and the footer mark on both agenda pages to plain paper
       (local quadratic paper-tone fit + matched grain), ruled lines and red squares untouched.
Everything outside the three zones stays byte-for-byte the v2 pixels (before the final JPEG encode).
"""
import json
import sys

import cv2
import numpy as np
from PIL import Image

ORIG = '/home/user/drafts/be2672d8-7527-434c-8be5-8fe201468af1.jpg'
V2 = '/home/user/drafts/fixed/be2672d8.jpg'
LOGO = '/home/user/brand/straightscale-logo-light.png'
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/user/drafts/fixed/be2672d8_v3.jpg'

orig = np.array(Image.open(ORIG).convert('RGB')).astype(np.float32)
v2 = np.array(Image.open(V2).convert('RGB')).astype(np.float32)
H, W = v2.shape[:2]
assert (W, H) == (1080, 1350)
out = v2.copy()
report = {}

# ----------------------------------------------------------------------------------------------------------------
# Fix 1 (V23): highlight beads above/right of the pasted mark
# ----------------------------------------------------------------------------------------------------------------
# Rebuild exactly what fixlogo2.py did on ORIG: the drawn-logo mask, its Telea clean plate, and the real logo's
# alpha at its pasted place (291x54 at x100 y1193).
img = cv2.imread(ORIG)
b_, g_, r_ = [img[:, :, i].astype(int) for i in range(3)]
zone = np.zeros((H, W), bool); zone[int(H*0.875):int(H*0.99), int(W*0.02):int(W*0.50)] = True
white = zone & (r_ > 200) & (g_ > 200) & (b_ > 190) & ((np.maximum(np.maximum(r_, g_), b_) - np.minimum(np.minimum(r_, g_), b_)) < 40)
ys, xs = np.nonzero(white); tx0, tx1, ty0, ty1 = xs.min(), xs.max(), ys.min(), ys.max()
near = np.zeros((H, W), bool)
near[max(0, ty0-int(H*0.04)):min(H, ty1+int(H*0.02)), max(0, tx0-int(W*0.12)):min(W, tx1+8)] = True
red = near & (r_ > 120) & (r_ > 2*g_) & (r_ > 2*b_)
gold = near & (r_ > 160) & (g_ > 90) & (g_ < 210) & (b_ < 100) & (r_ > b_ + 80)
raw = (white | red | gold) & near
dil = cv2.dilate(raw.astype(np.uint8)*255, np.ones((7, 7), np.uint8), iterations=2)
clean = cv2.cvtColor(cv2.inpaint(img, dil, 9, cv2.INPAINT_TELEA), cv2.COLOR_BGR2RGB).astype(np.float32)
ys2, xs2 = np.nonzero(dil)
logo = Image.open(LOGO).convert('RGBA'); logo = logo.crop(logo.getbbox())
lw = int(W*0.27); lh = int(logo.height*lw/logo.width); logo = logo.resize((lw, lh), Image.LANCZOS)
lx, ly = int(xs2.min()) + 4, (int(ys2.min()) + int(ys2.max()))//2 - lh//2
alpha = np.zeros((H, W), np.float32); alpha[ly:ly+lh, lx:lx+lw] = np.array(logo)[:, :, 3] / 255.0
assert (lx, ly, lw, lh) == (100, 1193, 291, 54), (lx, ly, lw, lh)

# The drawn logo itself = mask pixels below the bead line (its gold square starts at y~1210). The beads that the
# old colour test caught as "gold" sit at y 1166-1190 and are NOT logo.
drawn = raw.copy(); drawn[:1200] = False
drawn_guard = cv2.dilate(drawn.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0     # 4 px safety ring
BX0, BX1, BY0, BY1 = 120, 185, 1150, 1196                                            # inclusive box
box = np.zeros((H, W), bool); box[BY0:BY1+1, BX0:BX1+1] = True
assert not (box & drawn_guard).any(), 'drawn logo inside the restore box'
a = alpha[..., None]
target = np.where(a > 0, v2 + (1 - a) * (orig - clean), orig)       # alpha 0: ORIG; soft logo edge: re-composite
restore = box & (alpha < 1.0)                                        # fully opaque logo pixels keep v2
out[restore] = target[restore]
report['fix1'] = {'box': [BX0, BY0, BX1, BY1], 'restored_px': int(restore.sum()),
                  'soft_logo_edge_px': int((restore & (alpha > 0)).sum()),
                  'drawn_logo_min_y': int(np.nonzero(drawn)[0].min())}

# ----------------------------------------------------------------------------------------------------------------
# Fix 2 (V21): crimson box behind "sistem." -> flat #B31217
# ----------------------------------------------------------------------------------------------------------------
T = np.array([0xB3, 0x12, 0x17], np.float32)                       # 179,18,23
RX0, RX1, RY0, RY1 = 284, 583, 435, 517                             # box rect (coverage > 0.5), inclusive
IX0, IX1, IY0, IY1 = RX0+3, RX1-3, RY0+3, RY1-3                      # interior (no outer soft edge)
EX0, EX1, EY0, EY1 = RX0-4, RX1+4, RY0-4, RY1+4                      # outer band limit
blk = v2[RY0:RY1+1, RX0:RX1+1]
pure = (blk[..., 0] > 130) & (blk[..., 1] < 30) & (blk[..., 2] < 40)
C = np.median(blk[pure], 0)                                          # old box colour (~160,9,17)
letters = (blk[..., 0] > 225) & (blk[..., 1] > 225)
Wl = np.median(blk[letters], 0)                                      # letter ivory (~254,250,249)
ring = np.zeros((H, W), bool); ring[EY0-6:EY1+7, EX0-6:EX1+7] = True; ring[EY0:EY1+1, EX0:EX1+1] = False
Bg = np.median(v2[ring], 0)                                          # dark background around the box
# interior: two-colour model box/letter, letter coverage from G (box G~9, letter G~250)
reg = v2[IY0:IY1+1, IX0:IX1+1]
t = np.clip((reg[..., 1] - C[1]) / (Wl[1] - C[1]), 0, 1)
t = np.clip((t - 0.05) / 0.95, 0, 1)                                 # JPEG noise in the flat box -> exactly flat
model = (1 - t)[..., None] * T + t[..., None] * Wl
lam = np.clip((t - 0.85) / (0.98 - 0.85), 0, 1); lam = lam*lam*(3 - 2*lam)   # letter cores: keep v2 pixels
new_int = lam[..., None] * reg + (1 - lam[..., None]) * model
# outer soft edge band: three-colour unmixing (box C, letter/cedilla Wl, background Bg), shift only the box share
band = v2[EY0:EY1+1, EX0:EX1+1].copy()
M = np.stack([C - Bg, Wl - Bg], 1)                                   # 3x2
coef, *_ = np.linalg.lstsq(M, (band - Bg).reshape(-1, 3).T, rcond=None)
f = np.clip(coef[0], 0, 1); tt = np.clip(coef[1], 0, 1); f = np.minimum(f, 1 - tt)
band_new = band + f.reshape(band.shape[:2])[..., None] * (T - C)
out[EY0:EY1+1, EX0:EX1+1] = band_new
out[IY0:IY1+1, IX0:IX1+1] = new_int
report['fix2'] = {'rect': [RX0, RY0, RX1, RY1], 'interior': [IX0, IY0, IX1, IY1], 'band': [EX0, EY0, EX1, EY1],
                  'old_box': C.round(1).tolist(), 'letter': Wl.round(1).tolist(), 'bg': Bg.round(1).tolist()}

# ----------------------------------------------------------------------------------------------------------------
# Fix 3 (V11): pseudo-word day headers + footer mark on the agenda pages -> plain paper
# ----------------------------------------------------------------------------------------------------------------
# Each mark is a polygon drawn between the ruled lines (which stay outside it) and above the red squares.
# Polygons were placed from per-pixel darkness maps (paper median minus luminance) of every mark.
# mode 'fill' : replace by a local paper-tone fit (quadratic in x,y from clean paper around it) + matched grain.
# mode 'clamp': a letter blob sitting ON a ruled line; only lighten it to the line's own darkness (dmax), so the
#               line stays continuous.  ylim limits where paper samples are taken (keeps the page-edge highlight out).
def para(x0, x1, top0, bot0, s_top, s_bot=None):
    s_bot = s_top if s_bot is None else s_bot
    return [(x0, top0), (x1, top0 + s_top*(x1-x0)), (x1, bot0 + s_bot*(x1-x0)), (x0, bot0)]

def rect(x0, y0, x1, y1):
    return [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]

MARKS = {
    # left page
    'LT1 top heading':        dict(poly=para(199.0, 228.5, 815.2, 821.3, 0.0), ylim=(813, 831)),
    'LT2 top heading':        dict(poly=para(252.5, 293.5, 816.3, 823.2, 0.0), ylim=(813, 831)),
    'LC square-1 header':     dict(poly=para(151.5, 183.0, 841.5, 845.7, 0.08)),
    'LD square-2 header':     dict(poly=para(63.3, 93.0, 873.45, 878.0, 0.08)),
    'LE square-3 header':     dict(poly=para(235.5, 267.0, 872.08, 876.68, 0.165)),
    'LF lower block header':  dict(poly=para(91.5, 117.5, 923.38, 926.88, 0.05)),
    # right page
    'RT top heading':         dict(poly=[(446.5, 834.4), (500.5, 835.4), (500.5, 840.5), (480.0, 840.2), (456.0, 837.5), (446.5, 837.5)]),
    'RG square-1 header':     dict(poly=para(459.5, 484.5, 843.2, 846.6, 0.15)),
    'RH square-2 header':     dict(poly=para(387.5, 416.0, 884.5, 889.1, 0.2)),
    'RH glyph on line':       dict(poly=rect(387.5, 882.5, 391.5, 883.5), mode='clamp', dmax=10),
    'RI square-3 header':     dict(poly=para(580.5, 605.5, 872.2, 876.6, 0.2)),
    'RS right heading':       dict(poly=para(674.5, 708.5, 874.24, 877.54, 0.12)),
    'RJ square-4 header':     dict(poly=para(315.5, 347.0, 930.12, 936.12, 0.19)),
    'RK square-5 header':     dict(poly=para(516.5, 545.5, 915.35, 921.65, 0.233)),
    'RL square-6 header':     dict(poly=para(452.5, 482.5, 966.93, 975.23, 0.257)),
    'RF footer dot':          dict(poly=rect(480.5, 1061.5, 485.5, 1065.6)),
    'RF footer text':         dict(poly=para(493.5, 526.5, 1062.79, 1068.79, 0.235)),
    'RF glyph on line':       dict(poly=rect(503.5, 1062.5, 511.5, 1064.5), mode='clamp', dmax=18),
}

def coverage(poly, ss=8):
    m = np.zeros((H*1, W*1), np.float32)
    xs_ = [p[0] for p in poly]; ys_ = [p[1] for p in poly]
    x0, x1 = int(np.floor(min(xs_)))-1, int(np.ceil(max(xs_)))+2
    y0, y1 = int(np.floor(min(ys_)))-1, int(np.ceil(max(ys_)))+2
    hi = np.zeros(((y1-y0)*ss, (x1-x0)*ss), np.uint8)
    pts = np.array([[(x - x0 + 0.5)*ss - 0.5, (y - y0 + 0.5)*ss - 0.5] for x, y in poly])   # pixel centres at ints
    cv2.fillPoly(hi, [np.round(pts*16).astype(np.int32)], 1, lineType=cv2.LINE_8, shift=4)
    m[y0:y1, x0:x1] = hi.reshape(y1-y0, ss, x1-x0, ss).mean((1, 3))
    return m, (x0, y0, x1, y1)

Lv2 = cv2.cvtColor(v2.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
Dk = cv2.medianBlur(Lv2.astype(np.uint8), 13).astype(np.float32) - Lv2           # darkness vs local paper
rr, gg, bb = v2[..., 0], v2[..., 1], v2[..., 2]
redsq = cv2.dilate(((rr > 70) & (rr > 1.7*gg) & (rr > 1.7*bb)).astype(np.uint8), np.ones((5, 5), np.uint8)) > 0
paperRGB = np.stack([cv2.medianBlur(v2[..., c].astype(np.uint8), 13) for c in range(3)], -1).astype(np.float32)
rng = np.random.default_rng(43)
GRAIN = 0.85                                                            # grain ~ paper's own high-pass energy
HPV = v2 - np.stack([cv2.GaussianBlur(v2[..., c], (0, 0), 1.5) for c in range(3)], -1)
fix3 = {}
for name, mk in MARKS.items():
    poly = mk['poly']
    cov, (x0, y0, x1, y1) = coverage(poly)
    w = cv2.GaussianBlur(cov, (0, 0), 0.35)
    w = np.where(cov > 0.999, 1.0, w)                                   # full inside, soft only at the rim
    bbox = [round(min(p[0] for p in poly), 1), round(min(p[1] for p in poly), 1),
            round(max(p[0] for p in poly), 1), round(max(p[1] for p in poly), 1)]
    if mk.get('mode') == 'clamp':
        k = np.clip((Dk - mk['dmax']) / np.maximum(Dk, 1e-3), 0, 1) * w
        sl = (slice(y0, y1), slice(x0, x1))
        out[sl] = out[sl] + k[sl][..., None] * (paperRGB[sl] - out[sl])
        fix3[name] = {'bbox': bbox, 'mode': 'clamp', 'dmax': mk['dmax'],
                      'max_dark_before': round(float((Dk[sl] * (cov[sl] > 0)).max()), 1)}
        continue
    nx0, nx1, ny0, ny1 = x0-10, x1+10, y0-6, y1+6
    if 'ylim' in mk:
        ny0, ny1 = max(ny0, mk['ylim'][0]), min(ny1, mk['ylim'][1])
    yy, xx = np.mgrid[ny0:ny1, nx0:nx1]
    inside = cv2.dilate((cov[ny0:ny1, nx0:nx1] > 0).astype(np.uint8), np.ones((3, 3), np.uint8)) > 0
    samp = (~inside) & (np.abs(Dk[ny0:ny1, nx0:nx1]) < 5) & (~redsq[ny0:ny1, nx0:nx1])
    X = np.stack([np.ones_like(xx), xx-x0, yy-y0, (xx-x0)**2, (xx-x0)*(yy-y0), (yy-y0)**2], -1).astype(np.float64)
    dist = cv2.distanceTransform((cov[ny0:ny1, nx0:nx1] <= 0).astype(np.uint8), cv2.DIST_L2, 3)
    sw = np.sqrt(np.exp(-0.5*(dist/4.0)**2))[samp][:, None]               # samples close to the mark count most
    A = X[samp]; Y = v2[ny0:ny1, nx0:nx1][samp].astype(np.float64); dd = dist[samp]
    for _ in range(2):                                                  # robust: drop >2.5 sigma, refit
        coefs, *_ = np.linalg.lstsq(A*sw, Y*sw, rcond=None)
        res = Y - A @ coefs
        keep = (np.abs(res) < 2.5*res.std(0) + 1e-6).all(1)
        A, Y, sw, dd = A[keep], Y[keep], sw[keep], dd[keep]
    coefs, *_ = np.linalg.lstsq(A*sw, Y*sw, rcond=None)
    res = Y - A @ coefs
    cov3 = np.cov(res.T) + np.eye(3)*1e-3
    rim = dd <= 3.5                                                     # match the tone right at the rim
    delta = res[rim].mean(0) if rim.sum() > 10 else np.zeros(3)
    paper = (X @ coefs + delta).astype(np.float32)
    # grain: one fibre-like noise field (paper grain is mostly luminance), scaled per channel so that its
    # high-frequency energy equals that of the clean paper around the mark
    hp_paper = HPV[ny0:ny1, nx0:nx1][samp].std(0)
    n1 = cv2.GaussianBlur(rng.standard_normal(paper.shape[:2]).astype(np.float32), (0, 0), sigmaX=1.0, sigmaY=0.6)
    hp_n = (n1 - cv2.GaussianBlur(n1, (0, 0), 1.5)).std()
    n = n1[..., None] * (GRAIN * hp_paper / hp_n).astype(np.float32)
    fill = paper + n
    ww = w[ny0:ny1, nx0:nx1][..., None]
    out[ny0:ny1, nx0:nx1] = out[ny0:ny1, nx0:nx1] * (1 - ww) + fill * ww
    fix3[name] = {'bbox': bbox, 'mode': 'fill', 'px': round(float(cov.sum()), 1), 'paper_samples': int(len(Y)),
                  'rim_offset': delta.round(2).tolist(), 'fit_resid_std': np.sqrt(np.diag(cov3)).round(2).tolist(),
                  'grain_hp_std': hp_paper.astype(float).round(2).tolist()}
report['fix3'] = fix3

# ----------------------------------------------------------------------------------------------------------------
res = np.clip(np.round(out), 0, 255).astype(np.uint8)
Image.fromarray(res).save(OUT, quality=93)
np.save(OUT.rsplit('.', 1)[0] + '_prejpeg.npy', res)
print(json.dumps(report, indent=1))
