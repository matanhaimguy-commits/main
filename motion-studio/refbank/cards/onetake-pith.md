---
id: onetake-pith
title: "Pulling out from one glowing terminal pixel until a whole desktop app has grown around it"
url: references/onetake/cases/pith-21s/
platform: web
creator: onetake
plays: 0
likes: 0
shares: 0
saves: 0
followers: 0
posted: null
captured: 2026-10-14
duration_s: 21.5
category: ui-saas
hook: [scale-shock, wait-for-it]
devices: [zoom-through-scale, pixel-art, typing-caret, one-take-camera, reaction-shot, icon-system]
energy: medium
palette: [dark, light]
palette_hex: ["#e1e2dc", "#18160b", "#fefefd", "#d3d4cf", "#f1f1ee"]
sound: [sfx-heavy, silence-moments]
voiceover: false
text_on_screen: heavy
engine: [canvas]
difficulty: 4
fit: [saas, b2b, education, ecommerce]
wow: 4
relevance: 3
pacing:
  cuts_per_10s: 3.72
  mean_s_between_big_changes: 0.67
  change_rhythm_cv: 0.82
  quiet_share_2fps: 0.167
  hook_change_0_2s: 0.393
---

## The film in one line
The frame opens inside one amber phosphor pixel and pulls back through a typed terminal prompt and a wall of streaming agent output, a thin window border draws itself around the text, the title bar lands and flips everything from amber dark mode to a light theme in one frame, the camera dives into two blocky pixel eyes in the title bar that blink and glance down, follows their gaze to the input where a new message is typed, then pulls out to a small window with seven tool names lined up beneath it and the product name.

Craft reference, not a social post: a 16:9 launch film for Pith, a real desktop app that wraps a command-line coding agent, from the onetake repo. Study only (PolyForm Noncommercial): ideas in our words, no code, text, pixels, font or sound reused.

## Why it stops the scroll (first 2 s)
- 0.0 s: the frame is a few enormous amber cells with dark gaps, an abstract plaid, dead still.
- 0.5-1.0 s: still; one blink near 1.1 s.
- 1.5 s: the pull-back begins; more cells come in at the edges.
- 2.0 s: the cells resolve into giant pixel letters of a typed command.
Mechanism: scale shock and an abstract first frame that becomes legible inside two seconds ("what am I looking at"). Strongest measured open in the onetake set (hook change 0.393).

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-1.55 | one lit pixel at about 440x | dead still, one blink | phosphor hum and coil whine |
| 1.55-3.3 | the caret | pull back to about 9x; a prompt types in amber | dry key clicks |
| 3.3-6.3 | the wall | pull back to about 3x; output lines stream upward past a low-sitting frame | hum, ticks |
| 6.3-7.55 | the frame | pull to about 1.35x; a 1 px border draws itself clockwise | hum |
| 7.55-7.77 | the clamp | title bar drops on a spring and lands | impact |
| 7.77 | theme flip | amber on black becomes ink on light in a single frame; squash and shake | hum cut; first note in the silence after |
| 7.8-10.3 | the desk | held; detail lines fold away, a sidebar slides out, a hard shadow drops; a rest | notes, then silence |
| 10.3-12.1 | the eyes | push from 1x to about 44x into two pixel eyes; dead still; they blink, pupils snap aside | silence, two lid ticks, a snap with a sub |
| 12.1-15.0 | the gaze | camera follows the gaze down to the input; pointer clicks, types, sends | keys |
| 15.0-18.4 | answer and out | message lifts into the timeline, rows tick in; pull out to about 0.5x | ticks |
| 17.2-21.5 | seven tools, name | seven row squares leave on fanned arcs and line up, each naming itself; the name drops letter by letter in lavender | rising ticks, last notes |

Sound column from the case notes: no music until the window exists; synthesis, foley and tuned notes; rests are scored.

## Signature device
Carry by scale, pulling out. Everything that appears was already inside the previous frame: pixel, caret, prompt, output stream, window, desktop. The interior is drawn as a page in its own units under one transform, so type stays crisp at 440x; one bitmap pixel equals a fixed fraction of a page pixel; unlit cells keep a faint residue so the deep camera has texture to slide over; a bloom on lit content fades as the zoom falls. The mid-film transition is the product's own feature (its light and dark themes), and the claim (the agent is seven tools) is built by moving seven objects already on screen, not by a caption.

## Pacing read
2 fps proxy: 3.72 "cuts" per 10 s (the flip and the dives), big changes every 0.67 s, CV 0.82, 17 % quiet. Full-rate checker: 15 % still, 29 % quiet, 15 beats, transitions at 1.17, 2.0, 7.83 and 12.58 s, longest quiet run 2.42 s, beat CV 0.63, spread 8.8x. Shape: frozen open, a long continuous pull-out (1.5-7.5 s), a one-frame flip as the hit, a scored rest, then the eye close-up as a second rest that doubles as the hand-off, and a slow lockup. No loop.

## Look
First third: amber (#d1920b) on near-black (#18160b) with scanlines and pixel gaps. Then a light grey desktop (#d3d4cf to #fefefd) with ink text, a hard 3 px window shadow and a lavender name. The product's own bitmap pixel font throughout. Zoom range from 440x down to about 0.5x, screen-space shakes on the landing.

## Why it works
- Abstraction to recognition in the first two seconds.
- A long pull-out keeps adding context, so curiosity is sustained without cuts.
- The theme flip is a mid-film pattern interrupt; the blinking eyes add a character beat and a smile.
- The seven-tools gather turns the claim into a picture.

## Steal this (grammar) / Leave this (content)
- Steal: open inside the smallest unit of the product (a pixel, a cell, a stitch) and pull out; use a real product behaviour (a theme or mode switch) as the transition; a mascot close-up as the rest; build the claim from objects already on screen.
- Leave: the terminal content, the eyes, the app UI, the pixel font, the name and colours.

## Build it in our studio
Engine: canvas (deep zoom with crisp text needs our own transform and level of detail; scaling DOM to 440x in HyperFrames is unreliable).
1. Page model of the client's real UI in its own units.
2. A log-zoom spring anchored to a subject that travels (caret, mascot, input), not to a fixed point.
3. Texture at depth (pixel grid, grain or fabric).
4. A single-frame mode flip with an impact.
5. A close-up on a real logo or mascot detail as the rest.
6. A gather of the real feature icons into a row, then the name.
Hard part: zoom steps of several log units in under a second without the target drifting off frame; the notes needed a subject-tracking anchor and a longer settle. Difficulty 4, no paid steps.

9:16: the app window becomes a phone screen, which is portrait anyway; end the pull-out with the screen at about 60 % of frame height; the feature row becomes a two-row grid; anything meant to be read at 36-40 px or more. Relevance is middling: the grammar suits app and product clients, less so local services.

## Business translations
- Any app with a dark mode (saas): start inside one pixel of the dark UI, pull out, and make the flip to light mode the film's single hit.
- Online course platform (education): open inside one letter of a lesson, pull out to the course page, gather the real module icons into a row.
- Print shop or textile brand (ecommerce): open inside one halftone dot or one stitch, pull out to the finished product and the logo.
