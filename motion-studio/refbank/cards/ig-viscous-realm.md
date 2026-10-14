---
id: ig-viscous-realm
title: "A candy bar built layer by layer, nougat, falling peanuts, a caramel wave and a chocolate sleeve, after a 7 s breakdown of the trick"
url: https://www.instagram.com/p/DAVxX8zPQJO/
platform: instagram
creator: viscous.realm
plays: 10331214
likes: 13505
shares: 49
saves: 0
followers: 0
posted: 2024-09-25
captured: 2026-10-14
duration_s: 13
category: product-motion
hook: [text-headline, brand-name-drop]
devices: [assembly-build, split-screen, cloth-sim, rigid-body-drop, liquid-sim]
energy: medium
palette: [dark, light]
palette_hex: ["#2e2d2c", "#010101", "#d5d3cf", "#efe8dd", "#897966"]
sound: [music-beat]
voiceover: false
text_on_screen: headline
engine: [canvas, gen-video]
difficulty: 4
fit: [ecommerce, restaurant, agency]
wow: 3
relevance: 4
pacing:
  cuts_per_10s: 0.74
  mean_s_between_big_changes: 1.35
  change_rhythm_cv: 1.42
  quiet_share_2fps: 0.115
  hook_change_0_2s: 0.046
---

## The film in one line
A Blender artist first shows, in a split screen, how a cloth simulation fakes the caramel pour, then cuts to the
finished render: on a white studio sweep a cream nougat slab unfolds, peanuts rain onto it, a glossy caramel wave
rolls over them from the right and a chocolate shell slides on from the left to finish a Snickers-style bar.

## Why it stops the scroll (first 2 s)
- 0.0 s: split screen. Top 55%: a dark Blender viewport, a flat teal sheet hovering over a blue-grey bar covered in
  lumps, white caption "I used a cloth sim to fake liquid hitting the surface exactly". Bottom 45%: orange
  headline "Making snickers in blender" over a node graph with a small render of the wrapped bar in the middle.
- 0.5 s: no change; the viewer reads.
- 1.0 s: the sheet has dropped and draped over every lump.
- 2.0 s: the draped sheet holds; the bottom half never moves.
- Mechanism: a curiosity gap built from a headline plus a trick claim ("fake liquid"). The bottom panel shows the
  promised result, the top panel shows ugly grey geometry, and the viewer stays to see how one becomes the other.
  Visual change is almost zero (0.046); the text does the hooking.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | split: viewport (flat sheet over lumpy bar) / headline and node graph | nothing yet | not described (no audio data in package) |
| 1.0-2.5 | sheet draped over the lumps | cloth drop already done, slight settle | not described |
| 3.0-4.0 | caption "Gave it some thickness", the drape now a thick slab on a base | solidify step, a scrub line passes | not described |
| 4.5-6.5 | caption "Faked liquid fall off using geometry nodes" | the coat retreats to a thin pour at the right end, then rolls back over as a wave | not described |
| 7.0-7.5 | hard cut to the render, letterboxed, cream nougat folded like a Z on a white sweep; orange "Full tutorial on my youtube" in the bottom bar | the nougat unfolds flat | not described |
| 8.0-9.0 | flat nougat, peanuts | peanuts rain from top right, bounce and pile, right half first | not described |
| 9.5-10.5 | glossy orange caramel | a caramel wave rolls in from the right and curls over the peanuts to the left end | not described |
| 11.0-12.0 | chocolate sheet | a brown shell slides on from the left like a sleeve over the caramel | not described |
| 12.5-13.0 | finished ridged chocolate bar, soft shadow | settle, small camera drift | not described |

## Signature device
Layered assembly where every layer has its own physical entrance. Four layers, about 1-1.5 s each, on a locked
three-quarter camera in a seamless white studio: 1) the base unfolds like a mat dropping flat; 2) small solids
rain from above, bounce and pile, landing on one end first; 3) a viscous layer rolls along the length as a wave
with a curled glossy lip (actually a cloth sheet with thickness, revealed along the bar by a moving mask); 4) a
shell slides on from the opposite end, so the directions alternate (down, down, right to left, left to right).
The film opens with the "how" in a split screen so the beauty pass plays as a payoff.

## Pacing read
One hard cut (0.74 per 10 s) splits it into two halves of about 7 and 6.5 s. The first half is slow: a big
change every few seconds, only the top panel moves, captions do the work. After the cut, changes come every
0.5-1 s as each layer arrives, which is why the CV is high (1.42): slow tutorial, then fast payoff. Quiet share
is low (0.115), the longest still stretch is 1 s. It ends on the finished bar with a small camera drift and no
logo or end card, so a replay jumps back to the tutorial panel.

## Look
- Palette by role: Blender charcoal (#2e2d2c) and black letterbox bars (#010101) frame everything; the render is
  warm off-white (#d5d3cf, #efe8dd) with product colours as the only saturation: nougat cream, caramel orange,
  chocolate brown (#897966 range).
- Type: heavy rounded sans; orange for the headline and the YouTube line, white for the step captions, about
  55-70 px on a 1080 frame.
- Light: soft overhead studio key, gentle contact shadows, glossy specular on the caramel.
- Camera: locked three-quarter view slightly above the bar.
- Sound: no audio data for this reference; the `music-beat` tag is a placeholder, check the original before relying on it.

## Why it works
- Two hooks stacked: the product everyone knows and a trick claim that makes 3D artists curious.
- Process then payoff: the grey geometry makes the final glossy caramel feel earned.
- Each layer is a mini event with a clear start and end, so the second half is a run of small rewards.
- Like rate is low (13.5 K likes on 10.3 M plays), so the plays likely come from replays and broad distribution
  rather than a fan base; follower count is not known.

## Steal this (grammar) / Leave this (content)
- Steal: build the product from its real components, one per beat, each with its own physics (unfold, rain, wave,
  sleeve); alternate entrance directions; a locked camera on a seamless sweep; optionally open with the
  "how it's made" panel and a promise image.
- Leave: the Snickers brand, name and wrapper, their render, their captions and the Blender viewport footage.

## Build it in our studio
- Engine: `canvas` as a stylised side-on build (2D layers with fake depth), or `gen-video` (paid, approval) for a
  photoreal pour.
- Scene plan: 1) side-on or three-quarter projection of the product as stacked extruded shapes; 2) base layer
  unfolds with a hinge rotation driven by `spring()`; 3) small solids as 2D rigid bodies (closed-form fall plus
  one bounce, seeded positions, pile height map); 4) the liquid layer as a thick path whose leading edge travels
  along the bar with a curled lip, glossy highlight stripe, masked reveal; 5) shell slides on with squash at the
  end; 6) end on the hero packshot (the client's real photo or 3D file) with the logo.
- Hard part: making the liquid read as liquid in 2D. Use a moving wave front with a curl, a hard specular
  highlight, and a slight overshoot and settle.
- Difficulty 4 for photoreal (needs 3D or paid video); 3 for a clean stylised version.

## Business translations
- Bakery or dessert shop: their real signature cake assembled live, sponge unfolds, berries rain, cream rolls on
  as a wave, glaze slides over, ending on a photo of the real cake.
- Snack or supplement e-commerce brand: the bar's actual ingredients from the label land one per beat, each
  named in a small caption, ending on the pack.
- Burger restaurant: the house burger built bottom up on a white sweep, each ingredient with its own entrance,
  ending on the menu name and price from the real menu.
