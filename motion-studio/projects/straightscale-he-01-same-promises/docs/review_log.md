# Review log: StraightScale (Hebrew) · 01 "What everyone promises"

Every round is logged. Never ship with a known blemish without writing it here and telling the client.
Build: HyperFrames 0.8.150 in `film/` (Concept A, "The stamp"). Silent: no voice exists yet, timing is the scratch
timing from `docs/script.md` (`film/timing.json`).

## Styleframes, round 1 · 5 Nov 2026
Sheet (phone size, 360 px wide): `docs/styleframes/round1-phone-sheet.jpg`. Frames: (a) hook 2.0 s, (b) tally 10.9 s,
(c) price sticker 14.95 s, (d) blank slip with the stamp lifting 30.8 s. Rendered with `hyperframes snapshot`.

| Axis | (a) hook | (b) tally | (c) sticker | (d) blank slip |
|---|---|---|---|---|
| Hook (stops the thumb) | 8 | 8 | 8 | 7 |
| Readability at 360 px | 9 | 8 | 9 | 8 |
| Motion (weight, springs, implied path) | 7 | 7 | 7 | 7 |
| Composition (focal point, no empty half, safe zones) | 7 | 8 | 7 | 6 |
| Brand (palette, type, logo rules) | 8 | 8 | 9 | 8 |
| Message with the sound off | 8 | 9 | 8 | 7 |

Evidence:
- (a) The stamped "חינם" on a real headline under "רק שואלים אתכם מחיר?" reads at once; key line 92 px (31 px at 360),
  headline 68 px on screen, print about 120 px. But the slip and the hovering stamp sit high: the stamp almost touches
  the key line and the lower third holds one caption word.
- (b) "8 מתוך 14" in the right RTL order (8 on the right), source line under it, a full pile with red prints. The pile
  headlines are about 12 px at 360 (texture, not for reading); the prints and the count carry it.
- (c) The prints line up in one red column (they look identical), the gold "₪?" is the only different thing. The stack
  sits high and the lower 35 % is empty (no caption on line 5, the key line covers it).
- (d) Empty headline with the caret, tape over the name, the stamp lifting away at the left. The slip sits in the upper
  middle and the lower 45 % is empty until the caption.
- Motion is scored from stills and the springs' settle curves here; the draft cut checks it for real.

Three worst problems and the fix for each:
1. (d) composition 6: slip too high, empty lower half. Fix: camera frames the viewer's slip lower (centre at about
   1040 px) for lines 10 to 12.
2. (a) composition 7: stamp crowds the key line. Fix: hook framing lower (slip centre at about 1120 px), so the hover
   sits in the middle band and the slip in the lower middle.
3. (c) composition 7: stack high. Fix: stack framed lower (centre at about 1040 px).

## Styleframes, round 2 · 5 Nov 2026
Sheet: `docs/styleframes/round2-phone-sheet.jpg`. Full frames: `docs/styleframes/sf-a-hook-2.0s.jpg`,
`sf-b-tally-10.9s.jpg`, `sf-c-sticker-14.95s.jpg`, `sf-d-blank-slip-30.8s.jpg`. Motion checked on strips (scratchpad):
the hook toss and gravity fall 0 to 1.6 s, the cascade and the 7 hits 2.3 to 10.2 s, the stack and the sticker slap.

| Axis | (a) hook | (b) tally | (c) sticker | (d) blank slip |
|---|---|---|---|---|
| Hook (stops the thumb) | 8 | 8 | 8 | 8 |
| Readability at 360 px | 9 | 8 | 9 | 8 |
| Motion | 8 | 8 | 8 | 8 |
| Composition | 8 | 8 | 8 | 8 |
| Brand | 8 | 8 | 9 | 8 |
| Message with the sound off | 8 | 9 | 8 | 8 |

What changed since round 1 (and why the scores moved):
- Framing: the hook slip sits lower (centre about 1120 px) with the stamp hovering in the middle band, clear of the
  key line; the stack and the viewer's slip are framed lower too. No frame has an empty half any more except the
  short rests where the key line carries the whole spoken line (line 5).
- Ink: the print word was faint and sat under the headline's first line. The face is now 400 x 160 px, prints at the
  slip's bottom left (over the short last line), with fuller coverage; the word reads at once (a, b). The neat stack
  now lets each lower slip peek out at the bottom, so the eight prints form one red column (c).
- The stamp parks top left beside the stack so it no longer hides the sticker (c); its exit is a slow lift toward the
  camera and out to the left (d), and its shadow fades out as it rises (a pale band on the slip at 33.8 s is gone).
- Slips are tossed in from the side edges, never through the top band; key-line words rise from 165 % (no letter
  tops showing under the mask); the hook slip is already mid-toss on frame 0.
- Determinism bug found and fixed: GSAP's lazy first render left a stale caption on sequential seeks (snapshot at
  14.95 s after 13.4 s showed line 4's caption; a cold seek did not). The clock tween now has `lazy: false` and
  renders from its own time.

Still weak (logged, not blocking 8): the pile's headlines are about 12 px at 360 px in (b) (texture: the prints and
the count carry the beat); (a) shows only the first caption word at 2.0 s; the tape lets "[שם העסק]" show faintly
through, like real masking tape.

## Draft cut v0 (silent, scratch timing) · 5 Nov 2026
File: `renders/draft-v0-silent.mp4` (HyperFrames `render --quality draft`: 1080x1920, 30 fps, 1209 frames, 40.3 s,
11.8 MB, no audio). Contact sheet, one frame per beat at 360 px wide: `docs/contact-draft-v0.jpg` (22 beats).

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | 0.0 slip mid-toss + "רק" already up; 1.1 the stamp lands on "מחיר?"; 1.3 to 2.0 "חינם" in red under the question |
| Readability at phone size | 8 | key lines 92 px, captions 52 px, tally 140 px, prints about 110 px; pile headlines 3 to 11 s are about 36 px on screen (texture) |
| Motion quality | 8 | springs only (lib/motion.js), gravity fall + 2-frame squash + 3-frame shake on each hit, side tosses with bounce, slow lift-away |
| Continuity | 8 | one top-down shot; the stamp is in every beat until 31 s; the caret becomes the end card |
| Variety and pacing | 8 | pacing.py: 18 beats, CV 0.79, spread 16.4x, longest quiet run 2.92 s, no frozen stretch; calmer at 15 to 18 s and 20 to 24 s |
| Composition | 8 | focal point per beat, no text in the UI zones (check --caption-zone passes); the stamp-alone beat (15 to 18 s) is sparse by design |
| Brand accuracy | 8 | marble/ivory/charcoal, one red accent, gold only on the sticker, Frank Ruhl Libre + Heebo self-hosted, official white wordmark file |
| Sound | n/a | silent draft: no voice yet (HeyGen blocked), no score or foley yet |
| Message clear with the sound off | 8 | top band carries each key line, captions carry the rest; the count and the column of identical stamps carry the proof |

Automatic checks:
- `tools/seekcheck.mjs --hf --dur 40.3 --n 24`: PASS (same frame after a different seek at 24 sample times).
- `tools/pacing.py`: all PASS (still 14 %, quiet 46 %, longest quiet run 2.92 s, beat CV 0.79, spread 16.4x).
- `tools/audio_qa.py`: not run (no audio).
- HyperFrames `check --caption-zone "x0=0;y0=.79;x1=1;y1=1;severity=error"` (bottom 400 px): passed, 0 errors, 0
  warnings, 2 info (transients: the viewer's slip passing under the key line at 18.1 s; the hovering stamp over its
  label at 29.1 s); contrast 28/28 WCAG AA. Same with `--at-transitions`: passed. Extra runs with the top 250 px and
  the right 140 px as the band: passed.
- `node --test film/tests/*.test.mjs`: 11/11 pass; `python3 tools/test_timing.py`: 4/4 pass.

Found and fixed while checking (both would have shipped wrong frames):
1. `check` seeks the timeline with GSAP's plain `seek()` (callbacks suppressed), so an `onUpdate`-driven film went
   stale there. The film clock is now a GSAP getter/setter property, painted on every render whatever the seek mode.
2. Elements shown with `visibility: visible` inside a hidden parent still painted after a backward seek (end-card
   call to action, tape). Show/hide now uses `display`.
3. Render failed with "zero duration" because the timeline is registered after the fonts load; the build promise is
   now held as `window.__hf.buildReady["film"]` and the timeline is rebound.

Three worst problems (not fixed in v0) and the fix for each:
1. The pile is texture, not reading: from 3 to 11 s the 14 headlines are about 12 px at 360 px wide and overlap. Fix
   if Matan wants them read: hold one or two slips at full size during line 2 (a 0.6 s look at a headline) before
   the camera pulls back.
2. Two calm stretches (15 to 18 s, the stamp alone; 20 to 24 s, tape and underline) depend on the voice and the score
   to carry them. Fix after the voice exists: retime, then add the stamp's small turn on "ככה" and a pencil tick on
   "רק את הכותרת" if they still sit quiet.
3. Scratch timing: word starts are letter-count estimates. The 0.26 s save hits, the tally lock freeze and the two-line
   key breaks need a re-look on the real voice (`tools/retime.py audio/words.json`, a data change).
