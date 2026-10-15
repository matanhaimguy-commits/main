#!/usr/bin/env python3
"""Pacing, palette and a contact sheet for a reference reel from sampled frames (no video file needed).

    python3 refbank/tools/frames_metrics.py <frames_dir> --step 0.5 [--id ID] [--out refbank/metrics/ID.json]

Instagram and TikTok video hosts are blocked from our containers, so references arrive as frames sampled every
`--step` seconds (Apify seemuapps/video-frame-extractor, interval mode). Frames are taken in name order.
Writes the metrics JSON and <frames_dir>/sheet.jpg (hook frames at full rate for the first 3 s, then one frame per
second, each stamped with its time) for whoever writes the card to look at.

Numbers are coarser than tools/pacing.py (2 fps instead of 12): treat cuts and change rhythm as reliable, and
quiet share as approximate. Same thresholds, so a reference and our render compare on the same scale.
"""
import json, os, sys, glob
import numpy as np
from PIL import Image, ImageDraw

NOISE, QUIET, HARD, BIG = 10, 0.01, 0.4, 0.12   # per-pixel noise; quiet / hard-cut / big-change picture shares
HIST = 0.3                                       # colour-histogram distance (0-1) a cut must also exceed
W = 120                                          # analysis width


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def load(paths):
    imgs = [Image.open(p).convert('RGB') for p in paths]
    w0, h0 = imgs[0].size
    h = int(round(h0 * W / w0))
    small = [np.asarray(i.resize((W, h), Image.BILINEAR), np.float32) for i in imgs]
    return imgs, np.stack(small)


def palette(rgb, k=6, iters=12):
    """Dominant colours by k-means on a pixel sample; returns [(hex, share)] sorted by share."""
    px = rgb.reshape(-1, 3)[:: max(1, rgb.reshape(-1, 3).shape[0] // 20000)]
    rng = np.random.default_rng(7)
    c = px[rng.choice(len(px), k, replace=False)]
    for _ in range(iters):
        lab = np.argmin(((px[:, None] - c[None]) ** 2).sum(-1), 1)
        c = np.stack([px[lab == j].mean(0) if (lab == j).any() else c[j] for j in range(k)])
    share = np.bincount(lab, minlength=k) / len(lab)
    out = sorted(((('#%02x%02x%02x' % tuple(int(v) for v in c[j])), round(float(share[j]), 3)) for j in range(k)),
                 key=lambda x: -x[1])
    return [o for o in out if o[1] >= 0.02]


def runs(mask):
    out, start = [], None
    for i, m in enumerate(list(mask) + [False]):
        if m and start is None: start = i
        elif not m and start is not None: out.append((start, i - start)); start = None
    return out


def analyse(d, step):
    paths = sorted(p for p in glob.glob(os.path.join(d, '*')) if p.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))
                   and not os.path.basename(p).startswith('sheet'))
    imgs, f = load(paths)
    g = f.mean(-1)
    # change share between consecutive samples; the bottom 6% (frame-extractor time stamp) is masked out
    hh = int(g.shape[1] * 0.94)
    ch = np.concatenate([[0.0], (np.abs(np.diff(g[:, :hh], axis=0)) > NOISE).mean(axis=(1, 2))])
    t = np.arange(len(ch)) * step
    # a cut = most of the picture changes AND the colour distribution jumps (camera moves, morphs and full-frame
    # patterns change pixels but keep their colours); detections within 0.6 s are one cut spanning two samples
    q = (f[:, :hh] // 64).astype(int)
    idx = q[..., 0] * 16 + q[..., 1] * 4 + q[..., 2]
    H = np.stack([np.bincount(x.ravel(), minlength=64) / x.size for x in idx])
    hd = np.concatenate([[0.0], 0.5 * np.abs(np.diff(H, axis=0)).sum(1)])
    cuts = []
    for i in range(1, len(ch)):
        if ch[i] > HARD and hd[i] > HIST:
            if not cuts or t[i] - cuts[-1] > 0.6:
                cuts.append(round(float(t[i]), 2))
    full_frame_changes = int(sum(ch[1:] > HARD))
    big = [round(float(t[i]), 2) for i in range(1, len(ch)) if ch[i] > BIG]
    shots = np.diff([0.0] + cuts + [float(t[-1] + step)])
    gaps = np.diff([0.0] + big + [float(t[-1] + step)])
    gaps = gaps[gaps > 0]
    quiet = runs(ch[1:] < QUIET)
    hsv = np.stack([np.asarray(Image.fromarray(x.astype(np.uint8)).convert('HSV'), np.float32) for x in f])
    m = {
        'frames': len(paths), 'step_s': step, 'sampled_s': round(float(len(paths) * step), 1),
        'cuts': len(cuts), 'cut_times': cuts[:40], 'full_frame_changes': full_frame_changes,
        'cuts_per_10s': round(10 * len(cuts) / max(1e-6, len(paths) * step), 2),
        'mean_shot_s': round(float(shots.mean()), 2), 'longest_shot_s': round(float(shots.max()), 2),
        'big_changes': len(big), 'mean_s_between_big_changes': round(float(gaps.mean()), 2),
        'change_rhythm_cv': round(float(gaps.std() / gaps.mean()), 2) if len(gaps) > 1 else 0.0,
        'change_rhythm_spread': round(float(gaps.max() / gaps.min()), 1) if len(gaps) > 1 else 1.0,
        'quiet_share_2fps': round(float((ch[1:] < QUIET).mean()), 3),
        'longest_quiet_s': round(max((n for _, n in quiet), default=0) * step, 2),
        'mean_change': round(float(ch[1:].mean()), 3),
        'hook_change_0_2s': round(float(ch[1:int(2 / step) + 1].mean()), 3),
        'energy_curve': [round(float(v), 2) for v in ch],
        'luma_mean': round(float(g.mean() / 255), 2), 'luma_contrast': round(float(g.std() / 255), 2),
        'saturation_mean': round(float(hsv[..., 1].mean() / 255), 2),
        'palette': palette(f),
    }
    return m, imgs, t


def sheet(imgs, t, step, out, cell=200, cols=8):
    pick = [i for i in range(len(imgs)) if t[i] < 3.0 or abs((t[i] / 1.0) - round(t[i] / 1.0)) < 1e-6]
    w0, h0 = imgs[0].size
    ch = int(round(h0 * cell / w0))
    rows = (len(pick) + cols - 1) // cols
    S = Image.new('RGB', (cols * cell, rows * (ch + 18)), (24, 24, 24))
    dr = ImageDraw.Draw(S)
    for k, i in enumerate(pick):
        x, y = (k % cols) * cell, (k // cols) * (ch + 18)
        S.paste(imgs[i].resize((cell, ch), Image.BILINEAR), (x, y))
        dr.text((x + 4, y + ch + 3), f'{t[i]:.1f}s', fill=(235, 235, 235))
    S.save(out, quality=82)


if __name__ == '__main__':
    if len(sys.argv) < 2: sys.exit(__doc__)
    d, step = sys.argv[1], float(arg('--step', '0.5'))
    m, imgs, t = analyse(d, step)
    m['id'] = arg('--id', os.path.basename(os.path.normpath(d)))
    sheet(imgs, t, step, os.path.join(d, 'sheet.jpg'))
    out = arg('--out')
    s = json.dumps(m, indent=1)
    if out: open(out, 'w').write(s + '\n')
    brief = {k: v for k, v in m.items() if k not in ('energy_curve', 'cut_times')}
    print(json.dumps(brief))
