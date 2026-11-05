# IMG-W42-7 v4: two local code edits on top of v3

- Base: v3 `/home/user/drafts/fixed/ebd54bc2_v3.jpg` (md5 `5190cc4493b394b9bc7fb53c8a893a7c`).
- Output: `/home/user/drafts/fixed/ebd54bc2_v4.jpg`, 1080x1350, JPEG quality 93, 4:4:4 chroma (PIL `subsampling=0`), md5 `4ab6e4957ae66263c4e892eef5c0ccb7`, 380,318 bytes.
- Hub media: `5fe3368b-1e13-4655-b201-87baf256b0b3`, https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/5fe3368b-1e13-4655-b201-87baf256b0b3.jpg. The CDN bytes match the md5 above. Upload filename: `straightscale-2026-w42-7-image-v4.jpg`.
- Code: `v4_edit.py` is the exact script that was run (md5 `d28c79de89365e5959a48eeb726cf335`). It uses only PIL, numpy, OpenCV and scipy. Nothing was generated.
- Text is untouched: "PYETJA E JAVËS"; "Sa mesazhe mbetën / pa përgjigje / këtë javë?"; "Numëroji para se të paguash për më shumë reklama.". The script asserts that no letter pixel in the bar box changed (every pixel with G >= 225).
- The real logo (bottom-left, x 100-390, y 1220-1273) is untouched. It is outside both edit boxes, and before encoding its pixels are identical to v3.

## Fixes (boxes are x0,y0 to x1,y1, inclusive)

1. **Wall sign on the left wall, removed completely.** This covers the frame, the recoloured blue-cross emblem and the faint text-like marks.
   - **Box.** x 0-100, y 303-465. That is 16,378 solved pixels: the box minus the pure bar pixels at x 96-100, y 303-319.
   - **Method.** A Poisson fill. The guide is the wall itself, continued per column from the wall band above the frame (y 290-301) to the wall band below it (y 466-476). This carries the faint vertical panel tones (for example the darker seam near x 45-50) and the downward light gradient straight through.
   - **Boundaries.** The fixed (Dirichlet) boundary is the real wall just outside the box: row 302, row 466 and column 101. The image edge and the headline bar are free (Neumann) boundaries, so no red bleeds into the wall.
   - **Grain.** Fine grain was added, matched to the wall's own high-pass sigma 1 (std 0.66/0.62/0.65).
   - **Bar corner.** At the bar's bottom-left corner (x 89-100, y 303-327), the bar's soft edge was re-composited over the new wall in the new colour. The left-edge profile was measured on the recoloured bar in the rows just above. The bottom-edge profile is the median of 90 clean columns. This keeps the corner crisp with no jog.
   - **Result.** There is no frame, outline, rectangle or smudge left. In the box at x 0-90 the row means rise smoothly from 26 to 41, top to bottom, the same as the wall around it.
2. **Headline highlight bar, now a flat #B31217.**
   - **Box.** x 86-597, y 233-330. The bar itself spans x 92-591, y 240-322.
   - **Old colour.** The measured mean was (157.4, 13.1, 23.5), about #9D0D17.
   - **Mask.** A red-hue mask. The box weight per pixel is a = (R-G) / 144, the old box's R-G. It is gated to hues within 14-26° of the box hue (355.7°), which excludes the orange-brown wall at about 27° off. It is also gated to a >= 0.15 and away from near-white letter pixels.
   - **Recolour.** Box pixels more than about 3 px from any letter or from the bar's outer edge were set to exactly (179, 18, 23): 14,036 pixels fully flat. The band within about 3 px was shifted by a x (new - old). That band holds the letter anti-aliasing, the dark ringing beside the letters and the bar's outer soft edge. Letters keep their own colour and edges, and no old-crimson fringe is left.
   - **Result.** In the final JPEG, the flat pixels average (179.2, 18.2, 22.9), with std 1.2-1.7 from JPEG noise next to the letters.

## Checks run

- **Each fix, before and after.**
  - Fix 1 at 2x, a 3.6x contrast-boosted 2x crop, a contrast-boosted 3x crop of the right edge beside "k"/"N", and a 5x crop of the bar corner.
  - Fix 2 at 2x for the whole bar, and 4x for "pa p" with the left edge and for "gje" with the right edge.
  - Both at 1x (top-left crop), the full image at 540x675, and a 200x250 thumbnail.
  - Sign: nothing left at any scale, and the panel tones line up above and below.
  - Bar: flat, the letters are crisp, and there is no red or dark fringe.
- **Pixel diff, before encoding.** Outside the two boxes the max difference from v3 is 0 (asserted in the script).
- **Pixel diff, final JPEG vs v3 outside the two boxes.**
  - Max 12, mean 0.60, p99 3, p99.9 5. This is all re-encode noise: v3 re-encoded alone at q93 4:4:4 gives the same max 12 and mean 0.595.
  - v4 is bit-identical to v3 re-encoded at the same settings everywhere outside the 8x8 blocks that touch the two boxes (max 0).
  - Logo box: max 11 vs v3, purely from re-encoding (the q93 4:4:4 re-encode that was asked for), and 0 vs v3 re-encoded.
