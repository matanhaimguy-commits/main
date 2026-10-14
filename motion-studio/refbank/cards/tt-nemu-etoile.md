---
id: tt-nemu-etoile
title: "A student's 18 s After Effects reel: one star emblem stays centre while ring wipes flip the world through five colour scenes"
url: https://www.tiktok.com/@nemu_etoile/video/7149290182880087302
platform: tiktok
creator: nemu_etoile
plays: 3000000
likes: 439800
shares: 5677
saves: 84007
followers: 14000
posted: 2022-09-30
captured: 2026-10-14
duration_s: 18
category: beat-sync
hook: [text-headline, sound-hook]
devices: [shape-wipe, cut-on-beat, match-cut, grid-mosaic, pixel-art]
energy: frantic
palette: [saturated, neon]
palette_hex: ["#000100", "#d8cc93", "#983ed7", "#181a22", "#36b58f"]
sound: [music-beat]
voiceover: false
text_on_screen: headline
engine: [hyperframes, canvas]
difficulty: 2
fit: [agency, events, education, personal-brand]
wow: 3
relevance: 3
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 0.72
  change_rhythm_cv: 0.9
  quiet_share_2fps: 0.029
  hook_change_0_2s: 0.024
---

## The film in one line
A landscape motion-design exercise, letterboxed in a 9:16 frame under the caption "made this for class": a white
star inside a ring pops onto a dark navy screen, coloured arcs sweep in, and the star then stays near the centre
while ring wipes and colour flips carry it through a blue pixel-sprite world, a magenta dance-silhouette world, a
yellow world of echoing figures and a green tunnel of tumbling cubes, cut to a fast game soundtrack until it stops
dead.

## Why it stops the scroll (first 2 s)
- 0.0 s: almost nothing: a dark navy 16:9 strip with a faint dot grid across the middle third of a black 9:16
  frame, and the bold monospace caption "made this for class" in the black bar below.
- 0.5 s: a thick cyan ring with a white five-point star pops in, centred.
- 1.0 s: the ring splits into thin rings and the star spins.
- 2.0 s: the ring becomes a serrated starburst outline and a thin purple arc starts to swing in from the right.
- Mechanism: the caption does the work. "made this for class" is a humble, relatable frame that invites viewers
  to judge and compare ("this is a class project?"). The music (a fast, bright game track per the AI
  description) starts at full energy, and the badge pop at 0.5 s promises a motion piece.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-1.5 | navy strip, star badge pops in, rings split and reform | scale pop, spin, ring thickness changes | game track starts, energetic |
| 2.0-3.0 | badge turns serrated; purple, green, then yellow arcs swing in from the edges | arcs orbit the badge one per half second | music |
| 3.5 | a big white ring wipes the screen to a bright blue starfield; star now yellow in a dotted ring, pushed to the top right | ring wipe | beat |
| 4.0-5.5 | pixel cats with pastry bodies fly across, white bars rise and fall like an equaliser | sprites cross left to right, bars pump | music |
| 5.5-7.0 | mirrored kaleidoscope of pixel hedgehog sprites and huge blurred shapes around a yellow ring | mirror symmetry, zoom | music |
| 7.5-9.0 | hard flip to magenta: white dancer silhouettes with echo trails, orange diagonal hatch lines, green rings; a white block wipes across | silhouettes dance, echoes trail | beat |
| 9.5-10.5 | magenta grid of pixel figures in yellow, orange and white mirrored around a big white star in a yellow ring | grid pulses outward | music |
| 11.0-12.0 | yellow field with rows of pale green textured figures top and bottom, ruler tick marks, pink rings, star in a pink badge | rows slide horizontally | music |
| 12.5-14.0 | yellow with cream silhouettes of suited men echoing in a line, blue star gear badges orbit | silhouettes step, badges rotate | music |
| 14.5 | white flash frame | flash | hit |
| 15.0-17.5 | green tunnel: pale cubes spiral around the shrinking star, magenta shards fly past, a magenta ring closes in | spiral zoom into centre | music, ends abruptly (AI) |

## Signature device
A single emblem as the anchor through every transition. The star (white, five points, about 15% of frame width)
sits in a ring whose style changes each scene (solid cyan ring, thin double ring, serrated starburst, dotted
yellow ring, gear-toothed blue badge, magenta ring) while the whole world behind it is replaced. Scene changes are
ring or block wipes: a circle grows from off-frame or a rectangle slides across, and the new colour field fills
behind it in about 0.25 s. Each world is one flat saturated colour (navy, blue, magenta, yellow, green) with one
family of repeated elements (sprites, silhouettes, cubes) moving in mirror symmetry or echo trails. Coloured arcs
orbiting the badge mark the beat between wipes.

## Pacing read
A big change every 0.72 s with a CV of 0.9: the rhythm is uneven on purpose, with fast clusters of arcs and
wipes (2.0-3.5 s, 7.5-9.0 s) and slightly longer holds inside each world. Quiet share is almost zero, so there are
no rests at all. The cut metrics read 0 and the hook change 0.02 because the active picture is only about a third
of the 9:16 frame (letterbox); by eye there are about eight scene changes in 18 s. The only breath is the white
flash at 14.5 s before the green finale. It ends abruptly on the music, which pushes a rewatch.

## Look
- Palette by role: black letterbox (#000100) and navy opening (#181a22); scene fields in electric blue,
  magenta (#983ed7 range), yellow (#d8cc93 as measured with the cream silhouettes) and mint green (#36b58f);
  white for the star and silhouettes.
- Type: only the caption, a bold monospace in white, about 45 px cap height on a 1080 frame, two lines centred
  in the lower black bar. Nothing animated.
- Texture: flat vector shapes, subtle dot grid, sprite pixels left crunchy, some soft motion blur on the cubes.
- Camera: locked 2D, with a zoom into the tunnel at the end.

## Why it works
- "made this for class" lowers expectations and then beats them: people comment and save it as inspiration.
- Familiar internet and game sprites give recognition hits every few seconds.
- The star anchor keeps the eye in one place, so a frantic sequence stays readable.
- No ending, no logo: the hard stop loops it.

## Steal this (grammar) / Leave this (content)
- Steal: one emblem fixed near centre as the throughline; ring and block wipes that swap the whole colour world
  behind it; one flat colour plus one repeated element family per world; mirror symmetry and echo trails; arcs
  orbiting on the off-beats; a white flash before the last world; hard stop on the music.
- Leave: Nyan Cat, Sonic and other game sprites, the soundtrack, the star emblem as drawn, the caption text.

## Build it in our studio
- Engine: HyperFrames (SVG rings, GSAP timeline, registry shape-wipe and kaleidoscope effects if found in a
  search) or the canvas engine for the cube tunnel.
- Scene plan: 1) take the client's logo mark as the anchor emblem, drawn as clean SVG; 2) write a beat grid from
  a generated or licensed track (beats.py) and place a wipe on every bar and an orbiting arc on off-beats;
  3) five worlds, each one brand colour plus one element family drawn from the client's world (products,
  icons, staff silhouettes cut from client photos); 4) white flash, then a tunnel zoom into the logo;
  5) end on the logo mark, hard stop.
- Hard part: making five worlds feel designed rather than random. Fix the emblem size and position, use one ring
  geometry family, and keep each world to one element type.
- Difficulty 2. Render around 5 minutes in HyperFrames for 18 s. No paid steps; the music must be generated or
  licensed.

## Business translations
- Event agency: the festival logo stays centre while ring wipes flip through the stages, the crowd, the food
  trucks and the line-up, ending in a tunnel into the date.
- Design school: "made this in week 3" open, the school crest as the anchor, each world built by a different
  student.
- SaaS launch: the product icon stays centre while each world shows one feature's icon family in the brand
  colours, ending in the icon at full size.
