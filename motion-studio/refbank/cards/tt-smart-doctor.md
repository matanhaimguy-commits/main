---
id: tt-smart-doctor
title: "A realistic 3D heart turns glassy, tips to show its four valves snapping open and shut on the heartbeat, then closes up and loops"
url: https://www.tiktok.com/@smart.doctor/video/7499573973697580295
platform: tiktok
creator: smart.doctor
plays: 61100000
likes: 4500000
shares: 262200
saves: 372975
followers: 3000000
posted: 2025-05-01
captured: 2026-10-14
duration_s: 15
category: explainer-3d
hook: [beautiful-first-frame, sound-hook]
devices: [x-ray-cutaway, orbit, top-down-plan, beat-sync-hits, seamless-loop]
energy: medium
palette: [dark, natural]
palette_hex: ["#000003", "#af7e79", "#7e5d67", "#5e343a", "#8a4a49"]
sound: [asmr-foley]
voiceover: false
text_on_screen: none
engine: [hyperframes, gen-3d, canvas]
difficulty: 4
fit: [health, education, ecommerce, b2b]
wow: 4
relevance: 4
pacing:
  cuts_per_10s: 5.33
  mean_s_between_big_changes: 0.5
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.331
---

## The film in one line
A photoreal human heart floating on black turns from its front view, its outer wall goes translucent, the
camera tips over the top so the atria are cut away and the four valves are seen from above opening and closing in
time with a "boom boom" heartbeat, then the heart rolls back, the camera skims its surface past the coronary
vessels and returns to the opening front view so the film loops.

## Why it stops the scroll (first 2 s)
- 0.0 s: a full-frame realistic heart, front view, pink-grey muscle with bright red arteries and blue veins,
  filling about 90% of the width on pure black.
- 0.5 s: it turns slightly; the great vessels appear at the top.
- 1.0 s: the muscle becomes semi-transparent (x-ray look) and the camera starts tipping over the top.
- 2.0 s: top-down view of the valve plane: a pale aortic ring at top centre and two large valve openings below,
  a small "Smart Doctor" wordmark fades in top left.
- Mechanism: a body part everyone has and nobody has seen, shown in a quality that looks like a medical
  film, plus the heartbeat sound from frame one. The transcript reads only "boom boom", which is the heartbeat
  itself: there is no spoken voiceover and no on-screen hook text. The caption does the framing: "See the Heart
  Valves".

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | heart, front (anterior) view, full frame | slow turn | heartbeat "boom boom" |
| 1.0-1.5 | muscle turns translucent, internal structure visible | camera starts tilting over the top | heartbeat |
| 2.0 | top-down plan of the valve plane, atria removed; wordmark in | tilt completes | heartbeat |
| 2.5-8.0 | valves close (2.5 s), open (3.0 s), close and open again about once per second; the aortic ring flexes | leaflets snap, the whole base pulses slightly | heartbeat, each thump on a valve snap |
| 8.0-8.5 | camera rolls off the top view, aortic root now upper left, one valve visible | orbit back toward the side | heartbeat |
| 9.0-11.0 | heart in three-quarter side view on a faint blue perspective dot-grid floor | slow orbit around the heart | heartbeat |
| 11.5-13.5 | macro push-in skimming the surface: coronary arteries and veins fill the frame; copyright notice bottom right | fast dolly in and across | heartbeat |
| 14.0-15.0 | pull back to the exact opening front view | dolly out, settles | heartbeat, loop |

## Signature device
The cutaway orbit synced to the heartbeat. One continuous camera move (no hard cuts visible) does three jobs:
it shows the object whole, then strips it (outer wall to about 40% opacity, then the top layer removed) as the
camera tips 90 degrees to a top-down plan, then holds that plan view for about six seconds while the inner parts
move in exact sync with the sound: each heartbeat thump lands on a valve snap, roughly 60 beats a minute. After
the hold the camera rolls back to a three-quarter view, does one fast macro skim across the surface detail, and
lands on the first frame's framing so the cut back to frame one is invisible.

## Pacing read
Every sampled pair is a big change (one every 0.5 s, CV 0.0) and nothing is ever quiet: the heart never stops
moving. The 5.33 "cuts" per 10 s are not edits; the object fills most of the frame, so fast rotations and the
macro push-in at 11.5-13.5 s cross the hard-cut threshold. Read by eye it is one take in four phases: turn (2 s),
valve hold (6 s, the longest and calmest phase, with motion only inside the valves), orbit (3 s), macro skim and
return (3 s). Energy peaks at the macro push-in, then resolves into the loop.

## Look
- Palette by role: pure black ground (#000003) with a faint blue perspective dot grid; muscle in dusty pinks and
  mauves (#af7e79, #7e5d67, #8a4a49); deep red shadows (#5e343a); arteries saturated red, veins mid blue; valve
  tissue cream.
- Type: almost none. A small serif small-caps "Smart Doctor" wordmark top left (about 20 px on 1080) and a
  tiny copyright block bottom right late in the film.
- Material: subsurface-scattered wet tissue, glossy specular highlights, translucent shader for the x-ray phase.
- Light: soft key from the top left, rim light separating the heart from black.
- Camera: orbit and tilt around a fixed object, ending on a macro dolly.

## Why it works
- Curiosity about your own body: an organ everyone has, seen in a way nobody has.
- The heartbeat sound makes the motion feel alive and gives a rhythm without music.
- The six-second valve hold is the payoff and is long enough to study, which drives saves (373 k).
- The perfect loop: start and end frames match, so people watch it twice before noticing.
- Share trigger: "did you know your heart does this" with friends, students and patients.

## Steal this (grammar) / Leave this (content)
- Steal: one hero object on black; a single continuous move that turns it, makes its shell translucent, tips to a
  plan view and holds while inner parts work on a beat; a sound that is the object's own rhythm; a macro skim
  and a return to frame one for the loop; no text needed.
- Leave: their heart model, renders and wordmark, the medical content as filmed, the copyright notice.

## Build it in our studio
- Engine: HyperFrames with the Three.js adapter rendering a licensed or client-supplied GLB (software WebGL is
  slow but fine for one mesh), or `gen-3d` (paid, approval) to make a mesh from a product photo. Photoreal
  organic tissue like this needs a proper 3D asset; we cannot paint it in 2D convincingly.
- Stylised route: canvas engine, layered illustration of the object (outer shell, inner parts) with
  fake-3D projection for the tilt; the shell fades to 40% and slides away, the inner parts move on the beat.
- Scene plan: 1) source the model (client CAD, licensed anatomy, or gen-3d); 2) keyframe one camera path:
  front, tilt to top-down, hold, three-quarter orbit, macro skim, back to front; 3) material swap to translucent
  at 1.0 s; 4) animate the inner part on a 1 s beat; 5) heartbeat or mechanical foley placed on each motion
  event; 6) match the last frame to the first.
- Hard part: realistic material and a model that opens. Without a cutaway-ready model, choose the stylised
  route. Difficulty 4 for photoreal, 2-3 for stylised.

## Business translations
- Dental clinic: a tooth turns glassy, the camera tips to look down into it, and the root canal and nerve pulse
  on a heartbeat-like throb; loops back to the clean tooth.
- Appliance brand: the client's coffee machine shell turns translucent, the camera looks down into the brew
  chamber while valves and pumps cycle on a click track.
- Physiotherapy practice: a knee joint orbit, skin fades out, top-down view of the joint bending on each step
  sound.
