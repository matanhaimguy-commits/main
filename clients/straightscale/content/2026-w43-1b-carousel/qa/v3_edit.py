#!/usr/bin/env python3
"""StraightScale 2026-w43-1b carousel, v3: remove the logo the image model drew in the bottom-left corner of each
slide and paste the real logo at ONE fixed box on all 7 slides. Code only (PIL, numpy, OpenCV); no generation.

  python3 v3_edit.py [--write] [SL01 SL02 ...]

Per slide:
 1. Mask = the drawn logo's own pixels: red rounded square + gold square (convex hulls of their colour components)
    and the white wordmark letters (min channel > 105, blue > 110), each dilated by a small measured margin
    (inner mask, replaced by the fill: red square +7 px, gold square +4 px, letters +4 px, counters/slivers < 60 px
    closed). Outside that, a thin halo ring (gold 4..7 px, letters 4..8 px) holds the drawn logo's JPEG ringing; it
    keeps its low-pass (the real surface) and only its high-pass (the ringing) is replaced by surface grain. Warm
    highlights (table-edge beads) in the ring, and the lit table edge in the gold's ring, are protected and stay
    original.
 2. Inner fill: for each mask component, a donor = the same surface shifted ALONG the wood grain (structure-tensor
    angle, +-12 deg), offset chosen by the best colour match on an 8 px band around the component. Fill =
    donor x exp(C), where C is a harmonic (Laplace) membrane of the log-ratio low-pass(original)/low-pass(donor) on
    that band: the donor supplies the high-pass texture layer, the inpainted membrane supplies brightness/colour.
 3. Halo ring: low-pass (sigma 1.5, normalised, from the surface) + high-pass grain copied from just outside the
    halo along the outward normal.
 4. Real logo /home/user/brand/straightscale-logo-light.png, cropped to its alpha box, width 295 px, aspect kept,
    top-left (98, 1233), alpha composite.
 5. Only pixels in the mask/halo and under the logo change; everything else is copied back from the original
    before the JPEG (q93, 4:4:4) is written.

v3.1 (this file; 2026-10-18 rerun after the cut-off run of 2026-10-16, same method, three local fixes found at 4-6x):
 - the small gold square is replaced to +4 px only (red square still +7); its 4..7 px ring is de-rung like the
   letters' halo, and the part of that ring lying on the lit table edge stays original (SL05: the edge glow runs
   right beside the drawn gold square and the +7 px fill had redrawn it darker, a visible dark crescent);
 - the table-edge continuation inside the square's fill runs along the measured grain/edge angle (structure tensor)
   instead of a PCA of bright pixels (pulled ~9 deg flat by a bead), covers the edge's whole cross-profile
   (+8 px around the predicted lit part) and is feathered by distance from the rest of the component, not by
   brightness;
 - output JPEG is 4:4:4 (was 4:2:0) and the --write path is /home/user/drafts/fixed/<id8>_v3.jpg.
"""
import sys, json
import numpy as np, cv2
from PIL import Image

DRAFTS = "/home/user/drafts"
LOGO = "/home/user/brand/straightscale-logo-light.png"
WORK = "/home/user/w43v3qa"
SL = [["SL01","5d6ecdb0","5d6ecdb0-079b-4b2b-bf4a-56ec861f1a49"],["SL02","7e155c0b","7e155c0b-3f7a-4e1c-9235-b2b9746f6b9a"],
      ["SL03","3cdfd95e","3cdfd95e-3e25-416f-92db-f864a75bc004"],["SL04","26e094bc","26e094bc-4d29-4232-a21d-f8e80364cadb"],
      ["SL05","177e27a4","177e27a4-fb75-455e-8ddc-8e5c37e6a305"],["SL06","b6ed170a","b6ed170a-3479-4798-9168-1b55ca081961"],
      ["SL07","78eb641f","78eb641f-0675-43ce-a218-5d044c794616"]]
LOGO_X, LOGO_Y, LOGO_W = 98, 1233, 295
ZONE = (0, 1120, 560, 1350)          # x0, y0, x1, y1: everything outside must equal the original (JPEG noise only)
INNER = {"square": 3, "wordmark": 4, "gold": 4}
HALO = {"square": 7, "wordmark": 8}
BAND = 8
EDGE_GROW, EDGE_FEATHER = 8, 5.0   # table-edge continuation inside the square's fill (v3.1)

def disk(r): return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2*r+1, 2*r+1))
def dil(m, r): return cv2.dilate(m.astype(np.uint8), disk(r)) > 0 if r > 0 else m.astype(bool)
def hull_fill(m):
    out = np.zeros(m.shape, np.uint8); ys, xs = np.nonzero(m)
    if len(xs) >= 3: cv2.fillConvexPoly(out, cv2.convexHull(np.stack([xs, ys], 1).astype(np.int32)), 1)
    return out > 0

# ---------------------------------------------------------------- 1. masks
def logo_parts(img):
    H, W = img.shape[:2]
    b, g, r = [img[:, :, k].astype(int) for k in range(3)]
    zone = np.zeros((H, W), bool); zone[1130:1340, 60:480] = True
    red = zone & (r > 110) & (r > 1.8*g) & (r > 1.8*b)
    n, lab, st, _ = cv2.connectedComponentsWithStats(red.astype(np.uint8))
    k = max([k for k in range(1, n) if 1200 < st[k, 4] < 4000 and 40 < st[k, 2] < 70 and 40 < st[k, 3] < 70], key=lambda k: st[k, 4])
    rx, ry, rw, rh, _ = st[k]; rx1, ry1 = rx+rw-1, ry+rh-1
    sq = hull_fill(lab == k)
    gz = np.zeros((H, W), bool); gz[ry-10:ry+22, rx1-16:rx1+14] = True
    goldc = gz & (r > 140) & (g > 80) & (b < 120) & (r-b > 60) & ~sq
    n2, lab2, st2, _ = cv2.connectedComponentsWithStats(goldc.astype(np.uint8))
    gold = hull_fill(lab2 == 1+np.argmax(st2[1:, 4])) if n2 > 1 else np.zeros((H, W), bool)
    wz = np.zeros((H, W), bool); wz[ry-4:ry1+6, rx1+12:rx1+250] = True
    mn = np.minimum(np.minimum(r, g), b)
    letters = wz & (mn > 105) & (b > 110)
    n3, lab3, st3, _ = cv2.connectedComponentsWithStats(letters.astype(np.uint8))
    keep = np.isin(lab3, [k3 for k3 in range(1, n3) if st3[k3, 4] >= 6])
    return {"square": sq | gold, "wordmark": keep, "gold": gold}, dict(square=[int(rx), int(ry), int(rx1), int(ry1)])

def close_slivers(m, max_px=60):
    n4, lab4, st4, _ = cv2.connectedComponentsWithStats((~m).astype(np.uint8), connectivity=4)
    small = [k for k in range(1, n4) if st4[k, 4] < max_px]
    return m | np.isin(lab4, small)

def halo_profile(img, part, core):
    """fine-scale high-pass std by distance from the drawn shape: the logo's ringing raises it near its edges."""
    L = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
    hp = L - cv2.GaussianBlur(L, (0, 0), 1.0)
    dist = cv2.distanceTransform((~part).astype(np.uint8), cv2.DIST_L2, 5)
    near = dil(part, 16) & ~core
    prof = [float(hp[near & (dist >= d) & (dist < d+1)].std()) for d in range(1, 15)]
    plateau = float(np.median(prof[9:14]))
    rad = next((d for d in range(3, 10) if prof[d-1] <= 1.6*plateau), 9)
    return rad, [round(p, 2) for p in prof], round(plateau, 2)

def nblur(x, valid, sig):
    """Gaussian low-pass using only valid pixels (normalised convolution), so the drawn logo never leaks in."""
    w = valid.astype(np.float32); den = cv2.GaussianBlur(w, (0, 0), sig) + 1e-6
    if x.ndim == 2: return cv2.GaussianBlur(x*w, (0, 0), sig)/den
    return np.stack([cv2.GaussianBlur(x[..., c]*w, (0, 0), sig)/den for c in range(x.shape[2])], 2)

def directional_fill(I, allm, E, Lo, bright, reach=60.0, ang=None):
    """fill E by interpolating along the local line direction: each pixel takes the two nearest untouched pixels
    along that line, weighted by distance. v3.1: the direction is the measured grain/edge angle (structure tensor
    around the mask; it matches a ridge fit of the lit edge within ~1 deg); the old PCA of bright pixels (fallback)
    was pulled ~9 deg flat by the bright bead above the edge and shifted the continued glow sideways."""
    H, W = allm.shape
    pts = dil(E, 25) & ~allm & (cv2.GaussianBlur(Lo, (0, 0), 1.0) > bright)
    py, px = np.nonzero(pts)
    if ang is not None:
        d = np.array([np.cos(np.radians(ang)), np.sin(np.radians(ang))])
    elif len(px) >= 20:
        c = np.cov(np.stack([px, py]).astype(np.float64)); w, v = np.linalg.eigh(c); d = v[:, -1]
    else:
        d = np.array([np.cos(np.radians(55)), np.sin(np.radians(55))])
    Ib = cv2.GaussianBlur(I, (0, 0), 0.8)
    ys, xs = np.nonzero(E)
    out = I.copy()
    vals = []; dists = []
    for sgn in (1, -1):
        hit_t = np.full(len(xs), np.nan)
        for t in np.arange(0.5, reach, 0.5):
            qx = np.round(xs + sgn*t*d[0]).astype(int); qy = np.round(ys + sgn*t*d[1]).astype(int)
            inside = (qx >= 0) & (qx < W) & (qy >= 0) & (qy < H)
            free = np.zeros(len(xs), bool); free[inside] = ~allm[qy[inside], qx[inside]]
            new = free & np.isnan(hit_t); hit_t[new] = t
        qx = np.clip(np.round(xs + sgn*np.nan_to_num(hit_t)*d[0]).astype(int), 0, W-1)
        qy = np.clip(np.round(ys + sgn*np.nan_to_num(hit_t)*d[1]).astype(int), 0, H-1)
        vals.append(Ib[qy, qx]); dists.append(hit_t)
    t1, t2 = dists
    w1 = np.where(np.isnan(t1), 0, 1/np.maximum(np.nan_to_num(t1), 0.5)); w2 = np.where(np.isnan(t2), 0, 1/np.maximum(np.nan_to_num(t2), 0.5))
    tot = np.maximum(w1 + w2, 1e-6)
    out[ys, xs] = (vals[0]*w1[:, None] + vals[1]*w2[:, None]) / tot[:, None]
    return out

def build_masks(img):
    parts, info = logo_parts(img)
    core = parts["square"] | parts["wordmark"]
    b, g, r = [img[:, :, k].astype(int) for k in range(3)]
    L = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
    outer = close_slivers(dil(parts["square"], HALO["square"]) | dil(parts["wordmark"], HALO["wordmark"]))
    # warm highlights (table-edge beads, glints) more than 3 px from the drawn shapes stay original: bright, warm
    # and well above the local surface level (low-pass of the surface around the logo)
    surf = nblur(L, ~dil(core, HALO["wordmark"]), 6.0)
    far = ~dil(core, 3)
    protect = far & outer & (L > 38) & ((r-b) > 30) & (L > 1.6*surf)
    protect = dil(protect, 1) & far & outer
    # inner (replaced by the fill): square + gold with their whole halo (dark floor, filled from the boundary), letters
    # +4 px; the letters' outer halo ring (4..8 px) keeps its low-pass and only loses the ringing (dering)
    # v3.1: the small gold square is replaced to +4 px only; its 4..7 px ring joins the halo (keeps its low-pass, loses
    # only the ringing), so the lit table edge that runs right beside it (SL05) is not swallowed and re-drawn darker
    redsq = parts["square"] & ~parts["gold"]
    # ... and where that ring lies on the lit table edge (low-pass above 1.8x the floor around the square + 2) it stays
    # original: the edge's own beads are not ringing, and re-graining them leaves dark specks
    Llp = cv2.GaussianBlur(L, (0, 0), 2.0)
    sqring = dil(parts["square"], 14) & ~dil(parts["square"], 8) & ~dil(parts["wordmark"], HALO["wordmark"])
    lit_thr = 1.8*float(np.median(Llp[sqring])) + 2
    gring = dil(parts["gold"], HALO["square"]) & ~dil(parts["gold"], INNER["gold"]) & ~dil(redsq, HALO["square"]) & ~dil(parts["wordmark"], HALO["wordmark"])
    lit = gring & (Llp > lit_thr)
    protect = protect | lit
    info["gold_ring_lit_kept_px"] = int(lit.sum())
    inner = close_slivers(dil(redsq, HALO["square"]) | dil(parts["gold"], INNER["gold"]) | dil(parts["wordmark"], INNER["wordmark"])) & ~protect
    halo = outer & ~inner & ~protect
    info["halo_measured"] = {nm: halo_profile(img, parts[nm], core)[0] for nm in ("square", "wordmark")}
    info.update(core_px=int(core.sum()), inner_px=int(inner.sum()), halo_px=int(halo.sum()), protected_px=int(protect.sum()))
    ys, xs = np.nonzero(inner | halo); info["changed_box"] = [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]
    return parts, core, inner, halo, info

# ---------------------------------------------------------------- 2. inner fill
def grain_angle(img, M):
    L = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
    Lb = cv2.GaussianBlur(L, (0, 0), 1.5)
    gx = cv2.Sobel(Lb, cv2.CV_32F, 1, 0, ksize=3); gy = cv2.Sobel(Lb, cv2.CV_32F, 0, 1, ksize=3)
    ring = dil(M, 30) & ~dil(M, 4)
    Jxx = (gx*gx)[ring].sum(); Jyy = (gy*gy)[ring].sum(); Jxy = (gx*gy)[ring].sum()
    return float(np.degrees(0.5*np.arctan2(2*Jxy, Jxx-Jyy) + np.pi/2) % 180)

def find_offset(I, If, inner, allm, Mc, grain, P=None, ang_tol=12, step=2, lam=0.03, w_mean=0.2, w_std=15.0, w_chroma=20.0, w_pred=1.0, w_ang=0.15, around=None):
    """donor offset along the grain: best colour match on the band around the component (blurred, sigma 1), plus
    terms that keep the donor's own brightness and grain level close to the band's, and no foreign objects
    (saturated red, e.g. the phone case on slide 1) unless the band has them too."""
    H, W = Mc.shape
    band = dil(Mc, BAND) & ~allm
    by, bx = np.nonzero(band)
    fy, fx = np.nonzero(dil(Mc, BAND+2)); forb = dil(inner, 2)          # donor band footprint: clear of the inner mask
    iy, ix = np.nonzero(Mc); forb2 = allm                               # donor interior: clear of the whole logo + halo
    L = cv2.cvtColor(np.clip(I, 0, 255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float32)
    hp = L - cv2.GaussianBlur(L, (0, 0), 2.0)
    b, g, r = I[..., 0], I[..., 1], I[..., 2]
    redobj = (r > 50) & (r > 3.2*g) & (r > 3.2*b)                       # crimson objects (phone case), not orange wood
    chroma = np.log((r+3)/(g+3))                                        # warm-brown wood/floor vs red objects
    ref = dil(Mc, BAND+8) & ~dil(allm, 4)                               # reference surface, clear of the logo's ringing
    bmean = float(L[ref].mean()); bstd = float(hp[ref].std()); band_red = int(redobj[band].sum())
    bchroma = float(chroma[ref].mean())
    # prediction of the hidden surface from its boundary (harmonic low-pass): donors whose own low-pass inside
    # disagrees with it (an object, a reflection, a different surface) are penalised
    Llp = cv2.GaussianBlur(L, (0, 0), 3.0)
    Pi = P[iy, ix] if P is not None else None
    best = None
    rx = range(-200, 201, step) if around is None else range(around[0]-3, around[0]+4)
    ry = range(-170, 91, step) if around is None else range(around[1]-3, around[1]+4)
    for dy in ry:
        for dx in rx:
            if abs(dx) < 4 and abs(dy) < 4: continue
            ang = np.degrees(np.arctan2(dy, dx)) % 180
            if min(abs(ang-grain), 180-abs(ang-grain)) > ang_tol: continue
            yy, xx = fy+dy, fx+dx
            if yy.min() < 0 or yy.max() >= H-4 or xx.min() < 4 or xx.max() >= W-4: continue
            if forb[yy, xx].any() or forb2[iy+dy, ix+dx].any(): continue
            if redobj[yy, xx].sum() > band_red + 5: continue
            d = If[by, bx] - If[by+dy, bx+dx]
            dm = float(L[iy+dy, ix+dx].mean()) - bmean
            ds = np.log((float(hp[iy+dy, ix+dx].std())+0.1)/(bstd+0.1))
            dc = float(chroma[iy+dy, ix+dx].mean()) - bchroma
            mse = float((d*d).mean())
            pe = 0.0
            if Pi is not None:
                Dl = Llp[iy+dy, ix+dx]
                pe = float(((Dl*(Pi.mean()+1)/(Dl.mean()+1) - Pi)**2).mean())
            dev = min(abs(ang-grain), 180-abs(ang-grain))
            c = mse + lam*(dx*dx+dy*dy)**0.5 + w_mean*dm*dm + w_std*ds*ds + w_chroma*dc*dc + w_pred*pe + w_ang*dev
            if best is None or c < best[0]: best = (c, dx, dy, mse, dm, ds, dc, pe)
    return best

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

def fill_inner(img, inner, allm, sqpart=None, split=2.5):
    grain = grain_angle(img, inner)
    I = img.astype(np.float32)
    If = cv2.GaussianBlur(I, (0, 0), 1.0)
    n, lab = cv2.connectedComponents(inner.astype(np.uint8))
    out = I.copy(); log = []
    for k in range(1, n):
        Mc = lab == k
        band = dil(Mc, BAND) & ~allm
        S = (Mc | (allm & dil(Mc, BAND))) & ~band
        Lo = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
        P = membrane(nblur(Lo, ~allm, 3.0)[..., None], S, band, iters=600)[..., 0]
        for tol in (25, 45, 90):              # along the grain first (w_ang), wider only if nothing clean is found
            b = find_offset(I, If, inner, allm, Mc, grain, P=P, ang_tol=tol)
            if b: break
        b = find_offset(I, If, inner, allm, Mc, grain, P=P, around=(b[1], b[2]), ang_tol=90) or b
        _, dx, dy = b[:3]
        ys, xs = np.nonzero(dil(Mc, BAND+2))
        D = np.zeros_like(I); D[ys, xs] = I[ys+dy, xs+dx]
        band = dil(Mc, BAND) & ~allm
        eps = 3.0; w = band.astype(np.float32); nw = cv2.GaussianBlur(w, (0, 0), 3)
        lr = np.zeros_like(I)
        for ch in range(3):
            nI = cv2.GaussianBlur(I[..., ch]*w, (0, 0), 3); nD = cv2.GaussianBlur(D[..., ch]*w, (0, 0), 3)
            lr[..., ch] = np.log((nI+eps*nw+1e-6)/(nD+eps*nw+1e-6))
        S = (Mc | (allm & dil(Mc, BAND))) & ~band     # solve over the component and the halo ring that separates it from the band
        C = membrane(lr, S, band)
        fillv = (D+eps)*np.exp(C)-eps
        # texture layer: scale the donor's high-pass so its (robust) grain level matches the surrounding surface
        ref = dil(Mc, BAND+8) & ~dil(allm, 4)
        Lo = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
        hpo = Lo - cv2.GaussianBlur(Lo, (0, 0), 2.0)
        lpf = np.stack([cv2.GaussianBlur(fillv[..., c], (0, 0), 2.0) for c in range(3)], 2)
        hpf = fillv - lpf
        Lh = hpf @ np.array([0.114, 0.587, 0.299], np.float32)
        rstd = lambda v: 1.4826*float(np.median(np.abs(v-np.median(v))))
        kt = float(np.clip(rstd(hpo[ref]) / max(1e-3, rstd(Lh[Mc])), 0.6, 1.6))
        fillv = lpf + kt*hpf
        lp_mode = "donor"
        if sqpart is not None and (Mc & sqpart).any():
            # dark floor under the drawn square: low frequencies from the harmonic prediction of the boundary and
            # only the donor's fine grain (high-pass, sigma 2.5) on top, so no donor shapes (reflections, streaks,
            # pillar edges) come along ...
            comp = I.copy(); comp[Mc] = fillv[Mc]
            hpc = comp - np.stack([cv2.GaussianBlur(comp[..., c], (0, 0), split) for c in range(3)], 2)
            Lh = hpc @ np.array([0.114, 0.587, 0.299], np.float32)
            hpo2 = Lo - cv2.GaussianBlur(Lo, (0, 0), split)
            kt = float(np.clip(rstd(hpo2[ref]) / max(1e-3, rstd(Lh[Mc])), 0.6, 1.6))
            lim = 3.0*rstd(hpo2[ref]) / kt
            hpc = np.clip(hpc, -lim, lim)                      # no outlier specks from the donor's grain
            fm = float(np.median(nblur(Lo, ~allm, 2.0)[band])); thr = 1.8*fm + 2
            field = nblur(I, ~allm, split)
            fl = field @ np.array([0.114, 0.587, 0.299], np.float32)
            field = field*np.minimum(1.0, thr/np.maximum(fl, 1e-3))[..., None]   # the floor estimate ignores the lit edge
            Pc = membrane(field, S, band)
            B = Pc + kt*hpc
            lp_mode = "boundary-harmonic + donor fine grain"
            # ... except where the lit table edge (bright beads) runs through the square's corner: there a short
            # donor taken along that edge continues it, blended in by its own brightness
            E0 = Mc & (P > thr)
            if E0.sum() >= 30:
                # v3.1: the continuation covers the edge's whole cross-profile (glow and its dark flank), and its
                # weight falls off with the distance from the rest of the component, not with brightness, so no
                # dark crescent is left where the glow fades into the floor (seen on SL05 at 4x)
                E = dil(E0, EDGE_GROW) & Mc
                A = directional_fill(I, allm, E, Lo, max(thr, 2.5*fm), ang=grain) + kt*hpc
                rest = Mc & ~E
                dE = cv2.distanceTransform((~rest).astype(np.uint8), cv2.DIST_L2, 5) if rest.any() else np.full(Mc.shape, 99, np.float32)
                wA = np.clip(dE/EDGE_FEATHER, 0, 1)*E
                wA = cv2.GaussianBlur(wA.astype(np.float32), (0, 0), 1.0)*E
                B = wA[..., None]*A + (1-wA[..., None])*B
                lp_mode += f"; table-edge corner {int(E.sum())} px continued along the edge line"
            fillv = B
        out[Mc] = fillv[Mc]
        log.append(dict(part_px=int(Mc.sum()), donor_dx=int(dx), donor_dy=int(dy), band_mse=round(b[3], 1),
                        donor_minus_band_mean=round(b[4], 1), donor_vs_band_grain=round(float(np.exp(b[5])), 2),
                        donor_minus_band_redness=round(b[6], 2), prediction_mse=round(b[7], 1), texture_gain=round(kt, 2), low_pass=lp_mode))
    return out, log, round(grain, 1)

# ---------------------------------------------------------------- 3. halo ring
def dering(cur, core, inner, halo, allm, sig=1.5, reach=10):
    I = cur.astype(np.float32)
    lp = np.stack([cv2.GaussianBlur(I[..., c], (0, 0), sig) for c in range(3)], 2)
    hp = I - lp
    dist = cv2.distanceTransform((~core).astype(np.uint8), cv2.DIST_L2, 5)
    gy, gx = np.gradient(cv2.GaussianBlur(dist, (0, 0), 1.0))
    nrm = np.sqrt(gx**2+gy**2)+1e-6; gx /= nrm; gy /= nrm
    ys, xs = np.nonzero(halo)
    H, W = halo.shape
    out = I.copy()
    done = np.zeros(len(ys), bool); clear = ~dil(allm, 2)
    # v3.1: the copied grain is clipped to +-2.5 robust std of the clear surface's grain, so a bead or glint that the
    # outward sample happens to land on is not stamped into the ring as a speck
    hl = hp @ np.array([0.114, 0.587, 0.299], np.float32)
    ref = dil(allm, 14) & clear
    lim = 2.5*1.4826*float(np.median(np.abs(hl[ref] - np.median(hl[ref]))))
    hp = hp * np.minimum(1.0, lim/np.maximum(np.abs(hl), 1e-3))[..., None]
    for step in (reach, reach+4, reach+8, reach+14):
        qy = np.clip(np.round(ys + gy[ys, xs]*step).astype(int), 0, H-1)
        qx = np.clip(np.round(xs + gx[ys, xs]*step).astype(int), 0, W-1)
        sel = clear[qy, qx] & ~done
        out[ys[sel], xs[sel]] = lp[ys[sel], xs[sel]] + hp[qy[sel], qx[sel]]   # surface low-pass + clean grain
        done |= sel
    out[ys[~done], xs[~done]] = lp[ys[~done], xs[~done]]
    return out, dict(regrained=int(done.sum()), lowpass_only=int((~done).sum()))

# ---------------------------------------------------------------- 4. logo
def load_logo():
    lg = Image.open(LOGO).convert("RGBA"); lg = lg.crop(lg.getbbox(alpha_only=True))
    lh = round(lg.height*LOGO_W/lg.width)
    return lg.resize((LOGO_W, lh), Image.LANCZOS)

def paste(bgr, logo):
    im = Image.fromarray(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)).convert("RGBA")
    im.alpha_composite(logo, (LOGO_X, LOGO_Y))
    return cv2.cvtColor(np.array(im.convert("RGB")), cv2.COLOR_RGB2BGR)

# ---------------------------------------------------------------- metrics
def texture_stats(img, M, ring_in=3, ring_out=15, sig=2.0, excl=None):
    L = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
    hp = L - cv2.GaussianBlur(L, (0, 0), sig)
    ring = dil(M, ring_out) & ~dil(M if excl is None else excl, ring_in)
    return dict(in_mean=round(float(L[M].mean()), 1), ring_mean=round(float(L[ring].mean()), 1),
                in_std=round(float(hp[M].std()), 2), ring_std=round(float(hp[ring].std()), 2),
                in_rstd=round(rstd(hp[M]), 2), ring_rstd=round(rstd(hp[ring]), 2))

def rstd(v):
    """robust std (1.4826 x median absolute deviation): the grain level without the few lit beads / glints."""
    return float(1.4826*np.median(np.abs(v - np.median(v))))

def verdict(t, std_tol=0.25, mean_tol=4.0):
    r = t["in_std"]/max(1e-6, t["ring_std"]); d = t["in_mean"] - t["ring_mean"]
    return dict(std_ratio=round(r, 2), mean_diff=round(d, 1), ok=bool(abs(r-1) <= std_tol and abs(d) <= mean_tol))

def texture_stats_same_surface(img, M, ring_in=3, ring_out=15, sig=2.0, excl=None):
    """same numbers with the lit table-edge highlights (low-pass > 1.8x the ring's median + 2) left out of BOTH the
    filled area and the ring, so a ring that clips the beaded edge is compared like for like."""
    L = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
    hp = L - cv2.GaussianBlur(L, (0, 0), sig)
    Llp = cv2.GaussianBlur(L, (0, 0), 2.0)
    ring = dil(M, ring_out) & ~dil(M if excl is None else excl, ring_in)
    thr = 1.8*float(np.median(Llp[ring])) + 2
    rs, ms = ring & (Llp <= thr), M & (Llp <= thr)
    return dict(in_mean=round(float(L[ms].mean()), 1), ring_mean=round(float(L[rs].mean()), 1),
                in_std=round(float(hp[ms].std()), 2), ring_std=round(float(hp[rs].std()), 2),
                highlights_left_out_pct=[round(100*float(1-ms.sum()/M.sum()), 1), round(100*float(1-rs.sum()/ring.sum()), 1)])

def arrow_centre(img):
    b, g, r = [img[:, :, k].astype(int) for k in range(3)]
    z = np.zeros(r.shape, bool); z[1170:1345, 880:1075] = True
    red = z & (r > 140) & (r > 2*g) & (r > 2*b)
    n, lab, st, _ = cv2.connectedComponentsWithStats(red.astype(np.uint8))
    if n < 2: return None
    k = 1+int(np.argmax(st[1:, 4]))
    if st[k, 4] < 1500: return None
    cnts, _ = cv2.findContours((lab == k).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    (cx, cy), rad = cv2.minEnclosingCircle(max(cnts, key=cv2.contourArea))
    return [round(cx, 1), round(cy, 1), round(rad, 1)]

def tile_stats(img, changed, tile=24, grow=20, sig=2.0, min_px=80):
    """local version: per 24 px tile of the filled area, filled pixels vs untouched pixels within 20 px of the tile."""
    L = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)
    hp = L - cv2.GaussianBlur(L, (0, 0), sig)
    clear = ~dil(changed, 3)
    H, W = changed.shape
    ys, xs = np.nonzero(changed)
    rows = []
    for ty in range(ys.min()//tile*tile, ys.max()+1, tile):
        for tx in range(xs.min()//tile*tile, xs.max()+1, tile):
            ins = np.zeros_like(changed); ins[ty:ty+tile, tx:tx+tile] = True; ins &= changed
            if ins.sum() < min_px: continue
            win = np.zeros_like(changed); win[max(0, ty-grow):ty+tile+grow, max(0, tx-grow):tx+tile+grow] = True
            outs = win & clear
            if outs.sum() < min_px: continue
            rows.append((float(L[ins].mean()-L[outs].mean()), float(hp[ins].std()/max(1e-6, hp[outs].std()))))
    d = np.array([r[0] for r in rows]); q = np.array([r[1] for r in rows])
    return dict(tiles=len(rows), median_abs_dmean=round(float(np.median(np.abs(d))), 2), max_abs_dmean=round(float(np.abs(d).max()), 2),
                median_std_ratio=round(float(np.median(q)), 2), std_ratio_p10_p90=[round(float(np.percentile(q, 10)), 2), round(float(np.percentile(q, 90)), 2)])

def process(a, i8, full, write=False):
    img = cv2.imread(f"{DRAFTS}/{full}.jpg")
    parts, core, inner, halo, minfo = build_masks(img)
    allm = inner | halo
    cur, flog, grain = fill_inner(img, inner, allm, sqpart=parts["square"])
    cur, nder = dering(cur, core, inner, halo, allm)
    clean = np.clip(np.round(cur), 0, 255).astype(np.uint8)
    changed = inner | halo
    clean[~changed] = img[~changed]
    logo = load_logo()
    final = paste(clean, logo)
    lbox = [LOGO_X, LOGO_Y, LOGO_X+logo.width, LOGO_Y+logo.height]
    lalpha = np.zeros(changed.shape, bool); lalpha[LOGO_Y:LOGO_Y+logo.height, LOGO_X:LOGO_X+logo.width] = np.array(logo.split()[3]) > 0
    # texture numbers: the whole filled area before the logo, per part, and what stays visible after the logo
    n, lab = cv2.connectedComponents(changed.astype(np.uint8))
    per = []
    for k in range(1, n):
        Mc = lab == k
        if Mc.sum() < 200: continue
        per.append(dict(part="square" if (Mc & parts["square"]).any() else "wordmark", px=int(Mc.sum()),
                        ring=texture_stats(clean, Mc, excl=changed), same_surface=texture_stats_same_surface(clean, Mc, excl=changed)))
    vis = changed & ~dil(lalpha, 2)
    logo_rect = np.zeros(changed.shape, bool); logo_rect[LOGO_Y:LOGO_Y+logo.height, LOGO_X:LOGO_X+logo.width] = True
    st = dict(fill_before_logo=texture_stats(clean, changed), fill_before_logo_same_surface=texture_stats_same_surface(clean, changed), parts=per,
              local_tiles=tile_stats(clean, changed),
              visible_after_logo=dict(px=int(vis.sum()), **texture_stats(clean, vis, excl=changed | dil(lalpha, 2))))
    st["targets"] = dict(rule="hp std (img - gauss sigma 2) within 25%, mean within 4 levels, fill vs 3..15 px ring",
                         plain=verdict(st["fill_before_logo"]), same_surface=verdict(st["fill_before_logo_same_surface"]),
                         plain_robust_std_ratio=round(st["fill_before_logo"]["in_rstd"]/max(1e-6, st["fill_before_logo"]["ring_rstd"]), 2))
    out_path = f"{DRAFTS}/fixed/{i8}_v3.jpg" if write else f"{WORK}/final/{i8}_v3.jpg"
    cv2.imwrite(f"{WORK}/clean_{i8}.png", clean)
    Image.fromarray(cv2.cvtColor(final, cv2.COLOR_BGR2RGB)).save(out_path, quality=93, subsampling="4:4:4")
    # change check on the written JPEG
    back = cv2.imread(out_path).astype(int); o = img.astype(int)
    x0, y0, x1, y1 = ZONE
    outside = np.ones(changed.shape, bool); outside[y0:y1, x0:x1] = False
    dif = np.abs(back-o).max(2)
    ref = cv2.imread(f"{DRAFTS}/{full}.jpg"); Image.fromarray(cv2.cvtColor(ref, cv2.COLOR_BGR2RGB)).save(f"{WORK}/reenc_{i8}.jpg", quality=93, subsampling="4:4:4")
    reenc = np.abs(cv2.imread(f"{WORK}/reenc_{i8}.jpg").astype(int)-o).max(2)
    arrow = arrow_centre(img)
    logo_cy = LOGO_Y + (logo.height-1)/2
    placement = dict(logo_centre_y=logo_cy, arrow=arrow, arrow_minus_logo_centre_y=None if arrow is None else round(arrow[1]-logo_cy, 1),
                     drawn_logo_px_under_logo_box=round(float(core[logo_rect].sum()/core.sum()), 3),
                     drawn_logo_box=[int(v) for v in (np.nonzero(core)[1].min(), np.nonzero(core)[0].min(), np.nonzero(core)[1].max(), np.nonzero(core)[0].max())],
                     filled_px_hidden_by_logo=round(float((changed & lalpha).sum()/changed.sum()), 3))
    rep = dict(asset=a, id8=i8, path=out_path, grain_deg=grain, mask=minfo, donors=flog, halo_dering_px=nder, logo_box=lbox,
               placement=placement,
               logo_size=[logo.width, logo.height], texture=st,
               max_diff_outside_zone=int(dif[outside].max()), mean_diff_outside_zone=round(float(dif[outside].mean()), 3),
               max_diff_outside_zone_plain_reencode=int(reenc[outside].max()),
               pixels_changed_in_memory_outside_mask_and_logo=int((np.abs(final.astype(int)-o).max(2)[~(changed | logo_rect)] > 0).sum()))
    return rep, img, clean, final

if __name__ == "__main__":
    args = [x for x in sys.argv[1:] if not x.startswith("--")]
    write = "--write" in sys.argv
    reps = []
    for a, i8, full in SL:
        if args and a not in args: continue
        rep, *_ = process(a, i8, full, write)
        reps.append(rep); print(json.dumps(rep), flush=True)
    json.dump(reps, open(f"{WORK}/report{'_final' if write else ''}.json", "w"), indent=1)
