---
id: onetake-launch
title: "One prompt bar typed three times, shorter each time, each send blooming into a different finished film"
url: references/onetake/cases/onetake-launch-30s/
platform: web
creator: onetake
plays: 0
likes: 0
shares: 0
saves: 0
followers: 0
posted: null
captured: 2026-10-14
duration_s: 30
category: ui-saas
hook: [wait-for-it, text-headline]
devices: [typing-caret, morph, one-take-camera, whip-pan, word-stack, pull-back-reveal, silence-before-hit]
energy: high
palette: [light, saturated]
palette_hex: ["#ece1cf", "#472f48", "#f9f3e8", "#af8d72", "#202b44"]
sound: [music-beat, silence-moments]
voiceover: false
text_on_screen: heavy
engine: [hyperframes, canvas]
difficulty: 4
fit: [agency, saas, events, restaurant]
wow: 4
relevance: 4
pacing:
  cuts_per_10s: 6.67
  mean_s_between_big_changes: 0.71
  change_rhythm_cv: 0.93
  quiet_share_2fps: 0.034
  hook_change_0_2s: 0.084
---

## The film in one line
A rounded prompt bar on a cream desk types a full request and on send balloons into a calendar app that collapses into a phone, a shorter request opens a plum earbuds ad where comic noise words pile up until a charging case snaps shut, a one-word request becomes a line that whips across the desk into a festival poster, and finally all three films line up above the bar while a block cursor writes the name.

Craft reference, not a social post: the 16:9 launch film of the onetake repo (three fictional products). Study only (PolyForm Noncommercial): ideas in our words, no code, text, pixels or music reused.

## Why it stops the scroll (first 2 s)
At 0.0 s a pill-shaped bar with a chevron, a block cursor and a placeholder asking to describe a film; at 0.5 s a slash command types; at 1.0 s it becomes an orange chip; at 1.5-2.0 s a sentence types while the macro camera slides along it. Mechanism: the prompt bar is the most familiar interface of the moment, and "what will this make?" is the open loop; typing gives constant small motion (hook change 0.084).

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-4.4 | bar, request 1 | macro glide along the text; two dead-still holds | keys only |
| 4.4-9.5 | send, calendar film | the bar balloons, blurred, into a calendar window; events pop in; push, tilt, dive | music starts on a downbeat |
| 9.5-10.4 | phone | the week collapses into a phone; an event sheet opens | music |
| 10.95-12.0 | bar 2 | camera travels right to a second bar; short request; dead still | music |
| 12.1-16.1 | earbuds ad | bar opens into a plum frame; comic noise words pile up; the case rises and snaps shut | a breakdown, a dip near 16 s |
| 16.0-16.9 | bar 3 | one word typed; dead still | quiet beat |
| 16.9-21.1 | the drop | the bar compresses into a line that whips across with heavy blur and becomes a poster's first grid line | the drop |
| 21.1-25.9 | gather | the three films line up above the bar | music |
| 26.8-30.0 | stop and name | everything freezes on a silent beat; the next hit carries a cursor writing the name; dead still | silence, then the hit |

Sound: a licensed 115 BPM instrumental spliced so a silent beat lands on the freeze (case notes). Our loudness read agrees: about -23 LUFS under the typing, -13 to -18 with music, dips near 16, 19 and 27 s.

## Signature device
A recurring anchor that spawns every section. The prompt bar returns three times, each input shorter (a sentence, four words, one word), which accelerates the film. Each send is a container transform: the bar's rounded rectangle grows into the next frame (a window, an ad frame, a line that becomes a poster grid). Each mini-film has its own palette and motion language, held together by one paper desk and a camera that never cuts. At the end every section gathers over the anchor, and the anchor writes the name.

## Pacing read
2 fps: 6.67 "cuts" per 10 s (blooms and whips, no edits), big changes every 0.71 s, CV 0.93, 3 % quiet. Full rate: 3 % still, 14 % quiet, 24 beats, 9 transitions (4.5 to 27.42 s), longest quiet run 1.58 s, beat CV 0.60, spread 7.6x. A dense showcase: rest comes only from the dead-still bar beats and the one freeze before the name, so the stillness target is relaxed. Ends still; no loop.

## Look
Cream paper desk (#ece1cf, #f9f3e8) with tan shadows (#af8d72). Film one in muted pastel event colours, film two plum (#472f48) with multicoloured comic type, film three navy (#202b44) with orange, yellow and pink poster blocks. Clean grotesk in the bar, the name drawn as one stroke. Macro on the bar, wide pulls, blur on every bloom.

## Why it works
- A structure learned after one cycle; cycles two and three are anticipation, and shorter, so the film speeds up.
- Three different worlds keep novelty high inside one continuous space.
- The freeze plus hit on the name gives a clean end.

## Steal this (grammar) / Leave this (content)
- Steal: the anchor-respawn loop with a shortening input; container blooms as transitions; each section its own palette inside one shared world; a silent-beat freeze before the logo.
- Leave: the three fictional products and their art, the noise-word layout, the poster, the music, the name's lettering.

## Build it in our studio
Engine: HyperFrames (bar, typing and three mini-scenes as sub-compositions; GSAP container morphs). Canvas if one long camera move must cross all three.
1. Bar and typing; bloom into section A (a real client case).
2. Travel to bar 2, bloom into B.
3. Bar 3 compresses to a line, whip into C.
4. Gather row and logo.
5. A licensed or generated track with a breakdown and a drop; the freeze on a silent beat.
Hard part: three mini-films means three designs; keep each to 3-4 s and use the client's real material. Difficulty 4.

9:16: the bar at 85 % width in the middle band; blooms grow upward into portrait sections; the gather becomes a vertical stack. At 30 s it is long for a reel; aim for 18-22 s.

## Business translations
- Creative agency: one brief bar, typed three times, opens into three real client projects (with permission), ending on the agency name.
- Restaurant group: "a table for two", "lunch", "late" typed into a search bar, each opening a different venue's real room or menu.
- Event organiser (events): three event types typed, each opening its real poster or ticket page, then all three line up over the brand.
