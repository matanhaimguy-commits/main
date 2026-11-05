# 2026-w43-1b carousel: v4 cover (SL01), swipe arrow moved down (code only, no generation)

Date: 2026-10-18. Script: `qa/v4_cover_edit.py` (md5 `ad809feade46f3642937474a7592b69c`, the exact copy run in the
Higgsfield sandbox as `/home/user/v4c/v4_cover_edit.py --write`). It is deterministic: the dry run and the `--write`
run gave byte-identical JPEGs.

## Why
The fresh v3 hero review (`qa/SL01.v3.review.json`) failed on one minor defect, V18. The logo box [98,1233,393,1288]
is centred at y1260.5, but the cover's swipe-arrow button sat 19 px higher (bbox [932,1211,991,1271], centre y1241).
On slides 2 to 6 the arrows are centred at y1256 to 1262.5. The fix note asked to keep the logo where it is and move
the arrow down 20 px.

## Result
- Input: `/home/user/drafts/fixed/5d6ecdb0_v3.jpg` (md5 `94ecf69b1026d60fde81f8971b826b72`, CDN `44f2b217-...`).
- Output: `/home/user/drafts/fixed/5d6ecdb0_v4.jpg`, 1080x1350, JPEG q93, 4:4:4 (every component sampled 1x1),
  md5 `6f71ea3b1e1e7e23d9fc012934bd2085`.
- Uploaded as `straightscale-2026-w43-1b-carousel-SL01-v4.jpg`: media `9dc05cce-7d42-4f16-b914-4e8dfafc79bd`,
  https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/9dc05cce-7d42-4f16-b914-4e8dfafc79bd.jpg
  (the CDN copy has the same md5).
- New arrow button: bbox **[932,1231,991,1291]**, centre **(961.5, 1261.0)**, radius 30.3. With v3's own measure
  (min enclosing circle, r>140, r>2g, r>2b) the centre is y1260.8, which is 0.3 px from the logo centre (1260.5).
  The white arrow is intact (158 vs 159 px). Bottom margins: arrow 58 px, logo 62 px. Both are outside the 4% band
  (54 px).

## Method
1. **Lift.** The red disc (r>120, g<50, b<60) with its holes filled (the white arrow). The matte is 1 on the disc and
   its 1 px anti-aliased rim, then a linear 1 px feather. The button has no drop shadow: luma is flat from 1 px
   outside the rim on every side. So the matte holds the whole button. The rim profile of the moved button matches
   v3 within 0.8 luma levels on average (max 1.8) and 3.3 red levels (max 6.8, the outermost chroma fringe), in
   4 sectors from 2 px inside to 1 px outside the edge.
2. **Plate.** The old disc +5 px was refilled. That covers the rim, its JPEG red ringing and a 3 to 5 level dark
   fringe on the lit side. 3872 px in total, box [927,1206,996,1276]; 1730 px stay visible (the crescent
   [927,1206,996,1256]).
   - **Low-pass:** a harmonic (Laplace) membrane from the boundary. The boundary values come from a local plane fit
     (sigma 3) of the untouched surface. A plain normalised blur left a 6-level step against the lit gradient on
     the left, a faint arc at 4x. The plane fit removed it.
   - **Grain:** the sigma-3 high-pass of an adjacent untouched patch. The patch is offset (+64, +58), 86 px away
     along 42 deg; the fine grain on the right side runs at 34.5 deg. The patch was chosen by the best high-pass
     match on an 8 px band at the same grain level. The grain was scaled pixel by pixel to the surface's local grain
     level (gain median 1.25, p10 0.90, p90 2.37), clipped to +-3 local std, then calibrated once by k = 1.236.
3. **Paste.** The lifted button went 20 px lower, over the plate.
4. **Copy back.** Every pixel outside the plate and the moved matte was copied back from v3 before encoding. That is
   4809 changed px in box [927,1206,996,1292] and 0 changed px outside x900-1020, y1190-1310.

## Fill texture numbers
These cover the visible crescent, more than 5 px from the moved button (1269 px). "Natural" is the same measure on
untouched v3 wood, using the same shape at 12 nearby spots.

| Measure | Fill | Natural (median, range) |
|---|---|---|
| High-pass std (sigma 2) vs 3..15 px ring | 0.94 | 0.98 (0.52 to 1.32) |
| Robust std vs ring | 1.06 | 1.04 (0.55 to 1.62) |
| Mean vs ring (lit gradient included) | -3.5 | -2.05 (-13.7 to 35.5) |
| 12 px tiles: std ratio, median (min..max) | 0.91 (0.70..1.16) | 0.96 (0.40..1.41) |
| 12 px tiles: abs mean minus local plane, median / max | 2.43 / 7.77 | 6.45 / 40.4 |
| Luma step across the plate boundary vs next ring outside | 1.55 vs 1.52 | - |

## Change check
- Max difference outside x900-1020, y1190-1310: **8**. Mean 0.075, p99.9 3.
- A plain q93 4:4:4 re-encode of v3 gives the same max of 8, so this is JPEG noise only.
- The wood now under the button was plain table: luma 20 to 45, no red pixels, no bright pixels.

## Looked at
- The bottom row at 1x, before and after, with guides. The arrow centre line now lies on the logo centre line.
- The arrow area at 2x and 4x, before and after.
- The crescent at 6x, plain and contrast-boosted. No arc, seam, smear or repeated pattern.
- The 200 px thumbnail, before and after.

The views are in the sandbox at `/home/user/v4c/views/`, and the full numbers are in `/home/user/v4c/v4_report_final.json`.

## Next
Per the fix note: run a new SL01 hero review on v4 and a new G-SET review. Nothing else on the cover changed, so the
other V checks should stand. For future covers, draw the swipe arrow in code at a fixed box shared with the logo row
(centre y~1260 at 1080x1350).
