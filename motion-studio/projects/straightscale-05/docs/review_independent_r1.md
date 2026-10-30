# Independent review, round 1: StraightScale reel 05 "Three things, one system" (deliver/v1)

Reviewer: fresh take-reviewer (motion mode), independent. I did not build this film and re-measured every claim myself.
Date: 2026-10-20. Gates applied: G-MOTION-FRAMES M1 to M7, G-FINAL F1 to F8 where they apply to a code-rendered,
unvoiced piece, the G-MOTION-TEXT text checks, house rules (`motion-studio/CLAUDE.md`), onetake §8, the brand kit, and
`growth-engine/production/STANDARDS.md` (which takes precedence on numbers).

**Verdict: FAIL** (2 major findings; hook, readability, pacing and composition score under 8).
The craft is good: one continuous object, real logo, exact sound sync, clean loop. It fails on two numeric rules from
STANDARDS.md that the maker did not check against: the hook-text timing (M5) and the Reels safe zone (§6).

## What I ran and opened
- Frames from the delivered files, picked by exact frame index (not the fps filter): 0.5 s contact sheets at 360 px
  wide for 9:16 and 4:5; 12-frame strips at 1/30 s around the first spinner step (1.47 to 1.83 s), the collapse and
  merge (4.30 to 4.67 s), the crouch and launch (5.20 to 5.57 s), the fall, landing and reveal (6.00 to 6.37 s) and the
  slide and letters (6.97 to 7.52 s); full-res frames 0, 372 to 420, 480, 600, 800, 870, 883 and 884; the delivered
  poster and contact sheet.
- Logo: the 3 brand PNGs are byte-identical (md5) to `projects/straightscale-03/assets/brand/`. The rendered lockup at
  10.0 s and the hero mark at 6.7 s were composited against `wordmark-white.png` at 1.27x and the `logo-full.png` symbol
  region: same artwork, same colours, and the S channel stays transparent. No redraw and no recolour.
- `tools/seekcheck.mjs` on 9:16 and 4:5, `tools/pacing.py` on both MP4s, `tools/audio_qa.py`, `ffmpeg ebur128` on both
  MP4s, `tools/safezone.mjs` with the house zone and with the STANDARDS §6 zone, an onset and RMS envelope check of the
  mix against `audio/events.json`, and sampled pixel colours.

## Measured
| Check | Result |
|---|---|
| Files | 9:16 1080x1920 and 4:5 1080x1350, H.264 yuv420p, 60 fps, 885 frames, 14.750 s; AAC 48 kHz stereo; same audio in both (bit-identical decode) |
| Deliverables | 9x16 master, 4x5, poster.jpg (frame at 2.3 s, a good cover), contact-sheet.jpg, contact-sheet-4x5.jpg, captions.srt, CREDITS.md, CHANGELOG.md: all present |
| Loudness | -14.0 LUFS integrated, true peak -1.9 dBTP, LRA 5.6 LU (both files); audio_qa PASS (no dropouts, no mud) |
| Loop seam | frame 884 against frame 0: max 7/255, mean 0.61 (grain and codec noise); audio fades to -78 dB by 14.70 s |
| Seek | PASS on both formats (same frame on revisit, no errors every 0.1 s) |
| pacing.py 9:16 | still 23%, quiet 72%, 0 transitions, longest quiet run 5.0 s (at the limit), no frozen stretch over 3 s, CV 1.09, spread 27x |
| pacing.py 4:5 | still 22%, quiet 70%, longest quiet 4.92 s, CV 1.36 |
| Reference card | 8 s: about 2 s of dots, 2 s of blob, 3 s of lockup with a 2 s hold; a state change every 0.5 s for 5 s; merge at 2.0 s |
| Ours | dots and question for 4.5 s, merge at 4.5 s, ball 4.5 to 6.2 s, mark and lockup 6.2 to 8.3 s, then about 6 s of end card (about 3.8 s of it near-still) |
| Safe zone, house (250/400/140) | ok (the maker's claim is confirmed) |
| Safe zone, STANDARDS §6 (top 269, bottom 672, right 227 in the lower half) | FAIL: bottom labels 0.6 to 2.8 s (bottom edge 1353 to 1447 against a 1248 limit), "Follow-ups" right edge 884 to 918 against 853 at y 1300 to 1360 (2.1 to 2.4 s), "one step a week." bottom 1300 from 10.4 s to the exit. The flag on "separate things?" is a false positive (upper half). |
| Text sizes | labels Montserrat 600 50 px (the smallest text), CTA 56 px, question about 100 px, "One system." 128 px: all at or above 44 px |
| Colours (sampled) | mark #BC0C14 (kit #BE0F18), gold #DC9C14 (#DD9A10), ivory #F4F4EC (quantised #F8F6EF), background #1F1F1F |
| Contrast | gold on charcoal 6.8:1, ivory on charcoal about 15:1 |
| Sync (onset or RMS step against events.json) | pops 0.06, 0.20, 0.34 s: 0 ms off; ticks +5 ms; merge 4.50 s step from -14 to -9 dB; launch whoosh 5.30 s; planned hang 5.65 to 5.90 s at about -33 dBFS; down whoosh 5.905 s; thud 6.08 s (-27 to -7 dB); slide 7.0 s; chord 7.874 s; harp steps -10 ms; exit 14.26 s |

## Text, letter by letter (M1, M6)
"Posts" · "Replies" · "Follow-ups" · "Still running" / "your business" / "on" *"three"* / "separate things?" ·
the StraightScale lockup (real file) · "One system." · *"Built around"* / *"your business."* ·
"Follow for the build," / "one step a week."
All correctly spelled English. No em or en dashes in the page, captions or docs. No numbers, prices, results, names,
platform names or logos, guarantees, deadlines or hype words. No gold text on ivory and no red text on charcoal.
Fonts are Playfair Display and Montserrat only. captions.srt matches the on-screen words.

## Checks
| Id | Result | Evidence |
|---|---|---|
| M1 spelling | PASS | see above |
| M2 overlaps and clipping | PASS | the question parts around the ball on purpose (5.33 to 5.5 s); nothing clipped at the edges |
| M3 safe zones and contrast | **FAIL (major)** | passes the house zone and the task's 14%/20% rule, but fails the STANDARDS §6 zone (see Measured); contrast passes |
| M4 timing to voice | N/A | no voice; text times follow the beat grid |
| M5 motion by 1 s, hook text by 0.3 s | **FAIL (major)** | motion at 0.06 s passes; at 0.3 s there are only three 42 px dots and the "Posts" label is just starting. The question starts at 0.78 s, its first block reads at about 1.3 to 1.5 s and the full question at about 2.0 s. Frame 0 is empty charcoal by design. |
| M6 brand colours and fonts | PASS | sampled colours on brand; Playfair Display and Montserrat |
| M7 generated images | N/A | none; everything is drawn in code or is the real logo file |
| F1 frames clean | PASS with minors | label stepping during spinner steps (finding 3) |
| F2 sound-off | PASS | question, three becoming one, the brand, the answer and the CTA all read without audio |
| F3 captions | PASS | the SRT matches the on-screen text; there are no burned-in captions to place |
| F4 transcript | N/A | no voice |
| F5 loudness | PASS | -14.0 LUFS, -1.9 dBTP, LRA 5.6 LU |
| F6 hook timing | FAIL | same as M5 |
| F7 policy | PASS | no before/after, no "your [condition]", no AI people, voice or footage, so no AI label is needed |
| F8 credits | PASS | CREDITS.md complete; CC0 samples, OFL fonts, 0 paid generations |
| Process | note | `safezone.mjs` was run with the house zone, which STANDARDS §6 overrules. There is no G-MOTION-TEXT record in a pipeline ledger, and STANDARDS says G-MOTION-FRAMES fails on a version without one. This review covers its M1, M3 and M6 content checks, but the record itself is missing. |

## Scores (0 to 10)
| Axis | Score | Why |
|---|---|---|
| Hook | 6 | Empty first frame, small dots, hook text from 0.78 s (rule: 0.3 s). The reference's slow build works because viewers try to guess a famous brand from its colour; StraightScale has no such recognition to lean on. |
| Readability | 7 | Sizes, reading times and contrast pass. The 50 px labels carry "the three things" and smear into stacked copies on every step; key text sits in the STANDARDS bottom band. |
| Motion | 8 | Springs, squash and stretch, and a clean ball-to-mark handover through the circular mask; text stepping on the spinner labels. |
| Continuity | 9 | One object from frame 1 to the lockup, no cuts, no visible swap, clean loop seam. |
| Pacing | 7 | The first 8 s change every 0.5 s and match the card's rhythm. The merge comes at 4.5 s (the card's at 2.0 s). The end card is about 40% of the runtime, with about 3.8 s of near-stillness; the longest quiet run (5.0 s) is exactly at the limit. |
| Composition | 7 | One clear left edge. From 6.2 to 8.3 s the mark and lockup sit at y 585 with the lower two-thirds of the frame empty; the band 1300 to 1520 px is empty on the end card; the landing squash at 6.08 s implies a floor that isn't there. |
| Brand | 9 | Real files verified pixel by pixel, colours and fonts on brand, no banned content. The CTA is "follow", not the brand's one path (comment ANALIZA). |
| Sound | 8 | Sync is frame-exact, the loudness specs pass, the silence is planned and the loop fade is clean. The bed is quiet under the hook question (about -22 dBFS RMS from 0.5 to 1.5 s); unheard by anyone, this reviewer included. |
| Message, sound off | 8 | The question, the picture of three becoming one, the answer and the CTA read on their own; the labels are small. |

## Findings
1. **Major, 0.0 to 2.0 s, M5 hook timing.** The hook text is not on screen by 0.3 s: frame 0 is empty, then come three
   dots and one small label, and the question only starts at 0.78 s and completes at about 2.0 s. STANDARDS overrules
   motion-reel's "hook in the first 2 s", which is what the maker scored against. **Fix:** have "Still running your
   business" on screen by 0.3 s (the words rise from 0.0 to 0.3 s, or start set at frame 0 while the dots pop in), with
   "on three separate things?" by about 1.0 s. To keep the loop, let the end card's exit rise straight into that same
   opening frame instead of the empty frame (or accept a non-empty frame 0).
2. **Major, 0.6 to 2.8 s and 10.4 to 14.25 s, M3 safe zone (STANDARDS §6).** The bottom labels (bottom edge 1353 to
   1447 px), "Follow-ups" (right edge 884 to 918 px against 853 in the lower half) and the CTA's second line "one step a
   week." with its gold step rule (bottom edge 1300 px) sit in the zone that §6 keeps clear (bottom 672 px, right
   227 px in the lower half). §6 overrules the 250/400/140 house zone that was checked. **Fix:** shrink the label ring
   (R0 212 to about 175, Rly 318 to about 250) and lift triY to about 1050 so the bottom labels end above 1248 px; move
   the lockup and end card up about 70 px (lockCY 585 to 515; "One system." 862 to 792; "Built around" 962/1052 to
   892/982; CTA 1206/1282 to 1136/1212). This also closes the empty 1300 to 1520 band. Re-run
   `node tools/safezone.mjs <dir> --top 269 --bottom 672 --right 227 --left 65 --min 44`. The 4:5 layout is unaffected.
3. **Minor, 1.50-1.60 / 2.00-2.10 / 2.50-2.60 / 3.00-3.10 s, text stepping.** On each 120 degree spinner step
   (spring k 700, d 44) the labels peak at about 100 to 120 px per frame. Eight subframes leave gaps of about 13 to 15 px
   on strokes about 7 px wide, so each word shows as 5 to 8 stacked copies (strip frames 1.533 and 1.567 s). The
   maker's strips did not sample the spinner. **Fix:** a speed-driven subframe count (24 or more) for the label layer
   during steps, or dip the label alpha to about 0.3 during the fastest 70 ms of each step.
4. **Minor, 10.45 to 14.25 s, end card tail.** Only the 6 px rule steps and 12 px word hops move for about 3.8 s;
   pacing.py's longest quiet run (5.0 s) is exactly at the limit, and the end card is about 40% of the film against the
   card's 2 s hold. **Fix:** start the steps at about 10.75 s and exit at about 13.5 s (the CTA still gets 3.0 s fully
   visible against 2.5 s needed). The film would be about 14.0 s.
5. **Minor, 6.2 to 8.3 s, composition.** The mark lands and is revealed at y 585 with the lower two-thirds of the
   9:16 frame empty for about 2 s (a house banned look), and the landing squash implies a floor. **Fix:** land and reveal
   the mark near frame centre and let the existing FLIP slide carry it up into the lockup, or accept the sparse look and
   log it.
6. **Minor, 0.5 to 1.5 s and 13.0 to 14.25 s, sound level.** The bed sits about 8 dB under the mix average while the
   hook question builds, and at -24 to -26 dBFS through the final hold. The sync itself is exact. **Fix:** lift the bed
   about 3 dB under the question, then do the planned phone-speaker and headphone listen before the hub.
7. **Minor, 9.7 to 14.25 s, CTA (owner decision).** "Follow for the build, one step a week." commits to a weekly series
   that does not exist yet, and the brand kit's one path is "comment ANALIZA". Do not post until the series exists, or
   change the line. The unvoiced choice (the batch brief) is disclosed.

## What the edit cannot fix
Nothing here needs new material. Every fix is in `index.html` constants plus a re-render (and a light remix for
finding 6). After fixing 1 and 2, re-run the STANDARDS §6 safe zone, pacing.py, readcheck and seekcheck, and send a
new review round.
