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
  cuts_per_10s: 8.4
  mean_s_between_big_changes: 1.04
  change_rhythm_cv: 0.19
  quiet_share_2fps: 0.042
  hook_change_0_2s: 0.131
---

## The film in one line
A 4:3, VHS-soft motion-graphics edit of a West Coast rap hook (the creator's own audio edit): a black notebook
with the editor's monogram, a toy blue sports car driving under the words "COMIN' FROM THE WEST SIDE", a compass
needle pointing to "WEST", the credit "staring Ice Cube" among floating ice cubes, and chant syllables on blue
slanted bands, played twice and fading back to the white it started on.

## Why it stops the scroll (first 2 s)
- 0.0 s: a pale icy white, almost empty frame (soft, like a tape).
- 1.0 s: a small black notebook with a scratched "R" monogram tumbles in; a bracketed subtitle underneath:
  "[ you know how we ]".
- 2.0 s: back to white as the subtitle fades.
- Mechanism: the sound carries the hook (a famous chanted rap hook, the caption's "WEST SIIIIIDE"), while the
  near-empty, bright frame is an odd, quiet opening for a rap edit, which makes people wait for the drop. The
  subtitle line in brackets reads like a film caption and sets up the lyric.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-2 | icy white; black monogram notebook; bracketed subtitle | notebook tumbles in and out | vocal intro line |
| 3-4 | black pillars framing a narrow window with blue and pale-blue diagonal bars crossed by thin black lines; then a toy blue sports car on a road | pillars slide open like doors | beat drops |
| 5-6 | big black condensed italic "COMIN' FROM THE" in perspective above a road; white "WEST SIDE" painted on the asphalt | car drives across; camera tilts down the road | hook line |
| 7 | an album-style portrait card tumbling with floating banknotes, letterbox bars | card spins | beat |
| 8-9 | white field with black and blue dots, a compass needle pointing at "WEST"; whip blur | needle swings, whip | chant |
| 10 | black: "staring Ice Cube" in white with small ice cubes floating | cubes drift | credit beat |
| 11-12 | white oval lens wipe; blue slanted bands with "WOH", "UH", "OH" | bands slide past | chant syllables |
| 13-17 | second pass: pillars and bars, "SIDE" on a blue bar, car, "COMIN' FROM THE WEST SIDE" | same moves, new angles | hook repeats |
| 18-21 | portrait card and a photo card with "[ nothin' but the ]"; compass with "WEST SIDE" and a star; ice cube credit | spins and drifts | hook |
| 22-24 | "WOH / UH / OH" bands, then a fade to icy white | slide, fade | final line, music ends |

## Signature device
A literal visual pun for each lyric phrase, inside a strict retro broadcast kit. "Comin' from the" is a toy car
driving; "west" is a compass needle; the artist's name gets floating ice cubes; chant syllables are printed on
moving bars like a 90s sports package. The kit is tiny: icy white background (#e8f6f8), black, one royal blue
and its tints; condensed italic caps set in perspective as if painted on surfaces (the road, a bar); a small
wide sans for credits; bracketed subtitles at the bottom. Everything is softened (slight blur, washed contrast,
4:3 frame, letterbox bars) to read as an old tape. The whole sequence plays twice and ends on the same white as
the first frame, so it loops.

## Pacing read
At a 1 fps sample, 8.4 cuts per 10 s and a change every 1.04 s with a very regular rhythm (CV 0.19): a cut per
beat, locked to a constant tempo. Almost no rests (quiet share 0.04); the white frames at 0, 2, 11 and 23-24 s
act as breaths. The second half repeats the first with new angles, so the viewer recognises the pattern and
anticipates each pun. The white-to-white ending makes the loop seamless, which helps rewatches.

## Look
- Palette: icy white, black, royal blue (#555b83 in the washed sample), pale blue-grey (#9aa1b3).
- Type: condensed black italic caps (about 120-160 px on a 1080 frame, perspective-skewed), white bold sans on
  the road, a small geometric sans for credits, bracketed lower-case subtitles at about 30 px.
- Texture: soft focus, low contrast, slight VHS bleed; letterbox bars.
- Camera: tilts down the road, whip pans, door-like pillar wipes, a white oval lens wipe.

## Why it works
The puns make the viewer smile on each beat and want to catch the next one; the repeat pass rewards them for
learning the pattern. The restraint (three colours, one toy car) makes it look designed rather than busy, which
drives saves from motion designers. The loop and the chanted hook keep it playing. Rap fans share it for the
nostalgia.

## Steal this (grammar) / Leave this (content)
- Steal: one literal visual pun per phrase; a three-colour retro broadcast kit; type painted onto surfaces in
  perspective; bracketed subtitles; play the sequence twice; end on the opening frame for a loop.
- Leave: the song and its hook, the artist's name and portrait, the editor's monogram, the exact car and
  compass layouts.

## Build it in our studio
Engine: HyperFrames (type and layout) or canvas (if the car and props need custom drawing).
1. Take the client's slogan, split it into 4-6 phrases, and find a literal object for each (a delivery van for
   "on our way", a key for "move in", a clock for "open late").
2. Draw the props as flat or simple fake-3D shapes in the client's single brand colour plus black and white.
3. Set the phrase in condensed italic caps with a CSS perspective transform onto the road or bar it sits on.
4. Retro finish: a VHS or tape effect from the registry, 4:3 or letterboxed safe area, slight blur.
5. Generated beat-driven track; repeat the sequence once with new angles; end on the opening frame.
- Hard part: finding puns that read in one second. Test each at phone size; if the object needs explaining,
  replace it.
- Difficulty 2; render cheap (flat shapes, 25 s).

## Business translations
- Moving company (local service): "Comin' to your side of town" with a toy van on a road, a compass to the
  neighbourhood name, and the phone number on a bar.
- Ice cream shop (restaurant): flavour names as literal props (a cone for "cool", a sun for "summer") in a
  three-colour retro ident that loops.
- E-commerce sneaker store: the brand line on a running track with one shoe as the moving prop, played twice
  and looping.
