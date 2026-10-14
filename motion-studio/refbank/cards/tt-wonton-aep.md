---
id: tt-wonton-aep
title: "Edit-battle lyric edit on film clips: a DM cold open, then giant lyric words tucked behind the characters"
url: https://www.tiktok.com/@wonton.aep/video/7607256171472243976
platform: tiktok
creator: wonton.aep
plays: 17800000
likes: 2500000
shares: 71800
saves: 286183
followers: 70900
posted: 2026-02-16
captured: 2026-10-14
duration_s: 32
category: lyric-mograph
hook: [mid-action-start, familiar-ip]
devices: [mask-reveal, lyric-sync-type, word-by-word, cut-on-beat, whip-pan, typing-caret, trending-audio]
energy: high
palette: [natural]
palette_hex: ["#211811", "#4f403d", "#e8eaeb", "#7b9ecd", "#bca27e"]
sound: [trending-audio, music-beat]
voiceover: false
text_on_screen: heavy
engine: [hyperframes, footage]
difficulty: 3
fit: [real-estate, restaurant, events, personal-brand, local-service]
wow: 4
relevance: 4
pacing:                               # frames_metrics.py on a 1 fps sample (saturated: nearly every sample is a cut)
  cuts_per_10s: 6.56
  mean_s_between_big_changes: 1.0
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.377
---

## The film in one line
After 3 s of a screen-recorded DM ("edit battle?", reply typed: "Bet"), a 16:9 lyric edit of an animated feature
(the balloon-house film named in the scene description) cuts on every beat, each lyric word set as giant white
type behind the characters so they stand in front of it, ending on the old man alone in his armchair before a
final huge word.

## Why it stops the scroll (first 2 s)
- 0.0 s: the rival editor's profile page as a phone screen recording.
- 1.0 s: the DM: a bubble "edit battle?" and a typewriter caption, "another one of those...".
- 2.0 s: "Message request accepted", and "Bet" being typed with a caret.
- Mechanism: a story starts mid-action (a challenge issued and accepted), which creates stakes and a comment
  trigger (who won?). A famous film arrives at 3 s and pays the curiosity off.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-2 | phone UI: profile, DM, typing "Bet" | scroll, caret | music starts faint |
| 3-7 | girl in aviator goggles; "BITE" white serif, "THIS" teal outlined serif, "OOOY" giant teal | words slam on beats | upbeat track |
| 8-11 | balloon house over a hill, then in the sky before huge white letters; a plane; old man's face in front of a giant word | whip pans and zooms | faster section |
| 12-16 | "DAY" in giant letters with the young couple lying over them; a waterfall painting with "take ME"; "SEE" on a close-up of glasses | characters in front of type, push in | vocal, beat hits |
| 17-19 | old man against a skyline; "Ellie", "it's", "so" one at a time in pink-white script | word-by-word build | vocal slows |
| 20-23 | cliffs and waterfall; "BEAUTIFUL" in white condensed caps with clouds drifting in front; old man holding up a scrapbook | clouds pass over the word | uplifting section |
| 24-29 | frame-high translucent "CAN", "ON" behind the old man and the bride; couple in armchairs before big letters; sky-filled "STATIONS" behind the balloon house | type behind subjects, quick cuts | build |
| 30-31 | old man alone in his armchair, a huge translucent word behind him | slow push | drive to the end |

## Signature device
Text behind the subject. Each word is huge (letters 50-90% of frame height, bold condensed sans or high-contrast
serif, white or semi-transparent) and composited between the background plate and the character, so a head, a
body or a cloud overlaps the letters. Some words are filled with the scene's own texture (sky-filled
"STATIONS"), some are translucent. Tender lines switch to a pink-white script built word by word. Cut and word
change together on the beat, with whip pans between sections; the DM cold open frames it all as a contest.

## Pacing read
At a 1 fps sample nearly every sample is a new shot (8.12 cuts per 10 s, CV 0.0, saturated), so the real edit runs
at a beat or faster, with no rests. Rhythm changes by type size, not speed: giant words on strong beats, script
lines and the "Beautiful" landscape (20-21 s) give a longer read. It ends on a held push on the lonely armchair,
the source film's saddest image; no loop.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 21 cuts in 32.0 s sampled (6.56 per 10 s), at 3.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 17.0 s; 26 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
Warm film browns (#211811, #4f403d, #85624d), sky blue (#7b9ecd), off-white type (#e8eaeb), tan (#bca27e), teal and
pink accents. Three families only: condensed sans, outlined serif, script. Main words at 300-600 px on a 1080
frame, often cropped by the frame edge. Re-framed source shots with pushes, whips and blur.

## Why it works
The DM opening gives a reason to watch to the end and to comment. A beloved film plus a well-chosen song is an
emotional shortcut, and text behind the subject makes familiar footage look crafted, which drives 286k saves from
editors. The ending on the saddest image prompts replays and shares.

## Steal this (grammar) / Leave this (content)
- Steal: giant type behind the subject; one word per beat; a different type style for tender lines; words
  filled with the scene's texture; a genuine phone-UI cold open that sets stakes.
- Leave: the film footage and characters (third-party IP we never ship), the song and lyrics, the rival's
  profile, the DM screens.

## Build it in our studio
Engine: HyperFrames with the client's own footage and local subject matting.
1. Client clips with a clear subject (person, product, building) and headroom.
2. Matte each clip with the subject matting from the embedded-captions workflow (local; it already places
   captions behind the subject) or `hyperframes remove-background`.
3. Stack per shot: plate, giant word, matted foreground; words cut on beats from beats.py.
4. A phone-UI cold open only if it is a real message the client can share; a fake DM is invented content.
- Hard part: clean mattes on hair and fast motion. Pick static or slow subjects and cut before fast moves.
  Difficulty 3, about 16 s render per second plus matting.

## Business translations
- Real estate: an agent walks through a home in front of one giant selling-point word per room.
- Restaurant: the chef plates in front of giant dish names, ending on the dining room and the real logo.
- Gym or local service: the trainer or technician at work in front of three giant words stating the promise.
