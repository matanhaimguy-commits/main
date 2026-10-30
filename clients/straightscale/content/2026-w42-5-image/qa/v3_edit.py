"""IMG-W42-5 (2026-w42-5-image) v3 = v2 + three local code-only fixes (VISUAL-QA 5.5 route: paint-out / local edit).
No image generation. Inputs (Higgsfield sandbox):
  ORIG  /home/user/drafts/dd845791-e322-4bc7-a53d-11c66de474db.jpg   model output (has the drawn fake logo)
  V2    /home/user/drafts/fixed/dd845791.jpg                         drawn logo inpainted (fixlogo2.py) + real logo pasted
  LOGO  /home/user/brand/straightscale-logo-light.png                real logo (pasted at x=100,y=1219, 291x54)
Output: /home/user/drafts/fixed/dd845791_v3.jpg (1080x1350, JPEG q93, 4:4:4)

Fix 1 (V23): restore original counter-edge beads/grain inside v2's inpaint mask wherever the original pixel is not the
  drawn logo and the real logo's alpha is 0; on drawn-logo pixels keep a smooth fill and add matching texture copied
  from the untouched counter (Poisson fill: boundary = restored original, gradients = donor patch).
Fix 2 (V21): headline highlight box -> flat #B31217 (per-pixel unmix ivory / crimson / dark, swap only the crimson part).
Fix 3 (V11): soften pseudo-letters on defocused labels/stickers (glyph-excluding masked blur + faint ghost + matched grain).
"""
import numpy as np, cv2
from PIL import Image
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

ORIG = '/home/user/drafts/dd845791-e322-4bc7-a53d-11c66de474db.jpg'
V2 = '/home/user/drafts/fixed/dd845791.jpg'
LOGO = '/home/user/brand/straightscale-logo-light.png'
OUT = '/home/user/drafts/fixed/dd845791_v3.jpg'

def lum(a): return a[..., 0]*0.299 + a[..., 1]*0.587 + a[..., 2]*0.114

# ---------------------------------------------------------------- shared: v2 geometry (exact reproduction of fixlogo2.py)
def v2_inpaint_mask(o8bgr):
    img = o8bgr; H, W = img.shape[:2]
    b, g, r = [img[:, :, i].astype(int) for i in range(3)]
    zone = np.zeros((H, W), bool); zone[int(H*0.875):int(H*0.99), int(W*0.02):int(W*0.50)] = True
    white = zone & (r > 200) & (g > 200) & (b > 190) & ((np.maximum(np.maximum(r, g), b) - np.minimum(np.minimum(r, g), b)) < 40)
    ys, xs = np.nonzero(white); tx0, tx1, ty0, ty1 = xs.min(), xs.max(), ys.min(), ys.max()
    near = np.zeros((H, W), bool)
    near[max(0, ty0-int(H*0.04)):min(H, ty1+int(H*0.02)), max(0, tx0-int(W*0.12)):min(W, tx1+8)] = True
    red = near & (r > 120) & (r > 2*g) & (r > 2*b)
    gold = near & (r > 160) & (g > 90) & (g < 210) & (b < 100) & (r > b + 80)   # this also caught the two counter beads
    mask = (white | red | gold) & near
    mask = cv2.dilate(mask.astype(np.uint8)*255, np.ones((7, 7), np.uint8), iterations=2)
    clean = cv2.inpaint(img, mask, 9, cv2.INPAINT_TELEA)
    return mask > 0, white, cv2.cvtColor(clean, cv2.COLOR_BGR2RGB).astype(np.float32)

def logo_alpha(H, W):
    logo = Image.open(LOGO).convert('RGBA'); logo = logo.crop(logo.getbbox())
    lw = int(W*0.27); lh = int(logo.height*lw/logo.width)
    logo = logo.resize((lw, lh), Image.LANCZOS)
    A = np.zeros((H, W), np.float32); A[1219:1219+lh, 100:100+lw] = np.asarray(logo)[:, :, 3]/255.0
    return A

# ---------------------------------------------------------------- fix 1
def poisson_fill(base, donor, omega):
    ys, xs = np.nonzero(omega); n = len(ys)
    idx = -np.ones(omega.shape, np.int64); idx[ys, xs] = np.arange(n)
    rows, cols, vals = [], [], []
    bvec = np.zeros((n, 3), np.float64)
    for k, (y, x) in enumerate(zip(ys, xs)):
        rows.append(k); cols.append(k); vals.append(4.0)
        lap = 4*donor[y, x].astype(np.float64)
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            yy, xx = y+dy, x+dx
            lap -= donor[yy, xx]
            if omega[yy, xx]:
                rows.append(k); cols.append(idx[yy, xx]); vals.append(-1.0)
            else:
                bvec[k] += base[yy, xx]
        bvec[k] += lap
    Am = csr_matrix((vals, (rows, cols)), shape=(n, n))
    out = base.copy()
    for c in range(3):
        out[ys, xs, c] = spsolve(Am, bvec[:, c])
    return out

def shifted(img, dx, dy):
    H, W = img.shape[:2]; out = np.zeros_like(img)   # out[y,x] = img[y+dy, x+dx]
    out[max(0, -dy):H-max(0, dy), max(0, -dx):W-max(0, dx)] = img[max(0, dy):H-max(0, -dy), max(0, dx):W-max(0, -dx)]
    return out

def fix1(o, v, o8bgr):
    H, W = o.shape[:2]
    M, white, clean = v2_inpaint_mask(o8bgr)
    A = logo_alpha(H, W)
    L, Lc = lum(o), lum(clean)
    # D = drawn fake-logo pixels in the original (never restored)
    Dm = np.zeros((H, W), bool)
    Dm[1238-3:1293+4, 101-3:154+4] = True      # drawn red square (101..154 x 1238..1293) + 3 px
    Dm[1237-3:1246+4, 149-3:160+4] = True      # drawn gold square (149..160 x 1237..1246) + 3 px
    wb = np.zeros((H, W), bool); wb[1248:1292, 180:392] = True
    strong = white & wb                        # drawn wordmark letters (187..385 x 1256..1284)
    near5 = cv2.dilate(strong.astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))) > 0
    soft = near5 & wb & ((L - Lc) > 10)        # their anti-aliased edges
    Dw = cv2.dilate((strong | soft).astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))) > 0
    D = Dm | Dw
    Dmark = D & np.pad(np.ones((70, 70), bool), ((1230, H-1300), (95, W-165)))
    Dword = D & ~Dmark
    # background layer: original everywhere except D; D = Poisson fill with texture from untouched counter
    # donor offsets found by ring-SSD search over untouched original: mark <- (-92,-2) (dark front face to the left),
    # wordmark <- (+36,+40) (same counter edge, further down-right along the edge direction)
    BG = o.astype(np.float64).copy()
    for Dx, (dx, dy) in ((Dmark, (-92, -2)), (Dword, (36, 40))):
        BG = poisson_fill(BG, shifted(o.astype(np.float64), dx, dy), Dx)
    BG = np.clip(BG, 0, 255).astype(np.float32)
    chg = (M | D) & (A == 0)                   # only where the real logo is fully transparent
    out = v.copy(); out[chg] = BG[chg]
    info = dict(inpaint_mask_px=int(M.sum()), drawn_px=int(D.sum()),
                restored_original_px=int((M & ~D & (A == 0)).sum()), textured_fill_px=int((D & (A == 0)).sum()),
                changed_px=int(chg.sum()), box=[int(c) for c in (np.nonzero(chg)[1].min(), np.nonzero(chg)[0].min(),
                                                               np.nonzero(chg)[1].max(), np.nonzero(chg)[0].max())])
    return out, info

# ---------------------------------------------------------------- fix 2
def fix2(img, box=(82, 340, 668, 431), new_hex='#B31217'):
    img = img.copy(); x0, y0, x1, y1 = box
    sub = img[y0:y1, x0:x1].astype(np.float64)
    r, g, b = sub[..., 0], sub[..., 1], sub[..., 2]
    pure = (r > 120) & (g < 45) & (b < 50) & (r - g > 100)
    pure_e = cv2.erode(pure.astype(np.uint8), np.ones((3, 3), np.uint8)) > 0
    ivory = (r > 235) & (g > 225) & (b > 215)
    I = np.median(sub[cv2.erode(ivory.astype(np.uint8), np.ones((3, 3), np.uint8)) > 0], axis=0)
    ext = np.concatenate([img[y0-8:y0-3, x0:x1].reshape(-1, 3), img[y1+3:y1+8, x0:x1].reshape(-1, 3)]).astype(np.float64)
    Dk = np.median(ext, axis=0)
    def nblur(s):
        ws = cv2.GaussianBlur(pure_e.astype(np.float64), (0, 0), s)
        Cs = np.stack([cv2.GaussianBlur(sub[..., c]*pure_e, (0, 0), s) for c in range(3)], -1)/np.maximum(ws, 1e-6)[..., None]
        return Cs, ws
    C7, w7 = nblur(7.0); C25, _ = nblur(25.0)
    t = np.clip(w7/0.15, 0, 1)[..., None]; C = C7*t + C25*(1-t)          # local old crimson (the A31217 -> 901013 ramp)
    Cnew = np.array([int(new_hex[i:i+2], 16) for i in (1, 3, 5)], np.float64)
    # per-pixel unmix p = Dk + a*(I-Dk) + w*(C-Dk): a = ivory share, w = crimson share
    u = np.broadcast_to(I - Dk, sub.shape); q = C - Dk; pp = sub - Dk
    uu = (u*u).sum(-1); uq = (u*q).sum(-1); qq = (q*q).sum(-1); up = (u*pp).sum(-1); qp = (q*pp).sum(-1)
    det = uu*qq - uq*uq
    a = np.clip((qq*up - uq*qp)/det, 0, 1); w = np.clip((uu*qp - uq*up)/det, 0, 1)
    s = a + w; over = s > 1; a[over] /= s[over]; w[over] /= s[over]
    rec = sub + w[..., None]*(Cnew - C)                     # swap only the crimson share (letters + their AA untouched)
    f = np.clip((w - 0.85)/0.10, 0, 1)[..., None]            # pure box pixels -> exactly flat
    out = rec*(1-f) + Cnew*f
    gate = (w > 0.02)[..., None]                            # red-hue (crimson share) mask
    out = np.where(gate, out, sub)
    img[y0:y1, x0:x1] = np.clip(out, 0, 255).astype(np.float32)
    return img, dict(box=list(box), ivory=I.round(1).tolist(), old_left=C[45, 10].round(1).tolist(),
                     old_right=C[45, 575].round(1).tolist(), new=Cnew.tolist(), recoloured_px=int(gate.sum()))

# ---------------------------------------------------------------- fix 3
REGIONS = [   # (name, x0, y0, x1, y1) label / sticker faces carrying pseudo-letters
    ('shelf box A label',       0, 682,   41, 758),
    ('shelf box B label',      47, 682,   81, 758),
    ('shelf box C label',     102, 680,  142, 745),
    ('yellow pack label',      14, 443,   67, 481),
    ('red pack face',           0, 487,   35, 547),
    ('red pack white label',    0, 551,   30, 597),
    ('dark pack face',         36, 488,   68, 597),
    ('lower box label',        35, 612,   66, 672),
    ('door blue sticker',    1054, 372, 1080, 453),
    ('door red sticker',     1053, 458, 1080, 565),
    ('door dark sticker',    1055, 566, 1080, 622),
    ('door white label',     1055, 625, 1080, 658),
]
def fix3(img, regions=REGIONS, s_bg=4.0, s_ghost=2.5, k_ghost=0.30, seed=7):
    img = img.copy(); H, W = img.shape[:2]
    rng = np.random.default_rng(seed); log = []
    for (name, x0, y0, x1, y1) in regions:
        pad = 14
        X0, Y0, X1, Y1 = max(0, x0-pad), max(0, y0-pad), min(W, x1+pad), min(H, y1+pad)
        P = img[Y0:Y1, X0:X1].astype(np.float64)
        m = np.zeros(P.shape[:2]); m[y0-Y0:y1-Y0, x0-X0:x1-X0] = 1.0
        L = lum(P)
        med = cv2.medianBlur(np.clip(L, 0, 255).astype(np.uint8), 11).astype(np.float64)
        wg = np.exp(-((L - med)/7.0)**2)                    # ~0 on glyph strokes (dark or bright), 1 on label stock
        def nb(arr, wt, s):
            num = np.stack([cv2.GaussianBlur(arr[..., c]*wt, (0, 0), s, borderType=cv2.BORDER_REFLECT) for c in range(3)], -1)
            den = cv2.GaussianBlur(wt, (0, 0), s, borderType=cv2.BORDER_REFLECT)
            return num/np.maximum(den, 1e-6)[..., None]
        bg = nb(P, m*wg, s_bg)                              # label colour field without the glyphs
        gh = nb(P, m, s_ghost)                              # heavily defocused print, kept at 30% as a soft smudge
        new = bg + k_ghost*(gh - bg)
        hp = P - np.stack([cv2.GaussianBlur(P[..., c], (0, 0), 1.0) for c in range(3)], -1)
        sel = (m > 0) & (wg > 0.7)
        nstd = hp[sel].std() if sel.sum() > 20 else 1.5
        nz = rng.normal(0, 1, P.shape[:2]); nz = cv2.GaussianBlur(nz, (0, 0), 0.6); nz = nz/nz.std()*nstd
        new = new + nz[..., None]                           # grain matched to the label's own fine noise
        F = np.zeros(P.shape[:2]); F[y0-Y0+2:y1-Y0-2, x0-X0+2:x1-X0-2] = 1.0
        if x0 == 0: F[y0-Y0+2:y1-Y0-2, :x0-X0+2] = 1.0
        if x1 == W: F[y0-Y0+2:y1-Y0-2, x1-X0-2:] = 1.0
        F = cv2.GaussianBlur(F, (0, 0), 1.5)*m              # feathered, inset 2 px: label edges stay
        out = P*(1-F[..., None]) + new*F[..., None]
        img[Y0:Y1, X0:X1] = np.clip(out, 0, 255).astype(np.float32)
        log.append(dict(name=name, box=[x0, y0, x1, y1], grain_std=round(float(nstd), 2)))
    return img, log

if __name__ == '__main__':
    import json
    o8 = cv2.imread(ORIG)
    o = np.asarray(Image.open(ORIG).convert('RGB')).astype(np.float32)
    v = np.asarray(Image.open(V2).convert('RGB')).astype(np.float32)
    assert o.shape == v.shape == (1350, 1080, 3)
    v3, i1 = fix1(o, v, o8)
    v3, i2 = fix2(v3)
    v3, i3 = fix3(v3)
    out = np.clip(np.round(v3), 0, 255).astype(np.uint8)
    Image.fromarray(out).save(OUT, quality=93, subsampling=0)
    print(json.dumps(dict(fix1=i1, fix2=i2, fix3=i3), indent=1))
