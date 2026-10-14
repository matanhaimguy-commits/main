---
id: onetake-motion-web
title: "A small-type product film where pacing does the work: long holds, then a staccato word burst"
url: references/onetake/cases/motion-web-15s/
platform: web
creator: onetake
plays: 0
likes: 0
shares: 0
saves: 0
followers: 0
posted: null
captured: 2026-10-14
duration_s: 15
category: ui-saas
hook: [bold-claim, text-headline]
devices: [word-by-word, cursor-demo, typing-caret, ui-card-stack, silence-before-hit]
energy: medium
palette: [light, mono]
palette_hex: ["#f7f7f5", "#fefefe", "#e2dedb", "#0b0b0c", "#99bebb"]
sound: [asmr-foley, sfx-heavy]
voiceover: false
text_on_screen: headline
engine: [hyperframes, canvas]
difficulty: 2
fit: [saas, agency, b2b]
wow: 2
relevance: 3
pacing:
  cuts_per_10s: 0.67
  mean_s_between_big_changes: 2.14
  change_rhythm_cv: 1.11
  quiet_share_2fps: 0.172
  hook_change_0_2s: 0.019
---

## The film in one line
Small black words on an off-white page claim that web motion is usually decoration, a serif wordmark drops in, a prompt card types a request and a hand clicks send, a checklist ticks to PASS, three real web pages fly past tilted and blurred, four tiny interactive cards react to the pointer, a browser window holds, and four single words cut hard one after another before a black end card.

Craft reference, not a social post: the 16:9 (4K60) worked example the onetake skill was extracted from. It became the house template, and later films that copied its beat order were rejected. Study only (PolyForm Noncommercial): ideas in our words, no code, text, pixels or sound reused.

## Why it stops the scroll (first 2 s)
At 0.0 s "Web motion" in small black grotesk, centred; at 0.5 s "is usually" joins; at 1.0 s "decoration." lands in red; at 1.5-2.0 s the line dissolves as wordmark letters drop into a light serif logo. Mechanism: a contrarian claim set up to be overturned. On a phone it barely registers: the type is a few percent of frame height and almost nothing moves (hook change 0.019, the lowest in the set).

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.15-1.55 | the claim | three words spring in, the last one red | soft glass touches |
| 1.65-3.0 | wordmark | serif letters drop with a landing squash | a breath |
| 3.0-4.75 | prompt card | logo folds to the corner; a request types; a hand clicks send | key clicks, click down and up |
| 4.85-7.0 | checklist | seven lines tick, the last reads PASS | rising glass ticks, a chord |
| 7.05-8.85 | three real sites | each flies through tilted and blurred, about 0.9 s each | travelling air, felt landings |
| 9.55-12.15 | four micro cards | button, spring follower, jelly ring, string; the pointer causes each reaction | a bubble per card |
| 12.1-13.25 | browser window | slow push, then hard out | quiet |
| 13.25-14.3 | the burst | four single words, hard cuts at 0.22-0.25 s | four subs, the loudest moment |
| 14.3-15.0 | black end card | white serif wordmark | a deep sub |

Sound per the case notes: one small room of air, glass, wood and sub sounds, no music.

## Signature device
The rhythm contour, built from contrast rather than any one effect. Shot lengths from 0.22 s to 2.6 s (the notes give a CV near 0.78), about a third of frames dead still, small elements in a lot of empty space, and a calm hold right before a staccato burst of one-word hard cuts. A hand pointer is on screen whenever something responds. The rejected drafts (nine equal 0.74 s cards, then seven equal 1.55 s full-frame shots) both read as slides; varied durations and the hold-then-burst ending got it accepted.

## Pacing read
2 fps: 0.67 cuts per 10 s, big changes every 2.14 s, CV 1.11, 17 % quiet. Full rate: 19 % still, 59 % quiet, 7 beats, transitions at 8.92 and 14.33 s, longest quiet run 1.67 s, beat CV 1.11, spread 10.9x. Mostly small motion in a still frame, two peaks (the page fly-through at 7-9 s, the word burst at 13.3-14.3 s), then a black end. No loop.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 1 cuts in 15.0 s sampled (0.67 per 10 s), at 14.5 s; 1 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
Off-white ground (#f7f7f5), near-black type (#0b0b0c), one red accent word, small green and blue accents in the cards, a teal page (#99bebb) in the fly-through. Grotesk body, light high-contrast serif wordmark, monospace checklist. Elements about a fifth of frame width; soft shadows.

## Why it works
- For designers and developers the claim sets up a reversal and the demo proves it.
- The visible hand gives cause and effect; varied durations give the film a contour.
- The burst after a hold gives the ending a punch.

## Steal this (grammar) / Leave this (content)
- Steal: duration contrast as a target (longest beat at least 4x the shortest); a hand visible whenever UI reacts; a hold before the burst; a one-word staccato close; vary how shots exit.
- Leave: the claim and words, the wordmark, the third-party site footage, the micro cards, and above all the beat order, which was punished when reused.

## Build it in our studio
Engine: HyperFrames (DOM type, cards and pointer on one paused GSAP timeline; registry typing and cursor effects).
1. Claim word by word, then the logo.
2. Prompt card, pointer, send; checklist ticks.
3. The client's own real pages in perspective.
4. A frozen hold, then three or four single words on hard cuts, then the logo.
Hard part: truly frozen holds (a slow push still counts as motion), and not letting it feel like a template; pair it with a real concept. Difficulty 2, no paid steps.

9:16: words at 88 px or more, cards at 85-90 % width, micro cards stacked vertically, staccato words in the middle band. Relevance is middling because the visuals depend on small type; the pacing lesson transfers fully.

## Business translations
- Web design agency: a contrarian line word by word, a brief typed, the client's own launched pages fly past, a hold, a three-word close.
- SaaS onboarding tool: a setup checklist ticks to done, three real product screens, a four-word burst of the value.
- B2B consultancy: a claim about their field, a pointer-driven demo of a real deliverable, a frozen beat, the staccato close and logo.
