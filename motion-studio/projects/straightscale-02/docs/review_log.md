# Review log: StraightScale · Reel 02 "Klientët që kthehen"

Every round is logged. Never ship with a known blemish without writing it here and telling the client.

## Round 0 · 2026-10-13 · styleframes (stage 7)
Sheets: `out/sf_a.png`, `out/sf_b.png`, `out/sf_c.png`, then `out/sf_d.png` after fixes

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 6 | 0.3: only the red bands showed; the three tokens were too fast (1,150 u/s) to be on screen |
| Readability at phone size | 6 | 19.9 "Kërkoji një vlerësim" ran past the right edge; message card text clipped at 18.6 |
| Motion quality | 8 | ride 4.2-6.5 reads as one camera move (strip) |
| Continuity | 8 | the token survives every beat; the mark hands over to the real PNG at 27.6 |
| Variety and pacing | 7 | rest 7-10 s is real; 29.2-29.7 nearly empty |
| Composition | 6 | 18.6 thread line crossed the headline; 29.0 the mark swung off the left edge while shrinking |
| Brand accuracy | 9 | traced mark IoU 0.999 vs the real file; real lockup at the end; brand colours measured from the logo |
| Sound | n/a | not built yet |
| Message with the sound off | 8 | leak (token out and grey) vs loop (gold line, two tokens home) reads without words |

Fixes: denser, slower hook stream (5 tokens at 650 u/s); auto safe-zone check (`tools/safezone.mjs`) and smaller
sizes for 6 lines; card set in 3 lines; the thread now runs from the card up to the client; the shrink into the
lockup interpolates on screen, not in camera space; the lockup lands centred, then rises to a header.

## Round 1 · 2026-10-13 · draft cut (15 fps, `out/draft_av.mp4`)
Sheets: `out/contact.png`, `out/strip.png` (18.7), `out/phone.png`, `out/strip_ride.png`, `out/strip_lockup.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | two to three tokens always crossing, "zero?" lands on an empty band |
| Readability at phone size | 8 | phone sheet: every line readable at 360 px; smallest text 44 px (labels) |
| Motion quality | 8 | springs on every text; the ride needs the 60 fps / 4-subframe blur of the final render |
| Continuity | 9 | no cuts; token, mark and lockup are one object |
| Variety and pacing | 8 | pacing.py: 22% still, CV 0.80, spread 16.8x; refs 9-21% still, CV 0.61-0.83 |
| Composition | 6 | 7-17 s the client sits high and small: lower half empty; 29.0-29.7 a lone small symbol |
| Brand accuracy | 9 | as round 0 |
| Sound | 8 | audio_qa all PASS except low-mid warnings that come from the voice itself (same flags on the voice alone) |
| Message with the sound off | 8 | as round 0 |

Automatic checks:
- `tools/seekcheck.mjs`: PASS (same frame on revisit at 24 times; seek every 0.1 s without errors)
- `tools/pacing.py`: PASS (22% still, longest quiet run 1.75 s, no frozen stretch, CV 0.80, spread 16.8x)
- `tools/audio_qa.py`: -14.0 LUFS, -1.5 dBTP, no dropouts, music 15.8 dB under the voice; WARN low-mid (voice-driven)
- `tools/safezone.mjs`: ok (top 250, bottom 400, right 140, left 96, min 44 px)

Three worst problems and the fix for each:
1. Empty lower half 7-17 s: the camera now re-frames the waiting client on each beat (lower and larger, then up
   for the message card, then back down).
2. Lone small symbol 29.0-29.7: "Këtë sistem / e ndërtojmë ne." stays until the wordmark wipes in.
3. The message card faded out: it now wipes up out of a mask, like every other element.

## Round 2 · 2026-10-13 · draft cut 2 (15 fps, after the round 1 fixes)
Sheets: `out/contact.png`, `out/strip.png` (25.4), `out/r1_fix.png`, `out/r2_fix.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | unchanged |
| Readability at phone size | 7 → 9 | 24.6-26.4 ivory headline over the passing gold block of the mark (low contrast); fixed with a soft dark drop shadow on the lines that cross the moving mark (beats 2, 3, 10) |
| Motion quality | 8 | camera re-frames on beats 4-9 read as deliberate moves; final render adds 4-subframe blur |
| Continuity | 9 | card now wipes up out of a mask instead of fading |
| Variety and pacing | 8 | pacing.py: 24% still, CV 0.55, spread 10.2x |
| Composition | 8 | 7-17 s client lower and larger; 29.0-29.7 the line holds until the wordmark wipes in |
| Brand accuracy | 9 | unchanged |
| Sound | 8 | as round 1 |
| Message with the sound off | 8 | unchanged |

Automatic checks: seekcheck PASS, pacing PASS (all 5), safezone ok, audio_qa PASS except the voice-driven low-mid WARN.

Three worst problems and the fix for each:
1. Headline over the gold block during the pull-back: soft dark shadow (no glow) on lines over the moving mark.
2. Final render too slow (about 4 min per film second with three processes): the renderer blended subframes with
   four full readbacks and a JS loop per frame. `render.mjs` now keeps a running mean on the canvas (2x faster,
   mean error 0.1 of a level, max 3 levels, measured on 3 frames).
3. Open (logged, not fixed): low-mid WARN in audio_qa comes from the voice itself (same flags on the voice alone);
   a gentle voice EQ (-3 dB at 230 Hz) already reduced it from 12 to 10 flagged seconds.
