---
id: tt-peanar3d
title: "Stop dragging your duck: a 37 s software fix told over the same locked hero shot"
url: https://www.tiktok.com/@peanar3d/video/7681986956443536658
platform: tiktok
creator: peanar3d
plays: 6000000
likes: 422400
shares: 5045
saves: 66656
followers: 63700
posted: 2026-09-05
captured: 2026-10-14
duration_s: 37
category: ui-saas
hook: [direct-address, beautiful-first-frame]
devices: [before-after, word-by-word, ui-card-stack, voiceover-explainer]
energy: medium
palette: [saturated, natural]
palette_hex: ["#123a3c", "#92a7d4", "#3d6a87", "#d2d8ee", "#e3b9b7"]
sound: [voiceover]
voiceover: true
text_on_screen: captions
engine: [footage, hyperframes]
difficulty: 2
fit: [saas, education, b2b, agency]
wow: 3
relevance: 4
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 1.48
  change_rhythm_cv: 0.69
  quiet_share_2fps: 0.056
  hook_change_0_2s: 0.432
---

## The film in one line
A glossy rubber duck sits on a sunset ocean inside a 3D app; the narrator mocks animating it by hand, then
speed-reads eight shortcut steps while menus pop up under the duck, and the last two seconds show the duck
bobbing on the waves by itself.

## Why it stops the scroll (first 2 s)
- 0.0 s: a big orange rubber duck, centre frame at about 40% height, on teal water under a pink and
  periwinkle sunset sky. Only a thin strip of app interface at the very top hints that this is software.
- 0.5-1.0 s: the duck jerks up and the app's move readout appears in the header; caption "Dragging".
- 2.0 s: the duck tilts and dips, caption "And Down": the "wrong way" is being performed live.
- Opening line (verbatim): "Stop dragging your duck up and down to match the waves like this."
- Mechanism: a pretty, odd first frame (a bath duck at sea), then a command that names a pain a whole niche
  recognises. The cost line at 4-6 s ("That's three hours for six seconds") makes the promise concrete.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-4.0 | duck on ocean, move readout in the header | duck dragged up, down, rotated by hand | VO "Stop dragging your duck up and down to match the waves like this." |
| 4.0-6.0 | same | more manual jiggling | VO "That's three hours for six seconds." |
| 6.0-9.0 | a white square plane appears under the duck | plane added | VO "Instead, add a plane and press Tab to edit." |
| 9.0-16.0 | plane gets denser grid lines; captions "Select", "Subdivide", "Shift R" | grid subdivides in steps | VO "Hit A to select everything, right-click, Subdivide. Then Shift+R a few times until it's dense enough." |
| 16.0-20.0 | vertex group panel, then modifier menu floating in the lower third; plane turns into a wavy patterned sheet | panels pop in and out | VO "Assign it all to a new vertex group. Tab out and give it a Shrinkwrap modifier. Choose the ocean as the target." |
| 20.0-29.0 | constraint menus pop up under the duck: Copy Location, target fields | panel swaps | VO "Now select your duck and add a Copy Location. Set the plane as its target, then the vertex group you just made, so the duck copies whatever that point does. Do the same with a Copy Rotation." |
| 29.0-33.0 | the duck spins and shows its back, then faces front again with the Z axis unticked | gag turn | VO "Then turn off the Z rotation or your duck will turn its back to the camera." |
| 33.0-35.0 | plane disappears | hide | VO "Finally, hide the plane and hit Play." |
| 35.0-37.0 | clean low shot, duck bobbing and tilting with the swell, no captions, no interface | the payoff motion | VO "You never have to touch your duck again." |

## Signature device
Locked hero shot as the tutorial's stage. The finished scene (subject centred, horizon at about 27% height,
warm sky, rich water) never leaves the frame; every step happens on top of it. Software panels are cropped
from the app and float in the lower third (about 60% of frame width) for 1-2 s, then vanish; the subject's
state changes in place (a helper sheet under it gets denser, then turns wavy). Captions are single words or
pairs, white heavy sans with a soft dark shadow, centred just below the subject at about 60% height, so the
eye never leaves the duck. The real result is withheld until the last 2 s, which switch to a clean, lower
camera angle with no interface at all.

## Pacing read
A big change every 1.48 s and almost no rest (quiet share 0.056): captions change on every word and panels
pop roughly every 2-3 s. Cuts are low (1.89 per 10 s) because the background never changes. Hook change 0.432
in 0-2 s comes from the manual dragging, deliberately busy and wrong. CV 0.69: the steps section is steady, the
gag at 30 s breaks the rhythm, and the ending slows to one uncut 2 s shot that loops back to the jerky
opening, a clean before and after on rewatch.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 0 cuts in 37.0 s sampled (0.0 per 10 s); 7 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette by role: deep teal water (#123a3c, #3d6a87) as the ground, periwinkle and pale sky (#92a7d4,
  #d2d8ee), sunset pink (#e3b9b7) on the horizon, duck orange (#c2631f) and red beak as the only warm hero.
- Type: captions in a rounded heavy sans, about 70 px, white with a soft shadow; app UI at native size.
- Texture and light: glossy subsurface plastic, low sun reflections streaking the water, realistic ocean
  displacement.
- Camera: static three-quarter view slightly above the water; final shot lower and closer.

## Why it works
- Problem first, cost in numbers ("three hours for six seconds"), then the fix: the classic tip-video arc.
- The result is visible all the time but never in motion until the end: a built-in open loop.
- The Z-rotation gag gives a laugh in the middle of dry steps.
- Saves at 16% of likes: viewers keep it as a recipe.

## Steal this (grammar) / Leave this (content)
- Steal: "Stop doing X like this" over a live demo of the wrong way; quantify the waste; one locked hero
  frame for the whole tutorial; floating cropped panels in the lower third; one-word captions under the
  subject; a mid-tutorial gag; final shot that drops the interface and just shows the result.
- Leave: the duck, the ocean scene, their app's menus and wording, their voice.

## Build it in our studio
- Engine: `footage` (screen recordings of the client's own software and its real output) assembled in
  `hyperframes` with GSAP pop-ins for cropped panels and word captions from VO timestamps.
- Scene plan: 1) pick one satisfying end result the product makes and frame it as the hero; 2) record the
  wrong way (manual, slow) for 4 s; 3) record each step and crop only the relevant panel; 4) composite panels
  over the hero frame, one at a time, with word captions; 5) end on 2 s of the clean result.
- Hard part: keeping the hero frame stable while the real UI changes. Record the result render separately and
  use it as the fixed background; panels are overlays, not the full screen.
- Difficulty 2. No 3D needed if the client's product supplies the result.

## Business translations
- Spreadsheet or bookkeeping SaaS: "Stop retyping invoices into your sheet like this", then four steps in the
  real product, ending on the sheet filling itself.
- Photo-editing app: "Stop masking hair by hand", the portrait stays centred while tool panels pop in, ending
  on the clean cut-out.
- Scheduling tool for salons: "Stop texting every client a reminder", the calendar stays on screen, ending on
  reminders going out by themselves.
