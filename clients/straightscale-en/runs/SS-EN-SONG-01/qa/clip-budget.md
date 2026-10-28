# Step 9 budget, whole piece (28 Oct 2026, EN 03 production session 2)

Prices: STANDARDS 10 (28 Oct): H3 768P $0.024 per second asked; `openai/gpt-image-2` medium $0.059 per image (the
dearest size; 1152x2048 bills $0.047). Plan from step 6 (`qa/shot-logic.md`, `qa/look-bible-list.md`, `qa/o30-reuse.md`).

| Item | Count | Unit | Cost |
|---|---|---|---|
| H3 keyframe clips (CLIP-A 6 s, C 5, D 5, E 5, G 6, H 5) | 32 s | $0.024/s | $0.77 |
| Look-bible sheets (step 7) | 7 | $0.059 | $0.41 |
| Clip keyframes: 6 start (hook frame H-01 included) + 5 end | 11 | $0.059 | $0.65 |
| Stills with a code push-in (SH03, 04, 07, 08, 09, 12, 13, 15, 16, 21, 22, 23) | 12 | $0.059 | $0.71 |
| End card SH24 (cloth texture crop of PR-CLOTH, text in code) | 0 | | $0.00 |
| O30 (every picture reused from the O60) | 0 | | $0.00 |
| **Planned** | | | **$2.54** |
| With the 25% retake buffer | | | **$3.17** |

Already spent on this run: Suno masters about $0.26, STT under $0.01. Balance before step 7: $6.71.
The piece stays under the EN per-piece ceiling ($10, straightscale-en brain note).

`pipeline.py budget` could not record it: `clients/straightscale/brain.json` has no `package.monthly_usd_cap` (the
$100 Atlas cap is on `straightscale-en`, and this run stays under `straightscale`). Recorded FAIL; the main session
decides the cap route. Command once it is set:
`python3 growth-engine/tools/pipeline.py budget straightscale-en SS-EN-SONG-01 --planned 2.54 --balance <live>`.
