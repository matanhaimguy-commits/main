# 2026-w43-1b carousel: v3 logo fix (code only, no generation)

Date: 2026-10-18. Script: `qa/v3_edit.py` (md5 `eeec73e8acab4ebc1b50be403a864a95`, an exact copy of
`/home/user/w43v3qa/v3_edit.py` in the Higgsfield sandbox). Run it in the sandbox with `python3 v3_edit.py --write`.
The script is deterministic: a second run produced byte-identical JPEGs for all 7 slides.

## Why v3
The v2 set review (`qa/SET.v2.logofix.review.json`) failed on one major issue, C5. The real logo's top edge moved
between y1189 and y1239 across the slides, because v2 placed it wherever the drawn logo had been on each slide.
v3 starts again from the v1 originals (`/home/user/drafts/<full id>.jpg`, which still have the model-drawn logo). It
removes the drawn logo and pastes the real logo in **one fixed box on all 7 slides**.

## Resumed work
The earlier run of this task (2026-10-16, sandbox `/home/user/ss_w43_v3/`) was cut off before it saved anything to
`drafts/fixed/` or to the repo. Its `v3_edit.py` and outputs were reused as the starting point. They looked clean at
2x. At 4-6x, three local defects showed up, and they were fixed as v3.1:
1. **SL05, dark crescent on the lit table edge.** The drawn gold square sits right beside the table-edge glow. Its
   +7 px mask swallowed part of the glow, and the fill redrew it about 20 levels darker. Fix: the gold square is now
   filled only out to +4 px. Its 4..7 px ring is de-rung, and where that ring lies on the lit edge it keeps the
   original pixels (83 px on SL05).
2. **Edge continuation direction.** The table edge inside the red square's fill was continued along a PCA of bright
   pixels. A bead pulled that direction about 9 deg too flat (41.6 deg against 51.7 deg from a ridge fit). It now uses
   the measured grain/edge angle from the structure tensor. It covers the edge's whole cross-profile and is
   feathered by distance, not by brightness.
3. **Halo specks.** Grain copied into the halo ring could land on a bead and leave a 1-2 px speck (SL05, SL07). The
   copied grain is now clipped to +-2.5 robust std of the surrounding surface.

The output is now JPEG q93 4:4:4 (the earlier run wrote 4:2:0). All 7 files were checked: 1080x1350, every
component sampled 1x1.

## Method (per slide)
- **Mask.** The drawn logo's own pixels: the red square and the gold square (convex hulls of their colour
  components) and the white letters. The fill replaces the red square +7 px, the gold square +4 px and the letters
  +4 px. The halo ring (letters 4..8 px, gold 4..7 px) keeps its low-pass and only loses the JPEG ringing. Warm
  highlights (table-edge beads) more than 3 px from the drawn shapes stay original.
- **Fill = inpaint + texture layer from the same surface.**
  - Wordmark area: a donor patch shifted along the wood grain (offset about (+36, +46) px, about 51 deg). Its
    high-pass is the texture layer, and a harmonic membrane of the boundary sets brightness and colour.
  - Square area (dark front face/floor): a harmonic inpaint of the boundary low-pass, plus the donor's fine grain
    (sigma 2.5, clipped).
  - Where the lit table edge crosses the square's corner (SL05, SL07), the edge is continued along its own direction.
- **Logo.** `/home/user/brand/straightscale-logo-light.png`, cropped to its alpha box (1501x279) and resized to
  **295x55** (aspect kept). It is alpha-composited at **top-left (98, 1233), box [98, 1233, 393, 1288]**, identical
  on all 7 slides. The pasted logo's opaque pixels match the file within 2.3 levels mean on every slide.
- Outside the mask, the halo and the logo box, the original pixels are copied back before the JPEG is written. That
  is 0 changed pixels in memory on every slide.

## Logo y: kept at 1233
The logo centre is at y1260.0. The swipe-arrow centres, from a minimum enclosing circle of the red disc:

| Slide | Arrow centre y | Arrow minus logo centre |
|---|---|---|
| SL01 | 1240.9 | -19.1 |
| SL02 | 1262.6 | +2.6 |
| SL03 | 1261.6 | +1.6 |
| SL04 | 1261.7 | +1.7 |
| SL05 | 1256.0 | -4.0 |
| SL06 | 1261.5 | +1.5 |
| SL07 | no arrow | - |

Slides 2 to 6 sit within 4 px of the arrow line. Their mean offset is +0.7 px, so y1233 is already their best fit.
The cover's own arrow sits about 21 px higher than on slides 2 to 6. No single y lines up all six: the best compromise
(about y1224) would put every slide 5 to 12 px off. So no other y is clearly better, and **1233 stays**. The cover
keeps a 19 px logo-to-arrow offset, which is visible only on the cover itself. The arrow was not moved (change
nothing else). The bottom margin is 62 px.

## Results

### Hosted files and change check
Every CDN file was downloaded and md5-checked against the local file. "Max diff outside zone" is measured outside
x0-560, y1120-1350. It is equal to the max diff from a plain re-encode of the original at q93 4:4:4 on every slide,
so it is JPEG noise only.

| Asset | id8 | media_id | md5 | Max diff outside zone (plain re-encode) | Mean |
|---|---|---|---|---|---|
| SL01 | 5d6ecdb0 | 44f2b217-6413-454e-ba7c-8ed4a29caccc | 94ecf69b1026d60fde81f8971b826b72 | 22 (22) | 0.93 |
| SL02 | 7e155c0b | 30695814-37ef-40b4-ae13-5bad1ce7eb8f | 46f876745c4ab90313e4f48ecdb47c58 | 22 (22) | 1.03 |
| SL03 | 3cdfd95e | e81f23be-52b9-498d-ab80-52e8ea6be90a | 63bf7465e8368b680e5d813477d0e502 | 20 (20) | 0.92 |
| SL04 | 26e094bc | 7ce22a7e-e7c4-403c-a660-9c65a79ea2ef | 5deecc139586b04f7ea287905c4a48e4 | 25 (25) | 0.81 |
| SL05 | 177e27a4 | 95c233f5-42c4-4b88-8417-8c2df46e2772 | c1f3d580be4a2e226769d38c7fd8ba27 | 23 (23) | 0.83 |
| SL06 | b6ed170a | c7e2d786-32cc-4cf6-ae68-97775a73bfc7 | d200e2d6d0485f2767300b0a58922651 | 25 (25) | 0.98 |
| SL07 | 78eb641f | 047c9dd6-26cc-4139-9682-8dd095e861cf | a11922fbbb42b7561402c810fe6ba24b | 25 (25) | 1.05 |

CDN URLs follow `https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/<media_id>.jpg`. The local
files are `/home/user/drafts/fixed/<id8>_v3.jpg` (sandbox).

### Texture numbers
How they are measured:
- Fill = every replaced or de-rung pixel, measured before the logo goes on.
- Ring = untouched pixels 3..15 px around the fill.
- Std = std of the high-pass (luma minus gaussian sigma 2).
- Targets: std within 25%, mean within 4 levels.

Results, as fill / ring:

| Slide | Plain: mean | Plain: std | Plain: std ratio | Same surface: mean | Same surface: std | Same surface: ratio | Robust std ratio |
|---|---|---|---|---|---|---|---|
| SL01 | 10.9 / 10.7 | 1.08 / 1.08 | 1.00 pass | 10.6 / 10.1 | 1.02 / 1.01 | 1.01 pass | 1.01 |
| SL02 | 14.6 / 16.7 | 1.05 / 1.53 | 0.69 | 13.2 / 13.1 | 0.96 / 1.04 | 0.92 pass | 1.06 |
| SL03 | 12.6 / 14.0 | 1.12 / 1.91 | 0.59 | 12.1 / 12.7 | 1.05 / 1.22 | 0.86 pass | 1.07 |
| SL04 | 12.9 / 13.7 | 1.04 / 2.16 | 0.48 | 12.1 / 12.4 | 0.96 / 1.05 | 0.91 pass | 1.10 |
| SL05 | 13.7 / 15.9 | 1.49 / 2.69 | 0.55 | 13.3 / 13.5 | 1.42 / 1.52 | 0.93 pass | 1.02 |
| SL06 | 15.9 / 16.2 | 1.20 / 1.33 | 0.90 pass | 15.2 / 15.3 | 1.05 / 1.11 | 0.95 pass | 1.01 |
| SL07 | 12.6 / 13.0 | 1.15 / 1.82 | 0.63 | 12.1 / 11.9 | 1.01 / 1.13 | 0.89 pass | 1.08 |

- **Mean:** every slide is within 2.2 levels on both measures.
- **Plain std:** the target is missed on SL02, SL03, SL04, SL05 and SL07. The cause is the ring, not the fill.
  - Per part: the wordmark area passes against its own ring on every slide except SL04 (fill 1.14 against ring 1.57).
    On SL04 the like-for-like numbers match: robust 0.98 / 0.85, same surface 1.04 / 1.08.
  - The square's ring crosses the lit, beaded table edge. Its plain ring std is 1.4-3.8, but only 0.71-0.82 once
    the beads are left out. That same-surface ring matches the fill's 0.72-0.87.
- **Like for like:** with the lit edge pixels left out of both fill and ring (low-pass > 1.8x the ring median + 2:
  1.6-7.1% of the fill, 3-12% of the ring), every slide passes. The robust std ratios (1.4826 x MAD) are 1.01-1.10.
  Local 24 px tiles have a median std ratio of 0.87-1.09.

Full numbers, including per part, per tile and "visible after logo", are in the sandbox at
`/home/user/drafts/fixed/w43-1b_v3_report.jsonl`.

## Visual QA done (sandbox `/home/user/w43v3qa/`)
- **2x before/after** of the bottom-left (x70-430, y1185-1315), all 7 slides (`w_a.jpg`, `w_b.jpg`). The drawn logo is
  gone and the wood grain and table-edge glow continue. No ghost letters show, even at 2.5x brightness (`boost4.jpg`).
- **4-8x zooms** of the gold-square/table-edge area, all 7 (`gold_new.jpg`), plus SL05 and SL07 contour views. The
  earlier crescent and specks are gone.
- **7-slide grid** (`grid7.jpg`) and a bottom-band strip with guides at y1233, y1260 and y1288 (`band7.jpg`). The logo
  sits in the same place on all 7. It is on the arrow's centre line on slides 2 to 6. The cover's arrow is higher
  (see above).

## Open items for the caller
- These are new asset versions (v3). They need per-slide reviews (V23/V24 on the logo zone) and a new G-SET review
  before they replace anything in the hub. `hosted.json` still lists the v1 originals.
- SL01: its v2 hero review passed with the logo at y1209. v3 moves it to y1233, so the cover needs a new hero review.
