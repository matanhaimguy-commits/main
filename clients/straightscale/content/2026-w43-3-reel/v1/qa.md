# 2026-w43-3-reel · QA

- [x] 1080x1920, H.264 yuv420p, 60 fps, 1440 frames, 24.0 s, AAC 320k, 14 MB (under 100 MB, 3-90 s).
- [x] Loudness -14.0 LUFS, true peak -1.5 dB after AAC (audio_qa PASS; low-mid warnings only on the deliberate low hits).
- [x] seekcheck PASS (same frame on revisit, no seek errors); safe zones ok for all text; segment seams at 8 s and 16 s clean.
- [x] Pacing: beat rhythm CV 0.65, spread 12.5x; a planned rest after the crash (1.9-2.75 s) and a flat "silence" beat.
- [x] Reads with the sound off: spike vs staircase, the dashed MAJA VIRALE line, the steps labelled by month.
- [x] Facts: no numbers or claims; "45 minuta", "falas", office or at the business, "pa detyrim" from the hub profile.
- [x] One ask (comment ANALIZA), funnel `analiza` live (link mode).
- [ ] Native Albanian read (on-screen text and caption).
- [ ] A person listens to the mix on a phone.
- Known, logged: during the last fast steps (about 14.9-15.3 s) a fading month label passes through the right-hand UI zone.
