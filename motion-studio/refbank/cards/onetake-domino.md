---
id: onetake-domino
title: "Thousands of phones fall like dominoes and resolve, one phone per pixel, into a single picture"
url: references/onetake/cases/domino-25s/
platform: web
creator: onetake
plays: 0
likes: 0
shares: 0
saves: 0
followers: 0
posted: null
captured: 2026-10-14
duration_s: 25.6
category: product-motion
hook: [beautiful-first-frame, wait-for-it]
devices: [chain-reaction, grid-mosaic, rigid-body-drop, pov-camera, orbit, pull-back-reveal]
energy: high
palette: [light, mono]
palette_hex: ["#e9e9e7", "#131317", "#d1d2d2", "#2f4968", "#6b809e"]
sound: [asmr-foley, silence-moments]
voiceover: false
text_on_screen: none
engine: [canvas, gen-3d]
difficulty: 5
fit: [ecommerce, events, agency]
wow: 5
relevance: 3
pacing:
  cuts_per_10s: 11.37
  mean_s_between_big_changes: 0.52
  change_rhythm_cv: 0.19
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.182
---

## The film in one line
A single phone in a slow macro orbit tips over and starts a chain of falling phones that branches and floods ever larger grids, each grid's screens lighting as pixels of one picture (a smiling vintage-computer face), until the last phone standing shows the whole picture, winks and goes dark.

Craft reference, not a social post: a 16:9 film from the onetake repo in the style of a phone-review domino segment, built with a Blender model and instanced three.js. Study only (PolyForm Noncommercial): ideas in our words, no code, pixels or sound reused.

## Why it stops the scroll (first 2 s)
At 0.0-1.5 s a macro of a phone's back and camera bump on a pale grey sweep, orbiting slowly like a packshot; at 2.0 s the phone is mid-fall in slow motion, screen glowing blue; at about 2.6 s it lands on a 3 x 3 block. Mechanism: a premium product shot turns into a domino, a pattern everyone knows will escalate. The shipped file is silent for the first 1.5 s, so the first contact is the first sound.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-1.7 | one phone, macro | slow orbit | silence |
| 1.7-2.6 | the tip | slow-motion fall, screen lights | first contact |
| 2.6-6.9 | 3 x 3, then an S-line | block spreads; a run topples past a low moving camera | impacts, a dense click swarm |
| 6.9-8.6 | 10 x 10 struck | crane up; the picture becomes guessable | swarm |
| 7.8-12.2 | branching | first-person ride on the falling front, banking at splits; stepped pull-back | swarm |
| 12.6-13.7 | 32 x 32 fills, screens dark | lines lie down | building |
| 13.7 | the drop | 1,024 screens light at once; the picture appears | the big hit, shake |
| 13.7-21.4 | 100 x 100 field | chase, a circular front through 10,000 phones, a climbing reveal; the face winks | loudest stretch |
| 22.3-25.6 | the survivor | dive to the last upright phone; it winks, the screen goes black | sound cut dead, two lone hits |

Sound: cut to a licensed 140 BPM instrumental that is not shipped; the file carries foley and the film's own notes (case notes plus our loudness read: a steady -17 to -19 LUFS swarm, about -12 at the peak).

## Signature device
Product as pixel. Each unit is one pixel of a target image and the falling front is the scan that writes it. A resolution ladder (1, 3 x 3, 10 x 10, 32 x 32, 100 x 100) is the escalation. Each phone's fall time is its path distance divided by the front speed (a pure function of time), its angle easing in slowly and finishing fast like a real domino. Screens take the image colour at their grid position and light on the beat. The camera changes language per stage: orbit, crane, first-person ride, pull-back, climb, dive.

## Pacing read
2 fps: 11.37 "cuts" per 10 s (the camera never stops; no edits), big changes every 0.52 s, very even (CV 0.19), 0 % quiet. Full rate: 1 % still, 2 % quiet, longest quiet run 0.25 s (the only rest WARN in the onetake set), 12 beats, transitions at 4.0, 8.33, 12.17, 14.67, 17.33 and 22.67 s, beat CV 0.63, spread 6.8x. Continuous-motion genre: freezes on beats looked staged and were removed. Ends on a hard stop; no loop.

## Look
Light grey seamless studio (#e9e9e7, #d1d2d2), near-black fronts (#131317), titanium-blue backs (#2f4968, #6b809e), screens in blue, cream and black. No type. Shallow depth of field at the macro, shutter motion blur throughout.

## Why it works
- A familiar satisfying pattern with an obvious promise of escalation (1 to 10,000).
- An open question (what is the picture?) answered on the drop, then confirmed bigger.
- The wink is a character beat and a reason to finish.
- Share trigger: "how was this made".

## Steal this (grammar) / Leave this (content)
- Steal: product units as pixels; a resolution ladder as escalation; silence before first contact; one survivor as the ending; a camera that rides the front.
- Leave: the phone model, the vintage-computer face, the music, the review segment it echoes.

## Build it in our studio
As shot it needs real 3D instancing with a GPU; we have no Blender or GPU and HyperFrames WebGL runs in software, so 12,000 instances at 1080p is not practical: difficulty 5. Routes:
1. Stylised canvas re-imagining (about 4): fake-3D tiles with projected shadows toppling across a grid, each face a colour cell; draw only tiles in view, cache settled ones.
2. Paid, with approval: gen-3d for the hero product and gen-video for the macro opening, field done as in route 1.
Scene plan: client product close-up, the tip, branching lines, a dark field, the drop that lights the client's logo, the survivor. Hard part: thousands of tiles at 60 fps; precompute fall times.

9:16: run the chain toward camera or top to bottom; the survivor phone is natively vertical; keep the resolved logo in the middle band.

## Business translations
- E-commerce brand: product boxes fall in a chain, lids flipping to colour cells that resolve into the brand mark; the last box opens.
- Event or festival (events): tickets topple and resolve into the event's real date graphic; the last ticket shows the entry code.
- Design agency: business cards topple across a table into the agency monogram; the last card shows the contact line.
