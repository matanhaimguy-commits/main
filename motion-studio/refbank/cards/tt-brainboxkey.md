---
id: tt-brainboxkey
title: "A ball ricochets in a shrinking neon ring that flips colour on every hit, each bounce a note of a mystery tune"
url: https://www.tiktok.com/@brainboxkey/video/7347373904513568033
platform: tiktok
creator: brainboxkey
plays: 3500000
likes: 53000
shares: 991
saves: 5873
followers: 110900
posted: 2024-03-17
captured: 2026-10-14
duration_s: 61
category: beat-sync
hook: [guess-challenge, sound-hook]
devices: [beat-sync-hits, escalation-ladder, progress-ring, seamless-loop]
energy: high
palette: [neon, dark]
palette_hex: ["#000000", "#5921d2", "#e65b44", "#38f862", "#171618"]
sound: [music-beat, sfx-heavy]
voiceover: false
text_on_screen: headline
engine: [canvas, hyperframes]
difficulty: 1
fit: [events, personal-brand, education, any]
wow: 3
relevance: 2
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 1.81
  change_rhythm_cv: 0.39
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.28
---

## The film in one line
A textured black ball bounces around inside a circular arena on black; on every hit the thick outer ring
switches to a new neon colour and grows inward, so for a full minute the arena shrinks and the bounces speed
up while overlays beg for comments, follows and sends.

## Why it stops the scroll (first 2 s)
- 0.0 s: a thin lime-green ring on pure black, the arena filled with a faint diagonal tile of the creator's
  name, a tiny ball at the centre. No text yet.
- 0.5-1.0 s: not sampled; the ball has started moving and growing.
- 1.5 s: the ring is now blue, a large ball sits top right at the end of a wide cyan ribbon trail; small white
  text with a pink brain avatar at the top: "replying to EVERY comment i can till we hit 40k".
- 2.0 s: next hit, next colour (purple by 3.0 s).
- Mechanism: a sound hook. The caption tags (#guessthesong, #mysterysong, #fnaftune) say each bounce plays the
  next note of a known tune, so the viewer stays to name it. Colour flips at every hit give a strobe-like
  pattern interrupt.

## Beat map
Frames cover 0-60 s of the 61 s film. One continuous shot.

| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0 | thin green ring, empty dark arena, tiny ball at centre | ball starts | first note (sound not described in detail) |
| 1.5-6.0 | ring cycles blue, purple, red, green; ball grows until it fills the arena at 6.0 | ricochets with wide gradient trails | fast electronic beats, a note per hit |
| 7.5-18.0 | ring purple, teal, pink, cyan, about 15 percent of the radius; trails draw a triangle, a V, a star | ball resets small and grows again | beats continue |
| 19.5-30.0 | ring now about a third of the radius: pink, blue, red, blue, orange | arena noticeably smaller, trails tighter | beats |
| 31.5-39.0 | violet, yellow, purple rings, arena half its first size | quicker bounces | beats |
| 40.5 | bottom text: "if you've got this far, follow / subscribe brainling!" | same | beats |
| 42.0-57.0 | lime, purple, green, violet; the arena is a small hole in a huge ring | bounces near-continuous | beats |
| 60.0 | arena is a dot; text across the disc: "send this to your friends and see if they respond with this:" plus emoji | final hits | final burst, ends |

## Signature device
A closing arena. The ball (a black disc with the same fine texture as the arena, slightly outlined) bounces
off the inside of a circle. Each collision does three things at once: plays a note, swaps the ring to the next
colour of a saturated cycle (green, blue, purple, red, orange, teal, pink, yellow), and moves the ring's inner
edge inward a little. The ball also leaves a ribbon trail as wide as itself in a two-tone gradient, so
repeated paths draw polygon shapes. Because the arena shrinks, the time between hits drops steadily: an
automatic accelerando that needs no editing. Four small markers sit on the ring at 12, 3, 6 and 9 o'clock.

## Pacing read
0 cuts, a big change every 1.81 s and CV 0.39. Real change is faster than the 1.5 s sampling can show: the ring
changes colour on every hit, several times a second late in the film. Quiet share 0.0: no rests at all. Hook
change 0.28 is moderate because the opening frame is calm and the first hits are slow. Energy rises
monotonically as the arena closes; the end is the arena collapsing to a dot under a "send this" line, which
loops cleanly to the calm open circle.

## Look
- Palette: black ground (#000000, #171618), one fully saturated ring colour at a time (#5921d2 violet,
  #e65b44 red-orange, #38f862 green and others), trails in two-tone gradients.
- Type: small white rounded sans overlays with emoji, top and bottom, well under 44 px on a 1080 frame.
- Texture: a faint tiled watermark inside the arena and the ball; no light or depth, flat 2D.
- Camera: locked, centred.

## Why it works
- Guess-the-song: each hit is a note, so people stay to recognise it and comment the answer.
- Built-in acceleration from the shrinking arena keeps tension rising without new ideas.
- Engagement overlays on top of a passive watch ("replying to EVERY comment", "follow", "send this to your
  friends") convert attention into comments and sends.
- The low share count (991) shows its limit: high watch time, little reason to pass it on.

## Steal this (grammar) / Leave this (content)
- Steal: collision-driven events (each hit triggers note, colour and progress), a shrinking container as a
  progress bar, an accelerando from geometry, trails that draw shapes.
- Leave: their brain avatar, watermark tile, overlay lines, the melody and the "brainling" community language.

## Build it in our studio
- Engine: `canvas`. Pre-compute the bounce path analytically (circle reflection is closed-form), place a hit
  at each beat of a melody we compose or license, and solve the arena radius so collisions land on those
  beats. Export hit times as `window.EVENTS` for the note and click sounds.
- Scene plan: 1) melody note list; 2) solver for ball path and shrink rate; 3) ring colour cycle from the brand
  palette; 4) trail ribbon; 5) end on the brand mark inside the last tiny arena.
- Hard part: making every collision land exactly on a note. Solve offline: choose the next wall point from the
  required interval and ball speed, rather than simulating physics.
- Difficulty 1. Fast render.

## Business translations
- Music school: each bounce plays a note of a scale students learn in week one, ending on "Can you name it?"
  and the trial-lesson link.
- Event or festival: the ring cycles through the line-up's colours, each hit a beat of the headliner's
  licensed track, the arena closing to the date.
- Brand-palette teaser for an agency: the client's colours as the ring cycle, the arena closing on their real
  logo.
