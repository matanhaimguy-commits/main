#!/usr/bin/env python3
"""IMG-W42-7 (2026-w42-7-image) v3 = v2 + local code-only edits (VISUAL-QA 5.5 paint-out / local edit).

No generation. PIL + numpy + OpenCV + scipy only. Runs in the Higgsfield sandbox:
    python3 v3_edit.py            # writes /home/user/drafts/fixed/ebd54bc2_v3.jpg (1080x1350, q93)

Inputs
  ORIG  model output (has the model-drawn logo bottom-left)
  V2    ORIG with the drawn logo inpainted (Telea) and the real logo pasted (fixlogo2.py)
  LOGO  the real logo that v2 pasted
The v2 mask, inpaint and logo placement are recomputed here exactly as fixlogo2.py did, so the real
logo's alpha is known per pixel. Pixels where that alpha is 255 are never changed.

Fixes
  1  V23  desk edge highlight + strip under the wordmark: restore ORIG pixels inside the v2 mask
          wherever ORIG is not drawn logo and the real logo is transparent; fill the drawn-letter
          pixels by Poisson blending with the desk copied one step further along the desk edge
          (the highlight and the grain continue along the edge).
  2  V24  wall sign: red cross -> muted dark teal-grey (#3E5A5C hue at the sign's dim light),
          paper/ink unmixed per pixel so the soft edges and the ink shading are kept.
  3  V11  phone status-bar clock and input-field placeholder -> plain screen colour (harmonic fill
          + matched fine noise); ledger cover embossed fake lettering -> plain cover texture
          (Poisson clone of plain cover leather from the same cover).
"""
import numpy as np
import cv2
from PIL import Image
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

ORIG = '/home/user/drafts/ebd54bc2-4295-4a39-8392-b776d3c06d08.jpg'
V2 = '/home/user/drafts/fixed/ebd54bc2.jpg'
LOGO = '/home/user/brand/straightscale-logo-light.png'
OUT = '/home/user/drafts/fixed/ebd54bc2_v3.jpg'
DBG = '/home/user/v3w'          # debug masks go here (not part of the deliverable)

rng = np.random.default_rng(42)


def lum(a):
    return 0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2]


def poisson(base, omega, guides=None, kmap=None):
    """Solve lap(f) = lap(guide) inside omega with f = base on the outside border (per channel).
    guides: list of HxWx3 arrays (None -> harmonic fill, guide = 0). kmap: per-pixel guide index,
    so the guidance gradient of pixel p always comes from p's own guide (no fake steps at seams)."""
    H, W = omega.shape
    py, px = np.nonzero(omega)
    n = len(py)
    idx = -np.ones((H, W), np.int64)
    idx[py, px] = np.arange(n)
    if guides is None:
        G = np.zeros((1, H, W, 3))
        km = np.zeros(n, np.int64)
    else:
        G = np.stack(guides)
        km = np.zeros(n, np.int64) if kmap is None else kmap[py, px]
    rows, cols, vals = [np.arange(n)], [np.arange(n)], [np.full(n, 4.0)]
    b = np.zeros((n, 3))
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        qy, qx = py + dy, px + dx
        inq = omega[qy, qx]
        rows.append(np.arange(n)[inq]); cols.append(idx[qy[inq], qx[inq]]); vals.append(-np.ones(inq.sum()))
        b[~inq] += base[qy[~inq], qx[~inq]]
        b += G[km, py, px] - G[km, qy, qx]
    A = coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n)).tocsc()
    out = base.copy()
    for c in range(3):
        out[py, px, c] = spsolve(A, b[:, c])
    return out


def shifted(img, dx, dy):
    """g[y, x] = img[y + dy, x + dx] (edge-clamped)."""
    H, W = img.shape[:2]
    ys = np.clip(np.arange(H) + dy, 0, H - 1)
    xs = np.clip(np.arange(W) + dx, 0, W - 1)
    return img[ys][:, xs]


def poly_mask(shape, pts):
    m = np.zeros(shape, np.uint8)
    cv2.fillPoly(m, [np.array(pts, np.int32)], 1)
    return m.astype(bool)


o8 = np.array(Image.open(ORIG).convert('RGB'))
v2 = np.array(Image.open(V2).convert('RGB')).astype(np.float64)
o = o8.astype(np.float64)
H, W = o.shape[:2]
assert (W, H) == (1080, 1350) and v2.shape == o.shape
yy, xx = np.mgrid[0:H, 0:W]

# ---------------------------------------------------------------- v2 reconstruction (fixlogo2.py)
bgr = cv2.cvtColor(o8, cv2.COLOR_RGB2BGR)
r, g, b = [o8[:, :, i].astype(int) for i in range(3)]
zone = np.zeros((H, W), bool); zone[int(H * .875):int(H * .99), int(W * .02):int(W * .50)] = True
white = zone & (r > 200) & (g > 200) & (b > 190) & ((np.maximum(np.maximum(r, g), b) - np.minimum(np.minimum(r, g), b)) < 40)
ys_, xs_ = np.nonzero(white); tx0, tx1, ty0, ty1 = xs_.min(), xs_.max(), ys_.min(), ys_.max()
near = np.zeros((H, W), bool)
near[max(0, ty0 - int(H * .04)):min(H, ty1 + int(H * .02)), max(0, tx0 - int(W * .12)):min(W, tx1 + 8)] = True
red = near & (r > 120) & (r > 2 * g) & (r > 2 * b)
gold = near & (r > 160) & (g > 90) & (g < 210) & (b < 100) & (r > b + 80)
v2mask = cv2.dilate(((white | red | gold) & near).astype(np.uint8) * 255, np.ones((7, 7), np.uint8), iterations=2) > 0
clean = cv2.cvtColor(cv2.inpaint(bgr, v2mask.astype(np.uint8) * 255, 9, cv2.INPAINT_TELEA), cv2.COLOR_BGR2RGB).astype(np.float64)
logo = Image.open(LOGO).convert('RGBA'); logo = logo.crop(logo.getbbox())
lw = int(W * .27); lh = int(logo.height * lw / logo.width)
logo = np.array(logo.resize((lw, lh), Image.LANCZOS)).astype(np.float64)
my, mx = np.nonzero(v2mask)
lx0 = int(mx.min()) + 4; ly0 = (int(my.min()) + int(my.max())) // 2 - lh // 2
alpha = np.zeros((H, W)); alpha[ly0:ly0 + lh, lx0:lx0 + lw] = logo[:, :, 3] / 255.0
print('v2 mask box', (int(mx.min()), int(my.min()), int(mx.max()), int(my.max())), 'logo at', (lx0, ly0, lw, lh))

out = v2.copy()

# ---------------------------------------------------------------- FIX 1 (V23) desk edge + strip
# drawn logo in ORIG: the drawn white letters (wordmark + the S in the drawn square) with their
# anti-alias/JPEG ring (<= 5 px), and the drawn red square + gold square (left of x 175).
dist = cv2.distanceTransform((~white).astype(np.uint8), cv2.DIST_L2, 5)
drawn = (dist <= 5.0) & near
redgold = (red | gold) & near & (xx < 175) & (yy >= 1225)
drawn |= cv2.dilate(redgold.astype(np.uint8), np.ones((11, 11), np.uint8)) > 0
Z1a = (xx >= 235) & (xx < 330) & (yy >= 1185) & (yy < 1248)          # highlight stub + smear
Z1b = (xx >= 170) & (xx < 396) & (yy >= 1240) & (yy < 1300)          # wordmark band + strip below
Z1 = Z1a | Z1b
bg3 = clean.copy()
restore = Z1 & v2mask & ~drawn
bg3[restore] = o[restore]
STEP = (28, 25)                     # one step along the desk front edge (measured ridge slope dx/dy ~1.1)
fillA = Z1b & drawn & (yy >= 1266)  # strip under the wordmark: donor one step down the edge (ORIG desk)
fillB = Z1b & drawn & (yy < 1266)   # behind / between the pasted glyphs
# pass 1: joint solve, strip from ORIG one step down the edge, glyph band from ORIG two steps down
bg3 = poisson(bg3, fillA | fillB, [shifted(o, *STEP), shifted(o, 2 * STEP[0], 2 * STEP[1])], fillB.astype(np.int64))
# pass 2: glyph band again, now from the filled strip one step down (keeps the highlight on the edge line)
bg3 = poisson(bg3, fillB, [shifted(bg3, *STEP)])
changed1 = Z1 & (restore | fillA | fillB)
a3 = alpha[..., None]
upd = changed1 & (alpha < 1.0)
out[upd] = (v2 + (1.0 - a3) * (bg3 - clean))[upd]          # real logo kept exactly; only what shows through changes
print('fix1 restored px', int(restore.sum()), 'filled px', int((fillA | fillB).sum()), 'updated px', int(upd.sum()))
np.save(f'{DBG}/fix1_restore.npy', restore); np.save(f'{DBG}/fix1_fill.npy', fillA | fillB)

# ---------------------------------------------------------------- FIX 2 (V24) wall sign cross
SB = (8, 330, 92, 430)                                     # x0, y0, x1, y1 inside the frame
x0, y0, x1, y1 = SB
C = out[y0:y1, x0:x1].copy()
gr = C[..., 1] / np.maximum(C[..., 0], 1.0)                # red ink has G/R ~0.25, the lit sign paper ~0.6
w0 = np.clip((0.56 - gr) / (0.56 - 0.27), 0, 1) * (C[..., 0] > 55)
ncc, lab, stats, _ = cv2.connectedComponentsWithStats((w0 > 0.5).astype(np.uint8))
k = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))     # the cross = largest red component
crossreg = cv2.dilate((lab == k).astype(np.uint8), np.ones((11, 11), np.uint8)) > 0
holes = cv2.dilate(((w0 > 0.05) & crossreg).astype(np.uint8), np.ones((7, 7), np.uint8)) * 255
P = cv2.inpaint(np.clip(C, 0, 255).astype(np.uint8), holes, 9, cv2.INPAINT_TELEA).astype(np.float64)
P = np.where(holes[..., None] > 0, cv2.GaussianBlur(P, (0, 0), 2.0), C)   # sign paper under the cross
Iref = C[(w0 > 0.9) & crossreg].mean(0)                   # red ink colour
dv = P - Iref[None, None]
w = np.clip(((P - C) * dv).sum(2) / np.maximum((dv * dv).sum(2), 1.0), 0, 1) * crossreg   # linear unmix paper/ink
T0 = np.array([0x3E, 0x5A, 0x5C], np.float64)           # #3E5A5C muted dark teal-grey (hue 183 deg)
LIGHT, GREY = 0.7, 0.2                                     # as lit by the same dim warm light as the sign paper
T = T0 * LIGHT; T = T * (1 - GREY) + lum(T) * GREY         # (checked 0.8 / 0.65 / 0.55 in context: 0.8 read cyan)
ink_l = (lum(C) - (1 - w) * lum(P)) / np.maximum(w * lum(Iref[None, None]), 1e-3)
s = np.clip(ink_l, 0.6, 1.5)                               # the ink's own shading, kept
sm = np.clip((w - 0.3) / 0.3, 0, 1)
s = 1 + (s - 1) * sm
res = C - (P * (1 - w)[..., None] + Iref * (w * s)[..., None])   # what the paper/ink model does not explain
res_chroma = res - lum(res)[..., None]                     # keep its luminance (grain), drop its red cast
newC = C + (w * s)[..., None] * (T - Iref) - w[..., None] * res_chroma   # swap ink colour, paper share untouched
out[y0:y1, x0:x1] = newC
print('fix2 Iref', Iref.round(1), 'cross px(w>.5)', int((w > .5).sum()), 'new core mean', newC[w > 0.9].mean(0).round(1))

# ---------------------------------------------------------------- FIX 3 (V11) phone + ledger
Lv = lum(out)
# 3a status-bar clock "0101" -> plain screen
ck = (xx >= 240) & (xx < 271) & (yy >= 846) & (yy < 858)
ckm = ck & (Lv > 22)
ckm = (cv2.dilate(ckm.astype(np.uint8), np.ones((5, 5), np.uint8)) > 0) | ((xx >= 241) & (xx < 273) & (yy >= 847) & (yy < 857))
# 3b input placeholder "Mesisetan" -> plain pill
pb = (xx >= 500) & (xx < 606) & (yy >= 1038) & (yy < 1084)
pill = (pb & (Lv > 24)).astype(np.uint8)
pill = cv2.morphologyEx(pill, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
pill_in = cv2.erode(pill, np.ones((5, 5), np.uint8)) > 0
txt = pill_in & (Lv > 44)
txt &= (xx >= 512) & (xx < 595)                             # placeholder only (not the pill edge / send area)
txm = (cv2.dilate(txt.astype(np.uint8), np.ones((5, 5), np.uint8)) > 0) & pill_in
for m, nm in ((ckm, 'clock'), (txm, 'input')):
    ys2, xs2 = np.nonzero(m)
    bx = (xs2.min() - 6, ys2.min() - 6, xs2.max() + 7, ys2.max() + 7)
    ring = (cv2.dilate(m.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0) & ~m
    if nm == 'input':
        ring &= pill_in
    hp = out - cv2.GaussianBlur(out, (0, 0), 1.5)
    sig = float(np.median(np.abs(hp[ring])) * 1.4826)
    f = poisson(out, m)
    noise = cv2.GaussianBlur(rng.standard_normal((H, W)), (0, 0), 0.6)
    noise *= 0.7 * sig / max(noise[m].std(), 1e-6)       # JPEG adds the rest
    f[m] += noise[m][:, None]
    out[m] = f[m]
    print(f'fix3 {nm} px', int(m.sum()), 'box', tuple(int(t) for t in bx), 'noise sigma', round(sig, 2))
np.save(f'{DBG}/fix3_clock.npy', ckm); np.save(f'{DBG}/fix3_input.npy', txm)
# 3c ledger cover lettering -> plain cover (Poisson clone of plain cover leather, two donor offsets)
LET = poly_mask((H, W), [(986, 762), (1030, 754), (1078, 750), (1078, 771), (1050, 775), (1020, 776), (1000, 773), (986, 770)])
pen_top = 772 + 0.38 * (xx - 980)
assert not (LET & (yy > pen_top - 3)).any(), 'ledger mask touches the pen'
kmap = (xx >= 1031).astype(np.int64)
cov = poisson(out, LET, [shifted(out, -140, 20), shifted(out, -165, 22)], kmap)
out[LET] = cov[LET]
np.save(f'{DBG}/fix3_ledger.npy', LET)
print('fix3 ledger px', int(LET.sum()))

# ---------------------------------------------------------------- save
assert (np.abs(out - v2)[alpha >= 1.0] == 0).all(), 'opaque real-logo pixels changed'
res = Image.fromarray(np.clip(np.round(out), 0, 255).astype(np.uint8))
assert res.size == (1080, 1350)
res.save(OUT, quality=93)
print('saved', OUT, 'changed px', int((np.abs(out - v2).max(2) > 0).sum()))
