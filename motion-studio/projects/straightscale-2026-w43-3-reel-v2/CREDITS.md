# Credits and sources · The 22:47 race (v2)

All people and places are generated; nobody shown is a real client.

## Stills (Higgsfield, GPT Image 2, quality high, 2k, written as iPhone photos with a reference image, Section G7)
s1 Elira on the sofa (a1c36c8b-77bb-49ee-8c3b-103519a7b9a0) · s2 owner 1 asleep (ca6f62ff-a7c3-4b19-92bc-e9e0a37ed2ea) ·
s3 owner 2 at dinner (28a97587-013e-438e-a8d9-b544bff14d55) · s5 owner filming (1c69a416-70b5-4b3b-9b50-2e2d0a93126e) ·
s6 owner 3 morning (7f8e1aea-c188-4d22-b3b5-8d40e0e8ed71) · s7 strategist on a night street (4d96bcf9-8fd8-4c1e-90b6-29235d19b349) ·
s8 laser owner with gloves (2ffdecb8-7e6c-4c44-8ea1-d810ebd1b1d6) · s9 owner 3 asleep (67b5f8de-c9ca-4961-a9df-3c7cc4f0be60) ·
s10 Elira relieved (441b1c2f-d9ec-4a0b-a25a-07ba2b4139b0) · s11 owner 1 morning kitchen (4234ed76-4c08-4a1d-bf18-6d7656ccf304).
Identity references: the people from StraightScale's approved ads U1, U2 and V3 (owner 1, owner 2, strategist).

## Video (Higgsfield, MiniMax H3, 2K, 9:16, Section G1)
- k1-k8, k10: keyframe mode from the stills, 5.17 s each, no speech.
- t1b: reference mode (strategist still + ElevenLabs slice t1, 14 s), lip-synced L14-L16; drift check 0 (G6). t1a was
  rejected (drifted after 5 s).

## Sound (ElevenLabs, Section G8; flow tjm1hH2DO5wijd6ldvEh)
- Voice: eleven_v4, voice 8oGKUMljR779HzpZBiE4 ("Strategist"), 4 beats, 4 takes each (beat 4: 2 IPA and 2 plain-spelling takes), each take checked word for word with
  Whisper; picked b1_3, b2_4, b3_1, b4n_2. "ANALIZA" in plain spelling (the IPA takes read as "Analyzer").
- Music: eleven_music_v2_5 (music1). Effects: eleven_text_to_sound_v2 (swoosh, phone buzz, notification ping).

## Brand
Logo files from `../straightscale-2026-w43-3-reel/assets/brand/` (symbol.png, wordmark-white.png), quantized into
overlay/logos.js. Colours #BE0F18, #DD9A10, #F8F6EF, #1F1F1F. Font: Montserrat ExtraBold.

## Tools
ffmpeg 5.1, Playwright Chromium, faster-whisper, ImageMagick (Higgsfield sandbox).
