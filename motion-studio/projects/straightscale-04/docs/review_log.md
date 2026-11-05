# Review log: StraightScale · Film 04 "One message, all the way"

Every round is logged. Sheets are in `out/review/` (not in git: `out/` is ignored; regenerate with the commands
shown). Scores are my own; nobody has listened to the mix yet (we measure only).

## Round 0 · 2026-10-20 · styleframes and a debug overview (before any render)
Sheets: `out/review/r0_debug_a.png`, `r0_debug_b.png` (path trace), `r0_styleframes_a.png`, `r0_styleframes_b.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 7 | headline and a moving ball at 0.2 s, but the frame was sparse |
| Readability at phone size | 6 | labels 46 px at 1.0x looked small; captions fought the stations passing behind (3.8, 6.9) |
| Motion quality | 7 | arcs and contacts physically consistent (normals from in/out velocities); no squash check yet |
| Continuity | 8 | one wall, camera-only transitions |
| Variety and pacing | 7 | contact every 0.25-0.5 s; dark rest planned |
| Composition | 5 | lots of empty marble; the hole read as a black sign hanging under Reply |
| Brand accuracy | 7 | real logo, brand colours; marble looked like a contour map |
| Sound | n/a | not built yet |
| Message clear with the sound off | 7 | labels carry the path; the system idea not yet visible as one thing |

Automatic checks: page loads without errors; contact solver report (`node tools/report.mjs`): plate tilts -12° to
+3.5° (Referral is the kicker), pegs placed behind each contact.

Three worst problems and the fix for each:
1. Sparse frame, no "system" picture → working zoom 1.18x; an engraved route groove links the stations and lights
   crimson as the ball completes it (the map later shows one connected path).
2. Sub-labels under the plates: "instant answer" sat on the dark hole (red on charcoal, banned) → sub-labels moved
   onto the plate face as a second line that opens when the station lights.
3. Captions over passing stations; marble like a map; Booking's bounce arcing over the hole → caption haze only while
   a caption is on (stronger), new vein-based marble, Booking moved down 55 px and the hole made shorter; the hole got
   inner faces (wall thickness) so it reads as an opening.

## Round 1 · 2026-10-20 · draft 1 (30 fps, 2 subframes, silent) + strips
Sheets: `out/review/r1_strip_dive.png` (3.4-4.4 s), `r1_strip_rebuild.png` (6.2-7.6 s), `r1_strip_booking.png`
(12.6-14.2 s), `r1_4x5.png` (4:5 styleframes)

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | headline readable by 0.4 s, ball launched at 0.0, logo on the wall |
| Readability at phone size | 8 | labels 54 px on screen; rebuild caption still over COMMENT at 7.0-7.2 |
| Motion quality | 7 | the ball vanished into the hole within 0.1 s (3.6): the fall did not read |
| Continuity | 9 | no cuts; every change is the camera on one wall |
| Variety and pacing | 7 | `pacing.py`: still 17 %, quiet 28 %, longest quiet 4.25 s (end card), beat CV 1.08 |
| Composition | 7 | map logo under the captions (18.5); end card calm but static |
| Brand accuracy | 8 | "Gone." (gold) visible over the returning lit wall at 6.35-6.65 = gold on ivory for a moment |
| Sound | 7 | first mix: -13.7 LUFS / -2.2 dBTP; mud warnings at 1.5, 10.5, 24.5 s; dynamic loudnorm would pump |
| Message clear with the sound off | 8 | missing plate, fall, dark, lines all readable |

Automatic checks:
- `tools/seekcheck.mjs --dur 27`: PASS / PASS
- `tools/safezone.mjs`: BOOKING bottom 1556-1637 > 1520 at 13.1-13.3; REVIEW/REFERRAL under 44 px during the pull-back
- `tools/pacing.py out/draft.mp4`: transitions 2 (4.0 dark, 6.58 light), CV 1.08, spread 12.7x
- `tools/audio_qa.py audio/mix.wav`: PASS -13.7 LUFS, PASS -2.2 dBTP, FAIL dropout 5-6 s (the planned silence), WARN mud

Three worst problems and the fix for each:
1. The fall did not read → inside the hole the ball now recedes toward the shaft's vanishing point over 0.55 s
   (scale and darkening), the camera dives to 3.4x, the light goes out from 3.88 to 4.28.
2. Gold/ivory dark captions over the lit wall, caption band over COMMENT, map logo under captions, Booking label under
   the safe line → dark captions leave before the light returns (6.35/6.4, light from 6.5); rebuild framing puts Reply
   at y 1250 so COMMENT sits below the band; map zoom 0.45 centred lower; the camera aims at the ball's position
   0.22 s ahead (the follow lag); label checks only while the station is read at working zoom.
3. Static end card and a muddy, peaky mix → the waiting ball taps on the downbeats (23, 25 s) and each tap sends a
   spark down the groove; light flows along the finished route on the map; pad moved up an octave, cajon and pickup
   bass softer, peg tink and xylophone quieter, an oversampled look-ahead limiter, then a linear two-pass loudnorm.

## Round 2 · 2026-10-20 · draft 2 (30 fps, 2 subframes) with the mix
Sheets: `out/review/r2_contact_2fps.png` (whole film, 2 fps), `r2_phone.png` (360 px wide), `r2_strip_13s.png`
(12 fps around the Reply hit and the first downbeat), `r2_spectrum.png`

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | "Watch where this client gets lost." with the ball already in the air; a guessing game like the reference |
| Readability at phone size | 9 | 360 px phone sheet: every caption and label legible; captions never cross a moving label |
| Motion quality | 8 | squash on contact, plates dip and wobble, camera blur on the whip (7.9-8.6) and pull-back (17.0); the final is 60 fps x 4 subframes |
| Continuity | 9 | one continuous shot; survivors: ball, hole, wall, tube; loop seam invisible (`tools/loopcheck.mjs`) |
| Variety and pacing | 8 | `pacing.py`: still 13 %, quiet 28 %, longest quiet 4.42 s (the ask), CV 1.10, spread 12.7x; a station every 1.0 s in the run |
| Composition | 8 | ball in the centre third; current station between y 700 and 1500; logo inside the loop |
| Brand accuracy | 9 | real logo file, brand colours only, Playfair + Montserrat, no banned pairs |
| Sound | 8 | every contact a note on the grid; planned silence is digital zero; -13.8 LUFS / -2.4 dBTP; no mud |
| Message clear with the sound off | 9 | path, gap, fall, rebuild, lit system, ask |

Automatic checks:
- `node ../../tools/seekcheck.mjs --dur 27 --n 24`: PASS (same frame on revisit) / PASS (no seek errors every 0.1 s)
- `node ../../tools/safezone.mjs $PWD --dur 27 --step 0.05`: safe zones: ok (9:16)
- `node tools/safezone45.mjs $PWD --page "index.html?fmt=45" --dur 27 --step 0.05`: safe zones: ok (4:5, 64 px margins)
- `node tools/readcheck.mjs`: all 7 cues PASS (hold >= letters/15 + 1.5 s)
- `node tools/loopcheck.mjs` (both formats): PASS, seam step 1.57 vs neighbours 1.87 (9:16), 1.94 vs 2.27 (4:5)
- `python3 ../../tools/pacing.py out/draft2.mp4`: see above
- Against the reference card (same tool and step, `refbank/tools/frames_metrics.py` on frames every 1.5 s):

  | Metric | ig-satisfy3dverse | Ours | Read |
  |---|---|---|---|
  | mean s between big changes | 1.54 | 1.93 | slower overall because of the dark rest and the ask hold; the run (9-17 s) changes every 0.5-1.0 s |
  | change rhythm CV | 0.15 | 0.62 | ours has a contour (run, silence, run, map, ask); the reference is flat-high |
  | quiet share | 0.0 | 0.118 | one planned rest and one reading hold |
  | hook change 0-2 s | 0.425 | 0.196 | our camera moves less in the first 2 s (the headline needs a stable frame) |
  | cuts per 10 s (colour-gated) | 0.16 | 1.11 | not edits: the fade to the dark and back registers as colour jumps |
- `python3 ../../tools/audio_qa.py audio/mix.wav`: PASS -13.8 LUFS, PASS -2.4 dBTP, PASS no mud; FAIL dropout 5-6 s =
  the planned silence (intended, see treatment §5)

Three worst problems and the fix for each:
1. The ask is a 5 s reading hold, the calmest part of a beat-sync film (quiet run 4.4 s, under the 5 s limit) → kept
   (the reading rule needs 4.97 s for 52 letters); taps and sparks on the downbeats keep it alive. Logged as a known
   trade-off.
2. Hook change 0.196 vs the reference's 0.425 → not changed: a faster camera in the first 2 s would make the headline
   harder to read; the ball is in flight from frame 0.
3. Limiter catches mallet attacks (max 6.7 dB on about 0.1 % of samples, mostly the Reply hit and peg attacks) → peg
   and Reply layers softened; residual limiting is transient-only. Needs a human listen.

## Round 3 · 2026-10-20 · final (60 fps, 4 subframes), both formats
Filled in after the final render: see the section below.

### Round 3 results (final render, delivered v1)
Sheets: `deliver/v1/contact-sheet.jpg` (one frame per beat), `out/review/r3_final_frames.png`,
`out/review/r3_fast_moves.png` (before the fix), `out/review/r3_fast_moves_patched.png` (after),
`out/review/r2_4x5_beats.png` (4:5 at the same beats), `out/review/r3_spectrum_final.png`

Found on the final: the two fast zooms (pull-back to the map 17.0-17.9, zoom home 20.3-21.0) showed stepped copies of
the labels with 4 subframes. Fixed by re-rendering 16.9-18.0 and 20.2-21.2 at 16 subframes and splicing them in
frame-exactly (`tools/patch_fast.sh`, one re-encode at CRF 16); a static test frame showed no brightness bias between
4 and 16 subframes (mean difference -0.001 levels).

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | headline in by 0.4 s over the logo and a ball already in flight (poster frame 0.6) |
| Readability at phone size | 9 | every caption 64-176 px, labels 54 px on screen; reading-time check passes for all cues |
| Motion quality | 9 | 60 fps, 4 subframes, 16 on the two fast zooms; squash, dips, wobbles, landing jolts |
| Continuity | 9 | one continuous shot, no cuts; loop seam invisible |
| Variety and pacing | 8 | still 12 %, quiet 28 %, longest quiet 4.42 s (the ask), CV 1.22, spread 12.8x |
| Composition | 8 | centre-third ball, current station inside the safe zone, logo inside the cycle |
| Brand accuracy | 9 | real logo file, brand palette and type, banned pairs absent |
| Sound | 8 | every contact a note on the grid, planned silence, -13.8 LUFS / -2.3 dBTP after AAC; not yet heard by a person |
| Message clear with the sound off | 9 | the gap, the fall, the rebuild, the lit system, the ask |

Automatic checks on the delivered files:
- ffprobe: 9:16 1080x1920 and 4:5 1080x1350, both 60/1 fps, 1620 frames, 27.000 s, H.264 + AAC 48 kHz stereo;
  9:16 21.2 MB (no viewing copy needed, under 30 MB), 4:5 16.4 MB
- segment seams (`tools/seams.py`) at 9.0, 16.9, 18.0, 20.2, 21.2 s: all PASS in both formats (largest ratio at 20.2,
  0.28 vs 0.07 grey levels on a near-static frame: the flow pulses' blur changes; not visible)
- loop seam on the delivered master: 1.84 vs neighbours 1.82-1.86 (PASS); page loopcheck PASS in both formats
- `audio_qa.py deliver/v1/one-message-9x16.mp4`: PASS -13.8 LUFS, PASS -2.3 dBTP, PASS no mud; dropout 5-6 s is the
  planned silence; LRA 10.1 LU (ebur128)
- `pacing.py` on the master, and the reference-scale metrics (`frames_metrics.py`, step 1.5 s): mean between big
  changes 1.93 s (ref 1.54), CV 0.62 (ref 0.15), quiet share 0.118 (ref 0.0), hook change 0.194 (ref 0.425)
- `seekcheck` PASS/PASS, `safezone` ok (9:16) and ok (4:5), `readcheck` 7/7 PASS (unchanged since round 2)

Shipped with these known issues (told to the owner):
1. Nobody has listened yet; the mix is measured only. Transient limiting up to 6.7 dB on mallet attacks.
2. The ask is a 5 s reading hold, the calmest stretch of a beat-sync film (quiet run 4.4 s).
3. Hook change in the first 2 s is about half the reference's (the headline needs a steadier frame).

---

# v2 revision (after the independent review r1 FAILED v1)
The independent review (`docs/review_independent_r1.md`) failed v1 on one major finding (the hook headline, and the
rebuild caption, drawn over a washed-out logo and plate) and scored hook 7, pacing 7, composition 7, brand 7. Every
finding was fixed in the source (`index.html`, `audio/score.py`, `audio/mix.py`, `finish.sh`); see treatment §6.
New automatic checks written for this revision: `tools/ghostcheck.mjs` (renders each caption frame again without the
type and without grain and measures how far the pixels under every glyph row stray from the band's flat colour; also
checks that the logo never enters the band or its fade), `tools/hookchange.mjs` (the reference metric
`hook_change_0_2s` straight from the page), `audio/measure.py` (hit levels by kind, band shares, the silence floor,
loudness through a 150 Hz high-pass), `tools/strip.sh` (time-stamped strips from a render).

## Round 4 · 2026-10-20 · v2 page stills and 30 fps drafts (both formats)
Sheets (in `out/review/`): `r4_first_stills_a.png`, `r4_first_stills_b.png`, `r4_first_stills_end.png` (first v2
pass, 9:16), `r4_45_beats.png` (4:5), `r4_veins.png` (marble), `r4_hook.png` (0-2 s), strips from the 4:5 draft at
the windows the review named: `r4_45_hook.png` (0.6-3.2 s, 5 fps), `r4_45_rebuild.png` (6.8-7.2, 10 fps),
`r4_45_whip.png` (7.8-8.4, 10 fps), `r4_45_replay.png` (9.6-11.2, 5 fps); `r4_keyframes.png`, `r4_dark.png`,
`r4_spectrum.png`.

Found and fixed inside this round:
1. First v2 stills: a ghost of the COMMENT plate under "Build the" at 6.9 s. Cause: the band's opacity was multiplied by
   the light level, so while the light came back the wall showed through at up to 25 %. Fix: the band's opacity follows
   the captions only and its colour follows the light (charcoal to ivory); the rebuild lines now rise at 6.95/7.07 s
   when the light is at 99 %, and every band window opens 0.4 s before its first line and closes after its last line
   has gone (v1 faded the band while type was still leaving).
2. `safezone.mjs` 9:16: "instant answer" right edge 950 > 940 at 12.2-12.3 s (pass 2's swinging camera lagged left).
   Fix: pass 2 leans 60 px toward Reply from 11.6 s. Re-run: ok.
3. The rebuild framing parked the COMMENT plate inside the band's fade (9:16 y 648, fade to 659; 4:5 likewise). Fix:
   Reply framed at y 1300 (4:5: 1085), COMMENT settles at y 698 (4:5: 478), under the fade; sub-label still inside the
   bottom safe line (safezone ok).
4. The marble rewrite first came out as a regular wave grid; second pass: stretched contour lines with width variation
   and a third family of hairlines; veins a touch deeper (`r4_veins.png`).
5. The dark's shaft was too faint at phone size; edges and rings raised (`r4_dark.png`).

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | close shot of the ball on the flipper with the headline at frame 0, no logo, motion from frame 0 (the end's push-in still settling, the flipper); the reference metric is unchanged at 0.21-0.22 (pale wall, opaque band) |
| Readability at phone size | 9 | captions on a flat band: nothing behind any glyph (ghostcheck 0 levels); labels 54 px (pass 2: 65 px) |
| Motion quality | 8 | draft at 30 fps x 2 subframes shows double images in the whip and the plate slide; the final is 60 x 4 with 16 subframes on the two fast zooms |
| Continuity | 9 | one shot; the hatch is caused by the landing and by the flipper arming; loop seam 1.19 vs neighbours 1.54 (9:16), 1.34 vs 1.78 (4:5) |
| Variety and pacing | 9 | `pacing.py` (both drafts): still 6 %, quiet 9 %, longest quiet run 1.67 s (the planned dark), CV 1.24 (4:5 0.78); v1: quiet 28 %, longest 4.42 s |
| Composition | 8 | the logo shows only in the end frame, 28 px under the fade (4:5: 11 px); COMMENT clear of the band in the rebuild; the dark reads as the inside of the hole |
| Brand accuracy | 9 | real logo file, shown clean on an ivory plate, masked only by the doors as they open and close (21.06-21.4, 24.15-24.45) |
| Sound | 8 | stations +4.3 dB over pegs at the onset peak (+9.9 dB in the 150 ms band above 400 Hz); presence 2.5-6 kHz 5.0 % (v1 2.6 %); room tone -52.5 dBFS, 0 % digital zero; -14.0 LUFS, -2.6 dBTP; nobody has listened |
| Message clear with the sound off | 9 | unchanged: the gap, the fall, the rebuild, the lit system, the ask; the brand appears when the client is home |

Automatic checks:
- `node tools/ghostcheck.mjs` (step 0.05 s): 9:16 PASS, 306 caption frames, worst deviation 0 levels, logo 28 px under
  the fade at its closest; 4:5 PASS, 306 frames, 0 levels, 11 px. (First run: one frame at 4.15 s with 5 levels while
  the hook line left over the dimming band; the hook window now closes at 4.5 s: PASS.)
- `node ../../tools/seekcheck.mjs --dur 25 --n 24`: PASS / PASS
- `node ../../tools/safezone.mjs $PWD --dur 25 --step 0.05`: ok (after fix 2); `tools/safezone45.mjs`: ok
- `node tools/loopcheck.mjs` both formats: PASS
- `node tools/readcheck.mjs`: 7/7 PASS on the house rule; the ask holds 3.59 s for 3.5 s needed (Lemo advice 4.97 s:
  short by design, review finding 2)
- `python3 ../../tools/pacing.py out/v2/draft.mp4 out/v2/draft45.mp4`: as above, all PASS
- reference scale (`frames_metrics.py` on the 9:16 draft): step 1.5 s: mean between big changes 1.5 s (ref 1.54), quiet
  0.0 (ref 0.0), hook change 0.212 (ref 0.425), CV 0.0 (ref 0.15: every 1.5 s sample is a big change); step 0.5 s:
  quiet 0.041, longest quiet 1.0 s, mean between big changes 0.6 s
- `python3 ../../tools/audio_qa.py audio/mix.wav`: PASS -14.0 LUFS, PASS -2.6 dBTP, PASS no mud; FAIL dropout 5-6 s =
  the planned silence (now room tone at -52.5 dBFS, not digital zero; audio_qa flags any 1 s window 20 dB under the
  median, which a rest that still feels silent always is)
- `audio/measure.py`: station over peg +4.3 dB (onset peak) / +9.9 dB (150 ms RMS above 400 Hz); bands 60-120 Hz 22 %,
  300-2500 Hz 67 %, 2.5-6 kHz 5.0 %; through a 150 Hz high-pass -14.0 LUFS (v1 -15.0); limiter: 0.85 % of samples
  reduced by more than 3 dB, 0.04 % by more than 6 dB (max 6.6 dB, mallet attacks)

Three worst remaining problems:
1. Hook change at the reference's scale is still about half (0.21 vs 0.425). Not changed further: more pixel change
   would mean a busier wall or a band that moves; the hook has motion from frame 0 and a close subject.
2. The limiter still takes up to 6.6 dB off a few mallet attacks (0.04 % of samples), inherent to a mallet score at
   -14 LUFS; needs a human listen on a phone.
3. Draft-rate stepping in the whip and the plate slide: check on the 60 fps final (round 5).

## Round 5 · 2026-10-20 · v2 final (60 fps, 4 subframes; 16 on the fast moves), both formats, delivered `deliver/v2/`
Sheets (in `out/review/`): `r5_contact_sheet.jpg` (= `deliver/v2/contact-sheet.jpg`, one frame per beat), strips from
the delivered files at the review's windows: `r5_916_hook.png` / `r5_45_hook.png` (0.6-3.2 s), `r5_916_rebuild.png` /
`r5_45_rebuild.png` (6.8-7.2), `r5_916_whip.png` / `r5_45_whip.png` (7.8-8.4), `r5_916_replay.png` / `r5_45_replay.png`
(9.6-11.2), and the new end `r5_916_end.png` / `r5_45_end.png` (19.8-25.0); `r5_rebuild_fix.png`, `r5_reset_fix.png`,
`r5_2450.png`.

Found on the first final render and fixed before delivery (re-rendered windows spliced in one encode from the 4-subframe
master, `tools/splice.py`, so no generation loss):
1. The rise out of the hole still carried the COMMENT plate up through the band's fade at 6.9-7.1 s, just under the
   rebuild caption (not under the glyphs, but it read like the v1 ghost). Fix: the camera starts rising in the dark at
   6.05 s, so the wall has settled under the band before the light and the caption return (`r5_916_rebuild.png`).
2. The whip (7.9-8.4 s) showed stepped label copies at 4 subframes now that it lands on a closer frame. Fix: 5.95-8.6 s
   rendered at 16 subframes (`r5_916_whip.png`: clean blur).
3. On the reset (24.15 s) the lit plates' crimson shrank back into a red half-disc behind the label, with charcoal type
   on red for a few frames (`r5_2450.png`). Fix: the light fades evenly and the label cross-fades from ivory to charcoal
   (`r5_reset_fix.png`).
4. The contact sheet's last cell caught the doors half closed (a cropped logo between the leaves); the beat is now
   sampled at 24.5 s with the hatch shut.
Windows spliced: 4.05-5.95 (4 subframes, the dark's drift curve changed), 5.95-8.6 (16), 16.9-18.0 (16), 19.95-21.05
(16), 24.1-24.75 (4). Seams (`tools/seams.py`) at every join, both formats: all PASS (largest 0.36 vs 0.09 grey levels
at 5.95 s on a near-black frame: 16 vs 4 subframes measured -0.03 levels mean, no bias).

| Axis | Score /10 | Evidence (timestamps) |
|---|---|---|
| Hook in the first 2 s | 8 | frame 0: headline, closed hatch, the ball on the flipper in close-up, the camera still moving from the end's push; no logo and no ghost (`r5_916_hook.png`); reference metric 0.222 (4:5 0.232) vs 0.425 |
| Readability at phone size | 9 | every caption on a flat band (0 levels under the type, both formats); captions 64-176 px, labels 54 px (pass 2: 65 px); reading gate 7/7 |
| Motion quality | 9 | 60 fps; 16 subframes on the rise, whip, pull-back and flight home; squash, dips, wobbles, doors on springs |
| Continuity | 9 | one shot; the hatch has visible causes (landing, flipper arming); loop seam on the delivered master 1.60 vs neighbours 1.17-1.53 (4:5: 1.80 vs 1.18-1.53) |
| Variety and pacing | 9 | `pacing.py` master: still 0 %, quiet 9 %, longest quiet run 1.5 s, CV 0.90, spread 10.6x (4:5: quiet 7 %, longest 1.17 s); v1: quiet 28 %, longest 4.42 s |
| Composition | 9 | logo only in the end frame, 28 px clear of the band's fade (4:5: 11 px); COMMENT settles under the band in the rebuild; the dark reads as the inside of the shaft |
| Brand accuracy | 9 | real logo file on an ivory plate, never under type; masked only by the doors while they move (21.06-21.4, 24.15-24.45) |
| Sound | 8 | measured on the delivered master: -14.0 LUFS, -2.4 dBTP, LRA 11.4 LU; stations +4.2 dB over pegs (onset peak), +9.9 dB (150 ms above 400 Hz); presence 5.0 %; silence -53.0 dBFS room tone, 0 % digital zero; hit sync median +4 ms, worst 14 ms (23 hits); nobody has listened |
| Message clear with the sound off | 9 | the gap, the fall, the rebuild, the lit system, the ask; the brand appears when the client is home |

Automatic checks on the final source and the delivered files:
- ffprobe: 9:16 1080x1920 and 4:5 1080x1350, both 60/1 fps, 1500 frames, 25.000 s, H.264 + AAC 48 kHz stereo; 9:16
  21.6 MB (no viewing copy needed), 4:5 16.8 MB
- `tools/ghostcheck.mjs` full range, step 0.05 s: 9:16 PASS (306 caption frames, 0 levels; logo 28 px clear), 4:5 PASS
  (306 frames, 0 levels; 11 px)
- `safezone.mjs` 9:16 ok, `safezone45.mjs` ok; `seekcheck` PASS/PASS; `loopcheck` PASS both formats; `readcheck` 7/7
- `pacing.py` (above); reference scale (`frames_metrics.py` on the master): step 1.5 s: big change every 1.5 s (ref 1.54),
  quiet 0.0 (ref 0.0), hook 0.222 (ref 0.425), CV 0.0 (ref 0.15); step 0.5 s: quiet 0.02, longest quiet 0.5 s
- `audio_qa.py` on both files: PASS -14.0 LUFS, PASS -2.4 dBTP, PASS no mud; FAIL dropout 5-6 s = the planned rest, now
  room tone at -53 dBFS (the tool flags any second 20 dB under the median)
- events unchanged between the score's `audio/events.json` and the final page (re-exported and diffed)

Shipped with these known issues (told to the owner):
1. Nobody has listened yet; the mix is measured only. The limiter takes up to 6.6 dB off a few mallet attacks (0.04 % of
   samples over 6 dB, 0.85 % over 3 dB).
2. Hook pixel change at the reference's scale is about half the reference's (0.22 vs 0.425): a pale wall under an opaque
   caption band changes fewer pixels than the reference's dense set; the hook has a close subject and motion from frame 0.
3. The ask meets the house reading rule (3.59 s for 3.5 s) but not the stricter Lemo-Opuscar advice (4.97 s); it loops.
4. The logo is seen partly covered for about 0.3 s while the doors open and close (a mask, by design).
