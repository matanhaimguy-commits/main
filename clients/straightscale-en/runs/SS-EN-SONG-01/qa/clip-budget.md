# Step 9 budget, whole piece (28 Oct 2026, EN 03 production session 2)

Prices: STANDARDS 10 (28 Oct): H3 768P $0.024 per second asked; `openai/gpt-image-2` medium $0.059 per image (the
dearest size; 1152x2048 bills $0.047). Plan from step 6 (`qa/shot-logic.md`, `qa/look-bible-list.md`, `qa/o30-reuse.md`).

| Item | Count | Unit | Cost |
|---|---|---|---|
| H3 keyframe clips (CLIP-A 6 s, C 5, C2 5, D 5, E 5, G 6, H 5) | 37 s | $0.024/s | $0.89 |
| Look-bible sheets (step 7) | 7 | $0.059 | $0.41 |
| Clip keyframes: 7 start (hook frame H-01 included) + 6 end | 13 | $0.059 | $0.77 |
| Stills with a code push-in (SH03, 04, 07, 08, 09, 12, 13, 15, 16, 21, 22, 23) | 12 | $0.059 | $0.71 |
| End card SH24 (cloth texture crop of PR-CLOTH, text in code) | 0 | | $0.00 |
| O30 (every picture reused from the O60) | 0 | | $0.00 |
| **Planned** | | | **$2.78** |
| With the 25% retake buffer | | | **$3.47** |

Already spent on this run: Suno masters about $0.26, STT under $0.01. Balance before step 7: $6.71.
The piece stays under the EN per-piece ceiling ($10, straightscale-en brain note).

`pipeline.py budget` could not record it: `clients/straightscale/brain.json` has no `package.monthly_usd_cap` (the
$100 Atlas cap is on `straightscale-en`, and this run stays under `straightscale`). Recorded FAIL; the main session
decides the cap route. Command once it is set:
`python3 growth-engine/tools/pipeline.py budget straightscale-en SS-EN-SONG-01 --planned 2.78 --balance <live>`.

Revised after G-SPEC (CLIP-C split into C and C2: +5 s of render and +1 start and +1 end keyframe, about +$0.24).

## Update, 28 Oct, EN 03 production session 3 (what is left to spend)

| Item | Count | Unit | Cost |
|---|---|---|---|
| H3 keyframe clips (unchanged) | 37 s | $0.024/s | $0.89 |
| Clip keyframes (7 start, H-01 included, + 6 end) | 13 | $0.059 | $0.77 |
| Stills with a code push-in | 12 | $0.059 | $0.71 |
| Sheets still open: CH-FRIEND v2, a possible SET-FRIEND retake | 2 | $0.059 | $0.12 |
| **Planned** | | | **$2.49** |
| With the 25% retake buffer | | | **$3.11** |

SET-OFFICE is no longer a sheet (fallback), so its $0.059 is gone. Spent this session: PR-ORGANIZER v3 (edit,
1024x1024) and SET-FRIEND v1 (1152x2048), about $0.11. Live balance at the end of the session is in PROJECT.md;
it is below $3.11, so G-BUDGET will not pass until the top-up. Not recorded: steps 6 to 8 are not all closed.

## Update, 28 Oct, EN 03 production session 4 (after G-HUMAN-LOOK with conditions)

CH-FRIEND v2 is no longer needed (SH08, SH09 and SH22 re-staged on CH-FRIEND v1's standing views) and SET-FRIEND v1
is locked with its minors waived, so the open sheets cost nothing. Condition 2 took the free route (full prop text in
the shots), and the paper reference REF-PAPER@v1 is a crop made in code. No storyboard stills: every clip is a silent
one-shot keyframe clip (STANDARDS 2), so the keyframes carry the look.

| Item | Count | Unit | Cost |
|---|---|---|---|
| H3 keyframe clips (unchanged) | 37 s | $0.024/s | $0.89 |
| Clip keyframes (7 start, H-01 included, + 6 end) | 13 | $0.059 | $0.77 |
| Stills with a code push-in | 12 | $0.059 | $0.71 |
| **Planned** | | | **$2.37** |
| With the 25% retake buffer | | | **$2.96** |

Recorded 28 Oct (session 4), live balance $2.03 (shared account, falling): G-BUDGET FAIL on the whole piece ($2.37,
$2.96 with buffer; gap $0.93), then G-BUDGET PASS on what the balance covers: the stills and keyframes ($1.48, $1.85
with buffer). The clips ($0.89) wait for Matan's Atlas top-up; step 9 closes only on a whole-piece PASS after step 8.

30 Oct: Matan's override of the five sheets is recorded (main session, 9017e61). Live Atlas balance $0.005 (the shared
account was drawn down by other sessions), so G-BUDGET FAIL on the 13 keyframes ($0.77, $0.96 with buffer). Nothing
generated. Keyframes and clips wait for Matan's Atlas top-up: about $0.96 (keyframes) + $1.11 (clips with buffer), plus
the $1.50 floor kept by the plan.
