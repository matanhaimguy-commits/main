# Independent review, round 2: StraightScale 06 "The 108-hour week" (Film 3, v2)

- Reviewer: a fresh agent, independent. I did not make the film. I checked the maker's v2 claims against the delivered
  files myself.
- Date: 2026-10-20
- Files reviewed: `deliver/v2/straightscale-06-108-hour-week-9x16.mp4` (master) and
  `deliver/v2/straightscale-06-108-hour-week-4x5.mp4`, plus the poster, both contact sheets, `captions.srt`, `CREDITS.md`
  and `CHANGELOG.md`
- Reference: `refbank/cards/tt-foil-finance.md`
- Gates applied, where they fit a code-rendered piece with no voice:
  - G-MOTION-FRAMES (M1 to M7) and G-FINAL (F1 to F8) from `.claude/agents/take-reviewer.md`
  - G-MOTION-TEXT (M1, M3, M4, M6) on the `COPY` constants in `film/index.html`
  - onetake §8 gates 5, 6 and 8
  - `motion-studio/CLAUDE.md`
  - `clients/straightscale/brand-kit.md`

## Verdict: PASS

Every axis scores 8 or higher. There are no critical or major findings. Six minor findings are listed below. None of
them blocks posting, though finding 1 is worth fixing before the 4:5 is used. The v2 fixes I could test hold up. Before
posting, a person still has to listen to the mix on a phone and approve the cut in the hub.

| Axis | Score | Evidence |
|---|---|---|
| Hook (first 2 s) | 8 | Frame 0 already shows the headline, the note, the empty chart, "0 h", OPEN and "Mon 09:00". The clock ticks from about 0.07 s. The first climb is at 0.556 s, with its sound onset at 0.565 s, and the first bubble appears by 1.0 s. Hook change is 0.017 (reference 0.01). This is the reference's own grammar. The headline names the chart rather than making the reference's odd, true claim, which costs a point. |
| Readability | 8 | Reading text is never under 44 px: headline 80, note 44, maths 50, "Closed 108." 80, list 52, body 50, clock 116. `textcheck.mjs`, which I re-ran, gives every block its reading time; the tightest is "booking." with 2.28 s against 2.03 s needed. Contrast: grey 5.6:1 (glyph cores 5.8:1), gold 6.8:1, ivory 15.2:1. Weak spots: day labels at 27 px and the OPEN/CLOSED chip at 38 px; on 4:5 the "108 h" label touches the bubbles (finding 1). |
| Motion | 8 | A 60 fps continuous shot with masked rolls, springs and typing, and nothing simply fades in. The hop clears all copy on both formats (checked frame by frame at full resolution) and lands exactly on the logo's gold square. Short glitches remain: a wrong clock reading for 1 to 2 frames each midnight (finding 2), the flying "108" crossing labels and its own period (finding 3), and overlapping slivers in the headline swap (finding 4). |
| Continuity | 9 | One shot with no cuts. The line tip becomes the riding label, the "108" drops into "Closed 108.", the lit plot covers the closed hours, and the tip becomes the ANALIZA caret. The caret then lands on the real logo's gold square: I tracked it to (202, 1242) on 9:16 and (186, 1012) on 4:5, which are the gold-square centres of the logo file at its placed position. |
| Pacing | 8 | `pacing.py`: 30% still, beat CV 0.48, no frozen stretch over 3 s; one warning, a 5.58 s quiet run during the crawl. On the refbank 2 fps metric (as on the reference card): 0.0 cuts per 10 s (ref 0.0), 1 big change, mean gap 12.0 s (ref 13.0), quiet share 0.362 (ref 0.16), hook change 0.017 (ref 0.01). There is a real rest at 10.3-11.2 s after the landing. The CTA end hold is 2.5 s still after the gold rule, which the body copy's reading time needs. |
| Composition | 8 | Left-aligned grid. Pixel scan at 10 fps: on 9:16 all content stays inside y 286-1527 and x 88-935 (safe box 269-1536, x ≤ 940); on 4:5 inside y 67-1193 and x 78-1004 (60 px margin). The 4:5 is a real re-layout, and the gap under "booking." measures 41 px. "Closed 108." is now the biggest line from 13.0 s to 18.0 s. The 4:5 landing hold is crowded (finding 1). |
| Brand | 9 | The logo `wordmark-white.png` is byte-identical (md5 826fdf88...) to `straightscale-03/assets/brand/`. In the last frame it matches the file at its native size and position: mean error 2.2/255 on opaque pixels, red 193/18/28 against 200/18/27 in the file, gold 225/162/9 against 230/165/5 (codec only). Fonts are Playfair Display and Montserrat, with one gold accent. There is no red text on charcoal and no gold text on ivory. The grey is computed in code as marble at 60% over charcoal, and the code matches `brand.md`. |
| Sound | 8 | -14.0 LUFS integrated, -3.0 dBTP true peak, LRA 3.8 LU, astats peak -3.0 dBFS with no clipping; the same on 4:5. Onsets land 10-26 ms after every closing, the landing, the three maths lines, the turn, all nine answers, the fold, the typing, the logo and the gold rule. The rule cue (21.22 s) now reads: onset at 21.237 s, and the 4.5-12 kHz band rises +21.6 dB across it. The turn (13.56 s) is louder than its approach: -20.2 to -18.1 LUFS M, as the maker says. The ending rings out to below -55 dB. Nobody has listened yet. |
| Message with the sound off | 9 | The whole argument is on screen in order: the stated example, 168, 60, Closed 108, a system answers (bubbles turn gold with checks), Comment ANALIZA, and what comes in the DM. |

## What I did
1. **Probed both files** with ffprobe:
   - 1080x1920 and 1080x1350, H.264 yuv420p, 60/1 fps, 1440 frames, 24.000 s
   - AAC 48 kHz stereo, about 306 kb/s
   - 5,012,188 and 4,306,345 bytes
2. **Made my own phone-size sheets.** I extracted exact frames (`select` on the frame number, every 30th frame plus the
   last) at 360 px wide for both formats, and looked at all 49 per format. I also looked at full-resolution frames at
   0, 10.0, 12.0, 16.5, 23.0 and 23.98 s.
3. **Made exact-frame strips** and looked at each one:
   - day roll at four midnights (f46-50, 124-135, 206-210, 446-450)
   - "108" flight (f750-786 and f756-776 at full resolution)
   - headline swap (f798-832)
   - CTA fold (f1048-1090)
   - hop on both formats (f1118-1158, plus f1128-1145 at full resolution)
   - landing on the logo (f1148-1205)
   - gold rule (f1270-1288)
4. **Read every string letter by letter**, on screen and in `COPY`.
5. **Measured with scripts:**
   - contrast from sampled pixels
   - safe zones from a pixel scan every 6th frame of both formats
   - the hop path and speed by tracking the gold square every frame
   - the gap between the riding label and the bubbles every frame from 7.0 to 12.67 s on both formats
   - the logo against the file
6. **Re-ran the automatic checks:**
   - `motion-studio/tools/pacing.py`
   - `refbank/tools/frames_metrics.py` on my own 2 fps frames
   - `motion-studio/tools/audio_qa.py` on both files, with a spectrogram
   - ffmpeg `ebur128` (true peak) and `astats`
   - librosa onset detection against the cue sheet in `film/index.html` (B(j) = 0.556 + 0.667 j s)
   - momentary loudness (ebur128 metadata) and band RMS before and after each landing
   - `tools/seekcheck_hf.mjs` on both pages (PASS, PASS)
   - `tools/textcheck.mjs` on the 9:16 page (all reading times OK, zone PASS)
7. **Checked the deliverables.**

Not re-run: the HyperFrames `check --caption-zone` contrast report. My pixel contrast and safe-zone checks cover the
same ground.

## v2 claims, verified
| Claim | Result |
|---|---|
| 1. Axis labels 0/40/80/120, 34 px, grey | Confirmed on frames; glyph cores 5.8:1 on the ground |
| 2. "Closed 108." own line at 80 px | Confirmed (textcheck: math2 80 px); largest line from 13.0 s to 18.0 s |
| 3. Answered bubbles turn gold with a check, badge gone | Confirmed; each answer has a sound onset 15-40 ms after it |
| 4. Day roll in the last 3 frames of the 23:00 hour, midnight reads the new day | Mostly. 00:00 now shows the new day, but each midnight has one frame mid-roll and one or two frames reading "<new day> 23:00" (finding 2) |
| 5. CTA fold sequenced, at most three movers | Confirmed (top text out, chart fold and square from f1054 to f1066; "Comment" in from f1069; maths out from f1078 to f1084) |
| 6. Hop covers no letters; peak 65.6 px per frame | No overlap on either format. I measured a peak of 57.9 px per frame on 9:16 and 54.4 on 4:5 (under the reported figure and under the 80 limit) |
| 7. 4:5 lane 20 px lower, about 40 px under "booking." | Confirmed: 41 px |
| 8. Grey computed from kit colours | Confirmed in code (`mixHex(C.marble, C.char, 0.6)`) |
| 9. Gold rule cue at 21.22 s | Confirmed: onset at 21.237 s; +21.6 dB in 4.5-12 kHz |
| 10. Whoosh covers the hop; G chord at 18.89 s | The whoosh is there (4.5-12 kHz +14 dB at 18.89 s). The G chord is too soft for onset detection to separate it from the whoosh; it is only a musical detail |
| 11. 16 kHz low-pass, 17.4 kHz line lower | Confirmed on the spectrogram: only a faint trace remains |
| 12. Turn at 13.56 s louder than its approach | Confirmed: -20.2 to -18.1 LUFS M |

## Text check (M1, G-MOTION-TEXT)
On screen, in order:
- "Hours a week your / business is *closed* while / clients still write."
- "Example: open 09:00 to 19:00, / Monday to Saturday."
- Chart text: MON TUE WED THU FRI SAT SUN MON, OPEN / CLOSED, "Mon 09:00"-style clock, "N h", axis 0 / 40 / 80 / 120
- "168 hours in a week." · "You are open 60." · "Closed 108."
- "A system answers / in those hours:" · "instant replies, / follow-up, / booking."
- "Comment" · "ANALIZA."
- "The booking button for the / free 45-minute analysis / comes in the DM."
- The real logo

There are no misspellings, no em or en dashes (only the hyphens in "45-minute" and "follow-up"), no hype words, no
platform names or logos, and no prices, results, clients, reviews, guarantees or deadlines.

Numbers: 168 = 7 x 24. 60 = 6 x 10. 108 = 168 - 60. The riding values I checked along the crawl are correct
cumulative closed hours: 8, 14, 16, 25, 28, 33, 42, 50, 56, 58, 67, 70, 75, 84, 93, 101, 106, 108. 64% is not shown.
"instant replies, follow-up, booking" matches the kit's Build list (instant-answer and follow-up automations, AI
chatbot). "free 45-minute analysis" and "comes in the DM" match the kit's one offer and one path.

`captions.srt` matches the on-screen copy. Its cues overlap by design: it lists the lines, it is not a subtitle track.

## Findings (all minor)
1. **4:5 only: the "108 h" label touches the message bubbles during the landing hold** (10.0-12.55 s, 154 frames). The
   gap between the lower bubbles' tails and the top of "108" is 1 to 4 px, and their edges meet. At 360 px wide it reads
   as touching, at the film's climax. The 9:16 keeps at least 13 px.
   - Fix: in the 4:5 layout, set the riding label about 12 px lower or a little left of the tip after the landing, or
     raise the lane's lower bubble row.
2. **Each midnight shows a wrong time for 1 to 2 frames.** The day rolls before the hour does:
   - f49-50 (0.82-0.83 s) read "Tue 23:00"
   - f129 reads "Wed 23:00"
   - f209 reads "Thu 23:00"
   - f449 reads "Sun 23:00"

   Each of these frames is clean and legible, and f50 is an even frame, so it would survive a 30 fps re-encode. This is
   much better than v1's "Tue 00:00" for 3 to 4 frames, but it is not yet a clean roll. f50 also shows that the
   floor(h) at exact midnight lands on 23.
   - Fix: switch the hour digits on the same frame as the day settles, or start the day roll on the frame where the hour
     becomes 00.
3. **The flying "108" crosses the day labels and its own period** (12.67-12.93 s). It passes over "SUN MON" for about 3
   frames (f760-762). As it slides left into its slot, the slot's period is already drawn, so for about 4 frames
   (f770-774) the number reads "1.08", with a dot inside it.
   - Fix: reveal the period when the number lands, and drop the number right of the day-label row or above it.
4. **Headline swap slivers** (13.67-13.73 s, f820-824). The incoming "A system answers" rolls in over the band where the
   outgoing line is still clipping out, so for 2 to 3 frames it looks struck through. It is cosmetic at 60 fps.
   - Fix: let each outgoing line clear its band before the incoming line enters it.
5. **Small chart scaffolding.** The day labels are 27 px (9 px on a 360 px screen) and the OPEN/CLOSED chip is 38 px,
   both under the 44 px body floor. Their contrast is fine (5.8:1), and the 116 px clock carries the day.
   - Fix (optional): day labels at 30-32 px.
6. **Copy:** "while clients still write." reads slightly non-native. It is the brief's fixed wording, so this is the
   owner's decision; an alternative is "while clients still message you".

The list "instant replies, follow-up, booking." meets the per-line reading rule but not the stricter whole-block rule.
That is known and logged, so it is not a new finding.

## Gate checks
| Check | Result | Evidence |
|---|---|---|
| M1 spelling | PASS | All strings above, on screen and in `COPY` |
| M2 overlaps / clipping | PASS (minor) | Hop clean. Transit overlaps: findings 3 and 4. 4:5 label contact: finding 1 |
| M3 safe zones + contrast | PASS | Pixel scan inside the zones on both formats; reading text 5.6-15.2:1 |
| M4 text on its spoken word | N/A | No voice. Sound cues sit on the visual events (10-26 ms) |
| M5 motion by 1 s, hook text by 0.3 s | PASS | Text at frame 0, clock ticking from about 0.07 s, first climb at 0.556 s |
| M6 brand colours and fonts | PASS | Kit colours, a derived grey documented in code and `brand.md`, Playfair Display and Montserrat |
| M7 generated images passed G-VIS | N/A | No generated images |
| F1 frames clean | PASS (minor) | 0.5 s sheets on both formats, plus strips at every fast moment; findings 2-4 last 1 to 4 frames |
| F2 sound-off | PASS | The argument is complete on screen |
| F3 captions | PASS | `captions.srt` equals the on-screen copy |
| F4 transcript | N/A | No voice |
| F5 loudness / true peak | PASS | -14.0 LUFS, -3.0 dBTP, both formats |
| F6 hook timing | PASS | Hook text at 0.0 s |
| F7 policy | PASS | No before/after, no "your [condition]", no AI media, the example is labelled |
| F8 credits | PASS | 0 credits. CC0 samples, OFL fonts and the GSAP licence are listed in CREDITS.md |
| onetake gate 5 (render) | PASS | Peak 57.9 px per frame (under 80); 30% still, plus a rest of 1 s or more |
| onetake gate 6 (audio) | PASS | Landings louder than their approach (land, maths, turn, fold, logo, rule band); no mud beyond one window (16.5 s); post-AAC peak -3.0 dBFS; quiet windows present |
| onetake gate 8 (final viewing) | PASS | Muted: the idea is clear. Phone size: every word that matters is readable. No swapped beats, no frozen frame of 3 s or more |

## Deliverables
All present in `deliver/v2/`:
- 9:16 master (1080x1920, 60 fps, 24.000 s, 1440 frames)
- 4:5 (1080x1350, the same timing)
- `poster.jpg` (1080x1920, the finished chart at 108 h)
- `contact-sheet.jpg` and `contact-sheet-4x5.jpg`
- `captions.srt`, `CREDITS.md`, `CHANGELOG.md`

`deliver/v1/` is untouched.

## Still required before posting
1. A person listens on a phone speaker and on earbuds.
2. The person approves the cut in the hub.
3. After approval, the refbank ledger entry from `PROJECT.md` is logged.

Findings 1 and 2 are cheap fixes if a v3 is made. They are not blockers.
