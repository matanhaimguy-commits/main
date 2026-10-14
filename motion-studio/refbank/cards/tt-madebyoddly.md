---
id: tt-madebyoddly
title: "The logo's arrow becomes a subway train that rides a metro map of the order steps and builds the sandwich"
url: https://www.tiktok.com/@madebyoddly/video/7693389380097936661
platform: tiktok
creator: madebyoddly
plays: 1200000
likes: 233400
shares: 8557
saves: 22512
followers: 11000
posted: 2026-10-06
captured: 2026-10-14
duration_s: 35
category: logo-reveal
hook: [brand-name-drop, series-hook]
devices: [object-carries-camera, morph, map-zoom, shape-wipe, assembly-build, timeline-progression, series-episode]
energy: medium
palette: [brand-colour, saturated]
palette_hex: ["#fcfdfa", "#e6b80b", "#0b5125", "#109d39", "#c7a661"]
sound: [music-beat]
voiceover: false
text_on_screen: headline
engine: [canvas, hyperframes]
difficulty: 3
fit: [restaurant, saas, local-service, ecommerce, agency]
wow: 3
relevance: 5
pacing:                               # frames_metrics.py on a 1 fps sample
  cuts_per_10s: 3.71
  mean_s_between_big_changes: 1.3
  change_rhythm_cv: 0.35
  quiet_share_2fps: 0.029
  hook_change_0_2s: 0.104
---

## The film in one line
A sandwich chain's two-arrow logo comes apart, its green arrow becomes a segmented subway train that rides a
yellow metro line through six stations (Bread, Meat, Cheese, Veggies, Sauce, Wrap) where the sandwich is built,
and the wrapped train drives back and folds itself into the logo.

## Why it stops the scroll (first 2 s)
- 0.0 s: the logo centred on white, series caption below: "makings ads for brand that didn't ask [emoji] pt.6"
  plus the brand handle.
- 1.0 s: the green arrow splits into train cars with white windows, already moving.
- 2.0 s: the train pulls onto a yellow track; the empty arrow stays as a dashed ghost outline.
- Mechanism: brand-name drop and series promise, then an instant visual pun on the brand name, understood in 1 s.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-2 | logo on white, series caption | arrow segments into a train and drives off | not described (original sound, music assumed) |
| 3-5 | full metro map, one loop, six labelled stations; then close on the Bread stop with a black pill "NEXT STOP BREAD" and 6 dots | pull back, then zoom in on the train | |
| 6-9 | circle wipe to a yellow "NOW AT BREAD" card, giant outline word at the bottom; a bar becomes a scored loaf, a ruler counts to "12 INCHES" | texture appears, counter ticks; cars are now bread | |
| 10-17 | dark green "MEAT" (slices dealt onto the open loaf), bright green "CHEESE" (triangles layered) | wipes in and out between map rides | |
| 18-25 | yellow "VEGGIES" (toppings pop on), dark green "SAUCE" (zigzag drizzle) | cars change to show each new layer | |
| 26-28 | green "WRAP": striped paper wraps the cars, a logo sticker lands | wrap slides over | |
| 29-34 | train rides backwards, lines retract, cars curl back into the arrow, full logo with wordmark | reverse ride, rebuild, 2 s hold | |

## Signature device
The brand's own mark becomes the vehicle that carries the camera through the brand's process. The arrow is cut
into 5-6 rounded cars with window cut-outs plus the arrowhead as locomotive; cars follow a thick polyline track
with rounded 90-degree corners, each trailing the one ahead on the same path. At each station a circle wipe
centred on the train opens a full-bleed card in a brand colour: black transit pill on top ("NOW AT ...", one dot
fills per stop), station name as a giant outline word in the bottom third, the product assembled flat in the
middle. The ending reverses the ride and rebuilds the logo.

## Pacing read
At a 1 fps sample: 3.71 cuts per 10 s (the wipes), a big change every 1.3 s, even rhythm (CV 0.35), almost no
rests (quiet share 0.03). Shots last up to 7 s because cards and rides are continuous moves. Each station takes
4-5 s (arrive, build, depart), a cadence learned by the second stop, with the dots as a visible countdown. Last
frame equals the first, so it loops.

## Look
Brand white (#fcfdfa), yellow (#e6b80b), dark green (#0b5125), bright green (#109d39), bread tan (#c7a661); card
colours alternate per station. Heavy geometric caps for labels (about 40 px), giant outline station words (about
180 px). Flat vector; the camera pans and zooms on the map and cuts only through circle wipes.

## Why it works
The pun lands in one second and pays off six times. Each station is a small reveal with a predictable rhythm and
a progress bar. The build follows the real ordering steps, so it is relatable. The reverse ride closes the loop,
and the series framing ("which brand should i do next?") pulls comments naming the next brand.

## Steal this (grammar) / Leave this (content)
- Steal: the client's logo shape as a vehicle; a transit map as a process diagram; circle wipes into one colour
  card per step; progress pill with dots; giant outline step word; reverse ride back into the logo.
- Leave: the sandwich brand's logo, colours, wordmark, the subway pun, their food drawings and caption.

## Build it in our studio
Engine: canvas (path-following chain), HyperFrames possible with a motion path.
1. Vectorise the client's real logo (tools/vectorize_mark.py) and split one element into cars.
2. Route as a rounded polyline; place car i at arc length d minus i times spacing, rotated to the tangent.
3. Station cards: spring-driven circle-wipe radius, pill on top, outline word, step graphic built in 2-3 s.
4. Return ride in reverse, then interpolate car positions into the logo shape over 0.6 s.
5. Generated beat with an arrival chime and wipe whooshes placed from composition events.
- Hard part: smooth cornering and an exact morph back into the mark; arc-length sampling solves both.

## Business translations
- Bakery: the logo becomes a delivery scooter riding "order, bake, box, deliver", one card per step.
- SaaS onboarding: the logo mark rides through "sign up, connect, import, launch", each card showing the real
  screen.
- Moving or cleaning service: the van in the logo drives the four steps of a job and parks back as the logo.
