# Independent review, round 1: StraightScale 06 "The 108-hour week" (Film 3)

- Reviewer: fresh agent, independent. I did not make the film. I checked the maker's claims against the delivered files
  and did not rely on them.
- Date: 2026-10-20
- Files reviewed: `deliver/v1/straightscale-06-108-hour-week-9x16.mp4` (master) and `deliver/v1/straightscale-06-108-hour-week-4x5.mp4`
- Reference: `refbank/cards/tt-foil-finance.md`
- Gates applied: G-MOTION-FRAMES (M1 to M7) and G-FINAL (F1 to F8), as they apply to a code-rendered piece with no
  voice; G-MOTION-TEXT (M1, M3, M4, M6) on the `COPY` constants in `film/index.html`; onetake §8 gates 5, 6 and 8;
  `motion-studio/CLAUDE.md`; `clients/straightscale/brand-kit.md`.

## Verdict: PASS

Every axis scores 8 or higher. There are no critical or major findings. Eleven minor findings are listed below; none
of them blocks posting. A person still has to listen to the mix on a phone before it goes out, as the house rules
require.

| Axis | Score | Evidence |
|---|---|---|
| Hook (first 2 s) | 8 | Frame 0 shows the whole claim, the empty chart, "0 h" and "Mon 09:00". The clock ticks from frame 4 (0.067 s), the first climb is at 0.556 s and the first bubble at about 0.67 s. This is the reference's grammar exactly (hook change 0.017 against 0.01). The headline labels the chart rather than making the reference's odd, true claim, so it is a little less of a scroll-stopper. |
| Readability | 8 | Headline 80 px, note 44 px, maths 50 px, list 52 px, CTA body 50 px, clock 116 px. Main text contrast is 5.5:1 to 15.5:1, and every line meets 0.25 s per word + 0.5 s. Weak spots: axis tick numbers (about 27 px, 2.9:1), the 38 px OPEN/CLOSED chip, the tiny answer checks, and the payoff "Closed 108." set at body size. |
| Motion | 8 | 60 fps, masked rolls instead of fades, and springs on the axis rescales (3.27 s, 5.9 s) with no jitter. The fastest mover, the gold square's hop to the logo, peaks at about 58 px per frame (limit 80). Issues: the day roll is caught mid-roll for 3 to 5 frames each day, and the CTA fold has four movers for about 0.35 s. |
| Continuity | 9 | One shot with no cuts. The line tip becomes the riding label, the "108" drops into "Closed 108.", the lit plot covers the closed hours, the tip becomes the ANALIZA caret, and the caret lands on the logo's own gold square (19.23 s). |
| Pacing | 8 | 0 cuts. 35% of frames are frozen at 60 fps. Frozen rests: 10.42-11.22 s, 16.03-17.45 s, 19.68-21.25 s and 21.42-23.98 s; none is over 3 s. Beat CV is 0.48. Measured the same way as the reference card (2 fps): 0.0 cuts per 10 s (ref 0.0), 1 big change, mean gap 12.0 s (ref 13.0), quiet share 0.36 (ref 0.16), hook change 0.017 (ref 0.01). |
| Composition | 8 | Left-aligned grid, and safe zones hold (headline top 300 px, clock bottom about 1450 px, logo 1180-1393 px, right edge at most 937 px). The 4:5 is a real re-layout, not a crop. The climax "108" is never big after the clock leaves. |
| Brand | 9 | The logo `wordmark-white.png` is byte-identical (md5 826fdf88…) to `straightscale-03/assets/brand/`. It is shown at its native 640x213 with no filter and revealed only by a clip-path. Fonts are Playfair Display and Montserrat, with one gold accent. There is no red text and no gold-on-ivory. One neutral grey (#9B958D) is outside the kit. |
| Sound | 8 | -14.0 LUFS integrated, -3.1 dBTP true peak, no clipping, LRA 3.8 LU, same on both formats. Onsets land within 6-21 ms of every closing, the landing, the maths beats, the CTA fold, typing and the logo. The mix rings out and is quiet below -60 dB after about 23.2 s. Nobody has listened to it yet. |
| Message with the sound off | 9 | The whole argument is on screen: example, 168, 60, 108, the system's answer, Comment ANALIZA, and what arrives in the DM. |

## What I did
1. Probed both files with ffprobe: 1080x1920 and 1080x1350, H.264 yuv420p, 60/1 fps, 1440 frames, 24.000 s, AAC 48 kHz
   stereo at 320k. Sizes are 4,977,572 and 4,293,326 bytes.
2. Made phone-size contact sheets (360 px wide, one frame every 0.5 s) for both formats and looked at all of them. Note:
   ffmpeg's `fps=2` filter picks the frame about 0.23 s after each label, so I did all timing work on exact frame
   numbers. Also, the shared scratchpad held stale frames from another film, so I re-extracted into a fresh folder and
   used only those frames.
3. Made exact-frame strips of the day roll (frames 124-139), the first axis rescale (186-208), the landing (560-626), the
   maths line and 108 flight (660-796), the headline swap (790-856), the answer sweep (840-939), the CTA fold (1040-1091),
   the hop and logo reveal (1128-1179) and the gold rule (1265-1298). I also looked at full-resolution frames at 0,
   10.67, 16.67 and 23.0 s on 9:16 and four frames on 4:5.
4. Read every on-screen string letter by letter, on screen and in `COPY` (identical in `film/` and `film-4x5/`).
5. Sampled pixels to measure contrast.
6. Ran `tools/pacing.py` on the master, and `refbank/tools/frames_metrics.py` on 2 fps frames so the comparison with the
   card is like-for-like. Measured frozen runs from 60 fps frame differences.
7. Ran `tools/audio_qa.py` on both files and looked at the spectrogram. Ran `ebur128` and `astats`. Ran librosa onset
   detection against the cue sheet in `film/index.html` (B(j) = 0.556 + 0.667 j s), and momentary loudness before and
   after each landing.
8. Checked the deliverables, the poster and the delivered contact sheet.

Not re-verified: HyperFrames `check`, `seekcheck_hf.mjs` and `textcheck.mjs`. I did not re-run them; my own frame and
safe-zone checks agree with what they report.

## Text check (M1, G-MOTION-TEXT)
On screen, in order (no misspellings, no em dashes, no hype words, no platform names):
"Hours a week your / business is *closed* while / clients still write." · "Example: open 09:00 to 19:00, / Monday to
Saturday." · day labels MON TUE WED THU FRI SAT SUN MON · OPEN / CLOSED · "Mon 09:00"-style clock · "N h" · axis
0-140 · "168 hours in a week." · "You are open 60." · "Closed 108." · "A system answers / in those hours:" · "instant
replies, / follow-up, / booking." · "Comment" · "ANALIZA." · "The booking button for the / free 45-minute analysis /
comes in the DM."

Numbers: 168 = 7 x 24. 60 = 6 x 10. 108 = 168 - 60, and the chart's closed periods also sum to 5 x 14 + 38 = 108. The
riding label ends on 108 and the tip sits at 108 on the 0-140 axis. 09:00 and 19:00 are the labelled example. "45-minute"
is the offer as named in the brand kit. The clock, the "N h" values and the axis ticks are chart scaffolding taken from
the same example. 64% is not shown. No invented numbers. `captions.srt` matches the on-screen copy exactly.

## Findings (all minor)
1. **Axis tick numbers are 2.9:1 contrast at about 27 px** (any time the chart shows, 0-17.5 s). They are below the
   4.5:1 floor and unreadable at 360 px wide. Fix: raise them to the note grey (#9B958D, 5.6:1), or keep only 0 and the
   top tick.
2. **The payoff is set at the minimum body size** (12.56-17.5 s). After the 116 px clock leaves, "Closed 108." is a
   50 px line at the bottom of a three-line stack, so the film's biggest number is its smallest moment. Fix (next
   version): hold "108" big for about 0.5 s before it settles into the sentence, or set "Closed 108." at about 80 px.
3. **The answer checks are tiny at phone size** (14.2-17.5 s). The gold check badges are about 20 px (about 7 px on a
   360 px screen); the "answered" idea rests on the lit plot and the headline. Fix: make the checks 1.5-2x larger, or
   swap each bubble's fill to gold when it is answered.
4. **The day roll is caught mid-roll 3 to 5 frames per day, not about 2** (for example frames 131-135, 2.18-2.25 s).
   At frames 130-133 the clock reads "Tue 00:00" where midnight should read "Wed". Fix: run the roll ahead of
   midnight (start at 23:00) so it shows "Wed 00:00", and shorten it to 3 frames.
5. **The CTA fold has four movers at once** (17.53-17.88 s): the top text exits up, the maths exits down, the chart
   folds and the square flies. It is short and reads as "the board clears", but it is the busiest moment. Fix:
   sequence the maths exit after the fold, as the maker already planned.
6. **The gold square crosses the CTA body copy** (18.95-19.05 s). On its hop to the logo it covers letters in
   "button" and "the DM" for about 2 frames each. Fix: arc the hop to the left of the text block, or start it from
   below the body.
7. **The gold rule under ANALIZA has no audible cue** (21.22 s). The maker says it lands on a C6 piano note, but no
   onset is detected and the momentary loudness does not rise (-14.7 before, -14.8 after, mono). Also, the turn into
   "A system answers" (13.56 s) measures quieter than its approach (-17.9 vs -21.1 LUFS M, mono), which contradicts the
   log's "turn -20.7 -> -17.7". Fix: let a person check it on the listening pass; lift the note 3 dB if it does not
   read.
8. **A neutral grey outside the brand kit** (#9B958D in `C.grey`, the note, labels, grid and open-hour bars). It is a
   derived neutral and passes contrast, but M6 is strict. Fix: log it in the brand kit as the secondary-text tint, or
   derive it from marble at reduced opacity.
9. **4:5 spacing is tight** (14.9-17.5 s). "booking." sits about 25 px above the bubble lane, and the check badges
   nearly touch it. Fix: move the 4:5 lane down about 20 px, or trim the list gap.
10. **The pacing claim does not reproduce at the reference's scale.** The report says "one big change every 1.8 s in
    the second half". The refbank's own 2 fps metric finds 1 big change and a mean gap of 12.0 s, about the same as the
    reference's 13.0 s. That is fine for this format, but the 1.8 s figure counts designed beats, not measured picture
    changes. Fix: label it as such in the log.
11. **Leftovers noted by the maker are confirmed:** a 17.4 kHz sampler line in the first about 9 s of the spectrogram;
    and the list "instant replies, follow-up, booking." is on screen in full for about 2.4 s. That passes the 0.25 s per
    word + 0.5 s rule (needs 1.5 s), though not the stricter chars/15 + 1.5 s rule.

Not a finding: the mix decays to below -60 dB from about 23.2 s, so the loop point is about 0.8 s of near-silence over
the held end card. It reads as a planned ring-out.

## Gate checks
| Check | Result | Evidence |
|---|---|---|
| M1 spelling | PASS | All strings above, letter by letter, on screen and in `COPY` |
| M2 overlaps / clipping | PASS (minor) | Masks hide glyphs after exits. Brief overlaps only in transit: findings 4 and 6, and "108" crossing the line at 12.6 s |
| M3 safe zones + contrast | PASS (minor) | All key text and the logo are inside top 14%, bottom 20% and right 140 px. Main text 5.5-15.5:1; tick numbers 2.9:1 (finding 1) |
| M4 text on its spoken word | N/A | No voice. Music cues sit on the visual events instead (6-21 ms) |
| M5 motion by 1 s, hook text by 0.3 s | PASS | Text at frame 0, clock ticking at 0.067 s, first climb at 0.556 s |
| M6 brand colours and fonts | PASS (minor) | Playfair Display and Montserrat, gold accent, red only in the logo; grey tint (finding 8) |
| M7 generated images passed G-VIS | N/A | No generated images. The ground is code-made grain |
| F1 frames clean | PASS | 0.5 s sheets on both formats, plus strips at every transition |
| F2 sound-off | PASS | The argument is complete on screen |
| F3 captions | PASS | `captions.srt` equals the on-screen copy. Cues overlap by design (it lists the lines, it is not a subtitle track) |
| F4 transcript | N/A | No voice |
| F5 loudness / true peak | PASS | -14.0 LUFS, -3.1 dBTP after AAC, both formats |
| F6 hook timing | PASS | Hook text at 0.0 s |
| F7 policy | PASS | No before/after, no personal-attribute "your [condition]", no AI media, example labelled |
| F8 credits | PASS | 0 credits. CC0 samples, OFL fonts and the GSAP licence are listed in CREDITS.md |

## Deliverables
All present in `deliver/v1/`: 9:16 master, 4:5, `poster.jpg` (1080x1920, landing frame), `contact-sheet.jpg`,
`contact-sheet-4x5.jpg`, `captions.srt`, `CREDITS.md`, `CHANGELOG.md`. Duration, frame rate and frame count are as
reported.

## Still required before posting
A person listens on a phone speaker and on earbuds, checking the 21.22 s rule cue and the 13.56 s turn. Then the person
approves the cut in the hub. The refbank ledger entry from `PROJECT.md` is logged after approval.
