---
id: tt-jydnfilms
title: "Black-and-white lyric edit that flips between pure black and pure white frames around a phone, a crystal heart and walls of repeated type"
url: https://www.tiktok.com/@jydnfilms/video/7530964581670309142
platform: tiktok
creator: jydnfilms
plays: 3500000
likes: 426200
shares: 22300
saves: 89736
followers: 7118
posted: 2025-07-25
captured: 2026-10-14
duration_s: 43
category: lyric-mograph
hook: [wait-for-it, sound-hook]
devices: [lyric-sync-type, word-stack, glitch-cut, highlight-pill, word-by-word, silence-before-hit, trending-audio]
energy: high
palette: [mono, dark]
palette_hex: ["#000000", "#f6f5f7", "#262427", "#acabb0", "#5d5d61"]
sound: [trending-audio, music-beat, silence-moments]
voiceover: false
text_on_screen: heavy
engine: [hyperframes, canvas, gen-image]
difficulty: 3
fit: [saas, personal-brand, events, agency]
wow: 3
relevance: 3
pacing:                               # frames_metrics.py on a 1 fps sample
  cuts_per_10s: 3.26
  mean_s_between_big_changes: 1.48
  change_rhythm_cv: 1.09
  quiet_share_2fps: 0.19
  hook_change_0_2s: 0.006
---

## The film in one line
A square, almost colourless lyric edit: 8 s of near-black and a growing dot, then black-and-white type scenes
(a "SAY YOU" word wall behind a phone, a text thread, "START" tearing apart, a crystal heart with "got your
heart"), played twice, ending on "YOU KNOW YOU'RE BETTER THAN THIS" lighting up letter by letter.

## Why it stops the scroll (first 2 s)
- 0.0 s: pure black.
- 1.0 s: small lower-case serif "headlock" in the centre.
- 2.0 s: black again; the credit "by jydn" follows at 3 s.
- Mechanism: almost nothing on screen (hook change 0.006) while a well-known intro builds; the emptiness dares
  the viewer to wait. A dot appears at 6 s and swells into a white flash at 8 s, paying the wait off.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-8 | black, small serif title, small credit; a white dot becomes a ring, then a soft white disc | fades, dot grows into a flash | ambient intro building |
| 9-10 | white wall of "SAY YOU" in solid and outline type with a black phone on top; close-up of the phone: blue "can we please", grey "too late to start" with a red glow | rows slide opposite ways, bubbles pop | drop, first lyric |
| 11-13 | white blur; black label chips "to start.."; "STA" and "RT" split; giant "START" with motion blur | split and smear on the hit | beat hits |
| 14-17 | white starfield: "got your", black faceted heart, script "hea" completing to "heart"; heart spinning on black; heart in a thin square frame | heart turns, word completes, frame snaps | vocal |
| 18-22 | "HEADLOCK" with green echo outlines over a shattered glass tunnel; white flash; "i", then "i don't believe"; a warped wall of the editor's tag | tunnel rush, word-by-word, warp | chorus hit, vocal |
| 23-35 | white disc, concentric rings around a phone silhouette, then a second pass of 9-19 ("START" on black this time) | same moves | second verse and chorus |
| 36-42 | white bar wipe on black; a frame split darker and lighter, "YOU KNOW", "YOU'RE BETTER", "THAN THIS" lighting letter by letter; black; small "JYDN" | light sweeps across letters, fade | sustained vocal, fades to silence |

## Signature device
Hard black-and-white alternation as the rhythm. Nearly every scene is pure black with white elements or pure
white with black elements, and the flip between them lands on the beat. Three recurring anchors carry a story
through the flips: a phone with a text thread (the argument), a faceted crystal heart (the feeling), and walls of
one repeated word in solid plus outline type (the fixation). Words behave as objects that break or complete:
"START" splits and smears, "hea" completes to "heart", label chips hold small words like redaction tape. Colour
appears only as signal (message blue, a green echo on the title word). The finale slows to letters lighting one
by one.

## Pacing read
At a 1 fps sample: 4.88 cuts per 10 s, a big change every 1.48 s, the most uneven rhythm in this batch (CV 1.09):
an 8 s near-silent intro (longest quiet 7 s, quiet share 0.19), one cut per beat in the middle, then a slow 5 s
line build. The middle repeats almost exactly (9-19 and 25-35 s), making the song structure visible. Black first
and last frames give a quiet loop.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 14 cuts in 43.0 s sampled (3.26 per 10 s), at 9.0, 10.0, 11.0, 16.0, 17.0, 18.0, 19.0, 23.0, 25.0, 26.0, 30.0, 34.0 s; 21 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
Black, white (#f6f5f7) and greys (#262427, #5d5d61, #acabb0), with message blue and title green as accents. Heavy
grotesque caps up to frame width, outline versions in the walls, a script for "heart", small serif and italic for
quiet lines. Smear, light grain, bloom on flashes.

## Why it works
The silent opening filters for fans, who stay for the drop. The flips make each beat physical, and three anchors
tell a story without footage. "Project file in bio" turns saves (about 90k) into a download funnel.

## Steal this (grammar) / Leave this (content)
- Steal: strict two-tone alternation cut on beats; 2-3 recurring anchor objects; words that split or complete on
  the hit; solid-plus-outline word walls; colour only as signal; a slow letter-by-letter final line; a quiet
  intro that builds to a flash.
- Leave: the song and lyrics, the editor's tag walls, the crystal heart asset, the exact layouts.

## Build it in our studio
Engine: HyperFrames (type, chat bubbles, flashes); canvas if word walls need many moving rows.
1. Script 8-12 short lines; choose two anchors from the client's world (real app screen, real product).
2. Word walls: 6-8 rows in solid and outline styles, alternate rows sliding opposite ways.
3. Hits: words split into two spans that fly apart with a smear; black or white flashes on strong beats
   (beats.py).
4. Phone UI must be the client's real product, never an invented screen; a crystal or chrome object can come
   from the registry or `gen-image` (paid, approval).
5. Finale: one line lit letter by letter on a split-lit frame; small real logo on black.
- Hard part: two-tone discipline with phone-size legibility; readable words stay at 44 px or more. Difficulty 3.

## Business translations
- Messaging or scheduling SaaS: the thread "can we reschedule?" meets the product's real reply screen; the
  sign-up line lights up at the end.
- Coach (personal brand): a black-and-white manifesto with "stop waiting" word walls and one final lit line.
- Club night (events): 5 s of black, a white flash on the drop, then date and venue cycling in two-tone walls.
