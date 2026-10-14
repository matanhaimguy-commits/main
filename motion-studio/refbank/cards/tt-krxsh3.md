---
id: tt-krxsh3
title: "A student lyric video where pixel-font labels and vintage engraving cut-outs act out every line in teal duotone"
url: https://www.tiktok.com/@krxsh3_/video/7538097911683386642
platform: tiktok
creator: krxsh3_
plays: 2200000
likes: 302600
shares: 19400
saves: 80830
followers: 42000
posted: 2025-08-13
captured: 2026-10-14
duration_s: 60
category: lyric-mograph
hook: [familiar-ip, sound-hook]
devices: [lyric-sync-type, paper-cutout, type-on-path, pixel-art, cut-on-beat]
energy: high
palette: [dark, mono]
palette_hex: ["#060706", "#1b2b23", "#354c3d", "#afae7b", "#6e7758"]
sound: [music-beat]
voiceover: false
text_on_screen: heavy
engine: [hyperframes, collage, canvas]
difficulty: 3
fit: [events, agency, personal-brand, restaurant]
wow: 4
relevance: 3
pacing:                               # 1.5 s sampling, 40 frames cover 0-58.5 s of 60 s
  cuts_per_10s: 6.33
  mean_s_between_big_changes: 1.5
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.737
---

## The film in one line
A 16:9 kinetic-typography piece for a Glass Animals song in which each lyric becomes a cream "label" of pixel
or retro letters dropped into a black-and-teal collage of old engravings (skeletons, eyeballs, Victorian women,
statues, hanging fish, rotary phones, stacked TVs) that act the line out, ending on a TV that reads "brain dead".

## Why it stops the scroll (first 2 s)
- 0.0 s: almost black, a faint teal checkerboard fading up. Nothing readable yet.
- 0.5-1.0 s: not sampled; by 1.5 s huge pixel letters ("5 THOUSA...") crowd the top edge, small letters of the
  next word drift in, and a skull cut-out sits bottom right.
- 2.0 s: the first lyric is being built in mixed fonts over a framed Victorian figure.
- Mechanism: the song itself (a recognisable trending track, so the ear hooks before the eye) plus a dense,
  unusual look. Text is the lyric, so there is no separate hook line. The film is landscape on a vertical
  platform, which makes it look like a "real" piece of design work rather than a phone video.

## Beat map
Frames cover 0-58.5 s of 60 s. Sound is the song throughout (AI: upbeat rock, singing, percussion).

| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-4.5 | teal checker fades up; pixel words fill the frame edge to edge; Victorian woman in a white-bordered panel | letters slide and drop in, words cropped by the frame | song intro into first verse |
| 6.0-9.0 | black void with floating eyeballs; skeletons beside small label boxes | eyeballs drift, words pop in one at a time | verse |
| 10.5-15 | cream card with the song title held between two engraved hands; letters scattered around a checker sphere held by hands | hands frame and rotate the card | verse |
| 16.5-18 | radial cream and black sunburst with hands holding eyeballs; two statues face off over a two-line label | wedges rotate, statues slide in | verse |
| 19.5-27 | mirrored type, boxed pixel lines, an ornate mirror frame, full-frame pixel "JAMAICA RUM", a bottle over a city skyline | hard cuts per word, frame-filling type | chorus energy |
| 28.5-33 | rows of hanging fish, a cream card with the next line, a silhouette with a phone, a receiver with text on a curve | fish sway, text bends on path | verse |
| 34.5-37.5 | perspective checkerboard floor, two words standing on it; a woman with a megaphone in front of gears and columns, word blasting out | camera tilt over the floor, type shoots from the megaphone | build |
| 39-46.5 | big skull close-ups, letters of "HEAD" orbiting the skull on a circular path, x-ray skeleton with a brain | letters travel on an arc, skull spins | hook line |
| 48-55 | stacked retro TV sets showing pixel letters, skull with a small label, HEAD orbit repeated | TVs tumble, repeats from earlier | outro |
| 57-58.5 | x-ray skeleton with "brain dead" written on the brain, a TV with static stripes | flicker to static | music fades out (AI) |

## Signature device
Lyric-synced labels in a duotone engraving collage. Every lyric line is set in a "label" (cream fill #afae7b,
black type, thin black rule) or in raw pixel/bitmap letters, often mixing 2-3 fonts in one line. Each line gets a
literal picture pun built from public-domain-looking engravings tinted to the same teal duotone: a TV for
"brain dead", a megaphone for "say it", a bottle for rum, fish for an open-sea line. Letters travel on paths
(orbiting a skull, wrapping a receiver), and backgrounds rotate between three motifs: perspective checkerboard,
radial sunburst, black void. A CRT/VHS layer (soft blur, vignette, slight colour bleed, grain) sits on top of
everything so mismatched sources read as one world.

## Pacing read
6.33 cuts per 10 s (a new layout every 1.5-1.6 s) and zero quiet share: no rests, the song carries the flow.
The 0.737 hook change comes from black to full type within 1.5 s. The CV of 0.0 only reflects the sampling
step; the real rhythm follows the syllables, with frame-filling single words on the stressed hits (19.5-27 s)
and slower orbit moves on the hook line (42-46 s). It ends on the most memorable visual pun and static,
no loop.

## Look
- Palette by role: near-black ground (#060706), teal shadows and mids (#1b2b23, #354c3d), olive grey
  (#6e7758) for engravings, pale cream (#afae7b) for labels and highlights. One duotone map applied to every
  source.
- Type: pixel bitmap caps, outlined pixel caps, a rounded retro sans, a blackletter-like script; 120-400 px on
  a 1920 wide frame, often cropped by the edge.
- Texture: CRT/VHS softness, grain, vignette. Camera: flat 2D, occasional fake perspective on the floor plane.

## Why it works
- A trending song plus "finals project" story: viewers who love the track save it (80,830 saves, very high
  for 2.2 M plays) and designers save it as reference.
- Every line has a visual joke, so rewatching reveals new puns.
- A strict 3-colour duotone makes 30+ different images feel like one film.

## Steal this (grammar) / Leave this (content)
- Steal: one label style for every line; a literal image pun per line; three rotating backgrounds; text on
  paths around a central object; a single duotone map plus CRT layer over all sources.
- Leave: the song and its lyrics, the creator's specific collages and compositions, the title card.

## Build it in our studio
- Engine: `hyperframes` (GSAP timeline keyed to word timings, text on SVG paths, registry VHS/CRT effect), with
  `collage` for the cut-out engravings; `canvas` for the duotone map if CSS filters fall short.
- Scene plan: 1) licensed or generated song, or a client voice line, with word timestamps (transcribe);
  2) one label component, 3 fonts max; 3) source public-domain engravings and tint them to one duotone;
  4) build 3 background motifs (checker floor, sunburst, void); 5) one pun per line; 6) CRT pass on top.
- Hard part: 30+ bespoke layouts per minute. Solve with a small layout kit (5 templates) and swap images.
- Difficulty 3; render about 16 min for 60 s in HyperFrames.

## Business translations
- Music venue or festival: the headliner's licensed track as a lyric teaser, each line an engraving pun about
  the venue.
- Restaurant or cocktail bar: a generated jingle naming real menu items, each item a duotone engraving with a
  label.
- Agency: the studio's manifesto read as a voice line and typeset word by word in this style as a showreel
  opener.
