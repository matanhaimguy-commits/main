#!/usr/bin/env python3
"""IMG-W43-2 (2026-w43-2-image) v4 = v3 + one local code fix. No image generation.

Run in the Higgsfield sandbox:
    python3 v4_edit.py [SHIFT] [OUT]   # default SHIFT=5, OUT=/home/user/drafts/fixed/be2672d8_v4.jpg

Fix V10: the cedilla of the "ç" in "çdo" (line 3, x 444-466, rows 418-436) sat on the soft top rim of the crimson
box behind "sistem." (line 4). The whole of line 4 ("janë" + the crimson box with "sistem." inside it, including
the box's soft rim and its dark-red halo) is moved down by SHIFT px; the line above, the cedilla, the plant on the
left, the wall and everything else stay where they are.

Method (all float, one JPEG encode at the end):
  1. Ic  = v3 with the cedilla taken out: inside x 443-467, rows 418-441 each row is a straight line between the clean
           columns either side (wall above the box, the box's horizontal rim profile below). The rim is uniform along x.
  2. Wp  = wall plate with line 4 taken out:
           box zone  x 273-596, rows 426-530 -> per-column linear blend of the wall 5 rows above and 5 rows below
                                                (horizontally smoothed 15 px), i.e. the plain dark wall;
           "janë"    letters (luma > 40 in x 92-272, rows 436-523, dilated 4 px to take their AA and dark halo)
                     -> cv2 Telea inpaint of the wall.
  3. D   = Ic - Wp inside those two zones (the line-4 layer as an additive layer, halo and AA included), 0 outside.
  4. new = Wp + D shifted down SHIFT rows.  Vacated rows show the wall plate; outside both zones new == v3 exactly.
  5. Cedilla put back over the new background: alpha from luma (ivory 254,250,249 over the clean background Ic),
     out = v3 + (1 - alpha) * (new - Ic) in the cedilla rect, so only the background share under its soft bottom
     edge changes from crimson rim to wall; in rows 432+ (where the 4:2:0 source had bled the box's red chroma into
     the white) the glyph is re-composited as alpha * ivory + (1 - alpha) * new, so no pink fringe is left behind.
Everything outside x 86-596, rows 418-(530+SHIFT) is the v3 pixels exactly before the JPEG encode (asserted).
"""
import json
import sys

import cv2
import numpy as np
from PIL import Image

SRC = '/home/user/drafts/fixed/be2672d8_v3.jpg'
S = int(sys.argv[1]) if len(sys.argv) > 1 else 5
OUT = sys.argv[2] if len(sys.argv) > 2 else '/home/user/drafts/fixed/be2672d8_v4.jpg'

I = np.asarray(Image.open(SRC).convert('RGB')).astype(np.float32)
H, W = I.shape[:2]
assert (W, H) == (1080, 1350)

# geometry measured on v3 (x0, x1 exclusive; y0, y1 exclusive)
BOX = (273, 597, 426, 531)    # crimson box 50% edges x 284-583, y 434.5-518; rim from row 431, halo to row ~527
LET = (92, 273, 436, 524)     # "janë": dots from row 441, j descender to row 518, x 100-266
CED = (443, 468, 418, 442)    # cedilla of "ç": rows 418-436, x 444-466 (incl. its dark sharpening ring)

# 1. cedilla out -> Ic
Ic = I.copy()
cx0, cx1, cy0, cy1 = CED
lref = I[cy0:cy1, cx0 - 3:cx0].mean(1)          # columns 440-442
rref = I[cy0:cy1, cx1:cx1 + 3].mean(1)          # columns 468-470
t = ((np.arange(cx0, cx1) - (cx0 - 2)) / ((cx1 + 1) - (cx0 - 2))).astype(np.float32)
Ic[cy0:cy1, cx0:cx1] = lref[:, None, :] * (1 - t[None, :, None]) + rref[:, None, :] * t[None, :, None]

# 2. wall plate Wp
Wp = Ic.copy()
bx0, bx1, by0, by1 = BOX
top = cv2.blur(Ic[by0 - 5:by0, bx0 - 8:bx1 + 8].mean(0, keepdims=True), (15, 1))[0, 8:-8]   # rows 421-425
bot = cv2.blur(Ic[by1:by1 + 5, bx0 - 8:bx1 + 8].mean(0, keepdims=True), (15, 1))[0, 8:-8]   # rows 531-535
ty = ((np.arange(by0, by1) - (by0 - 3)) / ((by1 + 2) - (by0 - 3))).astype(np.float32)
Wp[by0:by1, bx0:bx1] = top[None] * (1 - ty[:, None, None]) + bot[None] * ty[:, None, None]

lx0, lx1, ly0, ly1 = LET
L = 0.299 * Ic[..., 0] + 0.587 * Ic[..., 1] + 0.114 * Ic[..., 2]
let = np.zeros((H, W), np.uint8)
let[ly0:ly1, lx0:lx1] = (L[ly0:ly1, lx0:lx1] > 40).astype(np.uint8)
let = cv2.dilate(let, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))
let[:, bx0:] = 0
inp = cv2.inpaint(np.clip(Wp + 0.5, 0, 255).astype(np.uint8), let * 255, 6, cv2.INPAINT_TELEA).astype(np.float32)
Wp[let > 0] = inp[let > 0]

zone = let > 0
zone[by0:by1, bx0:bx1] = True

# 3-4. move the line-4 layer down S rows
D = np.where(zone[..., None], Ic - Wp, 0).astype(np.float32)
Ds = np.zeros_like(D)
Ds[S:] = D[:-S]
new = Wp + Ds

# 5. cedilla back over the new background
#    alpha from luma (Y is kept at full resolution by the 4:2:0 source, chroma is not), ivory = the letter-core colour.
#    a) everywhere in the rect: out = v3 + (1 - alpha) * (new - Ic)   (only the background share changes)
#    b) rows 432+ (where the old background was the crimson rim and the 4:2:0 chroma had bled red into the white):
#       out = alpha * IVORY + (1 - alpha) * new, blended in by alpha so the dark sharpening ring keeps route a)
IVORY = np.array([254.0, 250.0, 249.0], np.float32)
Y_IV = float(0.299 * IVORY[0] + 0.587 * IVORY[1] + 0.114 * IVORY[2])
Yi = 0.299 * I[..., 0] + 0.587 * I[..., 1] + 0.114 * I[..., 2]
Yc = 0.299 * Ic[..., 0] + 0.587 * Ic[..., 1] + 0.114 * Ic[..., 2]
sl = (slice(cy0, cy1), slice(cx0, cx1))
alpha = np.clip((Yi[sl] - Yc[sl]) / np.maximum(Y_IV - Yc[sl], 1.0), 0, 1)[..., None]
out_a = I[sl] + (1 - alpha) * (new[sl] - Ic[sl])
out_b = alpha * IVORY + (1 - alpha) * new[sl]
wb = np.clip((alpha - 0.02) / 0.10, 0, 1)
wb[:432 - cy0] = 0
out = new.copy()
out[sl] = (1 - wb) * out_a + wb * out_b
out = np.clip(np.round(out), 0, 255).astype(np.uint8)

# scope check: nothing changes outside the edit window before the JPEG encode
EDIT = (lx0 - 6, bx1, cy0, by1 + S)
mask_out = np.ones((H, W), bool)
mask_out[EDIT[2]:EDIT[3], EDIT[0]:EDIT[1]] = False
v3u8 = I.astype(np.uint8)
changed = np.any(out != v3u8, axis=2)
assert not changed[mask_out].any(), 'pixels changed outside the edit window'

np.save(OUT.replace('.jpg', '_prejpeg.npy'), out)
Image.fromarray(out).save(OUT, 'JPEG', quality=93, subsampling=0)

ys, xs = np.nonzero(changed)
rep = {'shift': S, 'edit_window_x0x1y0y1': EDIT,
       'changed_bbox_prejpeg': [int(xs.min()), int(xs.max()), int(ys.min()), int(ys.max())],
       'changed_px_prejpeg': int(changed.sum()), 'changed_outside_window_prejpeg': 0}
fin = np.asarray(Image.open(OUT).convert('RGB')).astype(int)
dd = np.abs(fin - I.astype(int)).max(2)
rep['jpeg_vs_v3_outside_window'] = {'max': int(dd[mask_out].max()), 'mean': round(float(dd[mask_out].mean()), 3),
                                    'p99_9': float(np.percentile(dd[mask_out], 99.9)),
                                    'frac_px_ge_4': round(float((dd[mask_out] >= 4).mean()), 5)}
print(json.dumps(rep))
