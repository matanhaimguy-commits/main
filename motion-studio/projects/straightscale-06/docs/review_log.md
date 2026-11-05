# Review log: StraightScale · 06 "The 108-hour week"

Every round is logged. Never ship with a known blemish without writing it here and telling the client.
Nobody has listened to the mix yet: every sound judgement below is from measurements and spectrograms.

## Round 0 · 2026-10-20 · styleframes (page stills, no compile)
Sheets: `out/sf1_sheet.jpg`, `out/sf2_sheet.jpg`, `out/full/crop9.png`, `out/sf45_sheet.jpg`
Not scored; fixed before the first draft:
1. The day name rolled in too slowly and was unreadable on most day changes, and the time jumped sideways with the
   day's width: now a two-line roll (yesterday leaves, today arrives) in about 0.15 s, fixed-width day box.
2. Glyph tips (descenders, ascenders) peeked out of the masks after exits: lines now travel 160 % and are hidden once
   fully outside their mask.
3. "Comment" rose while "instant replies," was still leaving at the same place: system lines now clear 0.14 s
   before the CTA, the CTA starts 0.16 s later.
4. Five weekend bubbles piled into one clump: four bubbles, two rows 52 px apart; "SUN" and the last "MON" labels
   nudged apart.
5. A 4-line 76 px headline left the chart small: 3 lines at 80 px; the chart grew from 346 to 380 px tall.

## Round 1 · 2026-10-20 · draft 1 (HyperFrames render, 30 fps, silent): `out/draft1_9x16.mp4`
Sheets: `out/draft1_sheet.jpg` (one frame per beat), `out/strip_rescale.jpg` (axis rescale 3.15-3.9 s),
`out/strip_land.jpg` (landing and the 108 flight 9.75-13.1 s), `out/full/strip_cta.png` (CTA fold 17.45-17.9 s)

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | 0.0 s: the whole claim is readable, clock already ticking; first climb 0.56 s, first bubble 0.67 s |
| Readability at phone size | 8 | headline 80 px, body >= 44 px, clock 116 px; axis labels 30 px are secondary |
| Motion quality (weight, easing, blur, no strobing) | 8 | springs on rescale (3.22, 5.89 s) settle without jitter; 108 punch; day roll still 2 frames mid-roll |
| Continuity (beats grow out of each other, no swaps) | 8 | tip -> 108 into its sentence (12.6 s) -> light over the closed hours (14.2 s) -> caret -> logo square (19.2 s) |
| Variety and pacing | 6 | pacing.py: frozen stretch 19.75-24.0 s (4.25 s) FAIL |
| Composition (focal point, no empty halves, safe zones) | 8 | textcheck: 0 box-samples outside the zones; weekend bubbles' badges touch their neighbours |
| Brand accuracy (real logo, colours, type, voice) | 9 | wordmark-white.png only masked; mark-gold accent; Playfair + Montserrat self-hosted |
| Sound | n/a | silent draft |
| Message clear with the sound off | 9 | every claim is on screen; no voice needed |

Automatic checks:
- `tools/seekcheck_hf.mjs` (our HyperFrames adaptation of tools/seekcheck.mjs, which reads a canvas): PASS, same
  frame on revisit at 30 sample times; seek every 0.1 s without errors.
- `tools/pacing.py out/draft1_9x16.mp4`: still 32 %, quiet 84 %, 0 transitions (cuts), beat CV 0.51, FAIL frozen
  (19.75, 4.25 s). Reference card: 0.0 cuts per 10 s, quiet share 0.16 at 2 fps, CV 0.0; category median 0.7 cuts
  per 10 s. Like the reference, the film is one continuous shot with detail motion; unlike it, it adds four big
  changes (math, swap, sweep, fold).
- HyperFrames `check --caption-zone "x0=0;y0=.8;x1=1;y1=1;severity=error"`: PASS after fixes (it first flagged text
  translated out of its mask as "occluded" and a transparent slot; both resolved by hiding off-mask text).
- `tools/textcheck.mjs` (reading time + safe zones top 14 %, bottom 20 %, right 140 px): all lines OK, zone PASS.

Three worst problems and the fix for each:
1. Frozen end hold of 4.25 s: a gold rule draws under ANALIZA at 21.22 s (on the C6 piano note); frozen tail now 2.3 s.
2. Weekend answer badges overlapped the bubbles of the other row: rows 52 px apart (lane y + 40 / + 92); the 4:5 lane
   moved up 10 px to keep the lower row clear of the plot.
3. (Sound, first mix) pulses sat 13 dB over the music and the landing was quieter than its approach (-10.3 vs -9.1
   LUFS momentary): pulses -8 dB, ticks and air lower and low-passed, a 0.12 s string breath before the landing,
   landing chord and pulse up, the rest before the CTA quieter.

## Round 2 · 2026-10-20 · draft 2, both formats with the mix: `out/draft_9x16.mp4`, `out/draft_4x5.mp4`
Sheets: `out/round2_sheet_9x16.jpg` (18 frames), `out/round2_sheet_4x5.jpg` (8 frames), `out/full/end_check.png`,
spectrogram `out/spectrum_mix.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | frame 0 has the full claim and a piano note; the first pulse lands with the first climb (0.56 s) |
| Readability at phone size | 9 | textcheck: every line meets max(1.5, chars/15 + 1.5) s; smallest reading text 44 px (9:16), 42 px (4:5) |
| Motion quality | 8 | 108 drop-and-slide clean (12.6-13.3 s); fold at 17.6 s is busy for 0.4 s but reads as one gesture |
| Continuity | 9 | one survivor chain from the first frame to the logo; no hard cuts |
| Variety and pacing | 8 | no frozen stretch over 3 s; rests 10.19-11.22 s and 16.0-17.56 s planned; something changes every 0.33-1.78 s |
| Composition | 8 | safe zones PASS on both formats; 4:5 is its own layout (3-line headline, wider plot), not a crop |
| Brand accuracy | 9 | real logo revealed by a clip from its own gold square; one accent; voice calm, no hype words |
| Sound (sync, mix, ending) | 8 | -14.0 LUFS, TP -3.2 dBTP; every landing louder than its approach (land -14.2 -> -9.2; math3 -29.0 -> -10.0; turn -20.7 -> -17.7; CTA -19.2 -> -12.6; logo -21.7 -> -10.6 LUFS momentary); V-I cadence on the logo |
| Message clear with the sound off | 9 | unchanged |

Automatic checks:
- `tools/pacing.py out/draft_9x16.mp4`: PASS rests (32 % still), PASS frozen (none over 3 s), PASS beat CV 0.51;
  WARN longest quiet run 5.58 s (detail motion only: the clock and line are the only movers during the crawl, which is
  the reference's grammar; the reference's whole 13 s is one quiet run); WARN beat spread 3.3x (the energy detector
  sees only two big peaks; the designed beat sheet has a 12x spread, CV 0.85).
- `tools/audio_qa.py out/draft_9x16.mp4`: PASS -14.0 LUFS, PASS true peak -3.2 dBTP, PASS no dropouts, PASS mud
  (one 0.5 s window at 16.5 s: cellos A2 + piano A2 under the rest; left, it is the quietest section).
- `tools/seekcheck_hf.mjs`: PASS both formats. HyperFrames check (caption band): PASS. textcheck: PASS both formats.

Three worst problems and the fix for each (none blocking; all logged):
1. The CTA fold (17.45-17.9 s) has four things moving at once (two exits, the fold, the square's flight). Accepted:
   0.4 s, one direction each, reads as "the board clears". Next version: sequence the math exit after the fold.
2. A 17.4 kHz tonal line in the first 9 s of the spectrogram (a sampler harmonic); inaudible on phones, left in.
3. During the 18 h/s crawl the day name is mid-roll for about 2 frames per day; readable everywhere else.

## Round 3 · 2026-10-20 · delivered v1 (60 fps masters with AAC): `deliver/v1/`
Sheets: `deliver/v1/contact-sheet.jpg` (13 beats), `deliver/v1/contact-sheet-4x5.jpg`, spectrogram `out/spectrum_final.png`

| Axis | Score /10 | Evidence |
|---|---|---|
| Hook in the first 2 s | 8 | unchanged from round 2 |
| Readability at phone size | 9 | textcheck PASS both formats |
| Motion quality | 8 | 60 fps master: the 18 h/s clock and the line read smoother than the 30 fps drafts |
| Continuity | 9 | unchanged |
| Variety and pacing | 8 | pacing.py on the master: no frozen stretch over 3 s, rests 32 %, beat CV 0.48 |
| Composition | 8 | safe zones PASS; caption band PASS |
| Brand accuracy | 9 | real logo file, one accent, no banned words or numbers |
| Sound | 8 | -14.0 LUFS, TP -3.1 dBTP after AAC, no dropouts; not yet heard by a person |
| Message clear with the sound off | 9 | |

Automatic checks on the delivered files:
- `ffprobe`: 9:16 1080x1920, 4:5 1080x1350, both H.264 60/1 fps, 1440 frames, 24.000 s, AAC 48 kHz stereo.
- `tools/audio_qa.py` on both mp4s: PASS -14.0 LUFS, PASS true peak -3.1 dBTP, PASS dropouts, PASS mud (one window).
- `tools/pacing.py` on the 9:16 master: still 32 %, quiet 85 %, 0 cuts, CV 0.48; WARN longest quiet run 5.58 s
  (detail motion only). Against the reference card (0.0 cuts per 10 s, 13.0 s between big changes, quiet share 0.16
  at 2 fps): same one-shot grammar, more big changes (about one every 1.8 s over the second half, against the
  category median of 3.75 s), because our film adds the arithmetic, the answer beat and the CTA.
  Correction (after the independent review): the 1.8 s figure counts DESIGNED beats from the beat sheet, not measured
  picture changes. Measured at the reference's own scale (`refbank/tools/frames_metrics.py`, 2 fps): 1 big change,
  mean gap 12.0 s (reference 13.0 s), quiet share 0.36 (reference 0.16), hook change 0.017 (reference 0.01).
- HyperFrames `check` on film/ (with the bottom-20 % caption band) and film-4x5/: passed, 0 errors, contrast 111/111.
- `tools/seekcheck_hf.mjs`: PASS on both formats. `tools/textcheck.mjs`: PASS on both formats.

Known and accepted (told to the user): the CTA fold is busy for 0.4 s; the day name is mid-roll for about 2 frames
per day during the crawl; a 17.4 kHz sampler harmonic in the first 9 s; the list "instant replies, follow-up,
booking." meets the reading rule item by item but not as one 33-character block (2.2 s against 3.7 s), because each
item appears with its own beat; nobody has listened yet.

## Round 4 · 2026-10-20 · v2 after the independent review: `deliver/v2/`
Input: `docs/review_independent_r1.md` (PASS, 11 minor findings). Sheets: `deliver/v2/contact-sheet.jpg`,
`deliver/v2/contact-sheet-4x5.jpg`; exact-frame strips of the day roll (frames 126-135) and the CTA fold and hop
(frames 1050-1158) were looked at at 270 px wide; spectrogram `out/spectrum_v2.png`.

| Axis | Score /10 | Evidence |
|---|---|---|
| Hook in the first 2 s | 8 | unchanged: full claim at frame 0, clock ticking at 0.067 s, first climb 0.556 s |
| Readability at phone size | 9 | payoff "Closed 108." 80 px; axis labels at 360 px: core 6.4:1, median 3.8:1 (v1 5.5 / 3.1), level with the note (5.8 / 3.6); textcheck PASS both formats |
| Motion quality | 9 | midnight reads the new day; 2 mid-roll frames per day at 60 fps (v1 3-5); CTA fold sequenced (max three movers); hop peak under 66 px/frame |
| Continuity | 9 | unchanged chain: tip, 108, lit plot, caret, logo square |
| Variety and pacing | 8 | pacing.py: no frozen stretch over 3 s, still 30 %, CV 0.48, longest quiet run 5.58 s (WARN, detail motion only, the crawl) |
| Composition | 9 | the square never covers a letter (0 overlaps, every frame, both formats); 4:5 gap under "booking." about 40 px; safe zones PASS |
| Brand accuracy | 9 | grey documented as marble 60 % over charcoal and computed from the kit; real logo, one accent |
| Sound | 8 | -14.0 LUFS, -3.0 dBTP after AAC; rule onset now detected (21.237 s, strength 6.1, v1 none); 17.4 kHz line -16 dB; still not heard by a person |
| Message clear with the sound off | 9 | unchanged; the answer now reads as gold bubbles with checks |

Automatic checks on v2:
- `ffprobe`: 9:16 1080x1920 and 4:5 1080x1350, H.264 60/1 fps, 1440 frames, 24.000 s, AAC 48 kHz stereo.
- HyperFrames `check --caption-zone "x0=0;y0=.8;x1=1;y1=1;severity=error"` on film/ and `check` on film-4x5/: passed,
  0 errors, contrast 98/98.
- `tools/seekcheck_hf.mjs`: PASS on both formats. `tools/textcheck.mjs`: PASS on both (smallest reading text 44 px
  on 9:16, 42 px on 4:5; every line meets max(1.5, chars/15 + 1.5) s).
- Hop check (our scratch script, every frame at 60 fps from the fold to the logo): 0 overlaps with Comment, ANALIZA or
  the body on either format.
- `tools/pacing.py` on the master: see the table. `frames_metrics.py` at 2 fps: 0 cuts per 10 s (ref 0.0), 1 big
  change, mean gap 12.0 s (ref 13.0), quiet share 0.36 (ref 0.16), hook change 0.017 (ref 0.01).
- `tools/audio_qa.py` on both mp4s: PASS -14.0 LUFS, PASS true peak -3.0 dBTP, PASS dropouts, PASS mud (one window at
  16.5 s, unchanged).
- Momentary loudness, mono, 400 ms windows: the turn rises (-23.4 before 13.56 s, -22.2 and -20.8 after); the rule
  window barely moves (-14.4 / -14.8) because the held logo chord dominates it, but the onset is clear.

Three worst remaining problems (none blocking):
1. The axis labels' anti-aliased median at 360 px (3.8:1) is still under 4.5:1, like the note line itself; their
   glyph cores are 6.4:1. They are chart scaffolding, not copy.
2. The headline wording "clients still write." may read slightly non-native; it is the brief's fixed copy, flagged
   for the owner.
3. Nobody has listened to the mix. The rule cue and the turn were judged from onsets and loudness only.
