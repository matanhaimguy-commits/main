# Animation ads, organic adapter

Pass this file, the Post Card and `growth-engine/production/STANDARDS.md` with every `readymerce-animation-ads` call
for an organic piece (`reel_animation`, `reel_animation_short`). The skill's method stays (belief ladder, THE PICTURE,
style bible, shot ledger, 12 shot-logic tests, sheets, storyboards, H3). Where this file or STANDARDS.md disagrees with
the skill, they win for organic posts. Built from the full read of animation-ads v3.6 (15 Oct 2026).

## 1. The skill's phases on the 16-step pipeline
| Skill phase | Pipeline step | Gate in the ledger | Who |
|---|---|---|---|
| 1 Inputs, GATE 1 avatar | 0 | G-BRIEF | Claude, from brain.json and the card |
| 2 Format, style, tiers, GATE 2 | 1 | G-IDEA | Claude (card's format, `story_template`, `animation_style`) |
| 3 Angle, picture, GATE 3 | 1 | G-IDEA | Claude; the picture passes the one-second read |
| 3b Hook Lab | 2 | G-HOOK | hook-agent + a fresh grader (adapters/hook-lab-organic.md) |
| 4 Script Lab, GATE 4 spine + hook | 3 | G-SCRIPT 85+, G-HUMAN-SPINE | script-agent; spine pick delegated with the reason |
| 5 Voice casting, pilot, VO, GATE 5 | 4 | G-BUDGET before the first voice call (STANDARDS 10), G-AUDIO-MASTER, G-HUMAN-VOICE, G-AUDIO per audio asset | owner listens once per series voice (audition + 15 s pilot); later episodes pass on the measured take checks |
| 6 Audio analysis | 5 | G-TIMELINE, G-AUDIO per slice | word map, line table, pause map, slices |
| 7 Shot logic + ledger | 6 | G-PLAN (the 12 tests in `qa/shot-logic.md`), G-SPEC per shot | visual-planner + fresh prompt-reviewer |
| 8 Style bible, sheets, GATE 6 | 7 | G-BUDGET before the first sheet, G-PROMPT-IMG and G-VIS-SHEET per sheet, G-HUMAN-LOOK once per series | on the client's LIB run (below) |
| 9 Storyboards, GATE 7 | 8 | G-PROMPT-IMG and G-VIS-BOARD per board, G-CONTINUITY, G-HUMAN-HOOKBOARD for the hook board | fresh visual-reviewer; the owner sees only the hook board |
| 10 Video | 9-10 | G-BUDGET at step 9 (re-prices the whole video; no video call before step 9 closes), G-PROMPT-VID per clip at step 10; R2 (G-HUMAN-TEST, about 80 credits) before the first lip-synced episode (STANDARDS 14) | the gate checks every call (STANDARDS 10) |
| 12 Edit (frame, drift, words) | 11-12 | G-TAKE per clip, G-ASSETS (step 11) | fresh take-reviewer: frames 1 per second, not one mid-shot frame |
| 13 QA, 14 package | 13-14 | G-FINAL, G-DIRECTOR, G-HUMAN-FINAL | take-reviewer final mode, the Organic Director, the owner on the hub |

## 2. Formats for a service business (the skill's F1 to F13)
| Skill format | Organic shape | Story template | Tier |
|---|---|---|---|
| F6 One-character story | A staged story, never a real client: "Arben runs a kitchen showroom in Durrës: with clients all day, posts a rushed photo at 23:00, and the phone stays quiet..." his accommodations, the named hidden cause, the same moment lived differently | `pov_day` | O60 |
| F2 Villain POV | The Boost button (a generic button, no platform UI; or the ghosting agency, the "post every day" myth) mocks the owner's fixes, then admits what it fears: the method | `hidden_villain` | O30 or O60 |
| F1 Talking part | "I'm your inbox. I've been full since Friday, and nobody opens me." It claims the signs, mocks the fixes, says what it needs | `object_speaks` | O30 |
| F7 Witness story | Framed as a POV, never told as something that happened: "POV: at a café you overhear the owner of the busiest clinic on the street: she posts less than you do." The habit, the lesson, the narrator tries it, people notice | `overheard` | O60 |
| F9 Absurd metaphor | One impossible picture (money poured into a bucket labelled Boost, holes in the bottom) + a 20 s explainer | (hook-first, no template) | O15/O30 |
| F3 Roll-call | The method's steps as characters, one job line each (save-bait explainer) | (teaching) | O30 |
| F5 X-ray explainer | Zoom into a clinic's enquiry path (the ad, the page and the inbox as separate pieces); show where enquiries leak | (teaching) | O30/O60 |
| F8 Personality reviewer | A sassy strategist rates tactics out of 10 (buying followers 1/10 ... a hook-first reel series 9/10: opinion scores, never results or data). Never real competitors | (debate) | O30 |
| F4 30-day timeline | "What happens if you answer every message with one question and a next step, for 30 days": a documented habit with real tracked data only, or not at all; never a speed promise | `pov_day` series | O60 |
| F13 Flat 2D explainer | A 3-step how-to ("how to answer a price DM without losing the sale") | (teaching) | O30 |
| F10 Mixed media | The owner's real face (real footage, decision D1) for the hook and proof, animation for the mechanism. No AI "clients" | | O60 |
| F11 Text story | On-screen text over one looping animated scene; cheapest | | O15/O30 |
| F12 Song | Use `adapters/song-organic.md` | `song_day` | O60 |

## 3. Styles and the recurring cast
- The style block comes from `config/organic.json` `animation_styles` (`claymation`, `crochet`, `family_film_3d`,
  `storybook_2d`) and goes word for word into every sheet, storyboard and clip prompt. Style names are looks: never a
  studio's characters, logos or names on screen or in a prompt (V24).
- From a style skill (e.g. `claymation`) take only its style block and motion notes. **Not its model routing**
  (STANDARDS 1, claymation row): clay images on Nano Banana 2; clay transitions on H3 keyframe mode with start and end
  images, Kling 3.0 only with G-FALLBACK; its "Seedance 1.5 Pro for transitions" default is banned.
- **Build the cast once per client and series** on a LIB run (`clients/<slug>/runs/<CODE>-LIB-<SERIES>/`): a mascot or
  hero, 2 or 3 recurring characters, 1 or 2 sets, and prop sheets for every story prop (the phone with the chat UI as
  `PR-PHONE-CHAT`, showing states, never counts or a platform's name; the booking calendar). `pipeline.py budget`
  (G-BUDGET) runs before the first sheet (STANDARDS 10). 4 to 7 sheets, each with a G-PROMPT-IMG PASS before its call,
  reviewed (G-VIS-SHEET, hero rules) and approved once (G-HUMAN-LOOK). Every episode references them: the first episode
  of a new cast adds about 15 credits for the sheets (section 4), later episodes don't.
- Image model: Nano Banana 2 at 2k for stylized sheets and storyboards until re-test R1 says otherwise (STANDARDS 1;
  GPT Image 2.5 makes them only inside the R1 test).

## 4. Words, lengths, shots, credits
- Tiers (seconds in STANDARDS 8): O60 for stories, O30 for the short (`reel_animation_short`, and the short cut of a
  tier A piece, written on its own: `adapters/script-lab-organic.md`). "No story under 55 s" is replaced by "no full
  discovery story under 45 s".
- Words at the narrator's measured pace (Albanian narrator: measure on the 15 s pilot; about 2.5 words/s before).
  One line = one breath = one picture, 4 to 17 words; lines over 4 s get two pictures.
- Shots: picture change every 2 to 4.5 s (median 3.5). In the first 5 s something changes every 1 to 1.5 s (STANDARDS
  5), so 3 to 5 changes in the first 5 s (a cut, or a move or state change starting inside the shot); the skill's "1 to
  3 pictures in the first 5 s" is overruled. O30 about 8 to 10 shots in 3 or 4 generations; O60 about 15 to 22 shots in
  6 to 9 generations. 1 to 3 shots per H3 take, 4 at most (STANDARDS 2); silent keyframe clips are one shot each.
- Credits (with the cast already built): O30 about 70 to 100; O60 about 150 to 220 (H3 2 per second plus storyboards
  plus 25%). First episode of a new cast: add about 15 for the sheets.

## 5. Copy and the close
- Rungs 9 to 12 (offer, guarantee, urgency) are out: one organic CTA rung that fits the card's job
  (`adapters/script-lab-organic.md`): follow for part 2, save, send to a business-owner friend, comment an answer to a
  question, or comment the live keyword (`book` and `dm` are convert asks; animation's jobs are reach and trust).
- The mechanism is named as a teachable method and given away (it earns saves); the agency is named lightly at the end
  ("this is how we do it for clients") or not at all. No brand, price or offer in the first 3 s.
- End card: the CTA, never a link, price, discount, guarantee, urgency or fine print (STANDARDS 5). AI label on per
  STANDARDS 7 (D1 decides whether to extend it).
- Facts only from the brain; no AI people as proof, testimony or "customers". No counts on screens, phones or in lines
  unless the number is in brain.json (screens show states: "a pile of unanswered messages"); no real platform logos or
  names on screen ("the inbox", "the phone"); stories in the brand's voice are clearly staged or framed as POV, never
  told as something that happened (STANDARDS 6 and 7).

## 6. Voice and checks
- `eleven_v4` for Albanian (not `eleven_multilingual_v2`, which the skill names for non-English: hub G8 wins).
- Gap codes (S 0.15, B 0.4, H 0.8 s) are minimums; `vo_build2.py`'s 0.4 s inner-pause cap is not applied.
- The take score (word errors, pace band, pitch range 7+ semitones, flat lines) runs with a multilingual
  faster-whisper model. Pace band per STANDARDS 4: 4.3 to 5.5 syllables/s is the English band; for the Albanian
  narrator the band is measured on the approved audition and written in that voice's G-HUMAN-VOICE note. If
  `vo_build2.py` can't be fetched, run the same checks in the Higgsfield sandbox.
- Every voice, slice and music asset gets `pipeline.py gate <slug> <post_id> G-AUDIO --status PASS --by <who> --asset
  <ID>@v<n> --note "..."` before it is a reference in an H3 call or step 11 (G-ASSETS) closes (STANDARDS 9).
- Clips: STANDARDS section 2 (5 to 15 s, slices 4 to 14 s with the interim duration rule, `declined_preset_id`, 2K,
  9:16); never speed up a lip-synced clip; silent moves are one-shot keyframe clips cut together in the edit; Kling 3.0
  or Sync Lipsync 3 only with G-FALLBACK.

## 7. Package (tier A)
Main cut (O60), short cut (O30, its own script and release, never a trim of the main script: AI-VIDEO-PIPELINE step 1),
3 hook variants as trial reels, a carousel that retells the piece: a normal carousel run per `carousel-machine-organic.md` (4:5 slides, G-VIS-SLIDE, G-SET); storyboard panels are never posted (STORY-FORMATS 5.5), 2 or 3 story frames, and an ad
version for the organic-to-paid loop (ORGANIC-OS 7.7).
