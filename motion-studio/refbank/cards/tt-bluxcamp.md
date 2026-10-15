---
id: tt-bluxcamp
title: "A cloth drops on a green glass ring at 16 k, 65 k, 262 k and 1 M faces, and at 4 M faces the software freezes and crashes"
url: https://www.tiktok.com/@bluxcamp/video/7423782880058297618
platform: tiktok
creator: bluxcamp
plays: 45000000
likes: 3600000
shares: 71800
saves: 226285
followers: 38300
posted: 2024-10-09
captured: 2026-10-14
duration_s: 19
category: satisfying-sim
hook: [number-ladder, wait-for-it]
devices: [escalation-ladder, cloth-sim, big-number, series-episode]
energy: medium
palette: [dark, mono]
palette_hex: ["#2d2924", "#272520", "#35332e", "#abaca7", "#696a64"]
sound: [asmr-foley]
voiceover: false
text_on_screen: headline
engine: [canvas, gen-video, blender]
difficulty: 4
fit: [saas, b2b, ecommerce, agency]
wow: 4
relevance: 3
pacing:
  cuts_per_10s: 0.53
  mean_s_between_big_changes: 1.46
  change_rhythm_cv: 0.66
  quiet_share_2fps: 0.054
  hook_change_0_2s: 0.094
---

## The film in one line
The same shot repeats five times: a flat white sheet hangs above a glossy green glass torus on a dark backdrop,
a big counter says how many faces the sheet has (16,384, then 65,536, 262,144, 1,048,576), the sheet drops and
drapes with finer folds each time, and at 4,194,304 faces nothing falls: the window greys out and a crash dialog
appears.

## Why it stops the scroll (first 2 s)
- 0.0 s: bold italic white "16,384 FACES" across the upper third; a flat matte plane hovering just above a
  shiny green glass ring, both centred in the lower half of a dark warm-charcoal frame; small "@bluxcamp"
  watermark under them.
- 0.5 s: unchanged; the plane hangs.
- 1.0 s: the sheet has dropped and wrapped the ring; the ring disappears under white cloth with a soft dimple
  in the middle.
- 2.0 s: the cloth settles, corners hanging in coarse, angular folds.
- Mechanism: a number on screen promises a ladder ("16 k faces... what happens with more?"), and the drop pays
  off at once so the viewer learns the rules in one second. The caption's "16k to 4m" tells them there is a
  finale to wait for.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | "16,384 FACES", sheet above glass torus | hold | swoosh building (AI) |
| 1.0-3.5 | sheet drops, drapes, settles into coarse folds | cloth falls, corners swing, settles | swoosh |
| 4.0 | reset: "65,536 FACES", sheet back up | cut to the same start frame | |
| 4.5-7.0 | drop and drape, smoother folds, more hanging edge | cloth falls and settles | swoosh |
| 7.5 | reset: "262,144 FACES" | cut | |
| 8.0-10.5 | drop: four corners hang first like legs, then fine folds | cloth falls and settles | swoosh |
| 11.0-12.0 | reset: "1,048,576 FACES", the hold is longer (1.5 s) | hold, a slight shimmer | |
| 12.5-14.5 | drop, very smooth drape with fine wrinkles | cloth falls, settles | swoosh |
| 15.0-16.5 | reset: "4,194,304 FACES"; sheet does not fall | nothing moves | silence, waiting (inferred) |
| 17.0-17.5 | the whole frame washes to flat light grey like a frozen window | grey-out | |
| 18.0-19.0 | a small error dialog pops up in the centre of the sheet; end | dialog appears | sim halts (AI) |

## Signature device
A resolution ladder that breaks on the last rung. Five identical setups (same camera, same objects, same title
position) where only the number changes, multiplying by four each time. Each round is about 3.5 s: 0.5 to 1 s
hold with the number, a drop of about 0.5 s, 2 s of settling. The material detail rises visibly each round (coarse
angular folds, then smooth folds, then corners swinging like legs, then fine wrinkles), so the viewer learns
"more number, more beauty" and expects the best one last. The last rung subverts it: the hold stretches past
the usual drop time, the frame bleaches to grey like an app that stopped responding, and a tiny system dialog
appears. The crash is the punchline and the comment trigger.

## Pacing read
Big changes every 1.46 s with a CV of 0.66: a regular drop-settle-reset rhythm, with 2 hard cuts detected (the
other resets read as big changes because the sheet sits in the same place). Quiet share is only 5%; the cloth
keeps settling until each reset. The rounds get very slightly longer (the 1 M round holds 1.5 s before dropping),
and the final round is all hold: 2 s of nothing, then the grey-out at 17 s and the dialog at 18 s. The film ends
on the dialog, so the loop restarts at 16 k and many viewers watch again to compare the drapes.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 1 cuts in 19.0 s sampled (0.53 per 10 s), at 17.0 s; 2 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette by role: warm dark charcoal backdrop (#2d2924, #272520, #35332e), off-white matte cloth (#abaca7,
  shadows #696a64), saturated glass green torus with sharp specular highlights; final grey-out about #8a8a86.
- Type: one bold italic grotesque in white with a faint shadow, about 70 px cap height on a 1080 frame,
  numbers with comma separators, centred in the upper third. Changes only at resets.
- Material and light: path-traced look, soft top light, glass with refraction and caustic glints, cloth with
  soft subsurface sheen.
- Camera: locked, slightly high three-quarter angle, the objects small in frame with lots of empty backdrop.

## Why it works
- A clear rule set in one second, then escalation: each rung is a little better, so viewers stay for the top.
- Wait-for-it payoff that is a joke, not just more detail: the crash is relatable to anyone whose computer froze.
- Comment trigger: people argue about hardware, settings, and which drape was best.
- Series framing ("Pt.2") and a loopable structure.

## Steal this (grammar) / Leave this (content)
- Steal: same shot repeated with one number climbing by a fixed factor; a visible quality gain each rung; a
  longer hold before the last rung; a final rung that breaks the system (grey-out and a dialog) instead of
  delivering.
- Leave: their scene (glass torus, plane), Blender's dialog and UI, the watermark, the exact face counts.

## Build it in our studio
- Honest difficulty: real cloth draping over a glass object with path-traced light needs Blender or another 3D
  simulator. We have neither, so the original look is a 4.
- Stylised 2.5D route (difficulty 3): canvas engine. Verlet cloth (a grid of points, distance constraints,
  gravity, collision against a sphere or torus) simulated once at load with a fixed time step and stored per
  frame, so `seek(t)` only reads the array. Project the grid with simple perspective, shade each quad by its
  normal against one light, draw the object as a flat-shaded or gradient shape. Grid sizes 16, 32, 64, 128 per
  side give the visible ladder. The crash rung is pure 2D: hold, grey wash, our own neutral dialog box (no real
  OS or app UI).
- Paid route (difficulty 4): `gen-video` (with approval), image-to-video from one styleframe per rung; keeping
  five rounds visually identical is the hard part, so generate one drop and vary only the counter, or use
  client-supplied 3D renders.
- Scene plan: 1) styleframe the setup; 2) build the sim and bake per rung; 3) counter type per rung; 4) swoosh
  foley on each drop from the event times; 5) final rung hold, grey-out, dialog, end.

## Business translations
- Data SaaS: "1,000 rows... 10,000... 100,000... 1,000,000" files opened in the client's product, each loading
  smoothly, and the last rung opened in a generic spreadsheet greys out (use real tested limits only).
- Upholstery or bedding brand: a throw in the client's fabric drops onto a sofa at rising thread counts that
  the brand really sells, the top rung "sold out" dialog as the joke.
- Web agency: a page loading 10, 100, 1,000 product images on the agency's build, then the last rung on a
  "typical" site freezes; numbers from a real benchmark.
