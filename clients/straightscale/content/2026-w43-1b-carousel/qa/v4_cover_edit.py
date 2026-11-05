#!/usr/bin/env python3
"""StraightScale 2026-w43-1b carousel, cover (SL01) v4: move the cover's swipe-arrow button 20 px down so it sits on
the logo's centre line (review SL01.v3, V18). Code only (PIL, numpy, OpenCV); no generation.

  python3 v4_cover_edit.py [--write]       (Higgsfield sandbox; input /home/user/drafts/fixed/5d6ecdb0_v3.jpg)

 1. Lift: the red disc (r>120, g<50, b<60, largest component in the bottom-right corner), holes filled (the white
    arrow). Matte = 1 on the disc and its 1 px anti-aliased rim (mask grown 1 px), then a linear 1 px feather to 0.
    The disc has no drop shadow (radial profile flat from 1 px outside the rim on all sides, measured), so this
    matte holds the whole button: red face, white arrow, rim.
 2. Plate: the old disc +5 px (rim, its JPEG chroma ringing and the dark fringe on the lit side) is refilled:
    - low-pass = harmonic (Laplace) membrane from the boundary, the boundary values taken from a local PLANE fit
      (first-order normalised convolution, sigma 3) of the untouched surface, so the lit gradient on the left is
      not biased at the one-sided edge (a plain normalised blur left a 6-level step there, seen at 4x);
    - grain layer = the high-pass (sigma 3) of an adjacent untouched patch, the donor offset chosen by the best
      high-pass match on an 8 px band around the hole plus the same grain level, scaled pixel by pixel to the local
      grain level of the surface (local std map of the untouched surface carried in by the membrane / the donor's
      own local std), clipped to +-3 local std;
    - level calibration: one scalar k on the grain layer so the visible fill's grain sits at the surrounding
      surface's level (geometric mean of the ring std ratio, the ring robust-std ratio and the median tile ratio
      = 1), clipped 0.8..1.25.
 3. Paste: the lifted button 20 px lower (centre y1241 -> y1261) over the plate with its matte.
 4. Only pixels in the plate mask and under the moved matte change; every other pixel is copied back from v3 before
    the JPEG (q93, 4:4:4) is written.
"""
import sys, json, os
import numpy as np, cv2
from PIL import Image

SRC = "/home/user/drafts/fixed/5d6ecdb0_v3.jpg"
OUT = "/home/user/drafts/fixed/5d6ecdb0_v4.jpg"
WORK = "/home/user/v4c"
SHIFT = 20                              # px down
CORNER = (880, 1170, 1075, 1345)        # x0, y0, x1, y1: where the arrow button is searched
ZONE = (900, 1190, 1020, 1310)          # outside this box the output must equal v3 (JPEG noise only)
RIM = 1.0                               # matte: 1 out to 1 px outside the colour mask, then a 1 px linear feather
PLATE_GROW = 5                          # old disc + rim + chroma ringing + dark fringe
BAND = 8
SPLIT = 3.0                             # low-pass / grain split (Gaussian sigma)
CROP = (820, 1100, 1080, 1350)          # x0, y0, x1, y1: working window for the plane fit
LOGO_BOX = (98, 1233, 393, 1288)
LUMA = np.array([0.114, 0.587, 0.299], np.float32)

def disk(r): return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*r+1, 2*r+1))
def dil(m, r): return cv2.dilate(m.astype(np.uint8), disk(r)) > 0 if r > 0 else m.astype(bool)
def rstd(v): return float(1.4826*np.median(np.abs(v - np.median(v))))
def lp_of(X, sig): return np.stack([cv2.GaussianBlur(X[..., c], (0, 0), sig) for c in range(X.shape[2])], 2)
def nblur(x, valid, sig):
    w = valid.astype(np.float32); den = cv2.GaussianBlur(w, (0, 0), sig) + 1e-6
    if x.ndim == 2: return cv2.GaussianBlur(x*w, (0, 0), sig)/den
    return np.stack([cv2.GaussianBlur(x[..., c]*w, (0, 0), sig)/den for c in range(x.shape[2])], 2)
def locstd(h, valid, sig=6):
    w = valid.astype(np.float32)
    return np.sqrt(cv2.GaussianBlur(h*h*w, (0, 0), sig)/(cv2.GaussianBlur(w, (0, 0), sig)+1e-6))

# ---------------------------------------------------------------- 1. lift
def disc_mask(img):
    b, g, r = [img[:, :, k].astype(int) for k in range(3)]
    z = np.zeros(r.shape, bool); x0, y0, x1, y1 = CORNER; z[y0:y1, x0:x1] = True
    red = z & (r > 120) & (g < 50) & (b < 60)
    n, lab, st, _ = cv2.connectedComponentsWithStats(red.astype(np.uint8))
    k = 1 + int(np.argmax(st[1:, 4])); comp = lab == k
    cnts, _ = cv2.findContours(comp.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    filled = np.zeros(r.shape, np.uint8); cv2.drawContours(filled, cnts, -1, 1, -1)
    filled = filled > 0
    (cx, cy), rad = cv2.minEnclosingCircle(max(cnts, key=cv2.contourArea))
    ys, xs = np.nonzero(filled)
    info = dict(red_px=int(comp.sum()), filled_px=int(filled.sum()), holes_px=int((filled & ~comp).sum()),
                bbox=[int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())],
                centre=[round(cx, 1), round(cy, 1)], radius=round(rad, 1),
                bbox_centre=[(xs.min()+xs.max())/2, (ys.min()+ys.max())/2])
    return filled, info

def matte(filled):
    dist = cv2.distanceTransform((~filled).astype(np.uint8), cv2.DIST_L2, 5)
    return np.clip(1 + RIM - dist, 0, 1).astype(np.float32)

# ---------------------------------------------------------------- 2. plate
def plane_lp(X, valid, sig):
    """local first-order (plane) fit with Gaussian weights over valid pixels only: an unbiased low-pass right up to a
    one-sided boundary on a lit gradient."""
    x0, y0, x1, y1 = CROP
    out = X.astype(np.float32).copy()
    Xc = X[y0:y1, x0:x1].astype(np.float64); w = valid[y0:y1, x0:x1].astype(np.float64)
    yy, xx = np.mgrid[0:y1-y0, 0:x1-x0].astype(np.float64)
    G = lambda a: cv2.GaussianBlur(a, (0, 0), sig)
    S0 = G(w); Sx = G(w*xx)-xx*S0; Sy = G(w*yy)-yy*S0
    Sxx = G(w*xx*xx)-2*xx*G(w*xx)+xx*xx*S0; Syy = G(w*yy*yy)-2*yy*G(w*yy)+yy*yy*S0
    Sxy = G(w*xx*yy)-xx*G(w*yy)-yy*G(w*xx)+xx*yy*S0
    A = np.stack([np.stack([S0, Sx, Sy], -1), np.stack([Sx, Sxx, Sxy], -1), np.stack([Sy, Sxy, Syy], -1)], -2) + np.eye(3)*1e-6
    for c in range(Xc.shape[2]):
        f = Xc[..., c]; F0 = G(w*f); Fx = G(w*f*xx)-xx*F0; Fy = G(w*f*yy)-yy*F0
        out[y0:y1, x0:x1, c] = np.linalg.solve(A, np.stack([F0, Fx, Fy], -1)[..., None])[..., 0, 0]
    return out

def membrane(field, M, band, iters=1500):
    """harmonic interpolation into M of a field known on band (Telea start, Jacobi relaxation of Laplace)."""
    out = np.zeros_like(field)
    ys, xs = np.nonzero(dil(M, 2)); y0, y1, x0, x1 = ys.min()-2, ys.max()+3, xs.min()-2, xs.max()+3
    Mi = M[y0:y1, x0:x1]
    for ch in range(field.shape[2]):
        lp = np.where(band, field[:, :, ch], 0).astype(np.float32)
        u = lp[y0:y1, x0:x1].copy()
        u[Mi] = cv2.inpaint(lp, M.astype(np.uint8), 5, cv2.INPAINT_TELEA)[y0:y1, x0:x1][Mi]
        for _ in range(iters):
            avg = 0.25*(np.roll(u, 1, 0)+np.roll(u, -1, 0)+np.roll(u, 1, 1)+np.roll(u, -1, 1))
            u[Mi] = avg[Mi]
        out[y0:y1, x0:x1, ch] = u
    return out

def fine_grain_angle(L, M, side=None):
    """orientation of the fine wood grain (structure tensor of the sigma-3 high-pass, 4..50 px ring), and coherence."""
    hp = L - cv2.GaussianBlur(L, (0, 0), 3.0)
    gx = cv2.Sobel(hp, cv2.CV_32F, 1, 0, ksize=3); gy = cv2.Sobel(hp, cv2.CV_32F, 0, 1, ksize=3)
    ring = dil(M, 50) & ~dil(M, 4)
    if side is not None: ring &= side
    Jxx = (gx*gx)[ring].sum(); Jyy = (gy*gy)[ring].sum(); Jxy = (gx*gy)[ring].sum()
    ang = float(np.degrees(0.5*np.arctan2(2*Jxy, Jxx-Jyy) + np.pi/2) % 180)
    return round(ang, 1), round(float(np.sqrt((Jxx-Jyy)**2+4*Jxy**2)/(Jxx+Jyy)), 2)

def find_donor(I, M, forbid, band, reach=120, step=2):
    """adjacent untouched patch whose high-pass continues the band's (normalised MSE) at the same grain level."""
    H, W = M.shape
    hpL = (I - lp_of(I, SPLIT)) @ LUMA
    T = locstd(hpL, ~forbid)
    by, bx = np.nonzero(band); fy, fx = np.nonzero(dil(M, 14))
    best = None
    for dy in range(-reach, reach+1, step):
        for dx in range(-reach, reach+1, step):
            yy, xx = fy+dy, fx+dx
            if yy.min() < 0 or yy.max() >= H or xx.min() < 0 or xx.max() >= W: continue
            if forbid[yy, xx].any(): continue
            e = float(np.mean((hpL[by, bx]-hpL[by+dy, bx+dx])**2))/float(np.mean(hpL[by, bx]**2))
            lvl = float(np.log((T[by+dy, bx+dx].mean()+0.1)/(T[by, bx].mean()+0.1)))
            c = e + 2*lvl*lvl + 0.002*np.hypot(dx, dy)
            if best is None or c < best[0]: best = (c, dx, dy, e, lvl)
    return best

def plate_layers(img, M, forbid):
    I = img.astype(np.float32)
    band = dil(M, BAND) & ~M
    LP = membrane(plane_lp(I, ~M, SPLIT), M, band)
    _, dx, dy, e, lvl = find_donor(I, M, forbid, band)
    ys, xs = np.nonzero(dil(M, 14))
    hpD_full = I - lp_of(I, SPLIT)                       # donor high-pass in its own (clean) context
    hpD = np.zeros_like(I); hpD[ys, xs] = hpD_full[ys+dy, xs+dx]
    hpS = (I - nblur(I, ~M, SPLIT)) @ LUMA               # surface high-pass, the button left out of its low-pass
    T = locstd(hpS, ~forbid); Tm = membrane(T[..., None], M, band)[..., 0]
    Dl = locstd(hpD_full @ LUMA, np.ones_like(M)); Dm = np.zeros_like(Tm); Dm[ys, xs] = Dl[ys+dy, xs+dx]
    g = np.clip(Tm/np.maximum(Dm, 0.3), 0.4, 2.5)
    HP = np.clip(hpD*g[..., None], -3*Tm[..., None], 3*Tm[..., None])
    L = I @ LUMA
    xs_side = np.mgrid[0:M.shape[0], 0:M.shape[1]][1]
    log = dict(donor_dx=int(dx), donor_dy=int(dy), donor_dist=round(float(np.hypot(dx, dy)), 1),
               donor_dir_deg=round(float(np.degrees(np.arctan2(dy, dx)) % 180), 1),
               fine_grain_deg_right_side=fine_grain_angle(L, M, xs_side > 961), fine_grain_deg_all=fine_grain_angle(L, M),
               band_hp_nmse=round(e, 3), donor_vs_band_grain_level=round(float(np.exp(lvl)), 2),
               local_gain_median_p10_p90=[round(float(np.percentile(g[M], q)), 2) for q in (50, 10, 90)],
               target_grain_std_median=round(float(np.median(Tm[M])), 2))
    return LP, HP, log

# ---------------------------------------------------------------- metrics
def texture_stats(img, M, excl, ring_in=3, ring_out=15, sig=2.0):
    L = img.astype(np.float32) @ LUMA
    hp = L - cv2.GaussianBlur(L, (0, 0), sig)
    ring = dil(M, ring_out) & ~dil(excl, ring_in)
    t = dict(px=int(M.sum()), ring_px=int(ring.sum()),
             in_mean=round(float(L[M].mean()), 1), ring_mean=round(float(L[ring].mean()), 1),
             in_std=round(float(hp[M].std()), 2), ring_std=round(float(hp[ring].std()), 2),
             in_rstd=round(rstd(hp[M]), 2), ring_rstd=round(rstd(hp[ring]), 2))
    t["std_ratio"] = round(t["in_std"]/max(1e-6, t["ring_std"]), 2)
    t["rstd_ratio"] = round(t["in_rstd"]/max(1e-6, t["ring_rstd"]), 2)
    t["mean_diff"] = round(t["in_mean"]-t["ring_mean"], 1)
    return t

def tile_stats(img, vis, excl, tile=12, grow=12, sig=2.0, min_px=40):
    """per 12 px tile of the visible fill vs the untouched pixels within 12 px: mean minus a plane fitted to those
    pixels (the lit gradient taken out), and high-pass std ratio."""
    L = img.astype(np.float32) @ LUMA; hp = L - cv2.GaussianBlur(L, (0, 0), sig)
    clear = ~dil(excl, 3); ys, xs = np.nonzero(vis); R = []; Q = []
    for ty in range(ys.min()//tile*tile, ys.max()+1, tile):
        for tx in range(xs.min()//tile*tile, xs.max()+1, tile):
            ins = np.zeros_like(vis); ins[ty:ty+tile, tx:tx+tile] = True; ins &= vis
            if ins.sum() < min_px: continue
            win = np.zeros_like(vis); win[max(0, ty-grow):ty+tile+grow, max(0, tx-grow):tx+tile+grow] = True
            outs = win & clear
            if outs.sum() < min_px: continue
            oy, ox = np.nonzero(outs); c, *_ = np.linalg.lstsq(np.stack([np.ones(len(ox)), ox, oy], 1), L[oy, ox], rcond=None)
            iy, ix = np.nonzero(ins)
            R.append(float(L[ins].mean() - (np.stack([np.ones(len(ix)), ix, iy], 1) @ c).mean()))
            Q.append(float(hp[ins].std()/max(1e-6, hp[outs].std())))
    R = np.array(R); Q = np.array(Q)
    return dict(tiles=len(R), plane_resid_abs_median=round(float(np.median(np.abs(R))), 2), plane_resid_abs_max=round(float(np.abs(R).max()), 2),
                std_ratio_median=round(float(np.median(Q)), 2), std_ratio_min_max=[round(float(Q.min()), 2), round(float(Q.max()), 2)])

def seam(img, M, A2):
    """mean luma step across the plate boundary (1.5 px each side, visible part) vs the step between the next two
    rings outside (the surface's own gradient)."""
    L = img.astype(np.float32) @ LUMA
    din = cv2.distanceTransform(M.astype(np.uint8), cv2.DIST_L2, 5); dout = cv2.distanceTransform((~M).astype(np.uint8), cv2.DIST_L2, 5)
    near = dil(M & (A2 < 0.02), 4) & (A2 < 0.02)
    i1 = near & M & (din <= 1.5); o1 = near & ~M & (dout <= 1.5); o2 = near & ~M & (dout > 1.5) & (dout <= 3)
    lb = lambda m: cv2.GaussianBlur(L*m, (0, 0), 2)/(cv2.GaussianBlur(m.astype(np.float32), (0, 0), 2)+1e-6)
    a, b, c = lb(i1), lb(o1), lb(o2)
    return dict(step_across_boundary=round(float(np.abs(a-b)[o1].mean()), 2), step_next_ring_outside=round(float(np.abs(b-c)[o1].mean()), 2))

def control(img, vis, excl, disc, offs=((-110, -60), (0, -110), (-60, -110), (60, -110), (60, -160), (0, -160),
                                          (-160, -80), (-200, 0), (-120, 35), (60, -210), (0, -220), (-110, 0))):
    """the same numbers on UNTOUCHED v3 surface: the visible-crescent shape moved to 12 clear spots nearby."""
    rows = []
    for dx, dy in offs:
        ey, ex = np.nonzero(dil(excl, 16))
        if (ey+dy).max() >= img.shape[0] or (ex+dx).max() >= img.shape[1] or (ey+dy).min() < 0 or (ex+dx).min() < 0: continue
        v = np.zeros_like(vis); e = np.zeros_like(excl)
        ys, xs = np.nonzero(vis); v[ys+dy, xs+dx] = True; ys, xs = np.nonzero(excl); e[ys+dy, xs+dx] = True
        if (dil(e, 15) & dil(disc, 4)).any(): continue
        t = texture_stats(img, v, e); tl = tile_stats(img, v, e)
        rows.append([t["mean_diff"], t["std_ratio"], t["rstd_ratio"], tl["plane_resid_abs_median"], tl["plane_resid_abs_max"], tl["std_ratio_median"]])
    R = np.array(rows); names = ["mean_diff", "std_ratio", "rstd_ratio", "tile_plane_resid_abs_median", "tile_plane_resid_abs_max", "tile_std_ratio_median"]
    return dict(spots=len(rows), **{n: dict(median=round(float(np.median(R[:, i])), 2), min=round(float(R[:, i].min()), 2), max=round(float(R[:, i].max()), 2)) for i, n in enumerate(names)})

def rim_profile(img, cx, cy, R, ks=(-2, -1, 0, 1, 2, 3)):
    """luma / red by signed distance from the disc's circle, 4 sectors: the button's edge before vs after."""
    I = img.astype(np.float32); L = I @ LUMA
    yy, xx = np.mgrid[0:img.shape[0], 0:img.shape[1]]
    d = np.hypot(xx-cx, yy-cy) - R; a = np.degrees(np.arctan2(yy-cy, xx-cx)) % 360
    out = {}
    for nm, a0 in (("right", 315), ("down", 45), ("left", 135), ("up", 225)):
        s = ((a - a0) % 360) < 90
        out[nm] = [[k, round(float(L[s & (np.abs(d-k) < 0.5)].mean()), 1), round(float(I[..., 2][s & (np.abs(d-k) < 0.5)].mean()), 1)] for k in ks]
    return out

def arrow_centre(img):
    """v3_edit.py's measure: min enclosing circle of the red disc (r>140, r>2g, r>2b)."""
    b, g, r = [img[:, :, k].astype(int) for k in range(3)]
    z = np.zeros(r.shape, bool); z[1170:1345, 880:1075] = True
    red = z & (r > 140) & (r > 2*g) & (r > 2*b)
    n, lab, st, _ = cv2.connectedComponentsWithStats(red.astype(np.uint8))
    k = 1+int(np.argmax(st[1:, 4]))
    cnts, _ = cv2.findContours((lab == k).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    (cx, cy), rad = cv2.minEnclosingCircle(max(cnts, key=cv2.contourArea))
    return [round(cx, 1), round(cy, 1), round(rad, 1)]

# ---------------------------------------------------------------- views
def views(v3, v4):
    os.makedirs(f"{WORK}/views", exist_ok=True)
    q = [cv2.IMWRITE_JPEG_QUALITY, 90]
    gap = lambda w, h: np.full((h, w, 3), 255, np.uint8)
    cv2.imwrite(f"{WORK}/views/bottom_1x_before_after.jpg", np.vstack([v3[1170:1350], gap(1080, 6), v4[1170:1350]]), q)
    z2 = lambda x: cv2.resize(x, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(f"{WORK}/views/bottom_2x_right_before_after.jpg", np.vstack([z2(v3[1170:1350, 640:1080]), gap(880, 6), z2(v4[1170:1350, 640:1080])]), q)
    cv2.imwrite(f"{WORK}/views/bottom_2x_left_after.jpg", z2(v4[1170:1350, 0:440]), q)
    x0, y0, x1, y1 = ZONE
    z4 = lambda x: cv2.resize(x, None, fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
    cv2.imwrite(f"{WORK}/views/arrow_4x_before_after.jpg", np.hstack([z4(v3[y0:y1, x0:x1]), gap(6, 480), z4(v4[y0:y1, x0:x1])]), q)
    def boost(x, k=3):
        f = x.astype(np.float32); m = cv2.GaussianBlur(f, (0, 0), 12)
        return np.clip(m + k*(f-m), 0, 255).astype(np.uint8)
    cv2.imwrite(f"{WORK}/views/fill_4x_boost_before_after.jpg", np.hstack([z4(boost(v3[1195:1275, 915:1010])), gap(6, 320), z4(boost(v4[1195:1275, 915:1010]))]), q)
    t3 = cv2.resize(v3, (200, 250), interpolation=cv2.INTER_AREA); t4 = cv2.resize(v4, (200, 250), interpolation=cv2.INTER_AREA)
    cv2.imwrite(f"{WORK}/views/thumb200_before_after.png", np.hstack([t3, gap(6, 250), t4]))
    # bottom row guides at 1x: green = logo centre y, magenta = arrow centre y, cyan = logo box
    g = v4[1170:1350].copy()
    ly = (LOGO_BOX[1]+LOGO_BOX[3])/2 - 1170
    cv2.line(g, (0, int(round(ly))), (1079, int(round(ly))), (0, 255, 0), 1)
    ac = arrow_centre(v4); cv2.line(g, (600, int(round(ac[1]-1170))), (1079, int(round(ac[1]-1170))), (255, 0, 255), 1)
    cv2.rectangle(g, (LOGO_BOX[0], LOGO_BOX[1]-1170), (LOGO_BOX[2], LOGO_BOX[3]-1170), (255, 255, 0), 1)
    cv2.imwrite(f"{WORK}/views/bottom_guides_v4.jpg", g, q)

# ---------------------------------------------------------------- main
def compose(img, I, A2, S2, M, LP, HP, k):
    plate = I.copy(); plate[M] = (LP + k*HP)[M]
    out = A2[..., None]*S2 + (1-A2[..., None])*plate
    changed = M | (A2 > 0)
    out = np.clip(np.round(out), 0, 255).astype(np.uint8)
    out[~changed] = img[~changed]
    return out, changed

def main(write):
    img = cv2.imread(SRC)
    I = img.astype(np.float32)
    H, W = img.shape[:2]
    disc, dinfo = disc_mask(img)
    A = matte(disc)                                    # lifted button matte at the old position
    M = dil(disc, PLATE_GROW)                          # old button + rim + ringing + fringe, refilled
    forbid = dil(M, 2)
    LP, HP, flog = plate_layers(img, M, forbid)
    A2 = np.zeros_like(A); A2[SHIFT:] = A[:-SHIFT]     # the button 20 px lower
    S2 = np.zeros_like(I); S2[SHIFT:] = I[:-SHIFT]
    vis = M & (A2 < 0.02)                              # the refilled crescent left visible after the paste
    excl = M | (A2 > 0)
    meas = vis & ~dil(A2 > 0, 5)                       # measured part: >5 px from the moved button, so the sigma-2
                                                       # high-pass of the metrics does not pick up the button's edge
    # grain level calibration (one scalar on the grain layer)
    o1, _ = compose(img, I, A2, S2, M, LP, HP, 1.0)
    t1 = texture_stats(o1, meas, excl); tl1 = tile_stats(o1, meas, excl)
    gm = (t1["std_ratio"]*t1["rstd_ratio"]*tl1["std_ratio_median"])**(1/3)
    k = float(np.clip(1/gm, 0.8, 1.25))
    out, changed = compose(img, I, A2, S2, M, LP, HP, k)
    path = OUT if write else f"{WORK}/5d6ecdb0_v4_dry.jpg"
    Image.fromarray(cv2.cvtColor(out, cv2.COLOR_BGR2RGB)).save(path, quality=93, subsampling="4:4:4")
    back = cv2.imread(path)
    # ---- checks
    x0, y0, x1, y1 = ZONE
    outside = np.ones((H, W), bool); outside[y0:y1, x0:x1] = False
    dif = np.abs(back.astype(int)-img.astype(int)).max(2)
    Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)).save(f"{WORK}/v3_reenc.jpg", quality=93, subsampling="4:4:4")
    reenc = np.abs(cv2.imread(f"{WORK}/v3_reenc.jpg").astype(int)-img.astype(int)).max(2)
    new_disc, ninfo = disc_mask(back)
    ac_old, ac_new = arrow_centre(img), arrow_centre(back)
    under = (A2 > 0) & ~M                              # wood the moved button now covers (v3 pixels)
    Lv3 = I @ LUMA; bb, gg, rr = I[..., 0], I[..., 1], I[..., 2]
    white_old = disc & (img.min(2) > 180); white_new = new_disc & (back.min(2) > 180)
    vy, vx = np.nonzero(vis); my, mx = np.nonzero(M); cy_, cx_ = np.nonzero(changed)
    r3 = rim_profile(img, *dinfo["centre"], dinfo["radius"]); r4 = rim_profile(back, *ninfo["centre"], ninfo["radius"])
    dl = [abs(a[1]-b[1]) for s in r3 for a, b in zip(r3[s], r4[s]) if a[0] in (-1, 0, 1)]
    dr = [abs(a[2]-b[2]) for s in r3 for a, b in zip(r3[s], r4[s]) if a[0] in (-1, 0, 1)]
    with Image.open(path) as im: sub = im.layer if hasattr(im, "layer") else None; size = im.size
    rep = dict(source=SRC, output=path, size=list(size), jpeg_layers=sub, shift_px=SHIFT,
               button_v3=dict(**dinfo, arrow_centre_v3method=ac_old),
               button_v4=dict(**ninfo, arrow_centre_v3method=ac_new),
               white_arrow_px_v3_v4=[int(white_old.sum()), int(white_new.sum())],
               logo_box=list(LOGO_BOX), logo_centre_y=(LOGO_BOX[1]+LOGO_BOX[3])/2,
               arrow_minus_logo_centre_y=round(ac_new[1]-(LOGO_BOX[1]+LOGO_BOX[3])/2, 1),
               bottom_margin_px=dict(arrow=H-1-ninfo["bbox"][3], logo=H-LOGO_BOX[3]),
               matte=dict(rim_px=RIM, full_px=int((A >= 0.999).sum()), feather_px=int(((A > 0) & (A < 0.999)).sum())),
               rim_match_v4_vs_v3=dict(luma_abs_mean=round(float(np.mean(dl)), 2), luma_abs_max=round(float(max(dl)), 1),
                                       red_abs_mean=round(float(np.mean(dr)), 2), red_abs_max=round(float(max(dr)), 1), v3=r3, v4=r4),
               plate=dict(grow_px=PLATE_GROW, mask_px=int(M.sum()), mask_box=[int(mx.min()), int(my.min()), int(mx.max()), int(my.max())],
                          visible_crescent_px=int(vis.sum()), measured_px=int(meas.sum()), visible_box=[int(vx.min()), int(vy.min()), int(vx.max()), int(vy.max())],
                          split_sigma=SPLIT, grain_calibration_k=round(k, 3), **flog),
               covered_wood=dict(px=int(under.sum()), luma_min_max=[round(float(Lv3[under].min()), 1), round(float(Lv3[under].max()), 1)],
                                 saturated_red_px=int((under & (rr > 120) & (gg < 50) & (bb < 60)).sum()),
                                 bright_px_over_120=int((under & (Lv3 > 120)).sum())),
               texture=dict(visible_crescent_vs_ring=texture_stats(back, meas, excl), tiles_12px=tile_stats(back, meas, excl),
                            seam=seam(back, M, A2), before_calibration=dict(ring=t1, tiles=tl1),
                            natural_untouched_surface_same_shape=control(img, meas, excl, disc)),
               changed_px_in_memory=int(changed.sum()),
               changed_box=[int(cx_.min()), int(cy_.min()), int(cx_.max()), int(cy_.max())],
               changed_px_outside_zone_in_memory=int((changed & outside).sum()),
               max_diff_outside_zone=int(dif[outside].max()), mean_diff_outside_zone=round(float(dif[outside].mean()), 3),
               p999_diff_outside_zone=int(np.percentile(dif[outside], 99.9)),
               max_diff_outside_zone_plain_reencode_of_v3=int(reenc[outside].max()),
               max_diff_inside_zone=int(dif[~outside].max()))
    views(img, back)
    json.dump(rep, open(f"{WORK}/v4_report{'_final' if write else ''}.json", "w"), indent=1)
    print(json.dumps(rep))

if __name__ == "__main__":
    main("--write" in sys.argv)
