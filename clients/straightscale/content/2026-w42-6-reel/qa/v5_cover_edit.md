# Sat 17 quote reel: v5 cover (fixes D1 and D2 from the v4 review)

Date: 2026-10-18. Code only (PIL, numpy, OpenCV) in the Higgsfield sandbox. Nothing was generated.

| File | media_id | CDN url | Size | md5 |
|---|---|---|---|---|
| ss-2026-10-17-reel-v5-cover.jpg | 698cc70b-bfd2-46f1-aaa7-4eafbc7fcbb0 | https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/698cc70b-bfd2-46f1-aaa7-4eafbc7fcbb0.jpg | 567,327 B | 97fb6d1a897430f798cf76c95032e6e1 |

The file is 1080x1920, JPEG quality 93, 4:4:4. The PUT returned 200 and media_confirm returned `uploaded`. A HEAD on the CDN url returned 200 with image/jpeg, and the downloaded bytes have the same md5 as the local file.
Sandbox paths: `/home/user/daily/reel/v5/ss-2026-10-17-reel-v5-cover.jpg`. The script is `v5_cover_edit.py` (this folder, and a copy in `/home/user/daily/reel/v5/`). Check crops are in `/home/user/daily/reel/v5/cov/`.

## What changed from v4

v5 starts again from the v3 cover, so v4's blur is not reused. The blur settings stay the same: Gaussian sigma 9 px, then 12 % darker. The masks are new.

- **D1, frame:** v4 blurred a soft-edged rectangle. v5 blurs only the glass of the two panes. Each pane is bounded by straight lines measured on the frame's inner edges at 4x to 8x:
  - shutter and top rail: y = 1022.5 + 0.047x
  - post A: left face x ≈ 158, right face x ≈ 187
  - right post: inner face x ≈ 274 → 271
  - left bottom bead: y = 1747 − 0.56x
  - right bottom bead: y = 1640 − 0.56(x − 188)

  These lines have a 1 px anti-aliased edge and no ramp. Post A, its base below the sill (the x 184-198 zone), the right post, the beads, the lit sill, the base panels and the pavement are byte-identical to v3 before the JPEG save. The frame is therefore sharp along its whole length.
- **D2, owner:** The protect mask is now a colour key with no dilation:
  - Coat, sleeve and cuff are keyed at luma < 40. Above the sleeve the key is luma < 115, so the hand and the lit top rim of the sleeve stay with the owner.
  - The key searches only 6 px around the old outline, and it keeps only the parts connected to the inside of that outline.
  - A 2 px band along the outline gets a local luminance matte. On mixed edge pixels the sharp window share is swapped for the blurred window, so the coat edge stays sharp.
  - The blur is a normalised convolution over pure-window pixels only, so no coat or frame darkness bleeds into the glass.

  Result: the strip and orange-red fleck under the hem are now blurred glass. The bright rim on the coat's left edge at y 1420-1495 is gone. The sleeve underside is one smooth curve, with no steps.

## Checks

| Region | Max diff before JPEG | PSNR against v3 after JPEG | Mean abs diff |
|---|---|---|---|
| Glass outside the panes (frame, shutter, sill, base, street, headline) | 0 | | |
| Owner | 0 | 48.1 dB | |
| Headline, y < 950 | 0 | 47.9 dB | 0.46 levels |
| x ≥ 301 | 0 | 47.0 dB | |
| Frame, sill and base | | 45.2 dB | |

The PSNR and mean-difference figures after the JPEG save show re-encode noise only. Mean glass luma went from 103.3 to 90.8.

Views:
- **2x:** No letter-like shapes are left in either pane. Every frame line is continuous and sharp.
- **4x:** The red can is a soft blob. The bead and sill are sharp, and the glass meets them cleanly.
  - The coat edge at y 1385-1515 has no rim, no halo and no fleck.
  - The sleeve underside at x 180-310 is a clean curve.
  - The sleeve top and hand keep their lit rim.
  - Post A from y 1590 to 1840 is unchanged.
- **200 px wide and the 3:4 profile-grid centre crop:** These read like v4. The headline and the owner are untouched, and the window is a calm warm bokeh behind a crisp frame.

Check images: `c_hem.jpg`, `c_slv.jpg`, `h5.jpg`, `c_arm.jpg`, `c_tr.jpg`, `c_post.jpg`, `c_bead.jpg`, `c_lb.jpg`, `c_top.jpg`, `k_can4x.jpg`, `w2x_top.jpg`, `w2x_bot.jpg`, `cmp200.jpg` (v3, v4, v5), `cmp_grid34.jpg` (v4, v5), `v5_540.jpg` and `diff_x4.jpg`.
