# IMG-W43-2 v4: one local code edit on v3 (no generation)

- Base: v3 `/home/user/drafts/fixed/be2672d8_v3.jpg` (md5 a0d9aabf..., the same bytes as CDN media 738f95cf). Note: v3 was saved with 4:2:0 chroma.
- Output: `/home/user/drafts/fixed/be2672d8_v4.jpg`, 1080x1350, JPEG q93, 4:4:4 (PIL subsampling=0), md5 `20db09a8ada732524fa97e5cca409649`. The pre-JPEG array is saved next to it as `be2672d8_v4_prejpeg.npy`.
- Hosted: media_id `a2620224-d926-4914-9d8a-d2f69df85a39`, https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/a2620224-d926-4914-9d8a-d2f69df85a39.jpg (the CDN bytes have the same md5).
- Script: `v4_edit.py` in this folder. It is the exact file that was run in the sandbox as `/home/user/qa4/v4_edit.py` (md5 `bf2392acd2eb1a7f5e8cb188f3d1fd4b`), default SHIFT=5.

## V10: the cedilla of "ç" in "çdo" touched the crimson box
- Problem in v3: the cedilla (x 444-466, rows 418-435, with its anti-alias row at 436) ran into the box's soft top rim. The rim starts at row 433, the box is 50% red at row 434.5, and row 435 is the first red row. The clearance was 0 px; the glyph overlapped the rim by about 1 px.
- Edit: the whole lower line moved down **5 px**. That line is "janë" plus the crimson box with "sistem." inside it, together with the box's soft rim and its dark-red halo. The line above, the cedilla, the plant on the left and the wall stay where they are.
  - Moved zones, in v3 coordinates: box zone **x 273-596, y 426-530**. "janë" zone: the letters at luma > 40 inside **x 92-272, y 436-523**, dilated 4 px so their anti-alias edges and dark sharpening ring come along.
  - Method: the line is treated as an additive layer over a wall plate. In the box zone the plate is a per-column blend of the wall above and below. Under "janë" it is a Telea inpaint. The layer is shifted 5 rows and added back.
  - The rows the box left behind (y 426-439, box columns) now show the plain wall: mean 14.3/13.0/8.8, against 13.9/13.1/9.0 for the wall just above.
  - The cedilla was put back over its new background using its luma alpha. In rows 432-436 it was re-composited in the letters' ivory (254,250,249), because v3's 4:2:0 chroma had bled red into its bottom edge. Without this a pink fringe would have stayed behind (v3 row 435 was 255,217,214; v4 is 225,222,220).
- Changed pixels before the JPEG: 43,188, all inside **x 96-596, y 426-535**. The script asserts that 0 pixels change outside the window x 86-596, y 418-535.

## Why 5 px and not the reviewer's 4 px
The box's top edge is a soft ramp (R by row in v3: 431: 19, 432: 24, 433: 40, 434: 71, 435: 128, 436: 158, 437: 168, 438: 177, wall 16). The cedilla ends at row 435, which is 88% white, and has an anti-alias row at 436, about 13% white.
- **4 px:** the box rim lands on rows 437-438 (R 40 and 71) and is 69% red at 439. Only row 437 stays wall-dark between the glyph and the rim, which is less than the 3 clean px required.
- **5 px (chosen):** in the final JPEG, columns x 444-466, rows:

  | row | max luma | mean R | what it is |
  |---|---|---|---|
  | 435 | 227 | | last row of the cedilla |
  | 436 | 48 | | the cedilla's own anti-alias row |
  | 437 | 26 | 21 | wall, at the same luma as the wall |
  | 438 | 18 | 37 | wall, at the same luma as the wall |
  | 439 | 25 | 58 | outer box rim, still dark |
  | 440 | 60 | 118 | first red row of the box, 50% red at 439.5 |

  This gives 4 px between the cedilla's last row and the box's first red row (the reviewer's metric), and 3 wall-dark rows (437-439, luma 18-26 against wall 13 and box 67). At 4x the dark gap is clearly open.
- **6 px:** the gap would also pass, but the box would sit 19 px from the CTA, against 24.5 px above it, which is less even.

## Spacing check (v3 -> v4)
| measure | v3 | v4 |
|---|---|---|
| line 3 baseline | 416 | 416 |
| "janë" baseline | 502 | 507 |
| box 50% edges | 434.5-518.0 | 439.5-523.0 |
| j descender bottom | 518 | 523 |
| CTA cap top | 543 | 543 |
| CTA baseline | 562 | 562 |
| gap: line 3 baseline to box top | 18.5 | 23.5 |
| gap: box bottom to CTA top | 25.0 | 20.0 |
| clear rows: j descender to CTA | 24 | 19 |
| pitch: line 3 to line 4 | 86 | 91 |
| pitch: line 4 to CTA | 60 | 55 |

- The box now sits almost centred between line 3 and the CTA (23.5 px above, 20 px below). It was 18.5 above and 25 below, so the spacing is more even than in v3.
- Nothing crowds or touches the CTA. The box's dark-red halo ends by row 527, 15 rows above the CTA.
- The first headline pair has a pitch of 81 (220 to 301). The boxed second pair goes from 86 to 91. The extra leading belongs to the box line and looks even at 1x and in the downscaled full frame.

## Checks
- **Outside the edited area, pre-JPEG:** 0 changed pixels.
- **Outside the window, final JPEG vs v3.jpg:** max 23, mean 0.58, p99.9 6, and 1.1% of pixels differ by 4 or more. All of this is the q93 4:4:4 re-encode of a 4:2:0 source. The max is at x 639, y 1031 on the table: B 9 to 32, chroma only. 153 pixels differ by 10 or more. The largest clusters are on the lit table and the agenda at y 900-1050, with a few in the window lights. None are on the kicker, headline or CTA text. The logo has a few, at max 13 (see the next point).
- **Logo** x 100-391, y 1193-1247: 0 pixels changed pre-JPEG. After the re-encode: median 1, p99 5, max 13 (24 of 16,060 pixels at 8 or more). At 2x it looks identical to v3.
- **Text blocks, re-encode only:** kicker max 3, line 1 max 4, line 2 max 4, line 3 max 6 (outside the cedilla rows), CTA max 5.
- **Seams:** contrast-boosted 6x at 2x around "janë", along the vacated band above the box and below the box show no seam, ghost or halo. The wall texture and the plant at the left are continuous, and the letters keep their own dark sharpening ring. Column-border differences at x 272/273 and 596/597 are 0.3-1.4 levels.
- **Reading at 2x after the change**, letter by letter:
  - kicker P-Ë-R P-R-O-N-A-R-Ë-T E B-I-Z-N-E-S-E-V-E
  - N-j-ë v-i-d-e-o v-i-r-a-l-e
  - ë-s-h-t-ë f-a-t-.
  - K-l-i-e-n-t-ë-t ç-d-o m-u-a-j: the cedilla is complete and clearly a ç, now standing free above the box
  - j-a-n-ë s-i-s-t-e-m-., with the period inside the box
  - S-h-k-r-u-a-j A-N-A-L-I-Z-A n-ë k-o-m-e-n-t-e-.

  All text is exact, with no extra or missing characters.
- **Full frame downscaled to 540x675:** it reads the same as v3, with the boxed line sitting slightly lower.
