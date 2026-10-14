---
id: tt-settigation
title: "Four typed OTP digits lift off as playing cards, fan, stack into a deck and become a verification chip"
url: https://www.tiktok.com/@settigation/video/7677577067696835848
platform: tiktok
creator: settigation
plays: 1200000
likes: 46500
shares: 3215
saves: 22588
followers: 29900
posted: 2026-08-24
captured: 2026-10-14
duration_s: 5
category: ui-saas
hook: [wait-for-it, beautiful-first-frame]
devices: [ui-card-stack, morph, typing-caret, cursor-demo, transformation-sequence, seamless-loop]
energy: calm
palette: [dark]
palette_hex: ["#0d1115", "#13171c", "#05090a", "#080d0f", "#2b3239"]
sound: []                             # audio not described in the source package
voiceover: false
text_on_screen: headline
engine: [hyperframes]
difficulty: 2
fit: [saas, finance, b2b, ecommerce]
wow: 2
relevance: 4
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 5.0
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.333
  hook_change_0_2s: 0.009
---

## The film in one line
A 5 s screen recording of a dark web component: four one-time-code boxes are typed 1, 2, 3, 4, then the filled
boxes lift off as playing cards, fan out like a hand, gather into one deck, and the deck turns into a glowing
green microchip while the heading changes to "Checking your code".

## Why it stops the scroll (first 2 s)
- 0.0 s: near-black browser page: small title bar "OTP Verification DECK" with HTML, CSS, JS tags; a large
  heading "OTP Verification DECK" (DECK in blue); a centred dark card "Enter your code / We texted a 4-digit code
  to +1 415 ••• 0142" with four empty rounded boxes; three code panels (index.html, app.css, app.js) along the
  bottom quarter.
- 0.5 s: the cursor clicks the first box, a caret blinks.
- 1.0-1.5 s: digits appear one by one, each box tinting blue and rising slightly as it fills.
- 2.0 s: all four filled; they now look like raised tiles.
- Mechanism: a UI everyone has used a hundred times, framed as a "deck", so the viewer waits to see why. The
  code panels signal "you can build this", which is the save trigger for developers.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0 | idle OTP card, four empty boxes, code panels below | cursor enters | not described |
| 0.5 | first box focused | click, caret blink | not described |
| 1.0-1.5 | "1", "2", "3" typed, active box highlighted | each digit pops in, box tints and lifts | not described |
| 2.0 | "1 2 3 4" filled tiles | last tile pops | not described |
| 2.5 | the four tiles rotate into a fanned hand of cards, overlapping | fan out from a common pivot below centre | not described |
| 3.0 | cards gather, the first slides behind the others | collapse toward the centre | not described |
| 3.5 | one card left, a face-down deck | stack settles | not described |
| 4.0 | heading becomes "Checking your code / One moment, we're confirming it" | text swap, card glows blue | not described |
| 4.5-5.0 | the card becomes a glowing green microchip icon, text dims | morph and glow pulse, then loop | not described |

## Signature device
Inputs become objects. The four code boxes are treated as physical cards from the start: rounded rectangles
about 60 x 80 px on the 1080 frame, with a subtle top highlight and drop shadow, each lifting 4 to 6 px as its
digit lands (about 0.35 s apart). When the last digit lands, the four cards rotate around a shared pivot about
two card heights below the row to fan out like a hand (roughly -20 to +20 degrees), then slide together into a
single stack with the face turned away, then that card morphs (border, glow, inner shape) into a green chip icon
that stands for "verifying". Every state change is one continuous motion with no cuts, and the status text
changes in the same beat as the deck forms.

## Pacing read
The metrics read 0 cuts, no big changes and a quiet share of 0.333 because the moving parts fill only a small
part of a dark frame (hook change 0.009). In fact there is a steady event every 0.5 s: click, three digits, last
digit, fan, gather, deck, status, chip. No rest longer than about 1 s. It is 5 s long and the end state is close
enough to the start that the platform loop plays it again immediately, which is how short UI clips rack up
plays.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 0 cuts in 5.0 s sampled (0.0 per 10 s); 0 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette by role: near-black page and panels (#05090a, #080d0f, #0d1115, #13171c), slate card borders
  (#2b3239), one blue accent for "DECK" and filled tiles, green only for the final chip.
- Type: clean grotesk sans (Inter-like). Heading about 50 px on the 1080 frame, card title about 24 px, body and
  digits smaller. Too small for phones by our rules, which is why our version zooms in.
- Texture and light: flat dark UI, soft inner glows on focus, faint grid in the background.
- Camera: none; a static screen capture at 9:16 with browser chrome at the top.

## Why it works
- Save trigger: a copyable component with its code visible (22.6k saves, about 2% of plays).
- Familiar UI made playful: the "boring" step of logging in becomes a card trick.
- Tiny and loopable: 5 s, no reading needed, the loop starts before the viewer can scroll.
- Caption sets it up as a riddle: "Four boxes. One hand of cards."

## Steal this (grammar) / Leave this (content)
- Steal: treat a dull form input as a physical object; one continuous chain (fill, fan, stack, status); the
  status text changes on the same beat as the object; a 5 s loop.
- Leave: their component design, copy, the "DECK" title, the code panels and the creator's handle.

## Build it in our studio
- Engine: HyperFrames (it is literally HTML, CSS and GSAP); build it from the client's real UI tokens.
- Scene plan: 1) frame the client's real input component large: card 900 px wide on the 1080 frame, digits at
  least 60 px; 2) type digits on a 0.35 s grid with a pop and lift; 3) fan the tiles with CSS 3D transforms
  around a shared pivot; 4) stack and flip into the client's real status state (success icon from their system);
  5) end on the state that loops back to empty.
- Hard part: making it read on a phone. The original is tiny; we crop tighter and drop the code panels unless
  the audience is developers.
- Difficulty 2: a few hours of GSAP; render about 80 s for 5 s.

## Business translations
- Fintech app: the typed one-time code turns into four cards that stack and lock into the app's real security
  badge, for a "secure sign-in" feature reel.
- SaaS: a team invite code typed into the real onboarding form fans into member cards that drop into the
  workspace.
- E-commerce checkout: a real discount code typed at checkout flips into a card that becomes the order summary.
