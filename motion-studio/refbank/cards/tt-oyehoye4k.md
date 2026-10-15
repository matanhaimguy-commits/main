---
id: tt-oyehoye4k
title: "A round-headed sticker character says 'Good Morning' three ways, the caption retyping itself for each one"
url: https://www.tiktok.com/@oyehoye4k/video/7660740825822874900
platform: tiktok
creator: oyehoye4k
plays: 13200000
likes: 1400000
shares: 4700000
saves: 155410
followers: 291700
posted: 2026-07-10
captured: 2026-10-14
duration_s: 6
category: story-comedy
hook: [direct-address, sound-hook]
devices: [pose-to-pose-comedy, typing-caret, character-host, seamless-loop]
energy: medium
palette: [light, mono]
palette_hex: ["#fefeff", "#fdfefc", "#5f5c5a", "#ebe7e2"]
sound: [voiceover]
voiceover: true
text_on_screen: headline
engine: [canvas, hyperframes, cab]
difficulty: 2
fit: [restaurant, local-service, personal-brand, ecommerce]
wow: 3
relevance: 3
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 6.0
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.636
  hook_change_0_2s: 0.0
---

## The film in one line
On a plain white card a small round-headed line-art character says "Good Morning" three times in three moods
(holding a yellow sandal to its ear like a phone, then pulling down an eyelid and sticking its tongue out, then
pinching its own mouth shut while sweating), and the "Good Morning" headline above it types itself out again
with each new line.

## Why it stops the scroll (first 2 s)
- 0.0 s: white frame, black "Good Morning" in a clean sans at the top, the character in the lower left
  holding a yellow sandal against its ear like a phone, pink blush cheeks, a contented smile.
- 0.5, 1.0, 2.0 s: the same pose held; nothing moves in the sampled frames. The voice says "Good Morning"
  (AI description).
- Mechanism: the hook is the audio and the address, not the picture. A cute character greets the viewer
  directly and the sandal-as-phone is a small visual gag that reads at thumbnail size. The film is a ready-made
  greeting people send to someone: 4.7 M shares on 13.2 M plays (about one share per three views, roughly three
  times the like count), which is the real story of this post.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-2.5 | pose 1: smiling character, sandal held to ear as a phone; headline "Good Morning" complete | held pose, no visible motion at 2 fps | voice: "Good Morning" (cheerful, per AI) |
| 2.5 | hard swap to pose 2: eyes squeezed, one hand pulling down an eyelid, tongue out, two yellow "action" ticks beside the head; headline cleared and retyping ("Goo") | text types on letter by letter | voice: "Good Morning" again |
| 3.0-4.0 | pose 2 held, headline complete again | static | voice tail |
| 4.5 | hard swap to pose 3: character, larger and lower in frame, pinching its lips shut with one hand, sweat drop; headline retyping ("Go") | text types on | voice: "Good Morning" a third time |
| 5.0 | headline at "Good Morni" | typing | voice |
| 5.5-6.0 | pose 3 held, headline complete; cut back to pose 1 on loop | static | end, loop |

## Signature device
One line, three deliveries, pose-to-pose. The character never in-betweens: each delivery is a single held
drawing swapped on a hard cut, and the caption at the top resets and types itself on (about 6 to 8 characters
per 0.5 s, so the full 12 characters in about 0.75 s) in time with the spoken words, then holds. The holds get
shorter (2.5 s, 2.0 s, 1.5 s), so each joke lands faster than the last. The third pose is drawn larger and
cropped by the frame bottom, a small push-in that marks the punchline. The ending pose (mouth held shut) is the
opposite of the opening pose (talking on the "phone"), so the loop back to the first frame reads as a reset
rather than a jump.

## Pacing read
The metrics read almost nothing: 0 cuts, no big changes, 64% of sampled pairs quiet, hook change 0.0. That is
because the character fills only about a quarter of a white frame, so each pose swap changes less than the
12% threshold. Read by eye there are three shots (2.5 s, 2.0 s, 1.5 s), an accelerating rhythm, with the only
motion being the typing caption. The film is mostly rests, and the voice carries the timing. It ends on the
shortest beat and loops cleanly, which is why a 6 s piece gets watched several times.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 0 cuts in 6.0 s sampled (0.0 per 10 s); 0 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette: near-white ground (#fefeff), soft dark grey line (#5f5c5a), pink blush on the cheeks, a pale
  yellow sandal and yellow action ticks as the only colour accents.
- Type: one clean geometric sans, medium weight, black, centred at the top, about 50 px cap height on a 1080
  frame (small: it is a label, not a headline treatment). It types on with no caret visible.
- Character: sticker-style line art, round head, dot eyes, two-stroke body, uniform line weight, no fill
  other than white; soft grey contact shadow under the feet in pose 2.
- No camera, no texture, no background.

## Why it works
- Utility share: a good-morning greeting is something people send every day. The film is the message, so the
  share button is the call to action.
- Escalating moods on one line give a mini story (polite, cheeky, forced quiet) in six seconds that a viewer
  maps onto a friend or partner.
- The retyping caption tells the viewer a new "take" has started even with the sound off.
- Short and looping: the loop restarts the gag before the viewer decides to scroll.

## Steal this (grammar) / Leave this (content)
- Steal: one short phrase delivered three ways by a simple mascot; held poses swapped on hard cuts with
  shrinking holds; the caption resetting and typing on with each take; the last pose as the opposite of the
  first so it loops; built to be sent to someone.
- Leave: their character design (round head, blush, sandal phone), the poses, the voice recording and the
  "Good Morning" caption styling.

## Build it in our studio
- Engine: canvas 2D engine (line-art character drawn as paths, three static poses), or HyperFrames with three
  SVG poses and a GSAP typing effect; Claude Animation Base only if the client wants a painterly character.
- Scene plan: 1) design a client mascot as clean SVG line art in three poses that match three readings of one
  phrase; 2) record or generate the three line reads (ElevenLabs, with approval of the voice) and time each
  pose swap to the start of a read; 3) caption types on per character, timed so the last letter lands on the
  last syllable; 4) shrink holds 2.5, 2.0, 1.5 s; 5) end on the opposite of pose 1 and loop.
- Hard part: drawing poses that are funny on their own. Write the three moods first (the joke is in the
  contrast), sketch thumbnails, and keep line weight and proportions identical across poses.
- Difficulty 2. Render is seconds in the canvas engine. Only paid step is the voice if we generate it.

## Business translations
- Coffee shop: the cup mascot says "We're open" three ways (bright, half-asleep, fully caffeinated) as the
  morning post people forward to a coworker.
- Gym: the mascot says "Leg day" three ways (eager, dreading, unable to stand), made to be sent to a training
  partner.
- E-commerce brand: the mascot says "It shipped" three ways (proud, nervous, relieved) for the order-update
  season.
