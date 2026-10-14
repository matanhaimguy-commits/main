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
  cuts_per_10s: 9.64
  mean_s_between_big_changes: 1.0
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.732
---

## The film in one line
A 16:9 typography edit of an upbeat pop song in a 2000s screensaver look: each lyric word ("Rival", "You",
"Your rage", "Legendary", "Heart", "Bang!", "Down") is a chunky bevelled 3D chrome or bubble letterform that
flies, spins and explodes through a new neon world every beat (starfields, heart fields, fire clouds, rainbow
bloom), with outline stars and tilted coloured squares orbiting it.

## Why it stops the scroll (first 2 s)
- 0.0 s: black.
- 1.0 s: a neon starfield; the word "Rival" in 3D purple letters tumbles in with a lime diamond, pink diamond and
  outline star.
- 2.0 s: dark frame with glowing white "You" and a thin audio waveform line.
- Mechanism: a cut from black into a maximal, saturated 3D type world, on the first hit of a recognisable song.
  The nostalgia of the 2000s chrome-type look is itself the pattern interrupt in a feed of flat, minimal edits.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-2 | black, then "Rival" in a neon starfield, then glowing "You" over a waveform | word tumbles in, camera pushes | intro hits |
| 3 | white burst, chrome letters of a long word exploding outward on rainbow rays | letters scatter from centre | hit |
| 4-5 | red heart field, white "My"; red starfield with small "My Love" and big arched 3D "YOUR RAGE" | word arcs across, stars spin | vocal |
| 6-8 | pink bubble "CLAIM" with outline stars; giant close "OUR"; small "OUR BATTLE" over huge red 3D "LEGENDARY" on fire clouds | camera flies past letters very close | building verse |
| 9-11 | purple motion streaks; long purple 3D word on light rays; dark spinning starfield | whip spins between words | verse |
| 12-13 | "Heart" in chrome serif on a big red heart with confetti hearts; white "DO" in a blue particle tunnel | heart pulses, tunnel rushes | pre-chorus |
| 14-17 | "BANG!" small in a neon space, then a huge yellow 3D "BANG" with "TILL I", then "TAKE YOU" | words slam in on each beat, camera orbits | chorus starts |
| 18-20 | "DOWN" in rainbow-lit white space, coloured squares tumbling; a rainbow gradient with a small black line of lyric text | words fall away, bloom | chorus |
| 21-25 | "BANG!" giant chrome, "BANG TILL I TAKE", "DOWN!" in a pastel rainbow world | each word hits, rotates past | chorus repeat |
| 26-27 | rainbow bloom with tilted squares and stars, a small black lyric line | settle | music fades |

## Signature device
Every lyric word is a solid 3D object, not a caption. Letters are heavily extruded (depth about 30-40% of
the cap height) with rounded bevels, chrome or glossy bubble materials and rim light, set in a wide geometric
or bubble display face. The camera treats each word like a set: flies past it at close range, orbits it, or
lets it tumble through frame, with strong motion blur. Each beat changes the whole world behind the word
(starfield, heart field, fire clouds, purple light rays, white rainbow bloom) while a fixed prop kit (outline
neon stars, tilted squares with thick white borders, ribbon light streaks) stays constant across worlds. Quiet
lines break the pattern as tiny flat black text over a rainbow bloom, which makes the next big word hit harder.

## Pacing read
Sampled at 1 fps, every sample differs from the last (9.64 cuts per 10 s, CV 0.0), so the metric is saturated:
the real rate is at least one new word or world per beat, likely faster than one per second. No rests at all
(quiet share 0). The only change in rhythm is in scale: small words and flat text lines (2 s, 20 s, 26-27 s)
alternate with giant slammed words in the chorus (14-25 s). It ends on a bloom without a logo; the busy last
frame against the black first frame does not loop cleanly.

## Look
- Palette: deep violet-black space (#1d1526, #594388), hot purple (#bd5dd8), red (#b11e37), white highlights
  (#ece7ed), with lime, yellow, cyan and pink accents on the props.
- Type: extruded bubble and chrome display faces in caps, mixed sizes from about 60 px (lead-in words) to full
  frame width; one chrome serif for "Heart".
- Texture: glow, bloom, lens streaks, sparkles; heavy motion blur on camera moves.
- Camera: constant motion, close passes, orbits, whip spins between worlds.

## Why it works
Each beat delivers a new world, so there is nothing to scroll away from; the eye is always catching up. The
2000s chrome look triggers nostalgia and reads as "effort", which drives saves (214k, about one per 30 plays) from
editors who want the style. The words act out the lyric in big type, so it works with the sound off as long as
the viewer knows the song. Comments and shares come from fans of the track.

## Steal this (grammar) / Leave this (content)
- Steal: one word per beat as a solid 3D object; a new background world per line with a fixed prop kit to tie
  them together; alternating tiny flat text and giant 3D words to create contrast; camera passes through and
  around type.
- Leave: the song, its lyrics, the exact prop shapes and colourways, the screensaver nostalgia as a whole look
  unless the client's brand fits it.

## Build it in our studio
Engine: canvas engine (fast fake-3D and subframe motion blur), HyperFrames only for a lighter version.
1. Pick 12-20 words from the client's message, one per beat of a generated track (beats.py for the grid).
2. Fake extrusion in canvas: draw each word 24-32 times offset along a projected depth vector in a darker shade,
   then the face with a vertical gradient and a thin white top highlight; rotate with a 3D projection of the
   word's anchor points.
3. Worlds: 4-5 reusable backgrounds (gradient plus a field of stars or hearts or brand icons) cut on beats.
4. Camera: spring-driven pushes and orbits, motion blur from the renderer's subframes.
5. Note the house rules ban generic particle bursts and glow on UI: keep the props tied to the brand (its
   icons, its colours) and keep glow off any real interface.
- Hard part: extruded type that rotates convincingly in perspective. Stacked copies hold up to about 35 degrees
  of rotation; beyond that, cut on the beat rather than rotate further.
- Difficulty 3; render cost moderate (many layers per frame, 60 fps with motion blur).

## Business translations
- Events or nightclub: a festival line-up teaser with each act name as a chrome 3D word in its own neon world,
  cut to a generated beat.
- E-commerce streetwear drop: the real drop day and time in Y2K chrome type, each word slamming in on a beat.
- Personal brand (DJ or creator): a channel intro where the creator's catchphrase is built word by word in 3D
  chrome, ending on their real logo.
