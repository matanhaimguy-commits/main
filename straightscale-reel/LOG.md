# LOG
2026-10-12 19:12 · project created · motion-video-director kickoff · all folders, PROJECT/PROGRESS/LOG/manifest · ok
2026-10-12 19:12 · preflight · node 22, python 3.13, ffmpeg 6.1, chromium-1194, playwright 1.56.1 OK; demucs/faster-whisper/rembg not installed (HF + fbaipublicfiles blocked, no refs/footage) · ok
2026-10-12 19:12 · network check · freesound/unsplash/pixabay/lottiefiles/huggingface blocked; fonts.googleapis + npm OK · no API keys requested
2026-10-12 19:12 · npm i playwright@1.56.1 three gsap @fontsource/playfair-display @fontsource/montserrat · fonts copied to assets/fonts with OFL licences · ok
2026-10-12 19:12 · voice search · found workspace voice "StraightScale - Strategist (male, 45)" · chosen for VO
2026-10-12 19:12 · VO script v1 · plan/script.md · 119 words ≈ 49 s · awaiting approval
2026-10-12 19:14 · user approved VO script v1 ("Go"): hook A, ~50 s, default look, logo in code · PROJECT.md updated
2026-10-12 19:25 · ElevenLabs VO · eleven_v4, Strategist voice, 4 takes (~3.1k credits ≈ $0.56) · takes 45.9–47.8 s, no clipping (-2.4..-3.4 dBFS peak) · chose take 4 (45.92 s) → assets/vo/vo_v1.mp3
2026-10-12 19:25 · Scribe word timings (forced alignment; script diff 119/119 identical) → plan/beats.json · faster-whisper unavailable (HF blocked)
2026-10-12 19:25 · built engine: src/index.html, main.js, lib.js, render.js (CLI contract), scripts/preview.mjs · scenes S1, S3, S9, S13 built; rest placeholders
2026-10-12 19:25 · plan: plan/storyboard.md (13 shots), plan/fonts.md, plan/styleboard.png (palette + fonts + 4 code stills) · awaiting plan approval
2026-10-12 · user rejected storyboard v1 ("boring", "same design structures") · diagnosis: every shot was a centred UI card on a flat background with pop-ins; also broke studio rules (fades, glow, particles, centred titles)
2026-10-12 · redesign v2: ransom-note collage world (S1–S5) vs one straight gold line (S6–S13) · new toolkit src/fx.js (springs, paper, torn scraps, tape, label-maker, ransom letters, marker, stamp, gold-line mask)
2026-10-12 · built all 13 scenes · critique loop on contact sheets: fixed S2 overflow, caption fade → spring snap, stamp over labels, odometer overshoot, tape size, empty beat in S8, ads covering "falas", label behind clock, stray tape on pull-back, placeholder domain removed
2026-10-12 · storyboard v2 (plan/storyboard.md + plan/storyboard_v2.jpg) · rough cut renders/previews/roughcut_v2.mp4 (voice only) · awaiting approval
