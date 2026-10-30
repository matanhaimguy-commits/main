# Changelog: StraightScale 06 "The 108-hour week"

## v1 · 2026-10-20
First delivery. English, no voiceover, 24.0 s, 60 fps.
- `straightscale-06-108-hour-week-9x16.mp4`: master, 1080x1920, H.264 + AAC 320k, 5.0 MB (under 30 MB, so it is
  also the viewing copy).
- `straightscale-06-108-hour-week-4x5.mp4`: native 4:5 re-layout, 1080x1350 (own layout table, not a crop), 4.3 MB.
- `poster.jpg` (10.6 s: the finished chart at 108 h), `contact-sheet.jpg` (one frame per beat, 9:16),
  `contact-sheet-4x5.jpg`, `captions.srt` (the on-screen lines with their times), `CREDITS.md`.
- Measured: -14.0 LUFS integrated, true peak -3.1 dBTP after AAC, 1440 frames at 60 fps, 24.000 s.
- Checked: HyperFrames check (lint, runtime, layout, caption band bottom 20 %, contrast 111/111) on both formats;
  reading time and safe zones every 0.05 s (`tools/textcheck.mjs`); determinism (`tools/seekcheck_hf.mjs`);
  `tools/pacing.py`; `tools/audio_qa.py` + spectrogram; momentary loudness at every landing.
- Not checked: nobody has listened to the mix yet (a person should, on a phone, before posting); no native-speaker
  pass needed (English).
