# Changelog: StraightScale 06 "The 108-hour week"

## v2 · 2026-10-20
Fixes for the eleven minor findings of the independent review (`docs/review_independent_r1.md`, verdict PASS).
Same copy, same length (24.0 s), same concept. v1 is unchanged in `deliver/v1/`; v1 sources are kept in `versions/v1/`.

Picture (`film/index.html`; the 4:5 page is rebuilt from it by `tools/make45.sh`):
1. Axis labels: only 0, 40, 80, 120 (was every 20 up to 140), 34 px Montserrat 700 (was 30 px 600), in the note grey.
   At 360 px wide the glyph cores measure 6.4:1 (v1 5.5:1) and the anti-aliased median 3.8:1 (v1 3.1:1), now at or above
   the note line on the same yardstick (5.8:1 / 3.6:1). HyperFrames contrast check 98/98.
2. Payoff: "Closed 108." is its own line at 80 px (4:5: 76 px), the largest line on screen from 12.6 s to 18.0 s. The
   flying "108" lands in the bigger slot.
3. Answers: each answered bubble turns gold and its three dots become a charcoal check, with a small punch. The 20 px
   badge is gone.
4. Day roll: runs in the last 0.05 s (3 frames at 60 fps) of the 23:00 hour, so midnight reads the new day ("Wed 00:00",
   not "Tue 00:00"). Measured: 2 mid-roll frames per day at 60 fps (v1: 3 to 5).
5. CTA fold sequenced: top text leaves, the chart folds, then the maths leave (from 17.78 s, done by 18.07 s). At most
   three movers at a time.
6. The gold square's hop to the logo goes round the right of the body copy, down, and in under it (cubic Bezier,
   smoothstep), from 18.72 s (a quarter beat earlier) to the logo at 19.22 s. 0 overlaps with any text box, checked
   every frame at 60 fps on both formats; peak 65.6 px/frame over the CTA (limit 80).
7. 4:5 only: the message lane, plot, day labels, chip, clock and maths moved 20 px lower; with the badges gone the gap
   under "booking." is about 40 px.
8. Grey: unchanged pixels (#9B958D), now computed in code as brand-kit marble at 60 % over charcoal and documented in
   `brand.md` as derived. Proposed for the brand kit as the secondary-text tint (not edited from here).

Sound (`audio/score.py`):
9. The gold rule under ANALIZA (21.22 s) gets a clear cue: piano C6 at a higher velocity doubled by the glockenspiel
   (the message ping, resolved to the tonic). Onset now detected at 21.237 s, strength 6.1 against a local median of
   0.6 (v1: no onset).
10. The hop whoosh lasts the whole hop and pans with it; the G chord stays on the eighth-note grid at 18.89 s.
11. The mix is low-passed at 16 kHz (8th order): the 17.4 kHz sampler line in the first 9 s is 16 dB lower.
12. The turn into "A system answers" (13.56 s) was not changed: it measures louder than its approach (400 ms windows,
    mono: -23.4 LUFS M before, -22.2 and -20.8 after; onset strength 8.1). The review's opposite reading did not
    reproduce.

Not changed (logged): the headline wording "clients still write." is the brief's fixed copy (the reviewer's optional
"while clients still message you" is for the owner to decide); the list block "instant replies, follow-up, booking."
still meets the per-line reading rule, not the whole-block rule.

Files:
- `straightscale-06-108-hour-week-9x16.mp4`: master, 1080x1920, H.264 + AAC 320k, 60 fps, 1440 frames, 24.000 s,
  5.0 MB (under 30 MB, so it is also the viewing copy).
- `straightscale-06-108-hour-week-4x5.mp4`: native 4:5 re-layout, 1080x1350, 60 fps, 4.3 MB.
- `poster.jpg` (10.6 s, the finished chart at 108 h), `contact-sheet.jpg` (one frame per beat, 9:16),
  `contact-sheet-4x5.jpg`, `captions.srt` (the on-screen lines with their times), `CREDITS.md`.
- Measured: -14.0 LUFS integrated, true peak -3.0 dBTP after AAC, both formats.
- Checked: HyperFrames check (caption band bottom 20 %, contrast 98/98) on both formats; `tools/textcheck.mjs`
  (reading time and safe zones every 0.05 s) on both; `tools/seekcheck_hf.mjs` on both; `tools/pacing.py`;
  `refbank/tools/frames_metrics.py` at 2 fps; `tools/audio_qa.py` and a spectrogram (`out/spectrum_v2.png`);
  onset detection at the cues; exact-frame strips of the day roll, the CTA fold and the hop.
- Not checked: nobody has listened to the mix yet. A person should, on a phone speaker and on earbuds, before posting.

## v1 · 2026-10-20
First delivery. English, no voiceover, 24.0 s, 60 fps. See `deliver/v1/CHANGELOG.md`.
