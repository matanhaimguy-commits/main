# Review log: StraightScale · reel 05 "Three things, one system"

Every round is logged. Never ship with a known blemish without writing it here and telling the client.
Engine: canvas, so the safe-zone gate is `tools/safezone.mjs` (the canvas equivalent of HyperFrames
`check --caption-zone`, which does not apply to this page). Reading time: `tools/readcheck.mjs` (this project; same
rule as Lemo-Opuscar `core/render/readcheck.mjs`: each block stays fully visible >= max(1.5 s, chars/15 + 1.5 s)).

## Round 0 · 2026-10-20 · styleframes (straight from the page)
Sheets: `out/sf1.png`, `out/sf1_big.png`, `out/crop_lock.png`, `out/sf2.png`, `out/sf4x5_1.png`
- The top label ("Replies") sat 40 px under the question's descenders: triangle moved down (y 1105 -> 1165 after
  round 1), question top 318 -> 300.
- The triangle was visibly tilted at rest (step spring k 420 d 30 still ringing 0.25 s later): k 700 d 44.
- The lockup at 1.27x checked at 1:1 (`out/crop_lock.png`): letters clean, hi-res mark registered on the file's mark.
- Adjacent per-letter clips could leave hairline seams: once every letter is in, the wordmark is drawn through one clip.

## Round 1 · 2026-10-20 · draft 1 (30 fps, 2 subframes, 15.25 s, raw unmastered mix)
Sheets: `out/review_r1_contact.png` (one frame per beat, 240 px wide), `out/strips_r1.png` (12 frames around the
merge, the launch, the fall and the slide), `out/spectrogram_r1.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 7 | dots pop on notes at 0.06-0.34, question from 0.78; dots and labels small at phone size |
| Readability at phone size | 7 | labels 46 px read small; CTA 50 px is the weakest line on the end card |
| Motion quality | 7 | springs and squash read well; launch 5.3-5.5 strobes as double images at 30 fps / 2 subframes (draft setting) |
| Continuity | 9 | one object from frame 1 to the lockup; no cuts |
| Variety and pacing | 6 | pacing.py FAIL: frozen 11.5-14.83 s (3.33 s); longest quiet run 5.42 s |
| Composition | 7 | safezone FAIL: "Replies"/"Posts"/"Follow-ups" bottom edge 1549 > 1520 when a label passes the bottom of its ring mid-step (t 1.6, 2.1, 2.5) |
| Brand accuracy | 9 | real files only, brand colours and type, no banned words |
| Sound | 6 | raw mix -22.9 LUFS (not mastered yet); wood ticks 5-6 dB under the bed; the CTA click inaudible (-60 dB) |
| Message with the sound off | 8 | question, three-become-one, lockup, lines, CTA all on screen |

Automatic checks:
- `tools/seekcheck.mjs`: PASS (same frame on revisit at 24 times; seek runs every 0.1 s)
- `tools/pacing.py` draft1: still 36%, quiet 71%, 0 transitions; FAIL frozen (11.5, 3.33 s); CV 0.73, spread 28x.
  Reference card tt-rafaellfreitaas: 0 cuts per 10 s, mean 8.0 s between big changes, quiet share 0.2 (the card notes
  its metrics read flat because the elements are tiny; the real rhythm is a state change about every 0.5 s for 5 s,
  then a 2 s hold). Ours matches the grammar: 0 cuts, a change every 0.5 s for the first 8 s, then a calm end card.
- `tools/audio_qa.py` draft1: FAIL loudness -22.9 LUFS (unmastered), TP -1.0, no dropouts, mud at 10.0 s.
- `tools/safezone.mjs`: FAIL (labels, see above). `tools/readcheck.mjs`: all blocks OK (CTA margin 0.07 s only).

Three worst problems and the fix for each:
1. Frozen end card (3.33 s): CTA moved to 9.7 s, exit to 14.25 s (film 14.75 s), and the gold rule under
   "one step a week." now grows in steps on the beat with a harp note each.
2. Labels outside the bottom safe line and crowding: labels ride an elliptical ring (262 x 318 px), triangle centre
   y 1165, labels 50 px, dots 21 px.
3. Sound balance: ticks +10 dB, CTA click +9 dB and a vibraphone D5 under the CTA; mastering stage added.

## Round 2 · 2026-10-20 · draft 2 (30 fps, 2 subframes, 14.75 s) and the first master
Sheets: `out/review_r2_contact.png`, `out/sf5.png` (merge core and the end-card steps), `out/audio_qa_r2.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | as round 1, larger dots and labels, clear gap under the question |
| Readability at phone size | 8 | CTA 56 px; every block passes the reading rule; labels 50 px |
| Motion quality | 8 | the merge's ivory core read as a hard pink disc (a "target") at 4.62-4.70 |
| Continuity | 9 | unchanged |
| Variety and pacing | 7 | pacing.py still FAIL frozen (10.75, 3.58 s): a 5 px rule growing is under the tool's motion threshold, and it barely reads at phone size either |
| Composition | 8 | safe zones ok on 9:16 and 4:5 |
| Brand accuracy | 9 | unchanged |
| Sound | 7 | first master reached only -15.3 LUFS (crest about 21 dB: the merge and the thud are 15 dB over the quiet bed, so linear loudnorm hit the true-peak ceiling); mud at 10.0, 10.5, 13.5 s from the low strings in the end pad; a level dip 0.5-1.5 s while the bed faded in over 1.4 s |
| Message with the sound off | 9 | the step rule makes "one step a week" visible |

Automatic checks:
- `tools/seekcheck.mjs`: PASS (30 times, 9:16; 20 times, 4:5)
- `tools/pacing.py` draft2: still 34%, quiet 70%, FAIL frozen (10.75, 3.58 s), CV 0.72, spread 27x
- `tools/audio_qa.py` draft2 after the first master: FAIL -15.3 LUFS, TP -1.9, mud at 10.0/10.5/13.5 s;
  after the fixes below: PASS -14.0 LUFS, TP -1.9 dBTP, no dropouts, no mud
- `tools/safezone.mjs`: ok (9:16 default zones; 4:5 with margins 80/92/92/80 px). `tools/readcheck.mjs`: all OK
  (CTA 3.80 s against 3.57 s needed)

Three worst problems and the fix for each:
1. End card still frozen to the pacing tool: the rule now steps under one word per beat ("one", "step", "a",
   "week.") and each word hops 12 px as the rule reaches it; rule 6 px.
2. Hard merge core: replaced by a radial ivory gradient that fades in 90 ms.
3. Loudness and mud: master is now pre-gain plus a 3 ms look-ahead limiter (aimed in three passes at -14.2 LUFS),
   then two-pass linear loudnorm to -14 LUFS / -2.0 dBTP before AAC; music bus high-passed at 60 Hz with a -4 dB dip
   at 230 Hz; low strings in the end pad lowered (cellos 0.36 -> 0.24, contrabass 0.3 -> 0.18) while the pad as a
   whole came up 4 dB; the spinner bed came up 2.7 dB and fades in over 0.7 s.

## Round 3 · 2026-10-20 · v1 final (60 fps, 8 subframes per frame, mastered and muxed)
Sheets: `out/review_r3_contact.png` (= `deliver/v1/contact-sheet.jpg`), `out/review_r3_strips.png` (14 frames at
60 fps around the collapse 4.38 s, the launch 5.28 s, the fall 5.88 s and the slide 7.0 s),
`deliver/v1/contact-sheet-4x5.jpg`, `out/audio_qa_v1_9x16.png`, `out/spectrogram_v1.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | motion at 0.06 s, three notes, the question complete by 2.0 s; a slow-build hook by design (like the reference), not a shock open |
| Readability at phone size | 9 | all blocks pass the reading rule on both formats; smallest text 46-50 px labels |
| Motion quality | 9 | strips: the spiral, the launch (up to about 95 px per frame) and the fall smear smoothly with 8 subframes, no strobing; squash, stretch along the velocity and the impact read as weight |
| Continuity | 9 | dots -> ball -> real mark -> lockup -> end card, one object, no cuts; the question parts where the ball passes |
| Variety and pacing | 8 | no frozen stretch; longest quiet run 5.0 s is the end card while only the steps and hops move (at the tool's limit) |
| Composition | 8 | one left edge for all text; safe zones clean; the 9:16 end card leaves 1300-1520 px empty (above the platform's bottom UI band) |
| Brand accuracy | 9 | only the real logo files (masked, scaled, faded), brand colours by role, Playfair + Montserrat, no banned words, no numbers |
| Sound | 8 | measured, not heard: the pops, merge, whooshes, thud and reveal sit 12-33 dB over the bed in their 150 ms windows, the wood ticks 2-4 dB over it; the end-card cues are musical (harp steps, vibraphone) and live in the music stem; the merge and the thud are the loudest moments; planned near-silence while the ball is off screen; ends on the chord's tail and air, faded to digital silence for the loop |
| Message with the sound off | 9 | the words carry it: question, answer, CTA |

Automatic checks (final files):
- `tools/seekcheck.mjs`: PASS on both formats (same frame on revisit; seek every 0.1 s without errors)
- `tools/pacing.py` 9:16: 14.75 s, still 23%, quiet 72%, 0 transitions, longest quiet run 5.0 s (PASS),
  no frozen stretch over 3 s (PASS), beat rhythm CV 1.09 (PASS), spread 27x (PASS).
  4:5: still 22%, quiet 70%, longest quiet 4.92 s, no frozen stretch, CV 1.36. Reference: 0 cuts per 10 s (ours 0),
  change about every 0.5 s through the build (ours: 0.5 s spinner grid through 8 s), 2 s hold (ours: 1.2 s hold after
  the last step before the exit, and the 0.45 s rest on the revealed mark).
- `tools/audio_qa.py` on both delivered MP4s: PASS -14.0 LUFS integrated, PASS true peak -1.9 dBTP (after AAC),
  PASS no dropouts, PASS no low-mid mud. Spectrogram checked: riser sweep into 4.5 s, broadband merge, gap 5.6-5.9 s,
  thud at 6.08 s, chord at 7.87 s, harp steps 11.25-12.75 s, silence at the end.
- `tools/safezone.mjs`: ok (9:16: top 250, bottom 400, right 140, left 96, min 44 px; 4:5: margins 80/92/92/80).
- `tools/readcheck.mjs`: every block OK on both formats.
- Frame count 885 = 14.75 s x 60 fps on both; loop seam: first and last frames are both the empty charcoal frame
  (mean difference 0.63 grey levels, encoding noise).

Known and accepted (told to the owner):
1. Nobody has listened yet. Levels, sync and the spectrogram are measured; a phone-speaker and headphone listen is
   needed before posting (especially the wobble after the merge: tuned low and soft, but taste is a human call).
2. The sound is quiet for the first second after the three notes (about -37 dB RMS windows at 0.5-1.5 s): the slow
   build is deliberate, but if the first plays in the feed feel flat, raise the bed there.
3. The CTA promises a weekly series ("one step a week"); the series has to exist before this is posted.

## Independent review of v1 (`docs/review_independent_r1.md`): FAIL. What v2 does about each finding
| # | Severity | Finding | v2 change (in `index.html` / `audio/score.py`) | Measured on v2 |
|---|---|---|---|---|
| 1 | major | M5: hook text not on screen by 0.3 s (frame 0 empty, question from 0.78 s, full at 2.0 s) | "Still running / your business" is set on frame 0: its words rise from -0.44 s, and the page draws them again on (t - 14.0) in the last 0.44 s, so the end card lifts out while the question rises into frame 0. "on three / separate things?" starts 0.48 s. Labels moved after the question (0.90 / 1.02 / 1.14 s) | readcheck: question-1 fully visible at 0.00 s, question-2 at 0.96 s; loop seam frame 839 vs frame 0 mean 0.64/255 (same as any two neighbouring frames) |
| 2 | major | M3: text in the STANDARDS section 6 zone (bottom labels to 1447 px, "Follow-ups" right edge 918 px, CTA line 2 at 1300 px) | 9:16 text column x 96-853 (headline fitted to 757 px: 98 px, was 104); triangle centre y 1165 -> 980, R0 212 -> 170, cx 518 -> 500; labels now hang under their own dot (see 3); lockup 585 -> 515, "One system." 862 -> 792, "Built around" 962/1052 -> 892/982, CTA 1206/1282 -> 1136/1212 (the reviewer's numbers) | `safezone.mjs --top 269 --bottom 672 --right 227 --left 65 --min 44 --step 0.02`: ok (it applies the right margin at every height, so no false positive on the headline either). Text extremes: labels y 834-1240, x 184-812; CTA bottom 1230; rule 1237 |
| 3 | minor | stacked label copies on every spinner step | speed-driven in-page samples for the labels and the dots: each of the 8 subframes adds 1 to 24 samples across its 1/480 s slice (one per 1.5 px of travel), summed with 'lighter' at 1/n on a side canvas (an exact average). While fixing it, a second fault showed: on the v1 ring a label crossed its own dot mid-step and, in the slow tail of each step, a dot sat on top of a word for a few frames (1.6 s in `out/v2_sf2.png`). Each label now hangs 10 px under its own dot and turns with it, so it can never cross a dot or another label | strips at 60 fps (`out/v2_review_r5_strips.png`, row 1, frames 90-97): words smear continuously, no stacked copies, no dot over a word |
| 4 | minor | end card sags (5.0 s quiet run, 40% of the film) | "One system." 8.3 -> 8.2, CTA 9.7 -> 9.3, steps 11.25 -> 10.65 (three steps now), exit 14.25 -> 13.45, film 14.75 -> 14.0; the pad under the hold barely decays (floor 0.45 -> 0.85) | pacing.py: longest quiet run 4.25 s (v1 5.0), no frozen stretch; CTA fully visible 3.52 s against 3.43 s needed |
| 5 | minor | mark revealed at y 585 with the lower frame empty; the landing implies a floor that is not there | the ball lands on the floor it took off from (y 980, near frame centre) with its bottom held on that floor while it squashes; the mark is revealed there and then rises into the lockup row (y spring k 220 d 26 from 6.80 s) before the left slide (k 190 d 23 from 7.0 s): one curved FLIP | contact sheet 6.1 / 6.4 / 6.95 / 7.3 s; the empty band under the end card is now the section 6 bottom zone (1248-1920), kept clear on purpose |
| 6 | minor | bed about 8 dB under the mix while the question builds, -24 to -26 dBFS through the final hold | bowed bed enters mid-bow (the sample's 0.45 s attack skipped), fades in over 0.2 s, base +3 dB (0.55 -> 0.78) and a further lift to 1.0 s; ticks +5.4 dB to stay over it; label harp notes; end pad floor 0.85 | same -14.0 LUFS master: 0.5-1.5 s window -18.3 dBFS (v1 -21.7, +3.4 dB); 12.0-13.45 hold -21.6 dBFS (v1 13.0-14.25 -24.8, +3.2 dB); ticks 2.7-5.9 dB over the music in their 150 ms windows |
| 7 | minor | CTA "one step a week." promises a weekly series that does not exist; G-MOTION-TEXT not recorded; safezone run with the overruled zone | CTA line 2 is now "step by step." (no cadence, still a follow CTA, the rule still steps one word per beat). G-MOTION-TEXT self-check below. Section 6 safe zone run on v2 | see the G-MOTION-TEXT record; "the build" still points at content (The Build / One Step series in the content map are not live yet): owner check before posting |

## Round 4 · 2026-10-20 · v2 draft 1 (30 fps, 2 subframes, 14.0 s)
Sheets: `out/v2_sf1.png`, `out/v2_sf2.png` (styleframes from the page), `out/v2_steps_strip.png` and
`out/v2_steps_strip2.png` (60 fps / 8-subframe emulation around a step), `out/v2_review_r1_contact.png`,
`out/v2_spectrogram_r1.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook (STANDARDS M5: text by 0.3 s) | 8 | block 1 set on frame 0, block 2 complete 0.94 s, dots pop 0.06-0.34 |
| Readability at phone size | 7 | readcheck BAD: "Follow-ups" fully visible 2.08 s against 2.17 s needed; CTA 3.44 s against 3.43 s (no margin) |
| Motion quality | 7 | first label layout put a dot on top of a word in the tail of each step (1.6 s); after the hang-under fix, dots still stacked as copies (only the labels were sampled) |
| Continuity | 9 | one object from the dots to the lockup; the loop seam now flows (question rises into frame 0) |
| Variety and pacing | 8 | pacing.py: longest quiet run 4.25 s, no frozen stretch, CV 0.84 |
| Composition | 8 | reveal at frame centre, then the rise into the lockup; text inside the section 6 zone |
| Brand accuracy | 9 | real files only, colours and type unchanged |
| Sound | 7 | the bed under the question was only +1.9 dB over v1: the bowed vibraphone takes about 0.5 s to speak (sampler level -80 to -46 dB over its first 0.5 s); ticks -0.5 dB against the lifted bed at 1.5 s |
| Message with the sound off | 9 | question from frame 0, three labelled things, one ball, the mark, the line, the CTA |

Automatic checks: seekcheck PASS (30 times); safezone (section 6 zone, step 0.02 s) ok; readcheck 1 BAD (above);
pacing.py PASS (still 19%, quiet 72%, longest quiet 4.25 s, CV 0.84, spread 24.8x); audio_qa on the master PASS
(-14.0 LUFS, TP -2.0 dBTP).

Three worst problems and the fix for each:
1. Dots stacking and a dot over a word mid-step: labels hang under their own dot; dots get the same speed-driven samples.
2. Reading time: labels in at 0.90 / 1.02 / 1.14 s (was 0.95 / 1.10 / 1.25) and out from 3.40 s (was 3.32); CTA 9.35 -> 9.30.
3. Bed under the question and buried ticks: the bowed notes enter mid-bow (0.45 s skipped), 0.2 s fade, a lift to
   1.0 s; ticks +5.4 dB.

## Round 5 · 2026-10-20 · v2 draft 2 (30 fps) and v2 final (60 fps, 8 subframes, mastered and muxed)
Sheets: `out/v2_review_r4_contact.png` (draft 2), `out/v2_review_r5_contact.png` (= `deliver/v2/contact-sheet.jpg`),
`out/v2_review_r5_contact_4x5.png` (= `deliver/v2/contact-sheet-4x5.jpg`), `out/v2_review_r5_strips.png` (60 fps
frames around a step 1.50-1.62 s, the merge and launch 4.40-5.37 s, the landing and reveal 6.05-6.27 s, the rise and
slide 6.80-7.33 s, and the loop seam 13.87-0.10 s), `out/v2_sf_4x5.png`, `out/v2_audio_qa_r4.png`,
`out/v2_audio_qa_final_9x16.png`, `out/v2_audio_qa_final_4x5.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook (STANDARDS M5) | 9 | block 1 readable on frame 0 (98 px Playfair 900), full question at 0.96 s, motion at 0.06 s |
| Readability at phone size | 9 | every block passes the reading rule on both formats; smallest text 50 px labels (46 px on 4:5) |
| Motion quality | 9 | steps smear continuously (no stacked copies, no dot over a word); squash on a real floor; the curved rise and slide reads as one move |
| Continuity | 9 | dots, ball, mark, lockup, end card, question again: one continuous film and a seamless loop |
| Variety and pacing | 8 | pacing.py PASS, longest quiet run 4.25 s; merge still at 4.5 s against the card's 2.0 s (the question and the three labels need the time to be read) |
| Composition | 8 | reveal near frame centre, lockup and end card in the 269-1248 band; the bottom 35% stays empty by the section 6 rule |
| Brand accuracy | 9 | only the real logo files (masked, scaled, faded), brand colours by role, Playfair + Montserrat, no numbers or banned words |
| Sound | 8 | measured, not heard: pops, merge and thud onsets within 3 ms of the picture (one 2.5 ms analysis frame), ticks 0 ms on the effects stem, bed +3.4 dB under the question, hold +3.2 dB; nobody has listened |
| Message with the sound off | 9 | unchanged idea, now with the question from the first frame |

Automatic checks on the final files (`deliver/v2/`):
- `tools/seekcheck.mjs`: PASS on 9:16 (30 times) and 4:5 (20 times); seek every 0.1 s without errors.
- `tools/safezone.mjs` 9:16 with the STANDARDS section 6 zone (`--top 269 --bottom 672 --right 227 --left 65 --min 44
  --step 0.02`): ok. 4:5 (`--top 80 --bottom 650 --right 92 --left 92`, i.e. y 80-1270, x 92-988): ok.
- `tools/readcheck.mjs`: all 8 blocks OK on both formats (question-1 full at 0.00 s; Follow-ups 2.28 s of 2.17 s; CTA
  3.52 s of 3.43 s).
- `tools/pacing.py` 9:16: 14.0 s, still 21%, quiet 72%, 0 transitions, longest quiet run 4.25 s, no frozen stretch,
  CV 0.70, spread 24.8x, all PASS. 4:5: still 21%, quiet 67%, same runs, all PASS. v1 was 5.0 s longest quiet run.
  Reference tt-rafaellfreitaas: 0 cuts (ours 0), a state change about every 0.5 s through the build (ours: 0.12 to
  0.5 s through 8 s), merge at 2.0 s (ours 4.5 s), 2 s hold (ours 1.5 s rest 11.95-13.45 s).
- `tools/audio_qa.py` on both MP4s: PASS -14.0 LUFS integrated, PASS true peak -2.0 dBTP after AAC, no dropouts, no
  low-mid mud. ebur128: LRA 4.2 LU. Spectrogram: bed from 0.0 s, pops, label harp notes, ticks on the beats, riser into
  4.5 s, gap 5.6-5.84 s, thud 6.08 s, rise and slide airs 6.8 / 7.0 s, chord 7.87 s, step airs 10.65-11.65 s, exit
  13.45 s, silence at the end.
- Frames: 840 = 14.0 s x 60 fps on both; segment joins (frames 279/280 and 559/560) differ only by codec noise at the
  new GOP (mean 0.86 and 0.75 grey levels, max 107 on text edges, same as neighbouring pairs); loop seam frame 839 vs 0:
  mean 0.64 (the question settling by one frame of motion, like any neighbouring pair).

Known and accepted (told to the owner):
1. Nobody has listened yet (phone speaker and headphones), the bed lift especially.
2. "Follow for the build, step by step." still points at build content; the content map's The Build and One Step
   series are not live yet. No cadence is promised any more, but the owner decides whether this CTA or the brand's
   one path (comment ANALIZA) fits this reach post.
3. The merge stays at 4.5 s (the card's at 2.0 s): the question, three labels and four spinner beats need that time.
4. The CTA card runs 4.15 s, longer than STANDARDS' 2.5-3 s end card, because the reading-time rule needs 3.43 s.

## G-MOTION-TEXT record, v2 (self-check, not a fresh reviewer)
STANDARDS section 9 wants a fresh prompt-reviewer to check the code's text constants, layout, timing table and colours
before the render, recorded with `pipeline.py record` on the `motion_render` version. The ledger lives in
`clients/straightscale/runs/`, which this job may not write, so this is the maker's own check, written here. Open item:
a fresh reviewer and the ledger record before the hub.
- M1 spelling (constants in `index.html`): "Still running" / "your business" / "on" "three" / "separate things?" ·
  "Posts" / "Replies" / "Follow-ups" · "One system." · "Built around" / "your business." · "Follow for the build," /
  "step by step." All correct English; no em or en dashes; no numbers, prices, results, names, platforms, guarantees,
  deadlines or hype words.
- M3 layout: 9:16 text x 96-853, y 292-1240 (section 6 zone y 269-1248, x 65-853); 4:5 text x 92-920, y 106-1053
  (margins 80/92). Contrast: ivory on charcoal about 15:1, gold on charcoal 6.8:1; no gold text on ivory, no red text.
- M4 timing table: `T` in `index.html` matches section 6 of `docs/treatment.md` (exported to `audio/events.json`).
  No voice.
- M6 colours and fonts: C = charcoal #1F1F1F, ivory #F8F6EF, gold #DD9A10, crimson #B31217 (ball), mark-red only inside
  the logo file; Playfair Display 900 / 900 italic / 700 italic and Montserrat 600 / 700, self-hosted.
