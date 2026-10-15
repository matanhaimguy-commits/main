---
id: tt-skalitude-show
title: "One black dot multiplies into a living maze, and the song's question forms in it and melts away"
url: https://www.tiktok.com/@skalitude_show/video/7570427231818894606
platform: tiktok
creator: skalitude_show
plays: 24100000
likes: 4400000
shares: 291300
saves: 591436
followers: 42400
posted: 2025-11-08
captured: 2026-10-14
duration_s: 17
category: lyric-mograph
hook: [wait-for-it, familiar-ip]
devices: [type-morph, lyric-sync-type, word-stack, morph]
energy: medium
palette: [mono, light]
palette_hex: ["#f7f8f7", "#0d0e0d", "#d3d4d2", "#3d3e3d", "#a5a6a5"]
sound: [trending-audio, music-beat]
voiceover: false
text_on_screen: captions
engine: [canvas, hyperframes]
difficulty: 3
fit: [agency, events, health, ecommerce, b2b]
wow: 4
relevance: 4
pacing:
  cuts_per_10s: 0.59
  mean_s_between_big_changes: 0.55
  change_rhythm_cv: 0.48
  quiet_share_2fps: 0.03
  hook_change_0_2s: 0.178
---

## The film in one line
On a white square a single black dot swells, splits into cross and petal shapes like a dividing cell, then
bursts into hundreds of dots that join into a writhing black and white labyrinth (a reaction-diffusion
pattern), and three times the maze's own stripes bend into the stacked words "Are We Still Friends?" in sync
with the song before dissolving; at the end the field inverts to thin white lines on black and thins out.

## Why it stops the scroll (first 2 s)
- 0.0 s: almost empty white frame, one small black dot at the top left.
- 0.5 s: the dot has grown; a second, smaller dot appears lower right.
- 1.0 s: the first dot has become a four-lobed cross, a third dot appears top right.
- 1.5 s: the cross splits into a more complex petal shape; more seeds appear.
- 2.0 s: on the beat the frame fills with hundreds of dots that start to stretch and connect.
- Mechanism: minimal first frame plus visible growth. A dot that behaves like a living cell makes the viewer
  wait to see what it becomes, and the song (a recognisable track) starts underneath. The payoff, readable
  words, is held back to 4 s.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-1.5 | white, one dot growing and dividing, a few new seeds | slow organic growth | electronic beat begins |
| 2.0-2.5 | frame fills with dots that stretch into worms | burst, then connecting | beat lands |
| 2.5-4.0 | full labyrinth of black and white stripes | stripes crawl and reorganise | beat |
| 4.0-5.5 | "Are / We / Still / Friends?" grows in, stacked left, line by line | stripes bend around letter shapes | the lyric is sung (AI segment) |
| 6.0-7.5 | words melt back into the maze | dissolve | music |
| 8.0-9.0 | a second stacked question ending "Be / Friends?" forms on the right | same grow-in | next lyric |
| 9.5-11.0 | maze only, stripes turning diagonal | flow | music builds |
| 11.5-13.5 | "Are / We / Still / Friends?" again, larger "Friends?" at the bottom | grow-in, hold about 0.5 s | lyric |
| 14.0-15.5 | dissolve, stripes coarsen and align diagonally | flow | music |
| 16.0-17.0 | the field inverts: thin white lines on black, thinning | fade of the pattern | music fades out |

## Signature device
Type that is made of the texture. The whole frame is one reaction-diffusion field (Turing stripes: black and
white worms about 3% of frame width wide, equal black and white). The words are not laid on top; they bias the
field, so stripes follow the letter contours and the letters appear as stripe-built outlines with the same
stroke weight as the pattern. Words are a rounded geometric sans in initial caps, stacked one word per line,
left aligned, with the last word largest (about 15% of frame height, "Friends?" spanning about 80% of the
width). Each word takes about 0.5 s to resolve out of the noise, the full stack is clearly legible for about
0.5-1 s, then the bias is released and the stripes reclaim it over about 1.5 s. The creator says it was built
in Photoshop by repeating blur and threshold steps, which produces the same look as a Gray-Scott simulation.

## Pacing read
The metrics read 17.65 cuts per 10 s and a big change every 0.55 s, but there are no cuts at all: the stripes
change everywhere every frame, which the measure counts as cuts. The real rhythm is the lyric: a 2 s seed
phase, then words resolving at about 4, 8 and 11.5 s (every 3.5-4 s), each legible for under a second. The low
hook change (0.178) is the near-empty opening. Energy peaks on the third, largest "Friends?", and the ending
inverts and thins the pattern so it fades with the song. Not a loop, but the brief legibility windows drive
rewatches to read the words.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 1 cuts in 17.0 s sampled (0.59 per 10 s), at 2.0 s; 30 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette by role: paper white (#f7f8f7) and ink black (#0d0e0d) only; the greys (#d3d4d2, #3d3e3d, #a5a6a5)
  are anti-aliasing at stripe edges. The end inverts the roles.
- Type: rounded geometric sans, initial caps, stacked left, built from the pattern's own stripes; no other text.
- Texture: crisp, slightly soft-edged stripes like a microscope slide or animal skin; frames sampled square.
- Camera: none; the whole film is the field changing in place.

## Why it works
- Organic growth from one dot is hypnotic and makes viewers wait for the shape it becomes.
- The words are hard to see, then suddenly readable: a small puzzle each time, rewarded on the lyric.
- Sound and type match: the question appears exactly when it is sung.
- Saves (591k) and shares come from designers who want the technique; the caption names "reaction diffusion",
  which drives search and comments.

## Steal this (grammar) / Leave this (content)
- Steal: one seed growing into a full-frame generative field; words formed by the field itself rather than
  placed on it; a short legibility window per line synced to sound; an inversion to end.
- Leave: the song, the lyrics, the artist reference, the creator's exact pattern frames.

## Build it in our studio
- Engine: `canvas` for the field (Gray-Scott on a grid around 400 cells wide, or iterated blur plus threshold),
  text masks rendered offscreen to bias feed and kill rates inside the letters; HyperFrames only for timing if
  the field is baked to a frame sequence.
- Scene plan: 1) seed one dot, grow and split for 2 s; 2) burst seeds on the downbeat; 3) run to a full maze;
  4) at each cue, fade in a text mask that pulls stripes along letter contours, hold 0.8 s, release; 5) invert
  and lower the feed rate to thin the field at the end.
- Hard part: the render contract. A simulation carries state between frames, so bake it once (deterministic
  seed, fixed steps per frame) to a frame sequence and have `seek(t)` read the frame; and tune the bias so the
  words read at phone size.
- Difficulty 3: all 2D and in our engine, but the tuning takes iterations.

## Business translations
- Music festival (events): one dot grows into a maze on the first beat and each headliner's name forms in the
  pattern on the downbeat, ending on the dates.
- Skincare brand (e-commerce or health): a skin-cell pattern grows from one dot and the product name forms in
  it, then melts back; end on the packshot.
- Design agency: the agency's name and one line about what it does grow out of a living pattern as a showreel
  opener.
