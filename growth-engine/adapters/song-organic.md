# Song ads, organic adapter

Pass this file, the Post Card and `growth-engine/production/STANDARDS.md` with every `readymerce-song-ads` call for an
organic piece (`reel_song`). The skill's method stays: speech first, then lyrics, the lyric gate (4f), the moves menu,
THE PICTURE in the chorus, the vocal stem as the timing master, the 10 shot-logic tests, the style and character
bibles, sheets, storyboards and H3 reference mode. Where this file or STANDARDS.md disagrees with the skill, they win for
organic posts (section 7). Built from the song skill (no version number; last changelog 4 Oct 2026),
`production/audit/song-ads.json` and `production/audit/skill-audit-2026-10-15.md`. "Line" means a SKILL.md line.

## 1. The skill's phases on the 16-step pipeline
| Skill phase | Step | Gate in the ledger | Who |
|---|---|---|---|
| 0 Hook and Script Lab cards; 1 Inputs, GATE 1 avatar | 0 | G-BRIEF | Claude, from brain.json (AV-01) and the card; Hook Lab and Script Lab loaded with their organic adapters |
| 2 Genre and tiers, GATE 2; 3 Angle and THE PICTURE, GATE 3 | 1 | G-IDEA | Claude: tier from the card, genre from the series' LIB run; THE PICTURE passes the one-second read; the Organic Director checks Content Map fit |
| 3b Hook Lab | 2 | G-HOOK | hook-agent + a fresh grader (`hook-lab-organic.md`). The gate refuses every picture in a song run before G-HUMAN-SONG, so here the grader reads the H-01 Shot Spec; the concept frame (a hero H-01 still) is made after step 4 and opens the hook board at step 8 |
| 4a-4b Swipe study, Script Lab writes the speech | 3 | speech released at 85+, G-HUMAN-SPINE | script-agent with `script-lab-organic.md` and the song adapter 18b; listen and sound-off cold reads; spine pick delegated |
| 4c-4f Lyrics, lyric gate | 3 | G-SCRIPT: the run's one record, written after the speech and the lyrics both pass, its note naming both scores (STANDARDS 9) | a fresh lyric cold reader; no song is generated before this record |
| GATE 4 (Suno by hand); 5 Song into a workable place | 4 | G-AUDIO-MASTER, G-HUMAN-SONG; G-AUDIO per song take | `pipeline.py budget` first (the song is the run's first generation, STANDARDS 10); Claude makes the takes on ElevenLabs Music (section 6); the owner listens to every song master before any picture (G-HUMAN-SONG, per piece) |
| 6 Audio analysis | 5 | G-TIMELINE; G-AUDIO per slice | Claude: beat grid, vocal stem, word map, slices of 4 to 14 s (STANDARDS 2) |
| 7, 7a Visual plan, 10 shot-logic tests | 6 | G-PLAN (table in `qa/shot-logic.md`), G-SPEC per shot | visual-planner + fresh prompt-reviewer |
| 8 Style bible, sheets, GATE 5 | 7 | G-PROMPT-IMG, G-VIS-SHEET per sheet, G-HUMAN-LOOK once per series | on the client's LIB run (section 3); `pipeline.py budget` before its first sheet |
| 9 Storyboards, GATE 6 | 8 | G-PROMPT-IMG, G-VIS-BOARD per board, G-VIS per concept frame and keyframe start frame, G-CONTINUITY, G-HUMAN-HOOKBOARD | fresh visual-reviewer; the owner sees only the hook board |
| 10 Budget preflight | 9 | G-BUDGET | `pipeline.py budget` re-prices the whole video (cap, live balance, +25%) after steps 0 to 8 close; no video call before step 9 closes (STANDARDS 10) |
| 10 Video, 11 Deliverables | 10 | G-PROMPT-VID per prompt; G-FALLBACK | the gate checks every call; deliverables live in `runs/<post_id>/` |
| 12 Frame check, sync, edit | 11-12 | G-TAKE per clip, then G-ASSETS | fresh take-reviewer: frames, drift, every sung word; G-ASSETS closes step 11 (STANDARDS 9) |
| 13 QA and policy | 13 | G-FINAL, G-DIRECTOR | take-reviewer in final mode, then the Organic Director |
| (none in the skill) | 14-15 | G-HUMAN-FINAL, G-LEARN | the owner on the hub; the analyst at 72 h and 7 d |

On fail: 3 FIX loops per speech or lyric, then G-HUMAN-ESCALATE; 2 prompt loops, then the Organic Director; 3 asset
attempts, then G-HUMAN-ESCALATE. A model outside STANDARDS needs G-EXCEPTION; the R1 and R2 re-tests need G-HUMAN-TEST.

## 2. Song formats for a service business (the skill's 4c formats and Appendix S)
`reel_song` renders `song_day` and `pov_day` only (organic.json). Tier A: the card needs `angle_proven: true` or the
month's wildcard (card-check ERROR otherwise), one tier A a week at most. Judge it on sends and follows, not DMs.

| Skill format | Organic re-cast (StraightScale, AV-01) | story_template | Tier |
|---|---|---|---|
| 4c-NP Named-person story (06) | **Main use.** A composite owner of a kitchen and furniture showroom in Tirana: three tiny scenes of his day (a message arrives while he is on the floor, he adds ads, at night "klientët nuk kthehen"); each failed fix killed with its reason; the chorus names THE PICTURE; the payoff replays scene 1 as a process (the same message, answered with one question and a next step) | `song_day` | O60 |
| 4c-PR Problem rap (02, 47 s) | Hook + one chorus: the problem in the buyer's words, one plain cause line, a fix that keeps the habit. The skill's price anchor becomes a time anchor with no number (the evenings already spent on posts). First song test and the short cut | `song_day` | O30 |
| 4c-CE Characters explain (09) | The patchwork pieces sing their own parts (the boosted post, the page, the unanswered inbox) and none hears the others: that is THE PICTURE. "The product is never a character" (line 262) is about physical products | `song_day` | O60 (O30 with 3 pieces) |
| 4c-FB Fable (07) | "Once there was a clinic owner in Tirana who posted every dawn": told clearly as a fable, gentle, blame-free, one material, an identity close | `song_day` | O60 |
| 4c-AS Antagonist story (04) | A staged rival across the street (a showroom like his) and a friend who shows the method, framed as a POV story ("POV: ..."), never as a fact about a real street or business; the social-win payoff becomes the hero working differently | `pov_day` | O60 |
| 4c-TF Two futures (03) | `two_days` is not a `reel_song` template (card-check ERROR): route the angle to `reel_story_narrated` or `reel_animation` | (route away) | |
| 4c-CF Confession (08, 01); S05 timeline | Need a real person, real numbers or a real client case; the proof bank is empty (B6 `not_held`) | (waits for proof) | |

Visual moves kept from the swipe file (lines 224 to 230): one material for the whole series; a genre or style switch at
the mechanism verse; callbacks (the deep red phone returns). The climbing counter (line 229) needs a proof-bank number
with permission, so StraightScale has none: screens show states (an unread dot, "Seen", a silent phone), never counts.

## 3. Look, cast and reuse
- **One singer per series, locked:** a narrator-singer character, the brain's recurring object (the smartphone in a deep
  red case, #BE0F18) as a singing object, or a composite owner singing his own day. For a singing object the sheet says
  where the face sits and what the mouth is made of (line 277). Every person is a composite in a clearly staged,
  stylized scene (the stylized-animation route of STANDARDS 7's AI-people rule): never a real client, never carrying a
  result.
- **Style:** one block from `config/organic.json` `animation_styles` (`claymation`, `crochet`, `family_film_3d`,
  `storybook_2d`), word for word in every sheet, storyboard and clip prompt; a prompt never names a studio, its
  characters or a look-alike (V24). `crochet` fits when Patchwork Marketing is drawn as stitched squares; `storybook_2d`
  suits a fable (STORY-FORMATS 4). `reel_song` has no `styles` list in organic.json, so card-check ignores an
  `animation_style` with a WARN: the style lives in the series style bible and in every Shot Spec's `style` field (open:
  add `styles` there).
- **Build the world once per series** on `clients/straightscale/runs/SS-LIB-<SERIES>/`: the style bible (8a: style
  block, closing line, motion guard, 4 to 6 named colours from the brand kit: charcoal #1F1F1F, ivory #F8F6EF, marble
  #EDE4D6, crimson #B31217 as the one saturated accent, and mark red #BE0F18 only on the phone case; gold #DD9A10 is
  kept for the small counter, so a song has none), the character bible (8b, pasted word for word), sheets in the
  STANDARDS 3 order (singer hero, owner, group of the patchwork pieces, settings such as a showroom or a clinic
  reception in Tirana after dark, a prop sheet per story prop: the red phone in each screen state, the shutter), then
  state sheets (8d). G-VIS-SHEET at hero rules, G-HUMAN-LOOK once. The song's genre, tempo, singer description and music
  prompt are locked in the same run, so every episode sounds like the series (ORGANIC-OS 7.7 rule 3).
- **Genre:** the skill's map (line 59) has no row for Albanian owners aged 35 to 60. Offer 2 or 3 genres from the
  niche's outlier audio in research (ORGANIC-OS 7.7 rule 6) at G-IDEA and lock one on the LIB run.
- **Image model:** Nano Banana 2 at 2k for sheets, storyboards, concept frames and keyframe start frames until re-test
  R1 (about 10 credits, G-HUMAN-TEST, before the first series). H3 does not read Higgsfield elements (line 294): attach
  the sheet images directly. Retakes keep the same references in the same order and change one thing (line 302).

## 4. Words, lengths, shots, credits
- **Tiers** (STANDARDS 8): O60 is the story tier; `song_day` is laid out for 60 s; aim at 50 to 60 s because music runs
  long. O30 is the song short: hook + one chorus (4c-PR). No O15 song; O90 only with a stated reason. "No story under
  55 s" (line 57) becomes "no full discovery story under 45 s".
- **Speech first:** Script Lab writes the argument as speech for the low end of the tier at 2.5 words/s and releases it
  at 85+; the lyrics are turned from it (4d), never written from scratch, every rung kept in order.
- **Lyric lines** (STANDARDS 4, Lyrics row): 8 to 14 syllables each (line 158); O60 23 to 37 lines (the skill's S60
  row, line 166), 18 to 27 when the song runs 40 to 50 s, O30 about 11 to 19 (proposed, confirm on first run).
- **Hook timing** (STANDARDS 5, song; the skill states it four ways, lines 103, 157, 206, 207): after the intro trim
  the voice arrives within 0.3 s; the first sung word by about 1 s; the problem sung by about 3 s, in the first 6 words.
  Over 3 s to the problem: regenerate the opening before any picture; a slow hook never ships. Text hook 4 to 10 words,
  top third, frame 1 to about 3 s. No brand, mechanism name or offer in the first 3 s (Hook Lab gate 7).
- **Chorus:** carries THE PICTURE and its name (Patchwork Marketing) and is sung at least twice; the chorus shots show
  THE PICTURE (VISUAL-QA 10.4).
- **Shots** (STANDARDS 5): a picture change every 1.5 to 3.5 s (every 1 to 1.5 s in the first 5 s, motion in the first
  second), cuts snapped to the beat grid; 2 to 3 shots per sung H3 take, 4 at most; a sung sequence covers 4 to 10.5 s
  of song (14 s at most with 4 shots). O60 about 17 to 25 pictures, O30 about 8 to 14. The singer sings on screen in the
  hook and the choruses (reference mode); the verses show what is sung as silent keyframe shots (one 5 s H3 clip per
  picture, one shot, 1 take, trimmed to its slot: STANDARDS 2). Only the singer mouths words.
- **The 10 shot-logic tests (7a, lines 238 to 247), all kept; G-PLAN fails on any:** 1 one-second read by a stranger,
  sound off; 2 cause and visible result in the same shot; 3 an abstract line gets a contrast, not a stunt; 4 a narrator
  aside sets up the next idea; 5 real-world logic (nobody floats); 6 edit effects stay in the edit; 7 one panel = one
  moment = one state per character; 8 the prop that carries the line is exact and matches its prop sheet; 9 the thing
  that carries the line is the subject; 10 a blocked or simplified shot still carries its line. One row per shot:
  line | who does what | what visibly changes | what a stranger reads in 1 second | pass/fail (line 249).

**Credits (Higgsfield, STANDARDS 10 prices).** How computed: sung seconds x 1.15 (each slice rounded up + 1 s) x 2 takes
(STANDARDS 2, line 349); story seconds (runtime minus sung seconds minus the 3 s end card) as one 5 s keyframe clip per
3 s, rounded up, 1 take each; H3 at 2 credits/s; stills (3 concept frames, one storyboard per sung sequence, one start
frame per keyframe clip, one end-card still) at about 2 each (the skill's Nano Banana 2 figure, line 105; price them
with `get_cost`, STANDARDS lists 1 to 6.5); the 3 s end card is a still; then +25%. ElevenLabs is billed apart
(ORGANIC-OS 7.7: about 2,000 to 4,000 ElevenLabs credits per song piece).

| Piece | Low end | High end |
|---|---|---|
| O30 standalone | 25 s: hook 6 + chorus 8 s sung (32 s rendered, 64) + 3 clips (30) + 9 stills (18) = 112, +25% = about 140 | 35 s: hook, a 10 s chorus and one 5 s sung line (48 s, 97) + 4 clips (40) + 11 stills (22) = 159, +25% = about 200 |
| O60 | 45 s: hook + 2 choruses, 22 s sung (51 s, 101) + 7 clips (70) + 14 stills (28) = 199, +25% = about 250 | 65 s: 32 s sung (74 s, 147) + 10 clips (100) + 18 stills (36) = 283, +25% = about 355 |
| O30 cut of an O60 | reuses the hook and chorus clips: about 0 to 35 (ORGANIC-OS 7.7 cutdown) | |
| New series world, once | 6 to 8 sheets: 12 to 16, +25% = about 15 to 20 | |

Sung credits come from the unrounded seconds (22 s sung is 50.6 s rendered, 101 credits; 32 s is 73.6 s, 147).
`organic.json` gives `reel_song` 140 to 355. An O60 stays under 300 up to about 54 s,
with about half of it sung as in the rows above (27 s sung: 62 s rendered (124) + 8 clips (80) + 15 stills (30) = 234,
+25% = about 293); at 55 s it passes 300. A longer piece moves sung verse lines to keyframe shots or ships as O30.
ORGANIC-OS 7.7's "about 190 when characters exist" matches about one take per sequence (our reading); STANDARDS' 2 takes
on sung sequences cost more. Monthly cap 1,300 (brain.json). `pipeline.py budget` checks the cap and the live balance
before the run's first generation (the song at step 4) and again at step 9, which re-prices the whole video before any
video call (STANDARDS 10).

## 5. Copy and the close
- Moves kept (4b): H, SC, FF, T, promise, M (chorus), D, TL/PO, ID. Rungs 9 to 12 (OF, G, U, "link below", line 141)
  are out, with the price anchor and the PR proof move (no proof in the bank). One organic CTA, spoken (line 162), as the
  outro, from the ORGANIC-OS list (STANDARDS 5) for a reach or trust job: send ("Dërgoja një pronari biznesi."), follow
  ("Na ndiq për pjesën e dytë.", only when part 2 is planned), save ("Ruaje këtë postim."), comment (an answer to a
  question the song asks), DM, or the live keyword ("Shkruaj ANALIZA në komente."; ANALIZA is the only live keyword).
- **The "product" is the method.** The cause (Patchwork Marketing: paying several suppliers for pieces that do not work
  together) is named in the chorus after the open question is set. The turn is a spoken line from the contrarian vault
  (C1: "Nuk të duhet më shumë marketing. Të duhet marketing që punon bashkë."). One step of the Only Choice System (Find,
  Own, Attract, Convert, Close) is given away in verse 2. D (discovery) becomes how the owner found the fix.
  StraightScale is named at most once, on the end card or by the handle, not "at least twice" (line 163).
- **The payoff is a process, never a result.** No numbers (the proof bank is empty; IP-01 is internal only), no
  timeline of results, never "we answer within 1 hour", never "we chase the client's leads" (we build them a system).
  No price, offer, guarantee, deadline or urgency anywhere in the lyrics, supers, end card or caption.
- **Albanian lyrics in "ti"** (until D2), plain words, the avatar's words from the brain ("na shkruajnë po nuk blejnë",
  "mesazhet mbeten pa përgjigje kur jam në punë", "telefoni nuk bie"; written in Albanian by us, so confirm them with
  real buyer words). Chorus draft (STORY-FORMATS 3.7): "Reklama këtu, faqja atje, mesazhet askund." Numbers as words,
  the brand spelled for the singer (line 164). Every lyric, super and caption is marked for a native read.
- **End card** 2.5 to 3 s with the music under it: the CTA in large type; no offer, guarantee or "Results vary" fine
  print (line 375). AI label on per STANDARDS 7 (D1 decides whether to extend it). The caption's first line passes Hook
  Lab, then the CTA; a pinned comment when the CTA is ANALIZA; the cover is the text-hook frame.

## 6. Voice, audio and checks
- **Route:** ElevenLabs `eleven_music_v2_5` with the released lyrics as custom lyrics (STANDARDS 1). It runs as a flow
  node: read `creative_get_flow_node_types` and `creative_get_model_schema` for the lyrics and length fields before the
  first call, and never repeat a call to retry (each call is charged). 2 to 3 takes. The music prompt keeps the skill's
  style-prompt rule (line 176): under 25 words, with "clear lead vocal, lyrics up front", plus the series genre and
  singer. Suno only when the owner makes it by hand from the same lyrics (GATE 4, line 187); that song takes the same
  checks. "Suno runs 10 to 25 s long" (line 57) is Suno only: measure the ElevenLabs takes and log the overrun.
- **Spoken lines** (the turn, the CTA): inside the song when Whisper finds every word clearly; else the StraightScale
  narrator (`8oGKUMljR779HzpZBiE4`, `eleven_v4`, 4 takes) speaks them over an instrumental bar, pauses never capped;
  that voice needs its G-HUMAN-VOICE record once (STANDARDS 9).
- **G-AUDIO-MASTER:** pick the take with the highest Whisper match to the lyrics; a take under 0.88 is not used
  (STANDARDS 1, proposed, confirm on first run; our runs saw 0.88 to 0.95). Use a multilingual faster-whisper (`small`
  or `medium`, `language="sq"`), not the skill's `small.en` / `medium.en` (lines 203, 378); read spelling against the
  lyric sheet. Each song take and each slice gets its G-AUDIO record (STANDARDS 9). Hook timing as in section 4. A sung
  change that alters the meaning goes back through Script Lab FIX and is regenerated (line 206). **G-HUMAN-SONG**
  (STANDARDS 4 and 9): the owner listens to every song master before any picture, per piece; the gate refuses every
  image and video call in a song run until it is recorded. It is not G-HUMAN-VOICE (once per voice): sung Albanian can't
  be fully measured.
- **G-TIMELINE:** BPM and beat grid with `librosa.beat.beat_track`, every cut snapped to the nearest beat (line 202);
  vocal stem by ElevenLabs isolation or UVR MDX-Net `Voc_FT`, checked at about 30 dB under the mix in instrumental
  parts (line 204); re-time on the stem (RMS above about -38 dB); trim the intro on a beat. Slices from the vocal stem:
  start on the sequence's first frame, 0.03 s fade, 4 to 14 s, one singer, named `SEQ_vocal_<start>-<end>_pad<N>s.mp3`;
  H3 `duration` = slice rounded up + 1 s, within 5 to 15 (STANDARDS 2 interim; not "= padded length", line 338). Run R2
  (about 80 credits, G-HUMAN-TEST) before the first song if it hasn't run.
- **H3 card (the song skill lacks it, issue 6):** `minimax_h3`, `resolution: "2K"`, `aspect_ratio: "9:16"`,
  `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`; reference mode for sung sequences, keyframe mode for
  silent shots, never mixed. The 9-part card (VISUAL-QA 4.2): style block; `<<<image_1>>>` the storyboard, then singer
  and state sheets, then the setting, `<<<audio_1>>>` the vocal-stem slice, in upload order; "follow the storyboard shot
  by shot; never show panels, gutters or a split screen" (line 342); a hands and props line per shot; "Shot N, a to b s:"
  with one action on its sung word and "exactly N shots"; background action in every shot; the skill's lip-sync block
  (only the singer sings, wider on held notes, closed in every pause, the others only react) plus "use <<<audio_1>>>
  exactly, word for word, at the same timing"; negatives and the motion guard; the duration rule. 2 takes per sung
  sequence; 1 take per silent keyframe clip (STANDARDS 2).
- **G-TAKE:** frames 1 per second (2 under 6 s) plus the first and last 0.1 s (`vqa_crops.py frames`), not one middle
  frame at 180x320 (line 368); the 10 tests and the 8g sheet checks on every frame; the singing mouth at least a third
  of the frame (AI-VIDEO-PIPELINE step 6). **Drift (hub G6), not one cross-correlation at 0 ms (lines 338, 369):**
  `vqa_crops.py drift <clip> <slice>` (lag per 2 s window every 0.25 s); cut at each lag step inside a pause, or one
  median offset when steps are under 0.15 s; retake only for drift inside a word or a correlation under about 0.5.
  Whisper every sung clip against the lyrics. Never speed up a sung clip; a silent clip 2.5x at most (line 371's 2.7x is
  overruled, STANDARDS 5).
- **Edit and G-FINAL:** the song master is the only audio, clip audio muted; loudness per STANDARDS 4 (-14 LUFS ±1, true
  peak -1 dBTP or lower, the range and short-term limits: the pass flag of `vqa_crops.py loudness`; the skill has no
  target, line 372); 30 fps, 1080x1920; captions are the words as sung, 1 to 3 per card, bold sans, contrast 4.5:1; hook
  super frame 1 to about 3 s; supers 2 to 6 words; safe zone top 14%, bottom 35%, the right 21% of the lower half and 6%
  sides (STANDARDS 6; not bottom 20%, line 373). F1 to F8 include the sound-off and sound-on watches, the vocal-stem
  listen, the banned-model check on the run's `calls.jsonl` (STANDARDS 9), the hook check at phone size, THE PICTURE in
  both choruses and every sung word present; then G-DIRECTOR.

## 7. What this adapter overrides in the skill, and why
| Skill (line) | Organic rule | Why |
|---|---|---|
| The user makes every song and fix in Suno (3, 105, 187, 206) | ElevenLabs Music with custom lyrics by default; Suno only when the owner makes it | STANDARDS 1; the manual step stalls an automated week |
| S60/S90 + C45, "no story under 55 s", Suno overrun (38, 57, 166) | O60 and O30; no full discovery story under 45 s; overrun measured | STANDARDS 8 |
| Sequences of 3 to 6 shots; 2 x 3 grid (222, 318, 395) | 2 to 3 shots per take, 4 at most; 2 to 3 panels on 16:9, or 4 in a 2x2 grid of 9:16 panels on a 9:16 canvas | STANDARDS 2, 3 (issue 5); 3 shots in 15 s also broke the skill's own 1.5 to 3.5 s cadence |
| H3 with no model id, 2K or preset id; duration = padded slice (330 to 353) | `minimax_h3`, 2K, 9:16, `declined_preset_id`; slice 4 to 14 s, duration + 1 s, 5 to 15 | STANDARDS 1, 2 (issues 2, 3, 6) |
| 7-part prompt, written and approved by the same agent (340 to 347) | 9-part card + a fresh prompt-reviewer (G-PROMPT-VID) | VISUAL-QA 4.2, 4.3 (issue 6) |
| One middle frame per shot; one cross-correlation; speed-ups to 2.7x (368, 369, 371) | Frames 1 per second; windowed drift; no speed-up on sung clips, 2.5x at most on silent ones | STANDARDS 2, 5, 11; hub G6 |
| No loudness; bottom 20% safe zone (372, 373) | -14 LUFS, -1 dBTP; bottom 35% + right 21% | STANDARDS 4, 6 (issues 9, 11) |
| `small.en` / `medium.en` (203, 378) | Multilingual faster-whisper, `language="sq"` | STANDARDS 4 |
| Offer, guarantee, urgency; brand twice; offer end card and fine print (141, 163, 375) | One organic CTA; brand at most once; AI label | ORGANIC-OS 6.2; STANDARDS 5, 7 |
| "Write at full selling strength", a legal team decides (12, 184) | Facts only from the brain; nothing that reads as a promised result | `script-lab-organic.md`: no legal team on organic posts |
| Frame 1 "on the body"; Meta before-and-after fallback (27, 220, 388) | B2B profile: the problem where it lives in the business | `hook-lab-organic.md` (issue 15) |
| Live read: hook rate, CTR, cost per purchase (31) | Organic LEARN (section 8) | ORGANIC-OS 9 (issue 16) |
| Elements read by Seedance 2.0 and Kling 3.0; Sync Lipsync 3 fallback (294, 351) | Not permission: Seedance banned; Kling 3.0 and Sync Lipsync 3 only with G-FALLBACK; others with G-EXCEPTION | STANDARDS 1 |
| GATE 5 every sheet, GATE 6 every storyboard to the user (312, 326) | G-HUMAN-LOOK once per series; fresh reviewers on every board; the owner sees the hook board; G-HUMAN-SONG on every song master | VISUAL-QA 6, 9.4; STANDARDS 9 |
| About 30% retakes (353); no storyboard model named (Phase 9) | +25%; Nano Banana 2 at 2k until R1 | STANDARDS 1, 10 |

## 8. Package (tier A)
- Main cut (O60). A short (O30, 4c-PR) written as its own lyric and passed through 4f on its own; when its hook and
  chorus match the main song word for word it reuses that audio and those clips (a music edit on the beat grid plus its
  own spoken CTA, about 0 to 35 credits), else it is budgeted as a standalone O30.
- 3 hook variants as trial reels; a variant with a new sung line needs its own sung opening (line 105), an ElevenLabs
  take of the opening (Suno's Replace Section only when the owner makes it). A carousel that retells the piece: a normal carousel run per `carousel-machine-organic.md` (4:5 slides, G-VIS-SLIDE, G-SET); storyboard panels are never posted (STORY-FORMATS 5.5), 2 or 3 story frames, and an ad version with the ad CTA that is never posted organically (ORGANIC-OS 7.7).
- `runs/<post_id>/` holds the released speech and lyrics with both gate reports, the music prompt, the song takes with
  their Whisper match, the beat grid, the stem and slices, the shot logic table, Shot Specs, boards, prompts, the
  generation log, drift reports and the loudness check.
- Hub draft with `hub.py`, notes "AI label: on"; nothing posts before G-HUMAN-FINAL.
- G-LEARN at 72 h and 7 d: sends and follows per reach first, then skip rate, average watch time, rewatches, saves and
  ANALIZA comments. A drop at the first chorus means THE PICTURE did not land; a drop at the spoken turn means the
  bridge broke the song. Kill rule: under the account median on its job metric (sends per reach) 3 times in a row, pause
  songs for 60 days (ORGANIC-OS 7.7 rule 7). Lessons to `clients/straightscale/analytics/learnings.md`, the opening to
  the Hook Library.
