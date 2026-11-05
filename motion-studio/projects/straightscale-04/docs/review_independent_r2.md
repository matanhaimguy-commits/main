# Independent review, round 2: StraightScale film 04 "One message, all the way" (deliver/v2)

Reviewer: a new agent that did not make the film and did not see the maker's reasoning beyond the report handed to
it. I checked the report against the delivered files and my own measurements. Gates used: G-MOTION-FRAMES M1-M7 and
G-FINAL F1-F8 where they apply (code-rendered, no voice), G-MOTION-TEXT (M1, M3, M4, M6), onetake-principles §8,
motion-studio/CLAUDE.md, clients/straightscale/brand-kit.md. Round 1 is `docs/review_independent_r1.md`.

**Verdict: PASS.** No critical or major finding, and every axis scores 8 or higher. The round 1 major (headline over a
ghosted logo) is fixed in both formats, and the dead end is gone. Two conditions before posting, both outside the
file: a person listens on a phone, and the post goes out with `post-caption.txt` (comment ANALIZA) after the
owner approves it in the hub.

## What I opened
- My own frames from both delivered files (in my scratch folder, not in the project):
  - a 0.5 s contact sheet of the 9:16 master and of the 4:5 (50 frames each, 360 px wide, i.e. phone size)
  - full-resolution frames at 0.0, 3.7, 3.85, 4.0, 4.15, 6.6, 6.9, 7.2, 10.2, 17.3, 20.15, 20.3, 22.0 s (9:16) and
    4.0, 22.0 s (4:5)
  - strips: the dive (3.80-4.35 s, 20 fps), the rise and rebuild (6.3-7.4 s), the whip (7.70-8.58 s), the pull-back
    (16.8-17.9 s), the flight home (19.9-21.0 s), the caption handovers (20.15-20.33 s, every frame; 24.40-24.73 s),
    and the loop seam (24.30-24.95 s into 0.0 s)
  - frame by frame: the Reply station hit (12.450-12.550 s) and a tap at 22.0 s
  - a crop of the end-frame logo beside `straightscale-03/assets/brand/logo-full.png`
- Also: deliver/v2/poster.jpg, contact-sheet.jpg, captions.srt, post-caption.txt, CREDITS.md, CHANGELOG.md, PROJECT.md,
  docs/review_log.md (rounds 4-5), index.html (LINES, STYLE, LAY, scrim, drawLogo, hatchOpen, seek, the safe-zone
  boxes), audio/events.json, the reference card `refbank/cards/ig-satisfy3dverse.md`, and the logo files.

## Measured (my runs)
| Check | 9:16 master | 4:5 | Target / reference |
|---|---|---|---|
| Duration / frames / fps | 25.000 s / 1500 / 60, 1080x1920 | 25.000 s / 1500 / 60, 1080x1350 | as reported: yes |
| Size | 21.56 MB | 16.75 MB | as reported: yes |
| Integrated loudness (ebur128) | -14.0 LUFS | -14.0 LUFS | -14 +/- 1: pass |
| True peak / sample peak | -2.4 dBTP / -2.44 dBFS, 0 samples over -0.5 dBFS | the audio is bit-identical to the 9:16 | <= -1.5 dBTP: pass |
| LRA | 11.4 LU | 11.4 LU | |
| Phone-speaker proxy (150 Hz high-pass) | -14.6 LUFS | | v1: -15.1 |
| Band energy | 60-120 Hz 16 %, 300-2500 Hz 73 %, 2.5-6 kHz 5.5 % | | v1: 39 % / 51 % / 2.6 % |
| Half-second windows dominated by 100-300 Hz | 1 of 50 | | gate 6: none dominated: pass |
| Planned silence | room tone about -50 dBFS RMS from 4.4 to 6.6 s, no digital zero | | audio_qa flags 5-6 s as a dropout (expected) |
| Hit sync (audio onsets vs events.json, 30 hits, 2 kHz high-pass) | median +3 ms, worst 11 ms | same audio | pass |
| Stations vs pegs (onset peak above 800 Hz) | stations about 9 dB over pegs | | gate 6, hits loudest: pass |
| events.json vs the current page | re-exported with tools/events.mjs and diffed: identical (43 events, 25 s) | | |
| pacing.py | still 0 %, quiet 9 %, longest quiet run 1.5 s, CV 0.90, spread 10.6x, 2 transitions (3.92, 6.58) | quiet 7 %, longest 1.17 s, CV 0.77 | v1: quiet 28 %, 4.42 s |
| frames_metrics, 1.5 s step (the reference's scale) | 1.59 s between big changes, CV 0.23, quiet 0.0, hook change 0.227 | 1.59, 0.23, 0.0, 0.240 | reference: 1.54, 0.15, 0.0, 0.425 |
| frames_metrics, 0.5 s step | quiet 0.041, longest quiet 1.0 s, hook 0.178 | 0.041, 1.0 s, 0.181 | |
| Caption band, my own scan of the video (20 fps, top 540 px / 4:5 top 320 px, text masked) | 0 frames with structure under a caption; the only flag (20.15 s) is the exiting caption itself | same | |
| safezone.mjs (step 0.1 s) | ok | safezone45.mjs: ok | |
| readcheck.mjs | 7/7 PASS | | |
| seekcheck.mjs (25 s, 24 samples) | PASS, no seek errors every 0.1 s | | |
| Loop seam (mean frame change, last frames into first) | 1.60 against neighbours 1.10-1.53 | 1.80 against 1.10-1.54 | invisible in the strip |
| Audio seam | jump 0.077 (below the 99.9th percentile sample step of 0.23): no click | | |

My numbers match the maker's to within sampling differences. Two small differences: at the 1.5 s step I get change
rhythm CV 0.23 (the log says 0.0), and at the 0.5 s step quiet 0.041 with a 1.0 s longest quiet (the log says 0.02 and
0.5 s). Neither changes a verdict.

## Text, letter by letter (M1, G-MOTION-TEXT)
On screen and in `LINES`: "Watch where this / client gets lost." · "No reply." · "Gone." · "Build the / missing
step." · plate labels COMMENT, REPLY + "instant answer", BOOKING, REMINDER + "follow-up", VISIT + "rebooking", REVIEW,
REFERRAL · "Every step answered." · "That is a system." · "Send this to an owner / who loses clients / after the
first message."
- Spelling and English are correct in both formats. No em dashes ("follow-up" is a plain hyphen). No numbers, no hype
  words, no platform names or logos, no prices, deadlines or guarantees. Every sub-label is a Build item in the brand
  kit.
- Colour pairs: crimson on ivory (about 6.4:1), ivory on red plates, charcoal on ivory plates, ivory "No reply." and
  gold "Gone." on the dark. No gold text on ivory. No red text on charcoal, apart from 2-3 frames at 4.05-4.10 s
  where the exiting "gets lost." crosses the darkening band at low opacity. That is a fade, not a reading state.
- Logo: `assets/brand/logo-full.png` has the same MD5 as `straightscale-03/assets/brand/logo-full.png` (969e777f...).
  `drawLogo` only calls `drawImage` and masks it with the two doors. The crop at 22.0 s matches the file's shape,
  proportions and colours. See finding 2 for a small light lift.
- post-caption.txt: plain English, the ANALIZA path and the 45-minute offer exactly as in the brand kit, no em dashes
  or hype words.

## Readability (0.25 s per word + 0.5 s), sizes and safe zones
| Line | Words | Needs | Held (fully in to start of exit) |
|---|---|---|---|
| Watch where this client gets lost. | 6 | 2.0 s | 3.73 s: pass (it also rises in across the loop seam) |
| No reply. / Gone. | 2 / 1 | 1.0 / 0.75 s | 2.10 / 1.80 s: pass |
| Build the missing step. | 4 | 1.5 s | 2.78 s: pass |
| Every step answered. / That is a system. | 3 / 4 | 1.25 / 1.5 s | 2.40 / 2.10 s: pass |
| Send this to an owner who loses clients after the first message. | 12 | 3.5 s | 3.59 s: pass, with no margin |
| Station labels | 1-2 | <= 1.0 s | each in frame 2-3 s during the run: pass |

- Sizes: on 9:16 the headline is 96 px, the captions 88 and 76 px, the ask 64 px, "No reply." 132 px and "Gone."
  176 px; plate labels are 54 px, sub-labels 52 px. On 4:5: 84, 80, 69 and 58 px. All are at least 44 px and all read
  at 360 px wide.
- Safe zones: on 9:16 caption glyphs sit between y about 306 and 520, right edges at x 850 or less. The end-frame logo
  is at y 735-820, below the band and inside the zone. The 4:5 keeps its 64 px margins. Both safe-zone tools pass.
- Handover frames are clean. "That is a system." is fully out by 20.23 s and the ask starts at 20.25 s. The ask is
  out by 24.73 s and the hook rises from 24.75 s. No two captions ever share rows.

## Round 1 findings, re-checked
1. **Major, logo ghost under the headline: FIXED, both formats.**
   - The band is flat under the type in every caption frame of my scan, including the dive (the band follows the
     light) and the rebuild.
   - The hook frame has no logo. The hatch stays shut from 24.6 s through 21.0 s, and the logo shows only in the end
     frame, below the band's fade.
   - COMMENT is settled below the band before "Build the missing step." rises at 6.95 s (strip 6.3-7.4 s).
2. **Minor, dead end: FIXED.**
   - The ask holds 3.59 s.
   - The lit path stays lit, the ball taps on 22, 23 and 23.5 s, the doors close, the flipper arms and the camera
     keeps pushing.
   - pacing.py shows no quiet run over 1.5 s, and the end rows read "+" (moving), not ":".
3. **Minor, hook change: IMPROVED, still below the reference** (0.227 against 0.425). Frame 0 is now a close shot with
   the headline already in and the ball kicked. See finding 1.
4. **Minor, replayed footage: IMPROVED.** Pass 2 is closer (z 1.42), with a swinging camera. It is still the same
   pegs in the same order, which the story needs, since it is the same client.
5. **Minor, dark as a title card: IMPROVED.** Converging shaft edges, drifting rings, a last glint and a warm falloff
   now read as depth at full size. At phone size they are faint, so 4.3-6.3 s still reads mostly as centred type on
   dark (finding 4).
6. **Minor, sound: FIXED as far as measurement can tell.** The room tone is in, stations are louder than pegs and
   presence went from 2.6 % to 5.5 %. Nobody has listened (finding 3).
7. **Minor, ANALIZA path: FIXED in the post caption.**
8. **Minor, SRT: NOTED.** The maker marks it as reference only.
9. **Cosmetic, marble veins: FIXED.** Long, nearly straight runs, no curls in any frame I looked at.

## New findings (none critical or major)
1. **MINOR, hook (0.0-2.0 s): the opening frame changes about half as much as the reference, and its biggest shape is
   an empty closed hatch.**
   - The closed marble hatch (a pale rounded box with two gold pins, about 640x190 px at y 610-820) sits right under
     the headline in frame 0 and in the poster.
   - On first view it reads as a blank panel. It pays off at the end, but in the hook it is dead weight next to a
     30 px ball.
   - Fix (optional): start the hook framing lower or wider, so the hatch is cut by the band or out of frame and the
     ball and the first lit pegs carry the frame. Alternatively, give the closed doors a hint of what is behind them
     (a thin crimson line in the seam).
2. **MINOR, brand: the scene light lifts the logo by about 11 %.**
   - In the end frame the wordmark's black measures RGB 46,45,40 against the file's 19,19,17. The mark red measures
     197,39,44 against 191,15,20.
   - Cause: the "light falloff" pass in `seek()` lays a 10 % warm-white radial over everything, the logo plate
     included.
   - It is consistent with the scene lighting, and nobody will read it as a different logo, but strictly the file is
     shown slightly washed.
   - Fix (optional): draw the niche plate after the light pass, or exclude the niche rectangle from it.
3. **MINOR, sound (process): nobody has listened.**
   - Every measure passes: -14.0 LUFS, -2.4 dBTP, no clipping, hits within 11 ms, no low-mid mud, a phone-speaker
     proxy of -14.6 LUFS.
   - House rule: a human listens on a phone before final delivery. The limiter still takes up to 6.6 dB off a few
     mallet attacks (maker's figure).
   - Advisory, against onetake gate 6, not the house rule: the post-AAC sample peak is -2.4 dBFS (the gate says
     -3 dBFS), and 8-14 % of half-second windows are quiet (the gate says 15 % with no narration; the reference has
     0 %).
4. **COSMETIC, the dark (4.3-6.3 s): at phone size it is still mostly centred type on dark.**
   - The shaft edges and rings are at 13-24 % opacity and barely register at 360 px wide.
   - It is a planned 2.5 s rest with a clear cause (the fall), so it is not the banned look. It is the one stretch a
     viewer could take for a title card.
   - Fix (optional): lift the edges and rings by about 1.5x, or keep the rim of the hole in frame a little longer.
5. **COSMETIC: transitional frames.**
   - At 3.95-4.05 s "No reply." rises inside the hole, cut off by its mask, while the headline exits with its tops
     clipped (about 6 frames).
   - At 6.5-6.7 s the shaft and the wall cross-dissolve rather than the camera physically rising.
   - At 21.06-21.4 and 24.15-24.45 s the doors cut the wordmark into fragments ("raigh", "aig").
   - None of these lasts long enough to read as an error at playback speed. Listed so they are known.
6. **COSMETIC: the loop seam step is slightly larger than its neighbours** (9:16: 1.60 against 1.53 at most; 4:5:
   1.80 against 1.54). It is not visible in the strip, and the audio seam has no click.

## Gate checklist
- M1 spelling: PASS.
- M2 overlaps or clipping: PASS. Nothing ghosts under a caption, and no captions overlap. Mask clipping happens only
  in entrance and exit frames.
- M3 safe zones and contrast: PASS (both tools ok, every pair at least 4.5:1).
- M4 timing against words: N/A (no voice). Text lands on its events: the hook before the first kick, "No reply." on
  the fall, "Build the missing step." on the plate snap, "Every step answered." on the pull-back, and the ask on the
  flight home.
- M5 motion in the first second and hook text by 0.3 s: PASS. The headline is fully in by about 0.17 s, the ball is
  kicked at 0.0 s and hits pegs at 0.5 and 1.0 s.
- M6 brand colours and fonts: PASS (Playfair Display, Montserrat, brand palette). See finding 2.
- M7 generated images: N/A.
- F1 frames every 1.5 s plus every transition are clean: PASS.
- F2 sound-off: PASS. Gap, fall, rebuild, the full lit path, the system and the ask all read without audio.
- F3 captions: PASS (exact, timed, inside the safe zones).
- F4 transcript: N/A.
- F5 loudness: PASS (-14.0 LUFS, -2.4 dBTP).
- F6 hook timing: PASS (hook text on screen at 0.0 s).
- F7 policy: PASS (no before/after split, no "your [condition]", no AI media).
- F8 credits: PASS (0 spend; CC0 samples, OFL fonts, the owner's logo file).
- onetake §8:
  - gate 5: stillness is in line with the reference (quiet 0.0 at its scale) and there is a calm run of at least
    1 s (the 1.5 s dark).
  - gate 6: hits are loudest, there is no mud and the silence is planned. Advisories in finding 3.
  - gate 8: no beat is swapped, nothing freezes, and the lull (the dark) is the story's.
- Deliverables, all present in deliver/v2: one-message-9x16.mp4, one-message-4x5.mp4, poster.jpg (1080x1920, hook
  frame), contact-sheet.jpg, captions.srt, post-caption.txt, CREDITS.md, CHANGELOG.md. Duration and fps are as
  reported. v1 is untouched in deliver/v1.

## Scores (0-10)
| Axis | Score | Why |
|---|---|---|
| Hook in the first 2 s | 8 | headline in at frame 0, the ball in close-up and moving, first station lit at 1.5 s; pixel change half the reference's; the empty hatch dominates frame 0 |
| Readability at phone size | 9 | every caption on a flat band, 58-176 px, every hold passes; the ask passes with only 0.09 s spare |
| Motion quality | 9 | real arcs, squash, plate springs, 16-subframe blur on the fast moves, no stepping in any strip |
| Continuity | 9 | one world, every transition bridged, the hatch has visible causes, seamless picture and audio loop |
| Pacing | 8 | at the reference's scale a big change every 1.59 s (reference 1.54), quiet 9 %, longest quiet 1.5 s; the end is calm but alive; pass 2 retraces pass 1 |
| Composition | 8 | clean band, logo only in the end frame and clear of the band; empty hatch in the hook frame; the dark still reads mostly as centred type at phone size |
| Brand accuracy | 9 | the real file (same MD5, drawImage only), palette and fonts right, never under type; a light 11 % lift from the scene light |
| Sound sync | 8 | hits within 11 ms, stations louder than pegs, -14.0 LUFS / -2.4 dBTP, room tone instead of digital zero; nobody has listened |
| Message with the sound off | 9 | the missing Reply, the fall, the rebuild, the lit system and the ask carry the idea alone |

## Before posting (not defects in the file)
1. Someone plays the 9:16 on a phone speaker and on earbuds and confirms the mix: the silence feels intended, the
   mallets are not harsh, and the loop point is smooth.
2. Post with `deliver/v2/post-caption.txt` so the ANALIZA path is there. Do not upload captions.srt as closed
   captions.
3. Owner approval in the hub. Then the refbank ledger entry (command in PROJECT.md), commit and push.
