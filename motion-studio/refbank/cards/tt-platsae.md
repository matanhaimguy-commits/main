---
id: tt-platsae
title: "Y2K chrome-type lyric edit: every word is a bevelled 3D object flung through a different neon world each beat"
url: https://www.tiktok.com/@platsae/video/7648921302203452680
platform: tiktok
creator: platsae
plays: 6600000
likes: 785900
shares: 71200
saves: 214391
followers: 185100
posted: 2026-06-08
captured: 2026-10-14
duration_s: 28
category: lyric-mograph
hook: [pattern-interrupt, sound-hook]
devices: [3d-type, lyric-sync-type, cut-on-beat, beat-sync-hits, orbit, particles, trending-audio]
energy: frantic
palette: [neon, saturated]
palette_hex: ["#1d1526", "#ece7ed", "#594388", "#bd5dd8", "#b11e37"]
sound: [trending-audio, music-beat]
voiceover: false
text_on_screen: heavy
engine: [canvas, hyperframes]
difficulty: 3
fit: [events, personal-brand, ecommerce, agency]
wow: 4
relevance: 2
pacing:                               # frames_metrics.py on a 1 fps sample (saturated: every sample is a cut)
  cuts_per_10s: 8.21
  mean_s_between_big_changes: 1.0
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.732
---

## The film in one line
A 16:9 typography edit of an upbeat pop song in a 2000s screensaver look: each lyric word ("Rival", "You", "Your
rage", "Legendary", "Heart", "Bang!", "Down") is a chunky bevelled 3D chrome or bubble letterform flung through a
new neon world every beat, with outline stars and tilted coloured squares orbiting it.

## Why it stops the scroll (first 2 s)
- 0.0 s: black.
- 1.0 s: a neon starfield; "Rival" in 3D purple letters tumbles in with a lime diamond, a pink diamond and an
  outline star.
- 2.0 s: a dark frame with glowing white "You" over a thin audio waveform.
- Mechanism: a cut from black into a maximal, saturated 3D type world on the song's first hit (hook change
  0.732). The 2000s chrome look is itself the pattern interrupt in a feed of flat, minimal edits.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-3 | black; "Rival" in a starfield; "You" over a waveform; chrome letters exploding outward on rainbow rays | tumble, push, scatter | intro hits |
| 4-5 | red heart field with "My"; red starfield with small "My Love" and arched 3D "YOUR RAGE" | word arcs across, stars spin | vocal |
| 6-8 | pink bubble "CLAIM"; giant close "OUR"; huge red 3D "LEGENDARY" on fire clouds | camera passes letters at close range | verse builds |
| 9-13 | purple motion streaks; a long purple 3D word on light rays; chrome serif "Heart" on a big red heart; white "DO" in a particle tunnel | whip spins, heart pulses | pre-chorus |
| 14-17 | "BANG!" small, then huge yellow 3D "BANG", "TILL I", "TAKE YOU" | words slam in per beat, camera orbits | chorus |
| 18-20 | "DOWN" in white rainbow space; a rainbow gradient with a small flat black lyric line | words fall away, bloom | chorus |
| 21-27 | "BANG!" giant chrome, "BANG TILL I TAKE", "DOWN!", then rainbow bloom with squares and stars | hits, rotations, settle | chorus repeat, fade |

## Signature device
Every lyric word is a solid 3D object, not a caption. Letters are deeply extruded (depth about 30-40% of cap
height) with rounded bevels, chrome or glossy bubble materials and rim light, in a wide geometric or bubble face.
The camera treats each word as a set: flies past it, orbits it, or lets it tumble through frame, with heavy
motion blur. Each beat swaps the whole world behind the word (starfield, heart field, fire clouds, light rays,
rainbow bloom) while one prop kit stays constant (outline neon stars, tilted squares with thick white borders,
ribbon light streaks). Quiet lines break the pattern as tiny flat black text, which makes the next giant word
hit harder.

## Pacing read
At a 1 fps sample every sample is a cut (9.64 per 10 s, CV 0.0): the metric is saturated, and the true rate is at
least one word or world per beat. No rests (quiet share 0). Rhythm varies only by scale: small words and flat
lines (2, 20, 26-27 s) against giant slammed chorus words (14-25 s). It ends on a bloom with no logo and does not
loop cleanly.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 23 cuts in 28.0 s sampled (8.21 per 10 s), at 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0 s; 27 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
Violet-black space (#1d1526, #594388), hot purple (#bd5dd8), red (#b11e37), white highlights (#ece7ed), with lime,
yellow, cyan and pink props. Extruded bubble and chrome caps from about 60 px to wider than the frame; one chrome
serif for "Heart". Glow, bloom, lens streaks, sparkles; constant camera motion.

## Why it works
Each beat delivers a new world, so there is never a moment to scroll away. The chrome look triggers nostalgia and
reads as effort, which drives saves (214k, about one per 30 plays) from editors who want the style. Giant words
act out the lyric, and fans of the track share it.

## Steal this (grammar) / Leave this (content)
- Steal: one word per beat as a solid 3D object; a new background world per line tied together by a fixed prop
  kit; tiny flat text against giant 3D words; camera passes through and around type.
- Leave: the song and lyrics, the prop shapes and colourways, the screensaver nostalgia as a whole look unless
  the brand fits it.

## Build it in our studio
Engine: canvas (fast fake 3D, subframe motion blur); HyperFrames for a lighter version.
1. Pick 12-20 words from the client's message, one per beat of a generated track (beats.py).
2. Fake extrusion: draw each word 24-32 times offset along a projected depth vector in a darker shade, then the
   face with a gradient and a thin top highlight; rotate via projected anchor points.
3. Four or five reusable worlds cut on beats; spring-driven pushes and orbits.
4. House rules ban generic particle bursts and glow on UI: build the props from the brand's icons and colours.
- Hard part: perspective rotation of stacked-copy extrusions holds to about 35 degrees; cut on the beat rather
  than rotate further. Difficulty 3, moderate render cost.

## Business translations
- Nightclub or festival: each act name as a chrome word in its own neon world, cut to a generated beat.
- Streetwear e-commerce: the real drop day and time in Y2K chrome type, one word per beat.
- DJ or creator (personal brand): their catchphrase built word by word in 3D chrome, ending on their real logo.
