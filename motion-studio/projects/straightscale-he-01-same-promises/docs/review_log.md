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

## Draft cut v1 (silent) · fixes for the round 3 fresh review (`docs/reviews/round3-fresh-reviewer.md`) · 5 Nov 2026
File: `renders/draft-v1-silent.mp4` (1080x1920, 30 fps, 1209 frames, 40.3 s, 13.2 MB, no audio). Contact sheet (23
beats, 360 px wide): `docs/contact-draft-v1.jpg`. Strips (every 2 frames, 0.2 s before to 0.27 s after) at 1.1, 14.9,
24.0 and 34.4 s: `docs/strips-draft-v1.jpg`. Decisions per defect are the coordinator's (5 Nov).

| Defect | What changed (file) | Check |
|---|---|---|
| D1 sticker read "נם", "?" on the wrong side (blocking) | A gold hang tag (pointed end, hole) with "₪?" in Heebo 800 at 124 px, `direction: rtl` so the shekel sits right of "?" (read: shekel, then the question); its shadow on a wrapper; placed on the stack's top edge, clear of the headline and the right UI zone (`sticker.js`, `paper.css`) | 14.9 s strip and crop at 360 px: reads as a shekel price tag, not letters, so the "?" was kept |
| D2 slow second half | 21 new cues in `timing.json`, each on a spoken word, each a place for a sound later: the stamp turns over at the hook and back (`stamp.flip`, `stamp.flipback`); the stamp alone moves on line 6 (`stamp.slide`, `.settle`, `.rise`, `.drift`, `.sit`); it hops aside (`stamp.aside`); the viewer's slip settles with a small bounce (`viewer.settle`); a finger's shadow covers the name on "תכסו" (`finger.in`), the tape is pressed on "האצבע" (`tape.press`), the finger leaves (`finger.out`); the underline draws one step per word of "ותקראו רק את הכותרת" (`rule.1` to `rule.4`); the hover drifts, dips toward the headline and lifts (`hover.drift`, `.dip`, `.lift`); three camera cues (`cam.choose`, `cam.pointer`, `cam.meeting`). The camera follows the action on these cues (to the name, along the underline as it draws right to left, in on the dip, onto the backspaced line, onto the pointer). Nothing shortened (`stamping.js`, `viewer.js`, `cover.js`, `underline.js`, `layout.js`) | motion energy per second (mean frame difference, 10 fps): 14-18 s 4.0 to 4.5, 19-24.5 s 0.55 to 2.76, 25.5-30 s 0.92 to 2.10, 31-34.5 s 0.74 to 2.03; every second from 13 s to the end card is now at 1.1 or above (lowest 1.19 at 21 s); only the end-card hold (38-40.3 s) rests |
| D3 top 800 px empty 31.7-36 s | Line 11's pointer "למשל, מה קורה אצלכם בפגישה הראשונה?" is now the key line in the top band (two lines) and stays until the end card; the under-slip hint (`hint.js`) is gone (`content.js`, `band.js`) | contact sheet 33.6 and 35.6 s |
| D4 stamp read as a button | Drawn as a rubber stamp from above: a turned wooden handle (shaded, grain rings, top shifted toward the camera's corner, casting a shadow), a metal neck ring with the wooden neck in it, a dark rubber layer under the red mount. At the hook it turns over (1.34 to 1.8 s, about 0.45 s face up) to show its rubber face with "חינם" cut in mirror image, then turns back; a 2-frame tilt would not read, so the turn is slower and sits in the hook's rest (`stamp-body.js`, `stamp.js`, `stamp.css`) | 1.75 s frame; 17.2 s crop |
| D5 masks cut glyphs mid-rise | No hard mask any more: each word rises 38 % of its height while its ink comes up over 3 frames; a leaving line drops and fades in 0.16 s and is gone before the next arrives (`words.js`, `band.js`, `base.css`) | strips at 1.1 s ("מחיר?"), 24.0 s (caption) and 34.4 s: no half-cut glyph |
| D6 source label 40 px, covered at 4.0 s | 46 px, set higher (top 416 px), the pile framed 35 px lower, so the slips land below it (`overlay.css`, `layout.js`) | 4.8 s frame |
| D7 end card off centre | Wordmark and call to action centred on x = 540 and grouped in the middle of the safe area (logo 742-955 px, call to action 1010 px, Heebo 700 56 px); the caret is placed outside the centred line (`endcard.js`, `overlay.css`) | 39.5 s frame |
| D8 stamp covered "[הכותרת]" 25-27.9 s | It hovers over the empty left of the slip, beside the headline; its shadow stays off the words (`stamping.js`, `layout.js`) | 26.4 s frame |

Automatic checks on v1:
- `tools/seekcheck.mjs --hf --dur 40.3 --n 24`: PASS.
- HyperFrames `check --caption-zone "x0=0;y0=.79;x1=1;y1=1;severity=error"`: passed, 0 errors, 0 warnings, 0 info,
  contrast 32/32 WCAG AA. Top 250 px and right 140 px as the band: passed.
- `tools/pacing.py`: all PASS (still 7 %, quiet 25 %, 30 beats, CV 0.57, spread 7.6x, longest quiet run 2.58 s, no
  frozen stretch).
- Unit tests: `node --test film/tests/*.test.mjs` 11/11, `python3 tools/test_timing.py` 4/4.

My scores after the fixes (the next fresh review decides): hook 8, readability 8, motion 8, continuity 8, pacing 8,
composition 8, brand 8, message with the sound off 8; sound n/a.

Not done, and why:
- The pile's headlines (3-11 s) are still texture at 360 px; the review listed it as evidence, not as a defect, and
  holding slips at full size would change the cascade's timing by hand.
- The turn-over at the hook is about 0.45 s, not 2-3 frames: at 2-3 frames the mirrored word does not register.
- The camera now moves on most cues from 19 to 35 s; if the next review finds it too busy, the camera keys in
  `layout.js` are the one place to calm it.

## Draft cut v2 (silent) · fixes for the round 4 fresh review (`docs/reviews/round4-fresh-reviewer.md`) · 5 Nov 2026
File: `renders/draft-v2-silent.mp4` (1080x1920, 30 fps, 1209 frames, 40.3 s, 14.0 MB, no audio). Contact sheet (27
beats, 300 px wide): `docs/contact-draft-v2.jpg`. Strips (every 2 frames, 0.2 s before to 0.27 s after) at 3.0, 21.5,
30.0 and 37.0 s: `docs/strips-draft-v2.jpg`. Decisions per finding are the coordinator's (5 Nov).

| Finding | What changed (file) |
|---|---|
| N1 pacing (holding the verdict) | Story events on word cues (`timing.json`, now 62 cues), one at least every 1.1 s through 25-36 s: the competitors' three identical slips slide in under yours on "המתחרה" (`rival.in`), line up exactly on yours on "אחד" (`rival.match`: word for word, you cannot tell them apart), part on "כן" (`rival.part`, with a camera beat), square up on "בדיוק" (`rival.gather`) and are pushed off the desk on "בפגישה" (`rival.off`), leaving yours alone, which squares up on "הראשונה" (`viewer.square`). Your placeholder is struck through on "תחליפו" (`strike`) and backspaced on "אותה" (`clear`); on "במשהו" the old reflex "חינם" is typed (`retype`), struck on "לא" (`unsay`) and deleted on "יכול" (`unsay.del`). The push into the caret now steps on "תשמרו", "הסרטון", "תשלחו" (`cam.caret`, `cam.save`, `cam.send`). For 3-5.5 s the cascade starts on "זה" (1.9 s) with the middle rows first (also N9), the camera leans in on "משכנתאות" (`cam.ads`), the stamp rises toward the pile on "פייסבוק" (`stamp.ready`). 19-23 s: the hand runs along the tape on "העסק" (`finger.slide`). Nothing trimmed by hand. New files `rivals.js`, `headline.js` |
| N2 finger read as a pen | `finger.js`: the shadow of a hand pointing in from the lower right, a tapered fingertip on the name, a knuckle step, the back of the hand with curled fingers, soft edge (5 px blur), tilted 6 degrees; it slides in, runs along the name, presses, leaves (`cover.js`) |
| N3 tape see-through | The tape is opaque (#E9DEC4) and the name under it drops to 30 % ink, so nothing shows (`paper.css`, `cover.js`) |
| N4 logo cut by the mask | No mask on the logo; it rises (14 %) and comes up from 60 % ink only at t0 + 0.55 s, when the opening card has fully cleared it; the call to action follows at t0 + 0.95 s (`endcard.js`, `overlay.css`) |
| N5 maroon stamp face | Charcoal rubber with red #BE0F18 ink on the raised, mirrored letters, the red mount around it; the rubber layer under the mount is charcoal too (`stamp.css`) |
| N7 centred second lines | Titles are built as rows; a wrapped title's second row is right-aligned under the first, the block centred (`words.js`, `base.css`) |
| N8 words fade from light grey | New words start at 60 % ink and reach full in 3 frames (`words.js`) |
| N6 pile headlines | Not done (coordinator's decision): the stamps and the count carry that beat |

Motion energy per second (mean absolute frame difference, grey 270x480 at 10 fps; v1 and v2 measured the same way,
scratch `energy.py`):

| Second | 3 | 4 | 5 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v1 | 2.23 | 2.35 | 1.56 | 2.61 | 1.95 | 2.09 | 2.46 | 1.36 | 3.64 | 1.63 | 1.90 | 2.57 | 2.26 | 1.45 |
| v2 | 3.11 | 5.42 | 2.19 | 3.50 | 2.14 | 3.31 | 3.93 | 3.55 | 3.72 | 1.82 | 2.31 | 3.18 | 2.14 | 2.35 |

Means: 3-5.5 s 2.05 to 3.57; 25-36 s 2.17 to 2.90 (36 s: 3.94 to 5.87). The reviewer's own v1 numbers for 25-35 s were
lower (1.0-3.6); its metric runs at a different scale, so compare v1 and v2 on one method.

Automatic checks on v2:
- `tools/seekcheck.mjs --hf --dur 40.3 --n 24`: PASS.
- HyperFrames `check --caption-zone "x0=0;y0=.79;x1=1;y1=1;severity=error"`: passed, 0 errors, 0 warnings, 0 info,
  contrast 29/29 WCAG AA. Top 250 px and right 140 px as the band: passed.
- `tools/pacing.py`: all PASS (still 5 %, quiet 18 %, 37 beats, CV 0.64, spread 8.4x, longest quiet run 2.58 s, no
  frozen stretch over 3 s).
- Unit tests: node 11/11, Python 4/4.

Watch points for the next review: the "חינם" typed into your own headline on "במשהו" is struck on "לא" and deleted on
"יכול" (0.85 s up, 0.3 s of it struck): the old reflex, then "not that". If it reads as an instruction, drop the
`retype` cue and the line goes straight from backspace to the blinking caret. The camera moves on most cues from 19 s on;
the framings are all in `film/src/layout.js`.
