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
  cuts_per_10s: 8.12
  mean_s_between_big_changes: 1.0
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.377
---

## The film in one line
After a 3-second screen recording of a DM ("edit battle?", reply typed: "Bet"), a 16:9 lyric edit of an
animated feature film (the balloon-house film named in the scene description) cuts on every beat, with each
lyric word set as giant white type placed behind the characters so they stand in front of the words, ending on
the old man alone in his armchair in front of a final huge word.

## Why it stops the scroll (first 2 s)
- 0.0 s: the rival editor's profile page (handle, small follower count), as a phone screen recording.
- 1.0 s: the DM thread: a bubble "edit battle?" and a typewriter caption under it, "another one of those...".
- 2.0 s: "Message request accepted", and the reply "Bet" being typed with a caret.
- Mechanism: a story starts mid-action (a challenge has been issued and accepted), which creates stakes and a
  comment trigger (who won?). Then a well-known film appears at 3 s, which pays the curiosity off with something
  familiar.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-2 | phone UI: profile, DM "edit battle?", caption "another one of those...", typing "Bet" | scroll, typing caret | music starts, faint |
| 3-4 | film clip: girl in aviator goggles, old man's face in the foreground; "BITE" in white serif top | word fades on, slight push | upbeat track, first line |
| 5-7 | girl close-up; "THIS" in teal outlined serif; "OOOY" giant teal across the bottom | words slam on the beat | vocal |
| 8-11 | balloon house over a hill, then in the sky with huge white letters behind it, a plane, old man's face in front of a giant word | whip pans and zooms | faster electronic section |
| 12-13 | "DAY" in giant white letters with the young couple lying in the grass overlapping them; a painting of a waterfall with "take ME" | characters in front of type | vocal |
| 14-16 | whip blur; young man's glasses with "SEE" in white condensed caps | push in on the eyes | beat hits |
| 17-19 | old man's face against a city skyline; "Ellie", "it's", "so" appear one word at a time in pink-white script top right | word-by-word build | vocal slows |
| 20-23 | cliffs and waterfall; "BEAUTIFUL" in white condensed caps with clouds drifting in front; old man holding up a scrapbook | clouds pass over the word | uplifting pop section |
| 24-25 | "CAN" and "ON" as frame-high translucent letters behind the old man and the young bride | type behind subjects, quick cuts | vocal |
| 26-29 | couple painting a mailbox; couple in armchairs with big letters behind; "STATIONS" filling the sky with the balloon house in front | holds and cuts | build to the end |
| 30-31 | old man alone in his armchair, a huge translucent word behind him | slow push | music drives to the end |

## Signature device
Text behind the subject. Each lyric word is set huge (letters 50-90% of the frame height, bold condensed sans
or high-contrast serif, white or semi-transparent) and composited in the depth layer between the background
plate and the character, so the character's head, body or a cloud overlaps the letters. Some words are filled
with the scene itself (sky-textured "STATIONS"), some are translucent so the room shows through. Smaller emotional
words switch style completely (a pink-white script built word by word) to mark a softer line. The cut and the
word change together on the beat, with whip pans and motion blur between sections. The DM cold open frames the
whole thing as a contest.

## Pacing read
At a 1 fps sample, nearly every sample is a new shot (8.12 cuts per 10 s, CV 0.0 because the sampling saturates),
so the real edit runs at one change per beat or faster. No rests. Rhythm changes by type size, not speed: the
giant words land on strong beats, the script lines and the "Beautiful" landscape (20-21 s) give the eye a
longer read. The ending is a held push on the lonely armchair shot, the emotional beat of the source film; no
loop.

## Look
- Palette: warm film browns (#211811, #4f403d, #85624d), sky blue (#7b9ecd), off-white type (#e8eaeb), tan
  (#bca27e); teal and pink accents for a few words.
- Type: three families only: bold condensed sans (main words), outlined serif (teal words), script (tender
  words). Main words at 300-600 px on a 1080-wide frame, often cropped by the frame edge.
- Camera: the source film's shots, re-framed with pushes, whip pans and blur on the cut.

## Why it works
The DM opening gives a reason to watch to the end (to judge the battle) and drives comments. A beloved film
plus a well-chosen song is an emotional shortcut, and the text-behind-subject trick makes familiar footage look
new and crafted, which drives saves (286k) from other editors. Each beat carries a new word, so the viewer reads
along with the song. The ending lands on the saddest image, which prompts replays and shares.

## Steal this (grammar) / Leave this (content)
- Steal: giant type placed behind the subject; one word per beat; switch to a different type style for tender
  lines; fill a word with the scene's texture; a phone-UI cold open that sets up stakes.
- Leave: the film footage and characters (third-party IP we never ship), the song and lyrics, the rival
  editor's profile, the exact DM screens.

## Build it in our studio
Engine: HyperFrames with the client's own footage, using local subject matting.
1. Footage: client clips with a clear subject (person, product, building) and some headroom.
2. Matting: run the subject matting from the embedded-captions workflow (local, it places captions behind the
   subject) or `hyperframes remove-background`, to get a per-frame foreground matte for each clip.
3. Stack per shot: background plate, giant word, matted foreground. Words cut on the beats from beats.py.
4. A cold open in real phone UI only if it is genuine (a real customer message the client can share); never a
   fake DM, which our rules ban as invented content.
5. Grade lightly and add whip blur transitions from the registry.
- Hard part: clean mattes on hair and motion blur. Choose shots with static or slow subjects and hold the
  word behind them, and cut before fast moves.
- Difficulty 3; render about 16 s per second of film plus matting time.

## Business translations
- Real estate: an agent walking through a home in front of giant words for each room's selling point, one per
  beat.
- Restaurant: the chef plating in front of giant dish-name words, ending on the dining room with the real logo.
- Gym or local service: the trainer or technician at work in front of three giant words that state the
  promise, cut to a generated beat.
