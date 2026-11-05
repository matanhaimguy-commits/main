#!/usr/bin/env python3
"""v5 cover for the Sat 17 StraightScale quote reel (ss-2026-10-17), code only, no generation.

Starts again from the v3 cover (v4's blur is not reused). It softens only the two glass panes of the
lit shop window bottom-left, so the shelf pseudo-text goes, and leaves everything else as it was:

* The window frame stays sharp along its whole length: the shutter slat and top rail, post A between
  the panes (x ~158-187, plus its base below the sill), the right frame post (x ~273-300), the glazing
  beads, the lit sill, the base panels and the pavement. The blur area is the two panes' glass only,
  bounded by straight lines measured on the frame's inner edges (fixes D1: no ramp crosses a post).
* The owner is protected by a tight, colour-keyed mask (no dilation): coat, sleeve and cuff are keyed
  by luma (< 40); above the sleeve, where the glass is bright (~200), the key is luma < 115 so the
  hand and the lit rim of the sleeve stay with him. The key only searches 6 px around the old outline
  and keeps what is connected to its inside. A 2 px band along his outline gets a local luminance matte, and the sharp window share of
  each edge pixel is swapped for the blurred window (un-mixing), so the blurred window meets the coat
  with no rim, no halo, no fleck and no steps (fixes D2).
* Blur: Gaussian sigma 9 px as a normalised convolution over pure-window pixels only (frame, coat and
  hand never bleed in), then 12 % darker, as in v4.

Run in the Higgsfield sandbox:
    python3 v5_cover_edit.py [OUT.jpg]
Default output: /home/user/daily/reel/v5/ss-2026-10-17-reel-v5-cover.jpg (JPEG q93, 4:4:4).
"""
import sys

import cv2
import numpy as np
from PIL import Image

SRC = '/home/user/daily/reel/v3/ss-2026-10-17-reel-v3-cover.jpg'
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/user/daily/reel/v5/ss-2026-10-17-reel-v5-cover.jpg'
MASKS = '/home/user/daily/reel/v5/cov/masks.npz'
SIGMA = 9.0     # window blur, px
DARK = 0.12     # darkening of the blurred glass
T_COAT = 40     # luma below this = coat / sleeve / cuff (glass next to him is >= 47)
T_TOP = 115     # inside TOP_BOX (hand, cuff and the lit top rim of the sleeve; glass there is >= 134)
TOP_BOX = (150, 940, 277, 1096)   # x0, y0, x1, y1
BAND = 2        # px each side of the owner outline that gets a soft matte

# ---- frame geometry (pixel-index coordinates, measured on v3 at 4x-8x) ----
def y_top(x):    # lower edge of the shutter slat / top rail; glass below it
    return 1022.5 + 0.047 * x
def x_postA_l(y):  # left face of post A (left pane ends here)
    return 158.2 - 0.003 * (y - 1100)
def x_postA_r(y):  # right face of post A (right pane starts here)
    return 187.0 - 0.0012 * (y - 1215)
def x_postB_l(y):  # inner face of the right frame post (right pane ends here)
    return 274.1 - 0.0054 * (y - 1041)
def y_left_bot(x):   # glazing bead / bottom rail of the left pane
    return 1747.0 - 0.56 * x
def y_right_bot(x):  # top of the upper glazing bead above the lit sill of the right pane
    return 1640.0 - 0.56 * (x - 188)

# owner outline from v4 (coarse, up to 8 px outside the coat): used only as a search region and seed
OWNER = [(155, 950), (219, 950), (219, 1035), (230, 1045), (240, 1058), (249, 1074), (256, 1089), (272, 1082),
         (288, 1066), (300, 1042), (318, 1018), (338, 1000), (360, 975), (1080, 975), (1080, 1920), (395, 1920),
         (378, 1830), (365, 1780), (352, 1730), (345, 1700), (345, 1503), (300, 1502), (262, 1500), (260, 1490),
         (261, 1470), (264, 1445), (268, 1420), (272, 1402), (278, 1386), (281, 1370), (282, 1320), (286, 1295),
         (290, 1272), (295, 1250), (300, 1225), (306, 1200), (283, 1201), (262, 1204), (240, 1198), (220, 1189),
         (203, 1177), (190, 1160), (180, 1140), (171, 1117), (164, 1100), (159, 1080), (163, 1057), (170, 1040),
         (160, 1030), (155, 1000)]


def cov(d):
    """Anti-aliased coverage of a half-plane from a signed distance in px (inside > 0)."""
    return np.clip(d + 0.5, 0.0, 1.0)


def nconv(v, w, sigma):
    """Normalised Gaussian convolution of v (HxW or HxWx3) with weights w (HxW)."""
    if v.ndim == 3:
        num = cv2.GaussianBlur(v * w[..., None], (0, 0), sigma)
        den = cv2.GaussianBlur(w, (0, 0), sigma)[..., None]
    else:
        num = cv2.GaussianBlur(v * w, (0, 0), sigma)
        den = cv2.GaussianBlur(w, (0, 0), sigma)
    return num / np.maximum(den, 1e-6), den


def main():
    img = np.asarray(Image.open(SRC).convert('RGB')).astype(np.float32)
    H, W = img.shape[:2]
    L = img @ np.array([0.299, 0.587, 0.114], np.float32)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)

    # ---- glass coverage G: the two panes, frame excluded, 1 px anti-aliased edges ----
    top = cov(yy - y_top(xx))
    g_left = top * cov(x_postA_l(yy) - xx) * cov(y_left_bot(xx) - yy)
    g_right = top * cov(xx - x_postA_r(yy)) * cov(x_postB_l(yy) - xx) * cov(y_right_bot(xx) - yy)
    G = np.maximum(g_left, g_right).astype(np.float32)

    # ---- owner: colour key inside the (widened) old outline, seeded from its interior ----
    P = np.zeros((H, W), np.uint8)
    cv2.fillPoly(P, [np.array(OWNER, np.int32)], 1)
    k = lambda r: cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))
    region = cv2.dilate(P, k(6))
    core = cv2.erode(P, k(10))
    Ls = cv2.GaussianBlur(L, (0, 0), 0.6)
    thr = np.full((H, W), T_COAT, np.float32)
    x0, y0, x1, y1 = TOP_BOX
    thr[y0:y1, x0:x1] = T_TOP
    dark = ((Ls < thr) & (region == 1)).astype(np.uint8)
    n, lab = cv2.connectedComponents(dark, connectivity=4)
    keep = np.unique(lab[(core == 1) & (dark == 1)])
    keep = keep[keep > 0]
    own = (np.isin(lab, keep) | (core == 1)).astype(np.uint8)
    # fill small holes only (specks inside the coat), never large enclosed window areas
    inv = (1 - own).astype(np.uint8)
    n2, lab2, st, _ = cv2.connectedComponentsWithStats(inv, connectivity=4)
    for i in range(1, n2):
        if st[i, cv2.CC_STAT_AREA] < 60:
            own[lab2 == i] = 1

    # ---- soft matte in a 2 px band along the owner outline (local luminance key) ----
    d_in = cv2.distanceTransform(own, cv2.DIST_L2, 3)
    d_out = cv2.distanceTransform(1 - own, cv2.DIST_L2, 3)
    w_win = ((own == 0) & (d_out > BAND) & (G > 0.99)).astype(np.float32)
    w_own = ((own == 1) & (d_in > BAND)).astype(np.float32)
    Wl, _ = nconv(L, w_win, 2.5)
    Cl, _ = nconv(L, w_own, 2.5)
    a_key = np.clip((Wl - L) / np.maximum(Wl - Cl, 8.0), 0.0, 1.0)
    band = ((own == 1) & (d_in <= BAND)) | ((own == 0) & (d_out <= BAND))
    alpha = own.astype(np.float32)
    alpha[band] = a_key[band]
    alpha[(own == 1) & (d_in > BAND)] = 1.0

    # ---- blur the pure-window pixels only, then darken ----
    w_blur = ((G > 0.5) & (alpha < 0.01)).astype(np.float32)
    bl, _ = nconv(img, w_blur, SIGMA)
    soft = bl * (1.0 - DARK)

    # sharp window colour under each mixed edge pixel (for un-mixing), from nearby pure-window pixels
    w_pure = ((alpha < 0.01) & (G > 0.5)).astype(np.float32)
    win_est, den = nconv(img, w_pure, 1.5)
    win_est = np.where((alpha < 0.01)[..., None] | (den < 0.05), img, win_est)

    e = (G * (1.0 - alpha)).astype(np.float32)
    out = img + e[..., None] * (soft - win_est)
    out = np.clip(out + 0.5, 0, 255).astype(np.uint8)
    Image.fromarray(out).save(OUT, quality=93, subsampling=0)
    np.savez_compressed(MASKS, G=G.astype(np.float16), alpha=alpha.astype(np.float16), own=own, e=e.astype(np.float16))

    # ---- checks on the pre-JPEG pixels ----
    src8 = np.clip(img + 0.5, 0, 255).astype(np.uint8).astype(int)
    d = np.abs(out.astype(int) - src8).max(axis=2)
    ch = np.where(d > 0)
    print('changed px:', len(ch[0]), ' bbox x', ch[1].min(), '-', ch[1].max(), ' y', ch[0].min(), '-', ch[0].max())
    print('max diff where G==0 (frame, shutter, sill, base, street, headline):', int(d[G == 0].max()))
    print('max diff on owner (alpha==1):', int(d[alpha >= 1].max()), ' y<950:', int(d[:950].max()),
          ' x>=301:', int(d[:, 301:].max()))
    win = (G > 0.99) & (alpha < 0.01)
    print('glass luma mean: %.1f -> %.1f' % (L[win].mean(), (out.astype(np.float32) @ np.array([0.299, 0.587, 0.114]))[win].mean()))


if __name__ == '__main__':
    main()
