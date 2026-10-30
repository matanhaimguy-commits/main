# Kit test: review log (producer self-check; G-MOTION-FRAMES is the fresh reviewer's)

Renders: `deliver/kit-test-v5.mp4` (current: the two v4-review code fixes), `deliver/kit-test-v4.mp4` (round 4), `deliver/kit-test-v3.mp4` (round 3), `deliver/kit-test-v2.mp4` (round 2), `deliver/kit-test-v1.mp4` (round 1), viewing copies at CRF 24. The
CRF 16 master is rebuilt by `python3 twinkit.py compose examples/test-clip/edl.json --out examples/test-clip/out`.

## Inputs (all $0 today)
- Twin: Atlas H3 take `T-H3-1440` from `clients/straightscale-en/runs/SSEN-LIB-ATLAS-TESTS` (paid 28 Oct, an AI test
  character, not Matan), cut out here. Lip sync holds to about 4.2 s, then the take mouths its own words (that run's
  F2 result): fine for an edit test, not for a post.
- Voice: SLICE-CHRIS (same run, 8.2 s), starting at 0.0 so the twin is on frame 0. Bed: T-BED-A, 14 s from 20 s in.
- Word timings: `kit/align.py` estimate (no STT word times exist). UI copy is example copy and says so.

## Round 1 (main session, 30 Oct: CODE PASS with 3 FIX, G-MOTION-FRAMES FAIL on v1: M2, M3, M5) and what changed in v2
| Finding | Fix |
|---|---|
| EDLError printed a traceback | `twinkit.py` prints one line (`twinkit: EDLError: ...`) |
| Safe zones used the house numbers | `kit/zones.py`: STANDARDS 6 (top 269, bottom 672, sides 65, right 227 in the lower half), face band 15-55%, captions 80-100 px, 44 px floor |
| Safe zone skipped behind-twin words | every text layer is checked: heroes on any layer, UI scenes, captions |
| b1 "2 YEARS" hidden by the head, in the top 269 px, hook not on frame 0 | stage twin with the word above and behind the crown (y 434-686), on screen from frame 0, voice and twin from 0.0 |
| b4/b5 hard clip edges at x 270 and 810; face too low | per-mode soft mask (16% sides, 24% bottom) fades the clip into the set; stage face at 724-1050 px (38-55%) |
| b4 orbit words in the side, right and bottom zones | orbit is now a halo at forehead height (cy = head top + 11% of the head): the far side passes behind the crown, the near side stays above the brows, all inside 560-750 px |
| b5 mask clips the "A" | masks padded 0.12 em each side and 0.14 em below |
| Captions too small, UI text under 44 px | captions 88 px at 1130 px (59% down) inside 65-853 px; notification labels 44 px |
| Contrast: gold on ivory, fading orbit word | chat is dark (charcoal, ivory bubbles); orbit words full opacity (depth by scale only) |
| Duplicate wording | star has no label; orbit says NOT US / NO SCRIPT / NO AGENCY (not the caption's words) |
| Ghost on the star at 8.0 s | no sway after landing; landing 0.36 s; shutter 180 degrees |
| "BOOKS A CALL" held over silence | a card leaves 0.35 s after its last word, and before a hidden range (the end card's flash) |
| Italic N in "PLAN" | key words upright (end card and two-tone) |

## Round 2 (G-MOTION-FRAMES FAIL on v2: M2, M3) and what changed in v3
| Finding | Fix |
|---|---|
| "2 YEARS" cut about 40 px by the hair | the head may cover only space behind or between words: new rule (`kit/text_rules.py`, letters 20 px clear of the head top, with an upper-bound font estimate); word at y 460, 260 px, letters end about 545 px, head top 612 px |
| Orbit words collide; NOT US on the forehead | every word has its own lane (lane 0 at the crown, the next lanes 104 px higher: two radii plus the word height), so no two words can touch; a near word is not drawn while it would touch the head box (not only the face box) |
| Text under 44 px at its smallest scale | orbit depth scale floored at 0.8 (60 px words never under 48 px); UI text 50 px or more (app labels 52, titles 56, bodies 50, chat 50); test-card line removed; rules check the scaled size |
| Pop-in overshoot past the 65 px margin | behind-word fits to 890 px so its 1.06 slam stays 943 px wide; rules size every box at its move's biggest scale |
| No overlap rule | `text_rules.overlap_findings`: hero (each orbit lane), UI scene and captions never overlap in a beat unless an item sets `overlap_ok` |

## Round 3 (G-MOTION-FRAMES FAIL on v3, four points; main session: simplify, no more look tuning) and what changed in v4
| Finding | Fix |
|---|---|
| Two-line caption "SOMEONE BOOKS" 19 px into the bottom zone | one line per card: the template splits any card wider than the band, max 11 characters; `kit/caption_rules.py` groups cards the same way and fails one that would wrap |
| pop3d star broken at 7.4-7.6 s | pop3d disabled (kept on file, refused by the EDL); b6 is a two-tone "in a / REVIEW" with captions off |
| Seam and cut caption in the whip at 1.8 s | the whip now pushes in (scale 1.25) while it slides 110 px, so no frame edge shows; captions are hidden over each whip and a card that starts inside one waits for its end |
| Chin 13 px past the 55% band | chin estimate lowered (114% of head height), stage twin up 80 px: chin at 993 px (51.7%); the face-band rule checks the chin at 52% |
| Hook text 4 to 10 words | b1 is a two-tone hook "Two years of / POSTING" at double entrance speed (fully up by 0.3 s); "OWNER" became the behind-the-head word in b5; the rule checks the frame-1 hook |

Determinism findings while making v4 (tools/seekcheck.mjs --hf), all fixed in the kit:
- the whip wrote `filter: blur(0px)` onto the frame, so frames before and after the first whip rasterized text
  differently: `#frame` now starts with the same filter and transform;
- exit tweens wrote the same transform the entrance owned: exits now move the parent (two-tone block, behind-word
  line), every template uses `fromTo` only (a test enforces it), and those parents are layers from frame 0;
- what remains is Chrome re-rastering one glyph's antialiased edge after a layer is rebuilt (one "S", about 400 px,
  0.02% of the frame, nothing moved). seekcheck `--hf` now passes a frame whose changed pixels stay under `--tol`
  (default 0.1% of the frame) and lists it as glyph jitter; `--tol 0` is the exact check.

## Automatic checks on v3 (STANDARDS 9, G-MOTION-FRAMES list)
| Check | Result |
|---|---|
| `twinkit.py check` (edit rules incl. STANDARDS 6) | PASS, no findings. Twin on screen 39.6%, 7 beats, 5 heroes, 11 sound cues |
| `tools/seekcheck.mjs --hf` (10 samples, each re-seeked after a different time) | PASS |
| `tools/safezone.mjs --hf --top 269 --bottom 672 --right 227 --left 65` | PASS (see note) |
| HyperFrames `check --caption-zone "x0=0.06;y0=0.55;x1=0.79;y1=0.62;severity=error" --at-transitions` | ok: lint, runtime, layout, motion, contrast all 0 errors; 4 layout warnings, all intended: the set's oversize wall and light, the grain canvas at the frame edge, and text leaving the canvas only while the whip slides the whole frame (1.74 to 1.86 s) |
| `tools/pacing.py` | PASS all: 13% still, longest quiet run 1.5 s, no frozen stretch, beat CV 0.44, spread 5.0x |
| `tools/audio_qa.py` (with stems) | PASS all: -13.9 LUFS, true peak -1.9 dBTP, no dropouts, no mud, music 13.2 dB under the voice |
| Unit tests | 93 pass |

Note on safezone `--hf`: HyperFrames' zone check skips text it counts as occluded, so behind-twin words are not seen
by it; `kit/rules.py` checks those from the EDL instead. A positive control (band = top 40%) caught the end card's
"Comment", so the band mechanism works. The 44 px floor is checked from the EDL, not from the page.

## Still open
- G-MOTION-FRAMES from a fresh reviewer.
- A human listen (measured only).
- Real word times for the pilot.
- Minor, logged: the set's ledge reads as a horizontal line behind the stage twin; the orbit's back words can overlap
  each other for a few frames as they pass behind the crown.
