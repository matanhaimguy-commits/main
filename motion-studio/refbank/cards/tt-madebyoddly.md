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
A sandwich chain's two-arrow logo comes apart, its green arrow turns into a segmented subway train that rides a
yellow metro line through six stations (Bread, Meat, Cheese, Veggies, Sauce, Wrap), each stop building the
sandwich on a full-colour station card, and the wrapped train then drives back and folds itself into the logo.

## Why it stops the scroll (first 2 s)
- 0.0 s: the familiar logo, centred on white, with the series caption below: "makings ads for brand that
  didn't ask [emoji] pt.6" and the brand handle.
- 1.0 s: the green arrow splits into train cars with little white windows; it is already moving.
- 2.0 s: the train pulls out of the logo onto a yellow track; the empty arrow stays as a dashed ghost outline.
- Mechanism: brand-name drop plus series promise ("pt.6", unsolicited ad), then an instant visual pun on the
  brand name. The pun is the hook: the viewer gets it by 1 s and wants to see where the train goes.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-2 | logo on white, series caption | green arrow segments into a train and drives off the logo | not described (original sound; music assumed) |
| 3-4 | full metro map: one loop with six labelled stations, ghost logo in the middle | camera pulls back to show the route; train heads for Bread | |
| 5 | close on the train at the Bread stop, black transit pill "NEXT STOP BREAD" with 6 progress dots | train arrives, map zooms in | |
| 6-9 | circle wipe to yellow "NOW AT BREAD" card, giant outline word at bottom; a pale bar becomes a scored loaf, a ruler measures it, "12 INCHES" counts up | loaf texture appears, counter ticks, circle wipe back out; train cars are now bread | |
| 10-13 | dark green "NOW AT MEAT": loaf opens into two halves, round slices slide on in a row | slices dealt one by one | |
| 14 | "NEXT STOP CHEESE", train runs down a vertical line | track follow | |
| 15-17 | bright green "CHEESE": sandwich now vertical, triangle cheese slices layered | slices drop in | |
| 18-21 | yellow "VEGGIES": cucumber, olives, tomato, onion placed; back on the map the cars now show red and green dots | toppings pop on | |
| 22-25 | "SAUCE": dark green card, zigzag sauce drizzle across the fillings; train turns a corner | drizzle draws on | |
| 26-28 | green "WRAP": cars wrapped in green and white striped paper, a small logo sticker lands | wrap slides over | |
| 29-32 | map again: train runs backwards, lines retract | reverse ride, map unbuilds | |
| 33-34 | train curls back into the green arrow, yellow line shrinks into the yellow arrow, full logo with wordmark | rebuild and hold | |

## Signature device
The brand's own mark becomes the vehicle that carries the camera through the brand's process. Geometry: the
logo's arrow is cut into 5-6 rounded rectangular cars with window cut-outs plus the arrowhead as the locomotive;
the cars follow a thick polyline track with rounded 90-degree corners, each car trailing the one ahead along the
same path (path-following chain). The track is a single loop drawn like a transit map, stations as white
circles with bold caps labels. At each station a circle wipe (centred on the train) opens a full-bleed colour
card in a brand colour, with a black transit pill at the top ("NOW AT ...", progress dots filling one per stop)
and the station name as a giant outline word in the bottom third. The product is assembled flat on that card,
and the train cars change to show the new layer when the wipe closes. The ending reverses the ride and rebuilds
the logo, closing the loop exactly where it started.

## Pacing read
At a 1 fps sample, 3.71 cuts per 10 s (the circle wipes) and a big change every 1.3 s with an even rhythm (CV
0.35). Almost no rests (quiet share 0.03). Shots run up to 7 s because the station cards and map rides are
continuous moves rather than cuts. Each station takes about 4-5 s: arrival (1 s), card (2-3 s), departure
(1 s), a regular cadence the viewer learns by the second stop. The progress dots give a visible countdown.
It ends on a 2 s logo hold, and since the last frame equals the first, it loops cleanly.

## Look
- Palette: brand white (#fcfdfa), brand yellow (#e6b80b), dark green (#0b5125), bright green (#109d39), bread
  tan (#c7a661). Card backgrounds alternate between the brand colours, one per station.
- Type: heavy geometric sans in caps for station labels (about 40 px on the map, 1080 frame); station name as a
  giant outline word (about 180 px, 2 px stroke in a tint of the background); transit pill text small and bold.
- Texture: flat vector, no gradients except soft motion blur and a few blurred circle edges during wipes.
- Camera: 2D pan and zoom across the map, locked to the train; cuts happen only through circle wipes.

## Why it works
The pun lands in one second and then pays off six times; each station is a small reveal with a predictable
rhythm and a visible progress bar, so viewers stay to see the full set. The sandwich is built in the order a
customer orders it, which is instantly relatable. The reverse ride and logo rebuild close the loop and reward
watching to the end. The series framing ("pt.6", "which brand should I do next?") asks for comments naming the
next brand, which is the comment trigger.

## Steal this (grammar) / Leave this (content)
- Steal: turning a client's own logo shape into a vehicle or character; a transit-map route as a process
  diagram; circle wipes into one full-colour card per step; a progress pill with dots; outline giant step word;
  reverse ride back into the logo as the ending.
- Leave: the sandwich brand's logo, colours, wordmark and the subway-name pun; their food illustrations; the
  series caption wording.

## Build it in our studio
Engine: canvas engine (preferred for the path-following chain), HyperFrames possible with a motion path.
1. Vectorise the client's real logo (tools/vectorize_mark.py) and split one element into cars along a path.
2. Build the route as a polyline with rounded corners; compute arc-length positions so each car sits at
   distance d minus i times spacing, rotated to the path tangent.
3. Station cards: circle wipe (clip radius on a spring) to a full-bleed colour card, pill at top, outline word
   at bottom, step graphic in the middle built in 2-3 s.
4. Return ride: play the path in reverse and morph the cars back into the logo element.
5. Sound: generated beat with a chime at each arrival and a whoosh on each wipe, timed from the composition's
   events.
- Hard part: cars bending smoothly around corners and morphing back into the exact logo shape. Solve with
  arc-length sampling and a final interpolation from car positions to the logo's segment positions over 0.6 s.
- Difficulty 3; render cost low (flat vector, 35 s at 60 fps).

## Business translations
- Restaurant or bakery: the logo becomes a delivery scooter that rides a map of "order, bake, box, deliver", one
  colour card per step.
- SaaS onboarding: the product's logo mark becomes a train through "sign up, connect, import, launch" stations,
  each card showing the real screen for that step.
- Local service (cleaning, moving): the van in the logo drives a route of the four steps of a job, ending back as
  the logo with the booking line.
