# Motion studio

Code-rendered motion video pipeline (from "How to Build a Motion Design Studio With Opus 5.5").

- `CLAUDE.md` — house rules: render contract, banned looks, sound, critique loop.
- `render.mjs` — headless Chromium calls `window.seek(t)` per subframe, ffmpeg blends to `out/silent.mp4`.
  `node render.mjs --fps 60 --dur 15 --sub 4 [--from 0] [--w 1080 --h 1920] [--out out/silent.mp4]`
  Canvas pages blend subframes in the page (fast); other pages fall back to screenshots + ffmpeg tmix.
- `lib/motion.js` — closed-form `spring()` and stacked `track()`.
- `beats.py` — `python3 beats.py song.wav > beats.json` (needs `pip install numpy librosa soundfile`).
- `stills.mjs` — contact sheet of chosen moments straight from `index.html`, for critique before any render.
- `review.sh` — contact sheet, glitch strip, phone test and loop check for the critique loop.
- Skill: `/motion-reel` (`.claude/skills/motion-reel/SKILL.md` at the repo root).

Setup: `cd motion-studio && npm install` (Playwright; uses the preinstalled Chromium in cloud sessions).
Put API keys in `motion-studio/.env` (gitignored), e.g. `ELEVENLABS_API_KEY=...`.
