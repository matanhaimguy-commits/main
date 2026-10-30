#!/usr/bin/env python3
"""IMG-W42-7 (2026-w42-7-image) v4 = v3 + two local code-only edits. Nothing is generated.

Runs in the Higgsfield sandbox (PIL, numpy, OpenCV, scipy only):
    python3 v4_edit.py        # reads ebd54bc2_v3.jpg, writes ebd54bc2_v4.jpg (1080x1350, q93, 4:4:4)

Boxes are x0,y0 to x1,y1, inclusive.

Fix 1  Wall sign on the left wall (frame, recoloured blue-cross emblem, faint marks), box
       x 0-100, y 303-465: painted out completely with a Poisson fill.
       Guide = the wall itself, continued per column between the wall band above the frame
       (y 290-301) and the wall band below it (y 466-476), so the faint vertical panel tones and
       the downward light gradient carry straight through. Dirichlet boundary = the real wall
       pixels just outside the box (row 302, row 466, column 101). The image edge (x = -1) and
       the headline bar are free (Neumann) boundaries, so no red can bleed into the wall.
       Fine grain matched to the wall's own grain is added. Where the box meets the highlight
       bar's bottom-left corner (x 89-100, y 303-327) the bar's soft edge is re-composited over
       the new wall with the bar's own measured edge profiles (left edge x profile times bottom
       edge y profile), in the new bar colour.
Fix 2  Headline highlight bar, box x 86-597, y 233-330: red-hue mask. Per pixel box weight
       a = (R-G) / (R-G of the old box), gated to red hues (hue within ~14-26 deg of the box hue
       356 deg), to a >= 0.15 and away from near-white letter pixels. Box pixels at least ~3 px
       from any letter or from the bar's outer edge become flat #B31217; the pixels in that
       ~3 px band (letter anti-aliasing, the dark ringing beside the letters, the bar's outer
       soft edge) are shifted by a x (new - old), so letters and their edges keep their own
       colour and no old-crimson fringe is left. Letter pixels are not touched (asserted).
"""
import hashlib
import numpy as np
import cv2
from PIL import Image
from scipy.ndimage import gaussian_filter1d
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import splu

SRC = '/home/user/drafts/fixed/ebd54bc2_v3.jpg'
OUT = '/home/user/drafts/fixed/ebd54bc2_v4.jpg'
DBG = '/home/user/v4work'                 # pre-JPEG array for QA (not part of the deliverable)

NEW = np.array([0xB3, 0x12, 0x17], np.float64)   # #B31217 = (179, 18, 23)

# Fix 1 geometry (inclusive)
SX0, SX1, SY0, SY1 = 0, 100, 303, 465
TOP_BAND = (290, 301)          # wall rows just above the frame (x 0-88)
BOT_BAND = (466, 476)          # wall rows just below the frame (x 0-101)
# Fix 2 geometry (inclusive)
BX0, BY0, BX1, BY1 = 86, 233, 597, 330

rng = np.random.default_rng(404)


def smoothstep(x, e0, e1):
    t = np.clip((x - e0) / (e1 - e0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)


src = np.asarray(Image.open(SRC).convert('RGB')).astype(np.float64)
H, W, _ = src.shape
assert (W, H) == (1080, 1350)
out = src.copy()
yy, xx = np.mgrid[0:H, 0:W]

# =====================================================================================
# Fix 2: highlight bar -> flat #B31217 (red-hue mask, letters untouched)
# =====================================================================================
reg = src[BY0:BY1 + 1, BX0:BX1 + 1]
R, G, B = reg[..., 0], reg[..., 1], reg[..., 2]
core = (R > 130) & (G < 40) & (B < 50)
OLD = reg[core].mean(0)                                   # measured old box colour
alpha = np.clip((R - G) / (OLD[0] - OLD[1]), 0.0, 1.0)    # box weight from red chroma
hsv = cv2.cvtColor((reg / 255.0).astype(np.float32), cv2.COLOR_RGB2HSV)
hue = hsv[..., 0].astype(np.float64)                      # degrees 0..360
box_hue = float(cv2.cvtColor((OLD[None, None] / 255.0).astype(np.float32), cv2.COLOR_RGB2HSV)[0, 0, 0])
dh = np.abs(hue - box_hue)
dh = np.minimum(dh, 360.0 - dh)
hue_gate = 1.0 - smoothstep(dh, 14.0, 26.0)               # red hues only (wall brown is ~27 deg off)
letter_guard = 1.0 - smoothstep(np.minimum(G, B), 190.0, 215.0)   # near-white letter pixels: 0
w_shift = alpha * smoothstep(alpha, 0.15, 0.30) * hue_gate * letter_guard
# flat where the pixel is box and at least ~3 px from any letter or the bar's outer edge
box_mask = ((alpha >= 0.5) & (hue_gate > 0.5)).astype(np.uint8)
dist = cv2.distanceTransform(box_mask, cv2.DIST_L2, 3)
w_flat = smoothstep(dist.astype(np.float64), 1.5, 3.5)
shifted = reg + w_shift[..., None] * (NEW - OLD)
new_reg = w_flat[..., None] * NEW + (1.0 - w_flat[..., None]) * shifted
out[BY0:BY1 + 1, BX0:BX1 + 1] = new_reg
print('fix2 old box mean', OLD.round(2), 'hue', round(box_hue, 1), 'core px', int(core.sum()),
      'flat px', int((w_flat >= 0.999).sum()), 'shifted px', int(((w_shift > 0) & (w_flat < 0.999)).sum()))

# =====================================================================================
# Fix 1: wall sign -> wall (Poisson fill guided by the wall continued per column)
# =====================================================================================
# unknowns: the box minus the pure bar pixels it touches at the top-right
U = np.zeros((H, W), bool)
U[SY0:SY1 + 1, SX0:SX1 + 1] = True
U[SY0:320, 96:SX1 + 1] = False                        # pure bar (x 96-100, y 303-319) stays bar
# bar + its soft edges: never used as a boundary value (Neumann there)
BARZ = (xx >= 89) & (xx <= BX1) & (yy >= BY0) & (yy <= 325)

# guide: per-column wall above and below, linearly continued through the box
T = src[TOP_BAND[0]:TOP_BAND[1] + 1, 0:SX1 + 2].mean(0)
T[89:] = T[84:89].mean(0)                             # x >= 89 is bar in the top band: carry the wall on
Bb = src[BOT_BAND[0]:BOT_BAND[1] + 1, 0:SX1 + 2].mean(0)
T = gaussian_filter1d(T, 1.0, axis=0, mode='nearest')
Bb = gaussian_filter1d(Bb, 1.0, axis=0, mode='nearest')
yt = (TOP_BAND[0] + TOP_BAND[1]) / 2.0
yb = (BOT_BAND[0] + BOT_BAND[1]) / 2.0
gy = np.arange(H, dtype=np.float64)[:, None, None]
t = (gy - yt) / (yb - yt)
guide = np.zeros((H, SX1 + 2, 3))
guide[:] = T[None] + (Bb - T)[None] * t                # defined for x 0..101 only

ys, xs = np.nonzero(U)
idx = -np.ones((H, W), np.int64)
idx[ys, xs] = np.arange(len(ys))
rows, cols, vals = [], [], []
b = np.zeros((len(ys), 3))
diag = np.zeros(len(ys))
for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    ny, nx = ys + dy, xs + dx
    inb = (ny >= 0) & (ny < H) & (nx >= 0) & (nx < W)
    k = np.nonzero(inb)[0]
    ny_, nx_ = ny[k], nx[k]
    inU = U[ny_, nx_]
    isD = (~inU) & (~BARZ[ny_, nx_])                  # real wall pixel around the box
    use = inU | isD
    kk = k[use]
    diag[kk] += 1
    b[kk] += guide[ys[kk], xs[kk]] - guide[ny_[use], np.minimum(nx_[use], SX1 + 1)]
    ku = k[inU]
    rows += list(ku)
    cols += list(idx[ny_[inU], nx_[inU]])
    vals += [-1.0] * len(ku)
    kd = k[isD]
    b[kd] += src[ny_[isD], nx_[isD]]
rows += list(range(len(ys)))
cols += list(range(len(ys)))
vals += list(diag)
A = coo_matrix((vals, (rows, cols)), shape=(len(ys), len(ys))).tocsc()
fill = splu(A).solve(b)
print('fix1 unknown px', len(ys), 'dirichlet-free px', int((diag < 4).sum()))

# fine grain matched to the wall's own grain (high-pass at sigma 1, per channel)
def hp(a):
    return a - cv2.GaussianBlur(a, (0, 0), 1.0)
wall = np.concatenate([hp(src[262:302, 0:88]).reshape(-1, 3), hp(src[468:500, 0:100]).reshape(-1, 3)])
target = wall.std(0)
nz = rng.normal(0, 1, (H, W, 1)) * 0.85 + rng.normal(0, 1, (H, W, 3)) * 0.5   # luma-led, a little chroma
nz = cv2.GaussianBlur(nz.astype(np.float32), (0, 0), 0.6).astype(np.float64)
nz_patch = nz[SY0:SY1 + 1, SX0:SX1 + 1]
nz *= (target / hp(nz_patch).reshape(-1, 3).std(0))[None, None]
fill += nz[ys, xs]
print('fix1 grain target std', target.round(2))

# bar soft-edge re-composite where the box meets the bar's bottom-left corner
# left-edge profile: measured on the recoloured bar (fix 2 output) in the rows just above, so the
# re-composited edge continues the edge above it without a jog
rr = np.arange(280, 302)
Rrow = out[rr, :, 0]
Rw = Rrow[:, 82:87].mean(1, keepdims=True)
ax = np.zeros(W)
ax[86:102] = np.clip(((Rrow[:, 86:102] - Rw) / (NEW[0] - Rw)).mean(0), 0, 1)
ax[97:] = 1.0
ax[:89] = 0.0                                         # left of the bar's soft edge: wall only
colsel = [x for x in range(110, 590)
          if (src[300:319, x, 0] > 135).all() and (src[300:319, x, 1] < 40).all()
          and (src[326:332, x, 1] < 60).all() and (src[326:332, x, 0] < 90).all()]
Rc = src[:, colsel, 0]
Rbar = Rc[308:317].mean(0)
Rbel = Rc[328:332].mean(0)
ay = np.ones(H)
ay[314:332] = np.clip(np.median((Rc[314:332] - Rbel) / (Rbar - Rbel), axis=1), 0, 1)
ay[328:] = 0.0
print('fix1 bar edge ax[86..97]', ax[86:98].round(2), 'ay[318..328]', ay[318:329].round(2), 'cols', len(colsel))
a = ax[xs] * ay[ys]
a[(xs < 86) | (ys > 331)] = 0.0
fill = a[:, None] * NEW + (1.0 - a[:, None]) * fill
out[ys, xs] = fill

# =====================================================================================
# checks and save
# =====================================================================================
out8 = np.clip(np.round(out), 0, 255).astype(np.uint8)
src8 = src.astype(np.uint8)
edited = np.zeros((H, W), bool)
edited[SY0:SY1 + 1, SX0:SX1 + 1] = True
edited[BY0:BY1 + 1, BX0:BX1 + 1] = True
d = np.abs(out8.astype(int) - src8.astype(int)).max(2)
assert d[~edited].max() == 0, 'pre-JPEG change outside the two boxes'
letters = np.zeros((H, W), bool)
letters[BY0:BY1 + 1, BX0:BX1 + 1] = (src8[BY0:BY1 + 1, BX0:BX1 + 1, 1] >= 225)
assert d[letters].max() == 0, 'a letter pixel changed'
print('pre-JPEG: changed px', int((d > 0).sum()), 'max diff outside boxes', int(d[~edited].max()),
      'letter px (G>=225) changed', int((d[letters] > 0).sum()))
np.save(f'{DBG}/v4_prejpeg.npy', out8)
Image.fromarray(out8).save(OUT, quality=93, subsampling=0)
print('saved', OUT, hashlib.md5(open(OUT, 'rb').read()).hexdigest())
