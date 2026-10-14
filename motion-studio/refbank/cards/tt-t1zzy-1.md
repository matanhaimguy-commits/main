---
id: tt-t1zzy-1
title: "Warp-speed lyric tunnel: the camera flies forward through particle space while lyric words wrap around it on spirals and rings"
url: https://www.tiktok.com/@t1zzy_1/video/7582560901031611703
platform: tiktok
creator: t1zzy_1
plays: 3000000
likes: 451800
shares: 36400
saves: 76480
followers: 26000
posted: 2025-12-11
captured: 2026-10-14
duration_s: 32
category: lyric-mograph
hook: [pattern-interrupt, sound-hook]
devices: [type-on-path, 3d-type, particles, zoom-through-scale, lyric-sync-type, cut-on-beat, trending-audio]
energy: frantic
palette: [neon, dark]
palette_hex: ["#0b0d17", "#271156", "#445f68", "#e0e5e2", "#9d59a6"]
sound: [trending-audio, music-beat]
voiceover: false
text_on_screen: heavy
engine: [canvas, hyperframes]
difficulty: 3
fit: [events, personal-brand, ecommerce]
wow: 3
relevance: 2
pacing:                               # frames_metrics.py on a 1 fps sample (saturated: every sample is a cut)
  cuts_per_10s: 9.69
  mean_s_between_big_changes: 1.0
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.843
---

## The film in one line
A 16:9 3D typography edit: the camera rushes forward through a particle tunnel while lyric words ("I still
wanna be your favorite", "your number one", "cry") appear on rings, spirals and tumbling planes in nebulas that
change colour every beat, ending in a bubble burst that reveals the editor's anime avatar in a glass orb.

## Why it stops the scroll (first 2 s)
- 0.0 s: white particles streaking past at warp speed towards a small glowing rectangle in the centre.
- 1.0 s: the rectangle is now a bright card on the left; "NOO" glows pink in the dark.
- 2.0 s: blue light ribbons curl around the card; the pink word recedes into depth.
- Mechanism: instant forward motion (hook change 0.843) pulls the eye to the centre, and the glowing card reads
  as a portal about to be flown through. The opening vocal "no" works as a sound hook.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-3 | warp starfield, glowing card, pink "NOO", blue ribbons, "OOOOO" trailing into the card | camera flies forward, letters echo into depth | intro vocal |
| 4-8 | "I STILL"; "STILL" with "wanna be your" on a curved baseline; "FAVORITE" in a pink-blue gradient; giant letters by the lens with a ring of small O's; a torus of letters on a green-yellow swirl | words tilt past, camera flies through the ring | verse |
| 9-11 | green warp tunnel, "BE THE ONE THAT MAKES" tumbling in 3D | words fly past on different planes | build |
| 12-17 | teal ribbons; "YOU THINK" in a blue starfield; a band of letters spiralling into a vortex; "AWAKE" glowing at the centre | spiral rotates as the camera dives in | build |
| 18-26 | green and cyan nebulas with "TO", "YOUR", "NUMBER ONE", "BIGGEST"; "AND" on a rainbow white field; pink glassy "MINE"; a red laser band | words fly in from the sides, hard colour cuts | chorus |
| 27-29 | letters passing with neon ribbons; "LIKE YOU"; glassy mint "CRY" in a green nebula | words pass the lens | chorus end |
| 30-31 | cyan bubbles burst from a white core; a glass orb holding the editor's anime avatar (Santa hat, headphones) with the editor's tag | burst, orb floats | music fades |

## Signature device
A forward-flying camera through a particle tunnel, with words built around the flight path. The background is a
dense field of small particles streaking radially, regraded per section (white, blue, green, teal, cyan, pink).
Words sit in depth along the camera path and wrap onto shapes: a ring of repeated letters the camera passes
through, a rotating spiral band of text, curved baselines under bold words. Bold words are extruded with gradient
or glass materials; linking words sit on curves in italic or script. Thin glowing ribbons swirl around the path
for speed. Colour worlds change every beat, but the forward motion never stops, so it feels like one flight.

## Pacing read
At a 1 fps sample every sample is a new frame state (9.69 cuts per 10 s, CV 0.0, saturated); the real rate is at
least one change per beat, with no rests. Energy is flat-out from the first frame; variation comes from colour
and word size (lens-filling letters at 7 and 23 s versus small words deep in the tunnel). The ending switches mode
to a bubble burst and a held avatar orb, a signature rather than a loop.

## Look
Near black (#0b0d17), violet (#271156), teal grey (#445f68), white, orchid (#9d59a6), mint (#52edb4), pink and red
accents. Wide heavy caps, italic and script on curves, from 40 px deep in the tunnel to beyond frame width. Bloom
and motion streaks.

## Why it works
Constant forward motion is hypnotic and gives one focal point, so dense frames still read; each beat swaps the
colour world. The caption's software challenge ("prove DaVinci is as good as AE") starts comment arguments (4.4k)
and draws saves from editors.

## Steal this (grammar) / Leave this (content)
- Steal: a camera that never stops moving forward; words placed along the path and wrapped onto rings and
  spirals; a colour-world change per section while motion stays continuous; a short burst-to-signature ending.
- Leave: the song and lyrics, the avatar and tag, the exact colour sequence.

## Build it in our studio
Engine: canvas (particle tunnel and projection math are cheap there); HyperFrames for a simpler version.
1. Tunnel: a few thousand seeded particles in a cylinder; move the camera along z and draw each as a streak from
   its previous projected position (seeded noise, never Math.random).
2. Words on paths: place glyphs on a ring or helix in 3D (angle, radius, z), project and scale by depth; extrude
   bold words with stacked offset copies.
3. Per-section grade (background gradient plus particle tint) cut on beats from beats.py.
4. End on the client's real logo in a soft orb for 1.5 s.
- House rules ban generic particle bursts and glow on UI: tint the tunnel in brand colour and keep it a tunnel.
- Hard part: curved text legibility at phone size. Keep curved words short, slow the camera as key words pass
  the lens, check at 360 px wide. Difficulty 3, moderate render.

## Business translations
- Festival: a flight where each act's name wraps a ring the camera passes through, ending on the festival logo.
- Streamer (personal brand): a channel intro flying through their catchphrase on a spiral, ending on their logo.
- Tech accessory e-commerce: feature words on rings around a forward flight, ending on the product in a glass orb.
