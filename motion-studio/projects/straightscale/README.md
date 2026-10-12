# StraightScale reel: "Marketing copë-copë"

50 s, 1080x1920, 60 fps motion graphics reel for Instagram / Facebook (organic).
Everything is made in code: visuals in `index.html`, music and sound effects in `audio/score.py`.
Shot list with Albanian lines and English checks: `docs/shotlist.md`.

## Deliverables (`deliver/`)
- `straightscale_reel_9x16.mp4`: final video with sound, -14 LUFS
- `contact.png`: 2 frames per second, the whole film
- `poster.png`: cover frame (the 1.800 "cilësi" moment)

## Rebuild
```
cd motion-studio/projects/straightscale
python3 audio/score.py                      # music.wav + sfx.wav
python3 ../../beats.py audio/music.wav > beats.json
node ../../stills.mjs --from 0.3 --step 0.5 --dur 50 --cols 10 --scale 0.2   # review sheet
node ../../render.mjs --fps 60 --sub 4 --dur 50                              # out/silent.mp4
./finish.sh                                 # mix, master to -14 LUFS, mux, write deliver/
```

## Notes
- The logo is redrawn from the brief's description (red rounded square, white S, gold square, black wordmark
  in Montserrat). Replace `logoMark()` and the wordmark with the real logo file when we have it.
- The "Instalim brenda 10 ditëve. Data në kontratë." promise is the brief's example and is labelled SHEMBULL on screen.
- Only data from the brief is used: ~1,800 "cilësi" ads (Meta Ad Library, 11 Oct 2026) and the three growth figures.
