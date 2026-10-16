# IMG-W43-2 v3: local code edits on v2 (no generation)

- Base: v2 `/home/user/drafts/fixed/be2672d8.jpg` (md5 433a84de...). Reference: the v1 model output `be2672d8-7527-434c-8be5-8fe201468af1.jpg`.
- Output: `/home/user/drafts/fixed/be2672d8_v3.jpg`, 1080x1350, JPEG q93, md5 `a0d9aabf9de3f586e3f8b85dd8c639cb`.
- Hosted: media_id `738f95cf-783e-41bf-8c00-8778775ea688`, https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/738f95cf-783e-41bf-8c00-8778775ea688.jpg (CDN bytes have the same md5).
- Script: `v3_edit.py` in this folder, the exact file that was run in the sandbox (md5 `f13465cd7d65507384b4c592c9dd43a0`).
- Before the JPEG encode, 0 pixels changed outside the three zones below. Kicker, headline, CTA and the pasted real logo are byte-identical to v2. After re-encoding, the mean difference from v2 outside the zones is 0.36 levels (JPEG only).

## V23: highlight beads above the mark (caused by the v2 fix)
- Cause: the v2 drawn-logo colour test read beads 3 to 6 on the table edge as "gold". It inpainted them, which left a smear at x 129-178, y 1166-1196.
- Edit: restored the v1 pixels in the box **x 120-185, y 1150-1196**, in the places where the real logo's alpha is 0 (2,970 px). Where the logo has a soft edge (33 px), the logo was re-composited over the v1 background. Opaque logo pixels (99 px) were kept from v2.
- Checks:
  - The drawn logo starts at y 1212, and its 4 px guard ring does not touch the box (assertion in the script).
  - The drawn gold-square area x 146-162, y 1208-1226 is still exactly v2.
  - Restored pixels equal v1 exactly. Bead-zone texture std is 29.5 in v3, 29.6 in v1 and 21.7 in v2.
  - At the box border the final file differs from v1 by 1.7 levels inside the box and from v2 by 0.7 levels outside it, so there is no seam.
  - Seen at 2x and 3x as v1/v2/v3 strips and as contrast-boosted crops: the bead line now runs unbroken down to the real gold square. No smear, and no drawn gold or red came back.

## V21: crimson box behind "sistem."
- Box rect **x 284-583, y 435-517**. The interior x 287-580, y 438-514 was flattened. The soft-edge band x 280-587, y 431-521 was shifted by colour unmixing.
- Method:
  - Interior: the letter share was measured from G (box G 9, ivory G 250). Pixels became `(1-t)*#B31217 + t*ivory`, and letter cores (t > 0.85 to 0.98) kept their v2 pixels.
  - Outer edge and the "ç" cedilla: three-colour unmixing (box, ivory, background), where only the box share moves from (160,9,17) to (179,18,23).
- Checks:
  - Pre-JPEG, 98% of the flat box pixels are exactly 179,18,23. In the final JPEG the median is **179,18,23 = #B31217** (it was 160,9,17).
  - 0 of 4,878 letter-core pixels changed.
  - The red showing inside the "e" counter was recoloured with the box.
  - The edge profile keeps its v2 softness. At 2x and 6x (corners, cedilla, letter edges) there is no fringe or halo.

## V11: pseudo-word day headers and footer mark on the agenda
Each mark was placed from per-pixel darkness maps. Its polygon sits between the ruled lines and stays above the red squares, so lines and squares are outside it. Fill = local paper tone (distance-weighted quadratic fit of the clean paper around the mark, matched at the rim to within 0.7 levels) + fibre-like grain matched to the paper's own high-pass energy. Polygon bounding boxes (x0, y0, x1, y1; the sides are slanted along the rules):

| mark | box | mark | box |
|---|---|---|---|
| LT1 left-page top heading | 199-228.5, 815-821 | RT right-page top heading | 446.5-500.5, 834-841 |
| LT2 left-page top heading | 252.5-293.5, 816-823 | RG header over square 1 | 459.5-484.5, 843-850 |
| LC header over square 1 | 151.5-183, 841.5-848 | RH header, square 2 | 387.5-416, 884.5-895 |
| LD header, square 2 | 63-93, 873.5-880 | RI header, square 3 | 580.5-605.5, 872-881.5 |
| LE header, square 3 | 235.5-267, 872-882 | RS right heading | 674.5-708.5, 874-881.5 |
| LF lower-block header | 91.5-117.5, 923.4-928 | RJ header, square 4 | 315.5-347, 930-942 |
| RK header, square 5 | 516.5-545.5, 915-928 | RL header, square 6 | 452.5-482.5, 967-983 |
| RF footer dot | 480.5-485.5, 1061.5-1065.6 | RF footer text | 493.5-526.5, 1063-1076.5 |

Two letter blobs sat on top of a ruled line. They were only lightened down to the line's own darkness, so each line stays continuous:
- RH 387.5-391.5, 882.5-883.5 (darkness 32 to 16)
- RF 503.5-511.5, 1062.5-1064.5 (darkness 34 to 24)

Checks:
- Maximum darkness inside every polygon fell from 19-96 to 5-13, which is paper-grain level.
- Fill tone matches the paper next to it to within about 3 levels. Grain high-pass std is 2.2-2.9, against 2.0-3.7 for the paper.
- Each mark was compared at 4x, 5x and 6x, with and without CLAHE contrast boost, and the agenda as a whole at 2x. Every ruled line, junction, divider and the 9 red squares are intact. No letters, ghosts, seams or tone patches remain.
- The bold curved stroke at x 374-406, y 823-838 near the left-page gutter is one continuous ruled stroke, not a word, so it was kept.
- The full image downscaled looks unchanged apart from the brighter brand-red box.
