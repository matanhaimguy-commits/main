# IMG-W42-7 v3: local code edits on top of v2

- Base: v2 `/home/user/drafts/fixed/ebd54bc2.jpg` (drawn logo inpainted, real logo pasted at x 100, y 1220, 291x54).
- Output: `/home/user/drafts/fixed/ebd54bc2_v3.jpg`, 1080x1350, JPEG q93 (same quantisation tables as v2), md5 `5190cc4493b394b9bc7fb53c8a893a7c`.
- Hub media: `3525e9b0-2663-47b8-a32d-8423ed29b233`, https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/3525e9b0-2663-47b8-a32d-8423ed29b233.jpg (the CDN bytes match the md5 above).
- Code: `v3_edit.py`, the exact script that was run (md5 `6dd517ed5867c2ebc4044b7c87ad2e36`). It uses only PIL, numpy, OpenCV and scipy, and nothing was generated.
- The real logo is unchanged. The script rebuilds the v2 mask, inpaint and logo alpha exactly as `fixlogo2.py` did, and it asserts that every pixel with logo alpha 255 is byte-identical to v2 before encoding. Where the logo is semi-transparent, only the background showing through changed.
- On-image text is untouched: "PYETJA E JAVËS"; "Sa mesazhe mbetën / pa përgjigje / këtë javë?"; "Numëroji para se të paguash për më shumë reklama.".

## Fixes (boxes are x0,y0 to x1,y1, inclusive)

1. **V23: desk edge and the strip under the wordmark**
   - **Cause.** The v2 detector took the desk-edge highlight (y 1198-1222) for the drawn gold square and inpainted it.
   - **Restored.** Original pixels came back at x 177-393, y 1195-1290 (1,922 px; the stub part is x 259-310, y 1195-1241; 7,131 visible px changed in total for fix 1). They were restored only where they were inside the v2 mask, not drawn logo and not under opaque logo. "Drawn logo" means within 5 px of a drawn white letter (the letters' halo ends at 3 px), plus the drawn red/gold square dilated by 5 px, all left of x 175.
   - **Filled.** The drawn-letter pixels at x 178-392, y 1249-1289 (6,165 px, 5,429 of them visible) were filled by a Poisson blend. The donor is the desk one step further along the edge, offset (+28, +25), which matches the measured ridge slope dx/dy of about 1.1. The glyph band was solved a second time from the filled strip, so the highlight stays on the edge line.
2. **V24: wall sign cross**
   - **Box.** x 21-79, y 344-413 (2,504 px changed; frame kept, paper untouched).
   - **Method.** Paper and ink were unmixed per pixel: the paper comes from an inpaint under the cross, and the ink weight from a linear projection between paper and the red ink colour. The red ink (87,22,7) was swapped for #3E5A5C, lit like the sign (value x0.7, 20% toward grey), so the cross reads as muted dark teal-grey. The ink's own shading was kept and its red chroma residue dropped. The core mean is now (46,60,60).
   - **Rejected.** Full #3E5A5C (and x0.8) read as a light cyan cross against the warm wall. The first pass, a G/R-ratio weight, left a dark rim, and the residue-kept pass left a light teal rim. Both are gone in the final version.
3. **V11: phone and ledger**
   - **Clock "0101".** The patch at x 238-272, y 846-858 (367 px) was given a harmonic fill from the surrounding screen, plus noise matched to the screen (sigma 1.2 x 0.7). The back chevron and the status icons were kept.
   - **Input placeholder "Mesisetan".** The patch at x 515-588, y 1051-1073 (863 px) is the text dilated by 2 and kept inside the pill eroded by 2. It got a harmonic fill from the pill colour, with no text and no new edges.
   - **Ledger cover fake embossing.** The polygon in the box x 986-1078, y 750-776 (1,857 px) was Poisson-cloned from plain leather on the same cover. The donors are offset (-140, +20) for x < 1031 and (-165, +22) for x >= 1031, chosen to avoid the pen tip and its shadow, the cover's stitched edge and two bright specks. The script asserts the mask stays at least 3 px above the pen.

## Checks run

- **Per fix: before and after crops at 2-6x, plain and contrast-boosted (x3 to x8), and the full image at 540x675.**
  - Fix 1: the highlight runs continuously from y 1150 to below the wordmark, and the dark front face has grain where v2 had a smooth blob. In o vs v3 at x8 boost, no drawn letter edges came back in the strip or between the glyphs, and nothing red or gold came back.
  - Fix 2: no rim and no blotch, and the frame and the faint sign lettering are kept.
  - Fix 3: no ghost digits or letters, and no smooth patch visible at 1x.
- **Pixel diff.** All pre-encode changes lie inside the boxes above. Outside them the only differences are JPEG re-encode noise, with p99.9 = 9 levels.
