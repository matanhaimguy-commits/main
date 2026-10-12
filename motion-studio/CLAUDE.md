# Motion studio rules

## Render contract
- Every film is a pure function of time: window.seek(t) paints frame t.
- No CSS transitions, no setTimeout, no requestAnimationFrame in render mode,
  no state carried between frames. Seeded noise only, never Math.random.
- Render with node render.mjs. Encode H.264 yuv420p, CRF 16.

## Look
- Banned: centered title on a gradient, everything fading in,
  corner labels and frame borders, glow on UI, generic particle bursts.
- One display font, one UI font. One accent color unless the brief says otherwise.
- Every 2 to 4 seconds something new must happen on screen.

## Sound
- Music and sound effects are synthesized in code unless a track is supplied.
- Place hits on the measured beat grid (beats.json). Loudness -14 LUFS.

## Loop before you show me anything
1. Render one frame per beat as a contact sheet and LOOK at it.
2. Score it 1-10 on: hook in first 2s, readability at phone size,
   motion quality, variety, brand accuracy, sound sync.
3. Fix the 3 worst problems. Repeat until every score is 8+.
4. Only then do the full render.

## Studio tools
- lib/motion.js: closed-form spring() and track(). Use these instead of easing curves.
- beats.py: `python3 beats.py audio/track.wav > beats.json`.
- stills.mjs: `node stills.mjs --from 0.25 --step 0.5 --dur 20` contact sheet straight from index.html, no render needed.
- review.sh: `./review.sh [out/final.mp4] [4.1]` writes contact, strip and phone sheets to out/.
- render.mjs `--from 12 --dur 3` re-renders one segment; run 2-3 segments in parallel for long films and concat them.
- API keys live in .env (e.g. ELEVENLABS_API_KEY). Never paste keys into prompts.
