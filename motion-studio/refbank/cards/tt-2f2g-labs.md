---
id: tt-2f2g-labs
title: "The same fuzzy robot arm whips a plastic test tube ten times as its softness climbs from 0% to 100%"
url: https://www.tiktok.com/@2f2g_labs/video/7679106030076316950
platform: tiktok
creator: 2f2g_labs
plays: 10500000
likes: 374000
shares: 103000
saves: 38579
followers: 125500
posted: 2026-08-28
captured: 2026-10-14
duration_s: 62
category: satisfying-sim
hook: [number-ladder, wait-for-it]
devices: [escalation-ladder, softbody, counter-ticker, cloth-sim, rigid-body-drop, series-episode]
energy: medium
palette: [pastel, mono]
palette_hex: ["#a18dd5", "#8476ba", "#9288f2", "#665e8c", "#beb4f5"]
sound: [asmr-foley]
voiceover: false
text_on_screen: headline
engine: [canvas, gen-video]
difficulty: 4
fit: [ecommerce, b2b, agency, health]
wow: 4
relevance: 3
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 1.7
  change_rhythm_cv: 0.3
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.077
---

## The film in one line
On a lavender hexagonal pedestal, a clamp catches a falling translucent test tube and a three-segment fuzzy
robot arm rises and whips it, ten rounds in a row, while a "SOFTNESS" readout steps from 0% to 100% and the
tube goes from flying off like a rigid stick to squashing, stretching, sheeting and finally shredding.

## Why it stops the scroll (first 2 s)
- 0.0 s: symmetrical, centred still life: lavender background, a hexagonal pedestal with gold edge trims and a
  mottled felt surface, a small dome, a four-armed gold-tipped clamp, and a clear lavender test tube hanging
  above it. Top centre: "SOFTNESS" in wide-tracked thin caps over "0%".
- 0.5-1.0 s: not sampled; the tube descends.
- 1.5 s: the tube has dropped into the clamp, tilted slightly.
- 2.0 s: the clamp is about to open (by 3.0 s the arms spread and the tube stands in a collar).
- Mechanism: the "0%" readout is a promise of 100%. The viewer knows the test will repeat with a softer tube
  and stays to see what 100% looks like. The opening is calm (hook change 0.077); the number does the work.

## Beat map
Frames cover 0-61.5 s of the 62 s film. One locked shot, no cuts.

| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-6.0 | 0%: tube drops into the clamp, clamp opens, segmented arm rises under it | tube drop, arms spread, arm extends | original audio, not described (likely machine foley) |
| 7.5-12.0 | 11%: tube flung off the top left like a stick; arm bends hard right | rigid projectile, arm whip | foley |
| 13.5-18.0 | 22%: tube flies off to the right; arm snaps upright | same choreography | foley |
| 19.5-24.0 | 33%: the tube's base squashes into a flat pad between the clamp arms; arm bends left | first visible deformation | foley |
| 25.5-30.0 | 44%: bigger pad, shards of the tube thrown to the right | squash and spread | foley |
| 31.5-36.0 | 55%: tube necks and stretches, then lies crumpled beside the pedestal | stretch, crumple | foley |
| 37.5-43.5 | 66%: tube twists, then becomes a membrane stretched between the clamp arms; the arm bends through it | sheet stretches like a trampoline | foley |
| 45.0-49.5 | 77%: tube collapses into a flat sheet, the arm pushes up and the sheet drapes over its tip | drape, wrap | foley |
| 51.0-55.5 | 88%: flat sheet, the arm tents it upward and spins with it | tenting | foley |
| 57.0-61.5 | 100%: the tube falls straight into a puddle-like sheet; the arm tears through and shreds fly off | tear, shreds | foley; film ends mid-round |

## Signature device
A parameter ladder on an unchanging test rig. Everything is fixed: camera (frontal, slightly low, centred),
rig, lighting and the roughly 6.2 s choreography of each round (drop, clamp, release, arm rise, arm whip).
Only one material value changes, shown as a readout in 11-point steps. The tube's behaviour walks across a
material spectrum: rigid body (0-22%) flies off whole; softbody (33-55%) squashes and necks; cloth (66-100%)
stretches, drapes and tears. The rig is designed for contrast: the arm is matte fuzzy felt with polished
chrome rings at each joint, the tube is glossy translucent plastic, so deformation reads clearly against the
felt.

## Pacing read
0 cuts, a big change every 1.7 s and a low CV of 0.3: a steady machine rhythm with no rests (quiet share 0.0).
The round length stays at about 6.2 s, so the beat never changes; escalation comes only from the material
result. Peak interest is at 66-77% where the tube first turns into a sheet. The film ends mid-action at 100%
with shreds in the air, which makes the loop back to the calm 0% frame feel like a reset.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 0 cuts in 63.0 s sampled (0.0 per 10 s); 0 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette: monochrome lavender family (#a18dd5, #8476ba, #9288f2, #665e8c, #beb4f5), gold trims and ball tips
  as the only warm accent, chrome rings as highlights, deep blue-violet where the tube sheet is thickest.
- Type: one HUD label, thin sans in wide-tracked caps, about 40 px, with a soft white glow, top centre, plus
  the percentage under it.
- Texture and light: felt and mottled stone shaders, soft key from the right, gentle gradient background,
  motion blur on the arm whips.
- Camera: locked, no moves.

## Why it works
- Number ladder: 0% demands 100%; every round pays off a little and raises the question for the next.
- Material surprise: viewers predict "it bends more", but the jump from rigid to sheet at 66% is unexpected.
- Rewatch: rounds are fast enough that people scrub back to compare levels; comment bait is "which % was best".
- Toy-like rig and pastel palette make a violent action feel harmless.

## Steal this (grammar) / Leave this (content)
- Steal: one rig, one action, one variable, visible readout in even steps, ten rounds, end on the extreme
  value mid-action; matte versus glossy material contrast.
- Leave: their rig design, test tube and felt arm, the exact lavender look, the "SOFTNESS" label wording.

## Build it in our studio
- Engine: `canvas` as a stylised 2D re-imagining (fake-3D cylinders for the arm, a 2D mass-spring softbody for
  the deforming object, rigid trajectories for low values); `gen-video` (paid, needs approval) only if a
  photoreal version is required.
- Scene plan: 1) one fixed rig drawn in projection, centred; 2) a choreography function of time per round,
  identical every round; 3) the object as a spring mesh whose stiffness and damping are the ladder variable;
  4) readout steps on each round start; 5) foley placed from event times (clamp click, whoosh, thud, tear).
- Hard part: believable soft and cloth behaviour that stays deterministic and seekable. Solve by baking the
  mesh simulation per round offline with a seeded solver and storing frames, then playing them back by time.
- Difficulty 4: the softbody and tearing are the hard parts.

## Business translations
- Mattress shop: the same weight dropped on a mattress cross-section ten times, firmness readout from 0 to 100,
  ending on the client's real model.
- Packaging supplier: one box crushed by the same press as wall thickness rises, ending on their standard
  grade holding.
- Running shoe retailer: the same foot strike on a midsole as cushioning rises, showing how the foam behaves
  at each level.
