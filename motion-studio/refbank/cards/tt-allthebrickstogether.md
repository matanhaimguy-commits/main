---
id: tt-allthebrickstogether
title: "A brick Eiffel Tower builds itself on a table while the camera climbs it in one move"
url: https://www.tiktok.com/@allthebrickstogether/video/7172493688793271558
platform: tiktok
creator: allthebrickstogether
plays: 21400000
likes: 2600000
shares: 80500
saves: 180966
followers: 184500
posted: 2022-12-02
captured: 2026-10-14
duration_s: 40
category: product-motion
hook: [wait-for-it, mid-action-start]
devices: [assembly-build, one-take-camera, lego-bricks, top-down-plan, trending-audio]
energy: medium
palette: [natural, mono]
palette_hex: ["#786452", "#564b43", "#867e75", "#3e2923", "#a49d8b"]
sound: [trending-audio]
voiceover: false
text_on_screen: headline
engine: [canvas, hyperframes, blender]
difficulty: 4
fit: [ecommerce, real-estate, agency, events]
wow: 4
relevance: 4
pacing:
  cuts_per_10s: 0.25
  mean_s_between_big_changes: 1.03
  change_rhythm_cv: 0.15
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.595
---

## The film in one line
On a carved round table in an old ballroom, a stream of grey bricks flies in and snaps together into a large
brick Eiffel Tower, from the green baseplate and trees to the spire, while the camera rises with it in one
move and ends looking straight down as a tiny flag drops on top.

## Why it stops the scroll (first 2 s)
- 0.0 s: macro, low angle, very shallow focus: a pale green and beige baseplate fills the lower frame; a few
  white and red bricks sit in a small notch in the middle; a blurred antique room behind.
- 1.0 s: tan tiles flip and click into place across the plate; still no hint of what is being built.
- 2.0 s: dozens of small trees rain in from the top right and plant themselves; the camera starts to pull
  back.
- Mechanism: something is being built by itself and the viewer does not know what; "what is it going to be?"
  carries the first 10 s until the four arched legs appear.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-2.0 | baseplate macro, first bricks | tiles click in | dramatic French chanson opens (per AI) |
| 2.0-5.0 | trees and paths land; camera pulls back to show the plate on a round carved table | stream of green pieces from top right | song |
| 5.0-9.0 | four leg bases and the first lattice columns rise at the corners | grey stream arcs in, columns grow | song |
| 9.0-12.0 | the four legs meet in the great arches over the garden | arches close piece by piece | song |
| 12.0-16.0 | first deck builds; camera rises past it, room's blue door and red chairs pass behind | crane up | song |
| 16.0-24.0 | second section: four lattice pillars converge | crane up, slight orbit | song |
| 24.0-32.0 | upper spire narrows and climbs; background turns to wooden floor as the camera tilts down onto it | stream continues from upper right | song builds |
| 32.0-36.0 | top platform and antenna finish; camera is now almost top-down | last pieces | song peak |
| 36.0-40.0 | top-down view of the finished tower on the table; "Eiffel" then "Tower" appear top left, credit at the bottom; a small brick flag drops onto the tip | title word by word, flag drop | song fades |

## Signature device
Self-assembly in true build order with a camera that climbs alongside it. Pieces never pop on: they fly in a
continuous stream from one consistent off-frame source (top right), each on a short arc, and snap into place
from the bottom up, so the structure always grows from what is already there. The camera starts as a macro on
the first piece, pulls back to establish the table at about 5 s, then cranes up the tower at the speed of the
build, keeping the growing edge at about two thirds frame height, and finishes in a top-down plan view when
the last piece lands. A real, slightly shabby room (patterned wallpaper, red theatre chairs, worn floorboards)
grounds it as an object on a table. The name only appears after the build is complete.

## Pacing read
The metrics read 9.25 cuts per 10 s and a big change every 1.03 s, but this is one continuous camera move:
the constant crane and dense flying pieces change every frame by a lot, which the cut detector counts as cuts.
The very low CV (0.15) and zero quiet share confirm a perfectly even flow with no rests; tension comes from the
height of the build, not from rhythm changes. The only stop is the final 3 s top-down hold with the title and
flag drop, a clear end that does not loop.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 1 cuts in 40.0 s sampled (0.25 per 10 s), at 20.0 s; 37 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette by role: warm wood browns of the table and floor (#786452, #564b43, #3e2923) as ground, tower grey
  (#867e75, #a49d8b) as the hero, green garden as the only saturated colour until the red, white and blue flag.
- Type: only at the end; white heavy sans with soft shadow, about 110 px, top left, two lines; small credit
  line bottom centre.
- Texture and light: plastic bricks with soft specular highlights, warm interior daylight, very shallow depth
  of field in the macro start.
- Camera: one take; macro, pull back, crane up, tilt down to top-down plan.

## Why it works
- Curiosity: the identity of the build is withheld for about 10 s, then the arches make it instantly
  recognisable.
- Satisfaction: thousands of pieces finding their place, a familiar feeling for anyone who has built a kit.
- The camera keeps rising, so there is always more to see; the song's swell matches the climb.
- Save trigger for fans of the set (181 k saves); breakout about 116 x followers with 2.6 M likes.

## Steal this (grammar) / Leave this (content)
- Steal: build in true order from one off-frame source; macro start on the first piece; camera that rises at
  the build's pace; real everyday location as the stage; withhold the product name until the end; a small
  final "cherry on top" piece.
- Leave: the LEGO set and its design, the Eiffel Tower model, the room, the song, the title and credit lines.

## Build it in our studio
- Engine: photoreal brick physics needs `blender` (not in our stack) or a paid `gen-video` test; in our stack
  we do a stylised version in `canvas` (fake-3D isometric pieces with projection math and closed-form arcs) or
  `hyperframes` (SVG parts of the client's real product flying into place).
- Scene plan: 1) break the client's product or building into 40-200 real parts in build order; 2) each part
  flies from one corner on a parabola with a spring settle; 3) a virtual camera follows the growing edge
  (translate and scale), ending top-down or front-on; 4) final name and one small finishing piece.
- Hard part: hundreds of parts with readable order. Group parts into 8-12 build stages, stagger within each
  stage, and use seeded offsets so the stream looks organic.
- Difficulty 4 for anything close to the reference; 3 for a flat or isometric re-imagining.

## Business translations
- Property developer: the client's real floor plans extrude and stack into the building, floor by floor,
  ending on the finished elevation with the project name.
- Furniture e-commerce: a flat-pack wardrobe assembles itself from its real parts on a bedroom floor, ending
  top-down with the product name.
- Event agency: an exhibition stand builds itself on an empty hall floor, panel by panel, ending on the
  client's logo wall.
