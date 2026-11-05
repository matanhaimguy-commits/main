# Independent review, round 2: StraightScale reel 05 "Three things, one system" (deliver/v2)

Reviewer: fresh take-reviewer (motion mode). I did not build this film and re-measured every claim in the maker's v2
report myself. Date: 2026-10-20. Gates applied: G-MOTION-FRAMES M1 to M7 and G-FINAL F1 to F8 where they apply to a
code-rendered piece with no voice, the G-MOTION-TEXT content checks (M1, M3, M4, M6), house rules
(`motion-studio/CLAUDE.md`), onetake section 8, the brand kit, and `growth-engine/production/STANDARDS.md` (which wins on
numbers). Independence note: I read the maker's report and docs (the task packet included them), so a G-MOTION-TEXT
ledger record made from this review must carry `independent: false`.

**Verdict: PASS** (no critical or major finding; every axis 8 or more).
Both v1 majors are fixed and verified on the delivered files: the hook text is on frame 0, and every word sits inside
the STANDARDS section 6 zone. Seven minor items remain (below). Two of them are gates outside the film, not defects in
it: the G-MOTION-TEXT ledger record and a human listen. Both must be closed before the hub, and neither needs a
re-render.

## What I ran and opened
- Every frame of both delivered MP4s extracted by exact index (840 + 840 PNGs). Contact sheets every 0.5 s at 300 px
  wide (phone size) for 9:16 and at 270 px for 4:5. 60 fps strips around every fast moment: the first spinner step
  (1.47 to 1.85 s, plus a 1:1 crop of 1.517 to 1.567 s), the labels leaving and the spiral collapse (3.30 to 4.37 s),
  the merge (4.37 to 4.75 s), the crouch, launch and exit through the question (5.20 to 5.72 s), the hang, fall,
  landing and reveal (5.77 to 6.55 s, plus a 1:1 crop of 6.17 to 6.28 s), the rise, slide and letters (6.75 to
  7.95 s), the end-card steps (10.60 to 11.38 s) and the exit and loop (13.33 to 13.98 s, plus a 1:1 crop of 13.57 to
  13.73 s). I also opened the delivered poster.jpg and contact-sheet.jpg.
- Logo: the three brand PNGs are byte-identical (md5) to `projects/straightscale-03/assets/brand/`. I composited
  `wordmark-white.png` at 1.27x over charcoal and aligned it to the rendered lockup at 10.0 s: the mean difference is
  3.5/255, and only 2.1% of pixels (anti-aliased edges, plus the sharper registered hi-res mark) differ by more than
  40. Same artwork, same colours, no redraw and no recolour. The hero mark at 6.4 to 6.8 s is the same S, channel and
  gold square.
- `tools/seekcheck.mjs` on 9:16 and on `?fmt=4x5` (1080x1350); `tools/safezone.mjs` with the section 6 zone
  (`--top 269 --bottom 672 --right 227 --left 65 --min 44`, every 0.05 s); a pixel bounding-box scan of every second
  frame of both files (so the logo and the dots are checked too, not only the text boxes); `tools/pacing.py` on both
  MP4s; a frozen-run scan; `tools/audio_qa.py` with a spectrogram; `ffmpeg ebur128` and `astats` on both files; an
  onset check of the mix against `audio/events.json`; a v1-to-v2 bed level comparison; a seam check at the segment
  joins (frames 279/280 and 559/560) and at the loop (839/0).

## Measured
| Check | Result |
|---|---|
| Files | 9:16 1080x1920 and 4:5 1080x1350, H.264 High yuv420p, 60 fps, 840 frames, 14.000 s; AAC LC 48 kHz stereo; 5.40 MB and 4.22 MB. As reported. |
| Deliverables | 9x16 master, 4x5, poster.jpg (1080x1920, frame at about 2.3 s), contact-sheet.jpg, contact-sheet-4x5.jpg, captions.srt, CREDITS.md, CHANGELOG.md: all present |
| Loudness | both files: -14.0 LUFS integrated, true peak -2.0 dBTP, LRA 4.2 LU, sample peak -2.03 dBFS. audio_qa PASS (no dropouts, no low-mid mud). As reported. |
| Seek | PASS on 9:16 and 4:5 (same frame on revisit at 24 times; no errors every 0.1 s) |
| Safe zone, STANDARDS section 6 (tool) | "safe zones: ok", with no exceptions |
| Safe zone, pixel scan (9:16) | content x 86 to 871, y 285 to 1241 at every sample outside the ball flight (5.4 to 6.0 s, where the ball leaves through the top on purpose). The lockup reaches x 871 at y 437 to 591, in the upper half where only the 65 px side margin applies; every text box ends by x 846 (limit 853). Top 285 against 269; bottom 1241 against 1248. |
| Safe zone, 4:5 | content x 83 to 867, y 98 to 1046 (outside the ball flight); a feed post, no overlay UI |
| Text sizes | 9:16: question 98 px (auto-fitted from 104), labels Montserrat 600 50 px (smallest), CTA 56 px, "Built around" 86 px, "One system." 128 px. 4:5: labels 46 px, CTA 52 px. All at or above 44 px. |
| Contrast | ivory #F8F6EF on charcoal #1F1F1F about 15:1; gold #DD9A10 on charcoal 6.8:1 |
| pacing.py 9:16 | still 21%, quiet 72%, 0 transitions, longest quiet run 4.25 s, no frozen stretch over 3 s, CV 0.70, spread 24.8x: all PASS. As reported. |
| pacing.py 4:5 | still 21%, quiet 67%, longest quiet 4.25 s, CV 0.70: all PASS |
| Frozen runs (no pixel moving) | 5.58-5.83 s (0.25 s, the planned hang), 6.47-6.80 (0.33), 7.90-8.22 (0.32), 10.23-10.65 (0.42), 11.97-13.48 (1.52 s, the planned rest). Nothing important frozen over 4 s. |
| Reference card (tt-rafaellfreitaas) | 8 s, 0 cuts, a state change about every 0.5 s for 5 s, merge at 2.0 s, 2 s final hold |
| Ours | 14.0 s, 0 cuts; events at 0.06, 0.20, 0.34, 0.48-0.94 (words), 0.90-1.14 (labels), 1.5, 2.0, 2.5, 3.0 (steps), 3.4, 3.5-4.5 (spiral), 4.5 (merge), 5.05, 5.3, 5.84, 6.08, 6.17, 6.8, 7.0, 7.18-7.87 (letters), 8.2, 8.7, 9.3, 10.65, 11.15, 11.65, 13.45: no gap over 0.63 s in the first 8 s. Merge at 4.5 s (card 2.0 s); final frozen hold 1.52 s (card 2 s). |
| Loop seam | frame 839 to frame 0: mean 0.64/255, p99.9 12, max 57 (static grain re-quantised at a keyframe), the same size as the segment joins (0.75 and 0.86); background level identical (31.53). Invisible. Audio fades to -64 dBFS over the last 0.1 s and the last 20 ms are silent; the film opens at -74 dBFS, first pop at 0.06 s. |
| Segment joins (render in 3 parts) | 4.667 s and 9.333 s: only the static grain texture changes (bg abs 0.6/255, std 0.9), no picture jump |
| Sync (onset against events.json) | pops 0.06 / 0.20 / 0.34 s: -1 ms; merge 4.50 s: -1 ms; thud 6.08 s: -1 ms (12.6 dB step, the loudest hit, peak -2.3 dBFS); ticks 1.5 / 2.0 / 2.5 / 3.0 s: +7 to +9 ms (under one frame); CTA click 9.30 s: +3 ms; end steps 10.65 / 11.15 / 11.65 s: +1 to -5 ms on the high band. Swells (riser, whooshes, bloom, lines) have soft attacks, so their onsets read 20 to 80 ms late by design. |
| Bed level | 20th-percentile level under the question: v1 -19.1, v2 -16.9 dBFS (+2.2 dB; RMS +2.4 dB). End hold RMS: v1 -21.8, v2 -18.6 dBFS (+3.2 dB). The planned hang (5.60 to 5.84 s) sits at -23.7 dBFS. |

## Text, letter by letter (M1, M6)
On screen, in order: "Still running" / "your business" (frame 0) · "on" *"three"* / "separate things?" (in by 0.94 s) ·
"Posts" · "Replies" · "Follow-ups" · the StraightScale lockup (real file) · "One system." · *"Built around"* /
*"your business."* · "Follow for the build," / "step by step." · "Still running" / "your business" (rising back in,
13.56 to 14.0 s).
All correctly spelled English, with the punctuation intended. There are no em or en dashes in `index.html`,
captions.srt, CREDITS.md, CHANGELOG.md, PROJECT.md or the treatment. There are no numbers, prices, results, names,
reviews, guarantees, deadlines, platform names or logos, and no hype words. No gold text on ivory and no red text on
charcoal: the crimson ball and the mark's red are not text. The fonts are Playfair Display 900 / 900 italic / 700 italic
and Montserrat 600 only. The colours used are the kit's: ivory, gold, crimson, and the mark's own red and gold.

## Checks
| Id | Result | Evidence |
|---|---|---|
| M1 spelling | PASS | see above |
| M2 overlaps and clipping | PASS (minor note) | The question parts around the rising ball on purpose (5.33 to 5.45 s). Labels hang under their own dots and never cross a dot at rest (strip 1.63 to 1.85 s). Brief overlap at the loop: "your" passes over the fading mark at 13.70 to 13.75 s (finding 2). Nothing is clipped at the frame edges. |
| M3 safe zones and contrast | PASS | the section 6 tool run is clean; the pixel scan agrees (see Measured); contrast 6.8:1 or more |
| M4 timing to voice | N/A | no voice; text follows the 120 BPM beat grid in events.json |
| M5 motion by 1 s, hook text by 0.3 s | PASS | Frame 0 shows "Still running / your business" (98 px, y 285 to 481). The first dot pops at 0.06 s with a sound. The full question is in by 0.94 s. |
| M6 brand colours and fonts | PASS | see above; the logo was verified against the file |
| M7 generated images | N/A | none; everything is code or the real logo file |
| F1 frames clean | PASS (minor notes) | every 0.5 s frame and every transition strip is clean. Residual comb in the label smear on 3 to 4 frames per step (finding 3); a 4-frame double exposure at the reveal (finding 4). |
| F2 sound-off | PASS | the question, three labelled things becoming one ball, the brand, the answer and the CTA all read without audio |
| F3 captions | PASS | captions.srt matches the on-screen words. Nits: cue 1 shows the whole question from 0.0 s although its second half enters at 0.48 to 0.94 s, and cue 5 shows "Built around your business." from 8.2 s although it enters at 8.7 s. It is a sidecar file, with no burned-in captions to place. |
| F4 transcript | N/A | no voice |
| F5 loudness | PASS | -14.0 LUFS, -2.0 dBTP (limit -1.5), LRA 4.2 LU, no clipping |
| F6 hook timing | PASS | same as M5 |
| F7 policy | PASS | no before and after, no "your [condition]", no AI people, voice or footage, so no AI label is needed |
| F8 credits | PASS | CREDITS.md lists the reference (studied only), the owner's logo files, OFL fonts, CC0 samples, the MIT sampler and 0 paid generations |
| Process | OPEN | G-MOTION-TEXT has no `pipeline.py record` under `clients/straightscale/runs/` (finding 1). No human listen yet (finding 7). |

## Scores (0 to 10)
| Axis | v1 | v2 | Why |
|---|---|---|---|
| Hook | 6 | 8 | A readable, specific question on frame 0, motion and a pop at 0.06 s, and the full question by 0.94 s. It is still a text-on-charcoal opening with small dots, and the visual payoff (the merge) comes at 4.5 s against the card's 2.0 s. |
| Readability | 7 | 8 | Every line passes 0.25 s per word + 0.5 s with room (the CTA is fully visible for about 3.5 s against 2.25 s needed). Sizes are 50 px or more, contrast passes, and the section 6 zone is respected. The labels are the smallest text (about 17 px at 360 px wide) but each is one word and readable in every rest between steps. |
| Motion | 8 | 8 | Springs, squash and stretch, the spiral collapse, the landing on the take-off floor, the circular reveal out of the ball, the rise, slide and letter wipe. Label stepping is mostly solved. Minor: residual comb, the reveal's double exposure, and an exit that is a dissolve rather than a lift. |
| Continuity | 9 | 9 | One object from the first dot to the lockup, no cuts, survivors named at every handover, an invisible loop seam (0.64/255) and invisible segment joins |
| Pacing | 7 | 8 | Something changes every 0.12 to 0.63 s through 8 s; the planned 1.52 s frozen rest; longest quiet 4.25 s (v1 5.0 s). The end card is still 4.15 s against STANDARDS' 2.5 to 3 s (finding 5), and the merge is 2.5 s later than the reference. |
| Composition | 7 | 8 | The mark is now revealed at frame centre (y 843 to 1115) and rises into the lockup; the end card fills y 437 to 1236 on one left edge; the empty band under 1248 px is the mandated safe zone, not dead space. A 0.25 s fully empty hang at 5.58 s is planned. |
| Brand | 9 | 9 | Real files verified pixel by pixel, kit colours and fonts, no banned content. The CTA is "follow", which STANDARDS allows on an organic end card; the brand's one path (comment ANALIZA) is the owner's call. |
| Sound | 8 | 8 | Hits land within 1 ms (pops, merge, thud) and ticks within 9 ms; -14.0 LUFS / -2.0 dBTP; the bed is +2.2 dB under the question and +3.2 dB in the end hold; planned near-silence; clean fade at the loop. Capped at 8 because nobody has listened. |
| Message, sound off | 8 | 8 | Problem, picture of three becoming one, brand, answer and CTA all read on their own. "Follow for the build" is vague about what the build is. |

## Findings (all minor; none needs new material)
1. **Minor (process, blocks the hub record, not the film), G-MOTION-TEXT ledger record missing.** STANDARDS section 9
   says G-MOTION-FRAMES fails on a version without a G-MOTION-TEXT record. This review re-ran its content checks on the
   v2 constants and the render (M1 PASS, M3 PASS, M4 N/A, M6 PASS). **Fix:** the orchestrator records G-MOTION-TEXT
   for this `motion_render` version with `pipeline.py record` under `clients/straightscale/runs/`, either from a fresh
   prompt-reviewer given only the packet, or from this review with `independent: false`. Then it records
   G-MOTION-FRAMES. No re-render.
2. **Minor, 13.57 to 13.75 s, loop re-entry overlap.** The end card fades out almost in place while "Still running /
   your" rises in. "your" sits on top of the half-faded S mark at 13.70 to 13.75 s, so text is over the logo for about
   4 frames. **Fix:** start the end card's fade about 0.1 s earlier (13.35 s), or lift it 40 to 60 px as it fades, so
   the lockup is under about 10% opacity before line 2 of the question reaches y 400. Optional.
3. **Minor, 1.50 to 1.62 s (and the steps at 2.0, 2.5 and 3.0 s), label smear.** At 1:1 the fastest 3 to 4 frames of
   each step still show a comb: each stroke is repeated 5 to 7 px apart (frames 91 to 94). At 360 px wide this reads as
   motion blur, and it is far better than v1's 5 to 8 stacked copies. **Fix (polish):** raise the cap on speed-driven
   samples for the label layer (24 to 48 per subframe) during the peak, or add a 2 px directional blur at peak speed.
4. **Minor, 6.18 to 6.25 s, reveal handover.** The fading ball sits over the growing mark as a darker, desaturated
   disc for 4 frames, so the S channel looks double-exposed instead of carved. **Fix (polish):** clip the ball to the
   outside of the reveal circle, or fade it out by 6.20 s.
5. **Minor, 9.30 to 13.45 s, end card length.** The CTA card runs 4.15 s against STANDARDS section 5's 2.5 to 3 s. By
   the 0.25 s per word + 0.5 s rule the CTA needs 2.25 s fully visible and gets about 3.5 s (the maker's 3.43 s comes
   from a character-based rule). **Fix (optional):** shorten the frozen rest at 11.97 to 13.48 s from 1.5 s to about
   0.8 s (film about 13.3 s), or keep it and log the deviation as the maker did. A tighter tail helps the loop.
6. **Minor (owner decision), 9.3 to 13.45 s, CTA.** "Follow for the build, step by step." no longer promises a weekly
   cadence, but "the build" points at a series that is not live. The brand kit's one path is comment ANALIZA. The owner
   decides before posting. v1 keeps the original line.
7. **Minor (gate), whole film, unheard.** No human has listened. The label harp notes measure only about 1 dB over the
   bed and may vanish on a phone speaker; that is acceptable since they are designed to be soft. **Fix:** the planned
   phone-speaker and headphone listen before the hub (house rule).

Not findings: the merge at 4.5 s against the card's 2.0 s is a deliberate trade for the question and labels, and the
first 4.5 s are never still. The ball leaving through the top band is motion, not key content. The upper-half lockup
reaching x 871 is inside section 6, whose right 21% applies only in the lower half.

## What the edit cannot fix
Nothing. Findings 2 to 5 are optional constant changes in `index.html` plus a re-render; findings 1, 6 and 7 are
records and decisions outside the film. v2 can go to the G-MOTION-TEXT record, the human listen and the owner's hub
approval as it is.
