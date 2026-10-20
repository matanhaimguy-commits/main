# Independent review, round 1: StraightScale film 04 "One message, all the way" (deliver/v1)

Reviewer: a new agent that did not make the film and did not see the maker's reasoning. I checked the maker's
report against the files. Gates used: G-MOTION-FRAMES M1-M7 and G-FINAL F1-F8 where they apply (code-rendered, no
voice), G-MOTION-TEXT, onetake-principles §8, motion-studio/CLAUDE.md, clients/straightscale/brand-kit.md.

**Verdict: FAIL.** One major finding (text over a washed-out logo during the hook, in both formats) and three
axes under 8.

## What I opened
- My own frames from both delivered files: a 0.5 s contact sheet of the 9:16 master and the 4:5 (54 frames each),
  full-resolution frames at 0.0, 1.0, 1.5, 2.0, 2.5, 3.62, 8.0, 10.0, 13.0, 16.6, 17.5 and 24.0 s, strips at 12 fps
  around the dive (3.30-4.22 s), the rise and rebuild (6.20-7.20 s), the whip (7.70-8.62 s), the pull-back
  (16.8-17.9 s) and the zoom back in (20.1-21.2 s), a frame-by-frame strip of the Comment hit (1.40-1.60 s), and the
  loop seam (26.4 s to 0.9 s).
- Also: deliver/v1/poster.jpg, contact-sheet.jpg, captions.srt, CREDITS.md, CHANGELOG.md, PROJECT.md,
  index.html (LINES, STYLE, scrim, drawLogo, LAY), audio/events.json, the reference card ig-satisfy3dverse, and the
  logo files.

## Measured (my runs)
| Check | 9:16 master | 4:5 | Target / reference |
|---|---|---|---|
| Duration / frames / fps | 27.000 s / 1620 / 60 | 27.000 s / 1620 / 60 | as reported: yes |
| Size | 21.2 MB | 16.4 MB | as reported: yes |
| Integrated loudness (ebur128) | -13.8 LUFS | -13.8 LUFS | -14 +/- 1: pass |
| True peak | -2.3 dBTP | -2.3 dBTP | <= -1.5: pass |
| Sample peak / clipping | -2.37 dBFS, 0 samples over -0.1 dBFS | the audio is bit-identical to the 9:16 | pass |
| LRA | 10.1 LU | 10.1 LU | |
| Hit sync (audio onsets vs events.json, 30 hits) | median -11 ms, worst 25 ms | same audio | pass |
| Planned silence | digital zero 5.05-6.45 s; under -50 dB from 4.4 to 6.8 s | | audio_qa marks 5-6 s as a dropout |
| Band energy | 60-120 Hz 39 %, 300-2500 Hz 51 %, 2.5-6 kHz 2.6 % | | through a 150 Hz high-pass (roughly a phone speaker): -15.1 LUFS |
| pacing.py | still 12 %, quiet 28 %, longest quiet run 4.42 s (22.2-26.6 s), beat CV 1.22, 3 transitions | | |
| frames_metrics (1.5 s step, the reference's scale) | 1.80 s between big changes, CV 0.45, quiet 0.118, hook change 0.214 | | reference: 1.54, 0.15, 0.0, 0.425 |
| frames_metrics (0.5 s step) | quiet 0.245, longest quiet 4.0 s | | |

The pacing numbers I measured match the maker's to within frame-sampling differences (maker: 1.93, 0.62, 0.118, 0.194).
The run itself (9 to 17 s) is fast: a contact every 0.5 s and a station every 1.0 s.

## Text, letter by letter (M1, G-MOTION-TEXT)
I checked every string on screen and against `LINES`: "Watch where this / client gets lost." · "No reply." ·
"Gone." · "Build the / missing step." · plate labels COMMENT, REPLY + "instant answer", BOOKING, REMINDER +
"follow-up", VISIT + "rebooking", REVIEW, REFERRAL · "Every step answered." · "That is a system." · "Send this to an
owner / who loses clients / after the first message."
- Spelling and English are correct. There are no em dashes ("follow-up" uses a plain hyphen), no numbers, no hype
  words, no platform names or logos, no prices, deadlines or guarantees.
- Every sub-label is a Build item in the brand kit.
- Colour pairs: crimson on ivory is about 6.4:1, gold on charcoal about 6.8:1, ivory on red plates about 6:1, and
  charcoal on ivory passes. There is no gold text on ivory and no red text on charcoal.
- The ghost "REPLY" label (charcoal at 42 % opacity on marble) is low-contrast on purpose, because it stands for the
  missing step. It reads at the 3.5 s close-up.
- Logo: `assets/brand/logo-full.png` has the same MD5 as `straightscale-03/assets/brand/logo-full.png`
  (969e777f...). The crop at 24.0 s matches the file's shape and colours, and `drawLogo` only calls `drawImage`.
  So the file is real. How it is composited is a problem: see finding 1.

## Readability (0.25 s per word + 0.5 s)
| Line | Words | Needs | On screen (fully in to start of exit) |
|---|---|---|---|
| Watch where this client gets lost. | 6 | 2.0 s | 0.0-3.9 s: pass |
| No reply. / Gone. | 2 / 1 | 1.0 / 0.75 s | 3.95-6.35 / 4.3-6.4: pass |
| Build the missing step. | 4 | 1.5 s | about 7.0-10.05: pass |
| REPLY · instant answer | 3 | 1.25 s | on the plate from about 7.4 s, readable again at 12.5-14.5: pass |
| Station labels | 1-2 | <= 1.0 s | each in frame for 2-3 s in the run: pass |
| Every step answered. / That is a system. | 3 / 4 | 1.25 / 1.5 s | 17.3-20.5 / 17.9-20.55: pass |
| Send this to an owner who loses clients after the first message. | 12 | 3.5 s | 20.85-26.45 (5.6 s): pass, but 2.1 s longer than it needs (finding 2) |

Sizes on 9:16: headline 96 px, captions 88 and 76 px, the ask 64 px, "No reply." 132 px, "Gone." 176 px, plate
labels 46 x 1.18 = 54 px, sub-labels 52 px. All are at least 44 px. During the map pull-back the labels drop to
about 21 px (15 px in 4:5). They are a picture there, and the caption carries the message.

Safe zones on 9:16: key text sits between y 316 and 508 and stays clear of the right edge. The end-card logo's right
edge is at about x 929, which leaves 151 px. The wall logo passes through the top 250 px zone for a moment at about
11.3 s while the camera moves, which is acceptable. The 4:5 keeps its 64 px margins.

## Motion, continuity, loop
- Every transition is bridged: the push into the hole (3.5-4.1 s), the rise out of the dark with the plate sliding in
  (6.5-7.0 s), the whip back to the cradle (7.9-8.3 s), the pull-back with shutter blur (17.0-17.4 s) and the zoom
  back in (20.5-21.0 s). The strips show clean blur and no stepping.
- On the Comment hit, the ball touches the plate at frame 90 (1.50 s) and the plate lights at 1.52-1.55 s. That
  agrees with the audio onset (-14 ms).
- The loop seam is clean: the ask exits at 26.5-26.6 s, the headline rises in at 26.75 s, and frame 0 equals the end
  state. The ball kicks at 0.0 s. The headline is fully in at frame 0, so the hook text is there by 0.3 s and there
  is motion in the first second.

## Findings
1. **MAJOR: headline text over a ghosted logo, in the hook and twice more, in both formats.**
   - When: 0.8-3.0 s, 7.9-8.3 s and 9.8-11.0 s, in 9:16 and 4:5.
   - What I saw: the follow-cam carries the wall logo up into the caption band. The ivory scrim (90-94 % opaque,
     `scrim()`) washes it to a 6-10 % ghost, and "gets lost." / "missing step." are drawn across it (full-resolution
     frames at 1.5 and 2.0 s). The maker's own contact sheet shows it at 1.65 s.
   - Rules broken: M2 (no overlaps) and the brand rule that the real logo is shown clean. It looks like a watermark or
     a compositing error in the most-watched 3 seconds.
   - Related: a ghosted COMMENT plate sits behind "Build the / missing step." at 6.87-7.10 s.
   - Fix: keep the logo out of the text rows while captions are on. Options:
     a. Move the logo's wall position, or its relation to the first-pass camera path, so it leaves frame or stays
        below y about 730 during 0-3.95 s and 6.75-10.1 s.
     b. Make the scrim fully opaque behind the glyph rows, with the soft fade only below the text, so nothing ghosts
        through.
     c. Give the logo a deliberate exit, such as the wall light dimming on it, before it reaches the band.
   - Then re-check strips at 0.6-3.2, 6.8-7.2, 7.8-8.4 and 9.6-11.2 s in both formats.
2. **MINOR, scored on pacing: the end of the film runs out of energy.**
   - When: 18.3-27.0 s.
   - Measured: the map hold at 18.3-20.3 s is quiet, and so is the ask at 22.2-26.6 s (a 4.42 s quiet run, with the
     camera locked from 21.2 to 27.0 s). Only two 30 px ball taps and a groove spark move. In all, 6.4 of the last
     9 seconds are quiet, sitting on the loop seam the format depends on. Reference quiet share: 0.0.
   - It does not trip any frozen rule. pacing.py finds no stretch of more than 3 s where nothing moves.
   - The maker's claim that the ask "needs 5 seconds to read" is wrong under the house rule: 12 words need 3.5 s.
   - Fix: hold the ask about 3.5-4.0 s. Use the time to keep the camera alive (for example, a slow push to the cradle
     and the ball rolling on the beats) or start the ask during the zoom back in. Aim for no quiet run over 3 s. A
     livelier end also lifts the first 2 s, which are the same frames when the reel loops.
3. MINOR: the hook changes about half as much as the reference in its first 2 s (0.19-0.21 against 0.425). The
   opening frame is a sparse pale wall with one small ball. It improves with fixes 1 and 2.
4. MINOR: 9.0-12.0 s is the same footage as 0.0-3.0 s, with only the headline and the Reply plate changed. That is
   3 s of repeated footage in the middle. Consider a different camera on the second pass, wider or faster, or start
   the replay at Comment.
5. MINOR: 4.0-6.5 s is a flat charcoal frame with centred text, close to the banned "centred text on flat
   background" look. The dive motivates it, but nothing of the hole is left. Keep a trace of depth, such as the hole
   rim, a vignette, or the ball's last glint, so it reads as inside the hole and not as a title card.
6. MINOR, sound:
   - The planned silence is true digital zero for 1.4 s (5.05-6.45 s), and audio_qa flags it as a dropout. A faint
     room tone (about -50 dBFS) would make it read as intended and still feel like silence.
   - Station hits are no louder than peg hits: about -9 dB on both, the gap is within about 1 dB, and gate 6 says hits
     should be the loudest. Lift the stations 2-3 dB.
   - Presence is thin: 2.5-6 kHz holds 2.6 % of the energy and the limiter takes up to 6.7 dB off the mallet attacks.
   - Nobody has listened yet. Someone needs to listen on a phone before approval.
7. MINOR, brand path: "comment ANALIZA" is not on screen. It must be in the post caption, because it is the brand
   kit's only path.
8. MINOR, delivery: captions.srt repeats the burned-in text. Do not upload it as closed captions, or the text appears
   twice.
9. Cosmetic: some marble veins curl into loops (for example near 3.6 s right of the hole, and 16.6 s at the bottom)
   and look more like squiggles than marble.

## Gate checklist
- M1 spelling: PASS.
- M2 overlaps or clipping: FAIL (finding 1).
- M3 safe zones and contrast: PASS.
- M4 timing against words: N/A (no voice); text lands on the events.
- M5 motion and hook text: PASS.
- M6 brand colours and fonts: PASS. Logo handling: see finding 1.
- M7 generated images: N/A.
- F1 clean frames: FAIL (finding 1).
- F2 sound-off: PASS. The story reads from the images and lines alone.
- F3 captions: PASS.
- F4 transcript: N/A.
- F5 loudness: PASS.
- F6 hook timing: PASS.
- F7 policy: PASS.
- F8 credits: PASS (0 spend, CC0 and OFL sources listed).
- Deliverables: all present (9x16, 4x5, poster, contact sheet, SRT, CREDITS, CHANGELOG). Duration and fps are as
  reported.

## Scores (0-10)
| Axis | Score | Why |
|---|---|---|
| Hook in the first 2 s | 7 | headline at frame 0 and the ball kicked at 0.0, but a ghost logo behind the headline and half the reference's change |
| Readability at phone size | 8 | every line is big and on screen long enough; the logo ghost dirties the hook line |
| Motion quality | 8 | real physics, springs, shutter blur, no stepping in the fast moves |
| Continuity | 9 | one world, every transition bridged, seamless loop |
| Pacing | 7 | the run is faster than the reference, but 6.4 of the last 9 s are quiet, the hook changes half as much, and 3 s are replayed |
| Composition | 7 | logo and plate ghosts under the caption band; flat dark card |
| Brand accuracy | 7 | real logo file, palette and type are right, but the logo is shown washed out with text across it |
| Sound sync | 8 | hits within 25 ms, loudness and peak on target, no clipping; stations not accented; nobody has listened |
| Message with the sound off | 9 | missing Reply, fall, rebuild, full path, and the lines carry it |

Re-review after fix 1, plus fix 2 or a justified alternative. Render new strips for the windows listed in finding 1
and re-run pacing.py.
