# Kit test v1: review log (producer self-check; G-MOTION-FRAMES still needs a fresh reviewer)

Render: `deliver/kit-test-v1.mp4` (viewing copy, CRF 24; the CRF 16 master is rebuilt by `python3 twinkit.py
compose examples/test-clip/edl.json --out examples/test-clip/out`). Contact sheet: `deliver/kit-test-v1-sheet.jpg`.

## Inputs (all $0 today)
- Twin: Atlas H3 take `T-H3-1440` from `clients/straightscale-en/runs/SSEN-LIB-ATLAS-TESTS` (paid 28 Oct, an AI test
  character, not Matan), cut out here. Lip sync holds to about 4.2 s, then the take mouths its own words (known
  from that run's F2 result); fine for an edit test, not for a post.
- Voice: SLICE-CHRIS from the same run (ElevenLabs v3 on Atlas, 8.2 s). Bed: T-BED-A, 14 s from 20 s in.
- Word timings: `kit/align.py` estimate (no STT word times exist).
- UI copy is example copy and says so on screen.

## Automatic checks
| Check | Result |
|---|---|
| `twinkit.py check` (edit rules) | PASS, no findings. Twin on screen 39.6%, 7 beats, 5 heroes, 11 sound cues |
| `tools/seekcheck.mjs --hf` (10 samples, each re-seeked after a different time) | PASS |
| `tools/pacing.py` | PASS all: 13% still, longest quiet run 1.17 s, no frozen stretch, beat CV 0.44, spread 5.5x, 7 transitions |
| `tools/audio_qa.py` (with stems) | PASS all: -14.0 LUFS, true peak -2.0 dBTP, no dropouts, music 14.3 dB under the voice |
| HyperFrames `lint` | 0 errors, 0 warnings |
| Unit tests | 70 pass |

## Frame scores (1-10, phone size)
| Axis | Score | Note |
|---|---|---|
| Hook in 2 s | 7 | "2 YEARS" behind the head reads as "2 Y..RS" while the head covers it; a shorter word or a higher line reads faster |
| Readability | 8 | captions and heroes large, stroked; captions sit between the full-shot chin and the stage-shot hair |
| Motion | 8 | orbit, whip, star pop with blur, grade snap all land; the set ledge edge shows as a line behind the stage twin |
| Continuity | 7 | test copy, not a story; UI beats sit on flat backgrounds |
| Pacing | 9 | a change every 0.3 to 1.9 s |
| Composition | 7 | the chat beat leaves the lower half empty (house rule); place UI lower in real films |
| Brand | 8 | real wordmark, Playfair and Montserrat, charcoal, ivory, gold |
| Sound sync | 8 | every move has its cue from the EDL times; nobody has listened yet |
| Message, sound off | 7 | captions carry it |

## Open
- G-MOTION-FRAMES from a fresh reviewer (the plan asks for it; the producer cannot pass its own gate).
- A human listen (we cannot hear; only measured).
- Real word times for the pilot (see README "Word timings").
