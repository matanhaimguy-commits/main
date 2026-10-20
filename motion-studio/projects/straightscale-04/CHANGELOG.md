# Changelog: StraightScale · Film 04 "One message, all the way"

## v2 · 2026-10-20
Revision after the independent review r1 failed v1 (`docs/review_independent_r1.md`). v1 is kept untouched in
`deliver/v1/`.
- **Major, fixed: no logo or plate ghost under any caption.** The caption band is now fully opaque behind the glyph rows
  and fades only below the type; its colour follows the light so it stays opaque through the dive and the rebuild; each
  band window opens before its caption and closes after the last line has left. The real logo now sits behind a marble
  hatch above the cradle: the doors open when the ball lands home (21.06 s) and close as the flipper arms (24.15 s), so
  the logo is only ever seen clean in the end frame, below the band (28 px clear in 9:16, 11 px in 4:5), and the hook
  frame carries no logo. The rise out of the hole starts in the dark and the rebuild framing moved down, so COMMENT
  settles under the band before the rebuild caption arrives. New check
  `tools/ghostcheck.mjs`: 0 levels of deviation under every caption frame, both formats.
- **The end is alive (pacing).** Loop 27.0 s -> 25.0 s. The ask rises during the flight home and holds 3.6 s once fully
  in (12 words need 3.5 s); the lit path stays lit through the ask and each tap of the waiting ball sends a light pulse
  down it; the hatch opens and closes; the camera pushes from the logo frame into the hook's close-up; the flipper arms
  before it fires. The map drifts up with the ball. Longest quiet run 4.42 s -> 1.5 s (the planned dark only); quiet
  share 28 % -> 9 % (pacing.py on the delivered master).
- **Hook:** frame 0 is a close shot of the ball on the flipper (zoom 1.32), with the end's push-in still moving.
- **Pass 2 is new footage:** closer (zoom 1.42), a swinging follow that leans toward Reply.
- **The dark is inside the hole:** perspective edges, drifting rings of the shaft wall, a warm falloff, the ball's last
  glint, the camera still sinking.
- **Sound:** room tone at about -50 dBFS under the planned silence (no digital zero); station notes +2 dB and pegs -1 dB
  (stations now 4.3 dB over pegs at the onset); +3.5 dB presence at 3.8 kHz (2.5-6 kHz 2.6 % -> 5.0 % of the energy;
  through a 150 Hz high-pass -15.0 -> -14.0 LUFS); hatch, flight-home and flipper-arming foley; the score re-cut for 25 s
  (F, C after the landing, back into the opening D minor). Loudness trimmed so ebur128 reads -14.0 LUFS.
- **Marble:** veins redrawn as long, nearly straight runs (no curls).
- **Plates:** on the reset the light fades evenly and the label cross-fades (v1 shrank the crimson back to a red disc).
- **Render:** 60 fps, 4 subframes; 16 subframes on the rise and whip (5.95-8.6 s), the pull-back (16.9-18.0 s) and the
  flight home (19.95-21.05 s), spliced in one encode from the 4-subframe master.
- **Measured on the delivered master:** 25.000 s, 1500 frames at 60 fps, -14.0 LUFS, -2.4 dBTP after AAC, LRA 11.4 LU;
  9:16 21.6 MB (no viewing copy needed), 4:5 16.8 MB; loop seam 1.60 vs neighbours 1.17-1.53.
- **Delivery notes:** `post-caption.txt` carries the brand kit's path ("comment ANALIZA") for the post caption.
  `captions.srt` repeats the burned-in lines: keep it as a reference, do not upload it as closed captions.
- Still not done: nobody has listened (measured only); the hook's pixel change at the reference's scale is still about
  half the reference's (0.21 vs 0.425).

## v1 · 2026-10-20
First delivery (autopilot, batch film 1 of 3).
- `one-message-9x16.mp4`: master, 1080x1920, 60 fps, 27.0 s seamless loop, H.264 CRF 16 + AAC 320k.
- `one-message-4x5.mp4`: native 4:5 re-layout, 1080x1350, 60 fps (own camera anchor, caption band, rebuild framing
  and map zoom; same world and timeline).
- No separate viewing copy: the master is 21.2 MB (under the 30 MB chat limit); the 4:5 is 16.4 MB.
- `poster.jpg` (hook frame), `contact-sheet.jpg` (one frame per beat), `captions.srt` (the on-screen lines),
  `CREDITS.md`.
- No voiceover (as briefed). Music and effects built from the film's own impact times; no paid generation.
- Known: nobody has listened yet (measured only); the ask is a 5 s reading hold, the calmest part of the film.
- Measured on the delivered master: 27.000 s, 1620 frames at 60 fps, -13.8 LUFS integrated, -2.3 dBTP true peak
  after AAC, LRA 10.1 LU; loop seam step 1.84 vs neighbours 1.82-1.86 (invisible).
