---
id: onetake-knockon
title: "One key press sets off a tabletop chain reaction whose track turns out to be the product's icon"
url: references/onetake/cases/knockon-15s/
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
hook: [wait-for-it, mid-action-start]
devices: [chain-reaction, marble-run, top-down-plan, rigid-body-drop, pull-back-reveal, cursor-demo]
energy: medium
palette: [light, mono]
palette_hex: ["#e5dfd9", "#eae7e0", "#dfd8d1", "#f8f6f1", "#f1eee7"]
sound: [asmr-foley, silence-moments]
voiceover: false
text_on_screen: headline
engine: [canvas, hyperframes]
difficulty: 3
fit: [saas, b2b, finance, ecommerce, agency]
wow: 4
relevance: 5
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 1.67
  change_rhythm_cv: 1.12
  quiet_share_2fps: 0.034
  hook_change_0_2s: 0.037
---

## The film in one line
Seen from above on a pale table, a pointer presses a "return" key that pops a red marble down an orange track, over a bump and into a toggle that knocks over ten task tiles like dominoes, the last tile hits Send, a "10 tasks, done." notification is thrown up and lands with a check, and a pull-back shows the whole course traces a giant return arrow beside the product name.

Craft reference, not a social post: a 16:9 film for a fictional automation app from the onetake repo. Study only (PolyForm Noncommercial): ideas in our words, no code, text, pixels or sound reused.

## Why it stops the scroll (first 2 s)
At 0.0 s a white "return" keycap alone on warm grey paper, a pointer gliding in; at 0.5 s the key is pressed and its glyph turns orange; at 1.0 s a red marble has popped out; at 1.5-2.0 s the camera follows it down a vertical track that fills orange behind it like a progress bar. Mechanism: the first domino of a machine is instantly readable, so "what does this set off" holds the viewer. Visually quiet (hook change 0.037), but cause and effect starts inside 1 s.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.95 | keycap | pointer arrives, presses; a marble pops out | wooden thock, click, short sub |
| 0.95-2.3 | the track | marble accelerates down; the track fills behind it | rolling noise scaled by speed, rising ticks |
| 2.3-3.3 | the bump | climbs, stops on top, teeters | silence |
| 3.3-3.9 | over | rolls off into a toggle: ON | a knock, a note |
| 3.85-5.7 | ten tasks fall | tiles topple in a quickening run, each landing face up with a task word | a clack and a rising note per tile |
| 5.7-8.75 | Send | last tile presses Send; a notification is thrown up and hangs with a long soft shadow | whoosh, a bell, faint pad |
| 8.75-9.9 | it lands | drops with a squash, gets a check; a bell rings | soft heavy impact, sub |
| 9.3-15.0 | path and name | the pencilled course inks; camera rises; the course is a giant return arrow; name and tagline; one more key tap | pen scratch, chord, last tap |

Sound per the case notes (no music).

## Signature device
Causal carry seen from above. Every beat is physically caused by the previous one: key ejects marble, marble flips toggle, toggle tips the first tile, the last tile presses Send, Send throws the notification. Tiles fall like real dominoes: rotation eases in slowly and finishes fast, each triggers the next once it leans far enough to reach it, and each interval is about 10 % shorter, so the run accelerates. From overhead, height is shown only by the shadow (offset and blur grow with altitude) plus a slight scale-up. The course is laid along the product's glyph, so the final pull-back reveals the icon.

## Pacing read
2 fps: 0 cuts (one world, one camera), big changes every 1.67 s, CV 1.12, only 3 % quiet because the camera keeps drifting. Full rate: 3 % still but 24 % quiet, 6 beats, no transitions, longest quiet run 1.42 s, beat CV 0.68, spread 12.4x. The rests are scored rather than frozen: the silent teeter and the long hang of the notification. The last key tap rhymes with the first.

## Look
Warm off-white paper (#e5dfd9 to #f8f6f1), soft top-left light, one orange-red accent (marble, track, bell), green for toggle and check, white cards, neutral grotesk (task labels too small for a phone).

## Why it works
- Chain reactions promise a next step at every moment.
- The teeter is a micro cliff-hanger; the hanging notification a held breath.
- The reveal reframes everything watched (the path was the logo): a rewatch trigger.
- The tagline names the mechanism itself, so the message lives in the image.

## Steal this (grammar) / Leave this (content)
- Steal: one trigger, a visible causal chain, a summary card; tiles labelled with real tasks; shadow as height from above; a pull-back revealing the course as the brand shape; silence on the teeter.
- Leave: the keycap and arrow composition, the task words and copy, the fictional brand, the score.

## Build it in our studio
Engine: canvas. Closed-form motion is easy (marble position per track segment, tile angles from staggered start times); shadows must be scaled by zoom by hand.
1. Lay the course as a path in the client's icon shape.
2. Marble kinematics per segment.
3. Domino run with eased rotation and accelerating triggers.
4. Notification throw, hang and land with shadow lift; camera leading by 0.1-0.15 s.
5. Ink the path, pull back to icon and name.
Hard part: readability from above (standing tiles read as pale strips); give tiles coloured edges and land them face up with labels at 44 px or more.

9:16: lay the course as a vertical zigzag so the camera tracks downward; run the tiles across in two rows; end with the whole icon inside the middle 60 % of the height.

## Business translations
- Bookkeeping firm (finance): one "upload receipt" press starts a chain through sorted, matched, filed; the last tile sends the monthly report.
- Online shop (ecommerce): an order click rolls through packed, shipped, delivered; the course traces the shop's logo.
- B2B service or agency: one brief knocks over a chain of real deliverables; the course is the company monogram.
