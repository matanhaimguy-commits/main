---
id: tt-ripkuroi
title: "90s TV-ident rap edit: each lyric becomes a literal pun (toy car, compass, ice cubes) in black, icy white and one blue"
url: https://www.tiktok.com/@ripkuroi/video/7488505611374562582
platform: tiktok
creator: ripkuroi
plays: 5600000
likes: 598100
shares: 57100
saves: 127389
followers: 15300
posted: 2025-04-02
captured: 2026-10-14
duration_s: 25
category: lyric-mograph
hook: [sound-hook, familiar-ip]
devices: [lyric-sync-type, seamless-loop, cut-on-beat, whip-pan, shape-wipe, 3d-type]
energy: high
palette: [mono, light]
palette_hex: ["#e8f6f8", "#0d0e10", "#2b2c39", "#555b83", "#9aa1b3"]
sound: [music-beat]
voiceover: false
text_on_screen: heavy
engine: [hyperframes, canvas]
difficulty: 2
fit: [local-service, ecommerce, events, restaurant, agency]
wow: 3
relevance: 4
pacing:                               # frames_metrics.py on a 1 fps sample
  cuts_per_10s: 5.2
  mean_s_between_big_changes: 1.04
  change_rhythm_cv: 0.19
  quiet_share_2fps: 0.042
  hook_change_0_2s: 0.131
---

## The film in one line
A 4:3, VHS-soft motion-graphics edit of a West Coast rap hook (the creator's own audio edit): a black notebook
with the editor's monogram, a toy blue sports car driving under "COMIN' FROM THE WEST SIDE", a compass needle
pointing to "WEST", the credit "staring Ice Cube" among floating ice cubes, and chant syllables on blue slanted
bands, played twice and fading back to the white it started on.

## Why it stops the scroll (first 2 s)
- 0.0 s: a pale icy white, almost empty frame, soft like tape.
- 1.0 s: a black notebook with a scratched "R" monogram tumbles in; bracketed subtitle: "[ you know how we ]".
- 2.0 s: white again as the subtitle fades.
- Mechanism: the sound carries the hook (a famous chanted rap line, the caption's "WEST SIIIIIDE"); the quiet,
  bright frame is an odd opening for a rap edit and makes people wait for the drop (hook change 0.131).

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-2 | icy white; monogram notebook; bracketed subtitle | notebook tumbles in and out | vocal intro |
| 3-4 | black pillars framing blue and pale-blue diagonal bars with thin black lines; a toy blue sports car on a road | pillars slide open like doors | beat drops |
| 5-6 | black condensed italic "COMIN' FROM THE" in perspective; white "WEST SIDE" on the asphalt | car drives across, camera tilts down the road | hook line |
| 7-9 | portrait card tumbling with banknotes; compass needle pointing at "WEST" among black and blue dots; whip blur | spins, needle swings | chant |
| 10-12 | black with "staring Ice Cube" and floating ice cubes; white oval lens wipe; blue bands with "WOH", "UH", "OH" | cubes drift, bands slide | credit, chant |
| 13-21 | second pass with new angles: "SIDE" on a blue bar, car and full hook, photo card with "[ nothin' but the ]", compass with a star, ice cube credit | same moves | hook repeats |
| 22-24 | chant bands, then a fade to icy white | slide, fade | final line, music ends |

## Signature device
A literal visual pun for each lyric phrase inside a strict retro broadcast kit. "Comin' from the" is a toy car
driving; "west" is a compass needle; the artist's name gets floating ice cubes; chant syllables ride moving bars
like a 90s sports package. The kit is tiny: icy white (#e8f6f8), black, one royal blue and its tints; condensed
italic caps set in perspective as if painted on surfaces; a small wide sans for credits; bracketed lower-case
subtitles. Everything is softened (slight blur, washed contrast, 4:3, letterbox bars). The sequence plays twice
and ends on the opening white, so it loops.

## Pacing read
At a 1 fps sample: 8.4 cuts per 10 s, a change every 1.04 s, very regular (CV 0.19), a cut per beat at a
constant tempo. Almost no rests (quiet share 0.04); white frames at 0, 2, 11 and 23-24 s act as breaths. The
second pass repeats the first with new angles, so viewers anticipate each pun. White-to-white ending loops
seamlessly.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 13 cuts in 25.0 s sampled (5.2 per 10 s), at 3.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 15.0, 19.0, 20.0, 22.0 s; 21 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
Icy white, black, washed royal blue (#555b83), pale blue-grey (#9aa1b3). Condensed black italic caps at 120-160 px,
perspective-skewed; white bold sans on the road; small geometric credits; bracketed subtitles at about 30 px.
Soft focus, slight VHS bleed, letterbox bars; tilts, whips, door-like pillar wipes, an oval lens wipe.

## Why it works
Each pun is a small smile on the beat, and the repeat pass rewards viewers for learning the pattern. Three
colours and one toy car look designed rather than busy, which drives saves from motion designers. The loop and
the chanted hook keep it playing; rap fans share it for nostalgia.

## Steal this (grammar) / Leave this (content)
- Steal: one literal visual pun per phrase; a three-colour retro broadcast kit; type painted onto surfaces in
  perspective; bracketed subtitles; play the sequence twice; end on the opening frame.
- Leave: the song and hook, the artist's name and portrait, the editor's monogram, the car and compass layouts.

## Build it in our studio
Engine: HyperFrames (type and layout) or canvas (custom props).
1. Split the client's slogan into 4-6 phrases and find a literal object for each (a van for "on our way", a key
   for "move in", a clock for "open late").
2. Draw props flat or simple fake 3D in the brand colour plus black and white.
3. Set phrases in condensed italic caps with a CSS perspective transform onto the surface they sit on.
4. Tape finish from the registry, 4:3 or letterboxed safe area; generated beat; repeat once; end on frame one.
- Hard part: puns that read in one second at phone size; replace any that need explaining. Difficulty 2, cheap
  render.

## Business translations
- Moving company: "Comin' to your side of town", a toy van on a road, a compass to the neighbourhood, the phone
  number on a bar.
- Ice cream shop: flavour words as literal props in a three-colour retro ident that loops.
- Sneaker store (e-commerce): the brand line on a running track with one shoe as the moving prop, played twice.
