---
id: onetake-skill-demo
title: "A headline slides into a text field and every interface box grows out of the one before"
url: references/onetake/cases/skill-demo-15s/
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
hook: [text-headline, bold-claim]
devices: [morph, cursor-demo, typing-caret, ui-card-stack, word-by-word]
energy: medium
palette: [light, mono]
palette_hex: ["#f6f4f0", "#0a0a0a", "#e8d495", "#fdfdfd", "#5d4cdc"]
sound: [sfx-heavy, silence-moments]
voiceover: false
text_on_screen: headline
engine: [hyperframes]
difficulty: 2
fit: [saas, b2b, finance, local-service, agency]
wow: 2
relevance: 4
pacing:
  cuts_per_10s: 1.33
  mean_s_between_big_changes: 1.67
  change_rhythm_cv: 0.65
  quiet_share_2fps: 0.172
  hook_change_0_2s: 0.022
---

## The film in one line
A short headline types on off-white and its last two words slide down into a text field that grows around them, a slash menu filters and a row flies into the field as a chip, the field shrinks into a sent message, a card grows from the chip and ticks off loading steps, a progress run ends in a file chip that grows into a player showing a pale yellow sun card, then three all-caps lines cut hard on black and a serif wordmark drops in letter by letter.

Craft reference, not a social post: a 16:9 operation demo from the onetake repo, all drawn UI. Polished and bridged throughout, but its own user rejected it as too close to motion-web: use it for the container-morph grammar, not as an idea. Study only (PolyForm Noncommercial): ideas in our words, no code, text, pixels or sound reused.

## Why it stops the scroll (first 2 s)
At 0.0 s "A launch video" in small near-black grotesk; at 0.5 s the next word rises; at 1.0 s the last two words land in violet; at 1.5-2.0 s they slide down and a white input field forms around them as a pointer arrives. Mechanism: a claim that physically becomes the interface. Weak scroll-stop: small type, little motion (hook change 0.022).

## Beat map
| t (s) | on screen | what moves | sound (our loudness read) |
|---|---|---|---|
| 0.15-1.35 | headline | three word groups rise; still hold | soft ticks |
| 1.95-4.7 | input | field gains focus; a menu of four commands filters; a row flies in as a chip; request types; send | clicks, keys |
| 4.7-6.4 | loading card | field shrinks into a sent message; a card grows from the chip and ticks four files | ticks |
| 6.4-8.3 | the work | tool steps stream, spinner to tick, progress bar, a PASS line | near silence around 7 s |
| 8.3-11.95 | the result | pointer presses play; a pale yellow card with a short line; a sun lands, a stage opens and folds into a seal | louder hits around 10 s |
| 11.95-12.95 | the burst | three all-caps lines, white on black, hard cuts | loudest hits |
| 12.95-15.0 | wordmark | letters drop into a serif wordmark; still hold | silent from about 14.5 s |

The case notes do not describe the sound; the column is our loudness read only (integrated -21 LUFS, event hits, no obvious bed).

## Signature device
Container morph. Each element's rounded rectangle animates position, width, height and corner radius into the next element's box: headline words into the field, a menu row into a chip, the field into a message bubble, the chip into a card, a file chip into a player. Content cross-fades inside while the box springs (about 0.3-0.5 s, slight overshoot), so nothing appears from nowhere and the eye always has a survivor to follow.

## Pacing read
2 fps: 2.0 cuts per 10 s (only the staccato end), big changes every 1.67 s, CV 0.65, 17 % quiet. Full rate: 19 % still, 55 % quiet, 8 beats, one transition at 12.33 s, longest quiet run 1.5 s, beat CV 0.37 (the lowest in the onetake set), spread 4.4x (just over the 4x floor). Even through the UI section; the burst at 12 s is the only contrast. No loop.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 2 cuts in 15.0 s sampled (1.33 per 10 s), at 10.0, 12.5 s; 3 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
Off-white (#f6f4f0), near-black (#0a0a0a), one violet accent (#5d4cdc) for key words and chips, pale yellow (#e8d495) for the result card and sun, green ticks. Small grotesk UI, serif wordmark, soft card shadows.

## Why it works
- Continuous cause and effect is easy to follow: every box comes from a box.
- The headline becoming the field is a neat proof of the claim.
- It fails on idea, not craft: the shape is the house template (claim, prompt, work, result, burst, logo), so it reads as familiar. Low wow for a feed.

## Steal this (grammar) / Leave this (content)
- Steal: container morph as the default transition in a UI demo; let the headline become the interface; a pointer drives every reaction.
- Leave: command names and copy, the beat order (the template), the sun card, the wordmark.

## Build it in our studio
Engine: HyperFrames (DOM boxes on a GSAP timeline; FLIP-style morphs are native; registry typing and cursor effects).
1. Headline word by word, morph into the field.
2. Menu and chip; sent message into a card with ticks.
3. Progress into the result (real client UI).
4. Logo.
Hard part: none technical. The risk is the idea, so use it as the transition layer under a stronger concept from the three-pitch round. Difficulty 2, no paid steps.

9:16: UI at 85-90 % of frame width, type at 44 px or more, the menu drops below the field, the result card fills the middle band. Container morphs are the backbone of most SaaS reels, so relevance stays high despite the rejection.

## Business translations
- Booking app (saas, local-service): a headline about booking in one tap slides into the search field; a real time-slot chip grows into the confirmation card.
- Invoicing software (finance, b2b): an invoice line morphs into a payment card, then into a paid receipt row.
- Agency: a client's brief sentence slides into a form, becomes a project card, which grows into a real delivered piece.
