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
| 5 Voice casting, pilot, VO, GATE 5 | 4 | G-AUDIO-MASTER, G-HUMAN-VOICE | owner listens once per series voice (audition + 15 s pilot); later episodes pass on the measured take checks |
| 6 Audio analysis | 5 | G-TIMELINE | word map, line table, pause map, slices |
| 7 Shot logic + ledger | 6 | G-PLAN (the 12 tests in `qa/shot-logic.md`), G-SPEC per shot | visual-planner + fresh prompt-reviewer |
| 8 Style bible, sheets, GATE 6 | 7 | G-VIS-SHEET per sheet, G-HUMAN-LOOK once per series | on the client's LIB run (below) |
| 9 Storyboards, GATE 7 | 8 | G-VIS-BOARD per board, G-CONTINUITY, G-HUMAN-HOOKBOARD for the hook board | fresh visual-reviewer; the owner sees only the hook board |
| 10 Video | 9-10 | G-BUDGET, G-PROMPT-VID per clip | the gate checks every call |
| 12 Edit (frame, drift, words) | 11-12 | G-TAKE per clip | fresh take-reviewer: frames 1 per second, not one mid-shot frame |
| 13 QA, 14 package | 13-14 | G-FINAL, G-DIRECTOR, G-HUMAN-FINAL | take-reviewer final mode, the Organic Director, the owner on the hub |

## 2. Formats for a service business (the skill's F1 to F13)
| Skill format | Organic shape | Story template | Tier |
|---|---|---|---|
| F6 One-character story | "Arben runs a bakery in Durrës: up at 5, posts a blurry photo at 11, three likes..." his accommodations, the named hidden cause, the same moment lived differently | `pov_day` | O60 |
| F2 Villain POV | The Boost button (or the ghosting agency, the "post every day" myth) mocks the owner's fixes, then admits what it fears: the method | `hidden_villain` | O30 or O60 |
| F1 Talking part | "I'm your Instagram inbox. 14 unanswered DMs since Friday." It claims the signs, mocks the fixes, says what it needs | `object_speaks` | O30 |
| F7 Witness story | "The busiest restaurant in Tirana posts less than you do." The habit, the lesson, the narrator tries it, people notice | `overheard` | O60 |
| F9 Absurd metaphor | One impossible picture (money poured into a bucket labelled Boost, holes in the bottom) + a 20 s explainer | (hook-first, no template) | O15/O30 |
| F3 Roll-call | The method's steps as characters, one job line each (save-bait explainer) | (teaching) | O30 |
| F5 X-ray explainer | Zoom into a shop's Instagram funnel; show where followers leak | (teaching) | O30/O60 |
| F8 Personality reviewer | A sassy strategist rates tactics out of 10 (buying followers 1/10 ... a hook-first reel series 9/10). Never real competitors | (debate) | O30 |
| F4 30-day timeline | "What happens if you answer every DM within 5 minutes for 30 days": real tracked data only, or not at all | `pov_day` series | O60 |
| F13 Flat 2D explainer | A 3-step how-to ("how to answer a price DM without losing the sale") | (teaching) | O30 |
| F10 Mixed media | The owner's real face for the hook and proof, animation for the mechanism. No AI "clients" | | O60 |
| F11 Text story | On-screen text over one looping animated scene; cheapest | | O15/O30 |
| F12 Song | Use `adapters/song-organic.md` | `song_day` | O60 |

## 3. Styles and the recurring cast
- The style block comes from `config/organic.json` `animation_styles` (claymation, crochet, 3D family-film, 2D
  storybook) and goes word for word into every sheet, storyboard and clip prompt. Style names are looks: never a
  studio's characters, logos or names on screen (V24).
- From a style skill (e.g. `claymation`) take only its style block and motion notes. **Not its model routing**: its
  "Seedance 1.5 Pro for transitions" default is banned (STANDARDS section 1).
- **Build the cast once per client and series** on a LIB run (`clients/<slug>/runs/<CODE>-LIB-<SERIES>/`): a mascot or
  hero, 2 or 3 recurring characters, 1 or 2 sets, and prop sheets for every story prop (the phone with the chat UI as
  `PR-PHONE-CHAT`, the booking calendar). 4 to 7 sheets, reviewed (G-VIS-SHEET, hero rules) and approved once
  (G-HUMAN-LOOK). Every episode references them, so episode 2 on costs about a third less.
- Image model: Nano Banana 2 at 2k for stylized sheets and storyboards until re-test R1 says otherwise.

## 4. Words, lengths, shots, credits
- Tiers: O60 (45 to 75 s) for stories, O30 (20 to 35 s) for the short (`reel_animation_short`). "No story under 55 s"
  is replaced by "no full discovery story under 45 s".
- Words at the narrator's measured pace (Albanian narrator: measure on the 15 s pilot; about 2.5 words/s before).
  One line = one breath = one picture, 4 to 17 words; lines over 4 s get two pictures.
- Shots: picture change every 2 to 4.5 s (median 3.5), 1 to 3 pictures in the first 5 s. O30 about 8 to 10 shots in
  3 or 4 generations; O60 about 15 to 22 shots in 6 to 9 generations. 2 to 3 shots per H3 take, 4 at most.
- Credits (with the cast already built): O30 about 70 to 100; O60 about 150 to 220 (H3 2 per second plus storyboards
  plus 25%). First episode of a new cast: add about 15 for the sheets.

## 5. Copy and the close
- Rungs 9 to 12 (offer, guarantee, urgency) are out: one organic CTA rung that fits the card's job (follow for part 2,
  save, send to a business-owner friend, comment the live keyword).
- The mechanism is named as a teachable method and given away (it earns saves); the agency is named lightly at the end
  ("this is how we do it for clients") or not at all. No brand, price or offer in the first 3 s.
- End card: the CTA, never an offer, a guarantee or fine print. AI label on (STANDARDS section 7).
- Facts only from the brain; no AI people as proof, testimony or "customers".

## 6. Voice and checks
- `eleven_v4` for Albanian (not `eleven_multilingual_v2`, which the skill names for non-English: hub G8 wins).
- Gap codes (S 0.15, B 0.4, H 0.8 s) are minimums; `vo_build2.py`'s 0.4 s inner-pause cap is not applied.
- The take score (word errors, pace band from the audition, pitch range 7+ semitones, flat lines) runs with a
  multilingual faster-whisper model; the English pace band (4.3 to 5.5 syllables/s) is replaced by the band measured on
  the audition. If `vo_build2.py` can't be fetched, run the same checks in the Higgsfield sandbox.
- Clips: STANDARDS section 2 (5 to 15 s, the interim duration rule, `declined_preset_id`, 2K, 9:16); never speed up a
  lip-synced clip; keyframe chains for silent moves; Kling 3.0 or Sync Lipsync 3 only with G-FALLBACK.

## 7. Package (tier A)
Main cut (O60), short cut (O30), 3 hook variants as trial reels, a carousel from the storyboard panels or stills, 2 or
3 story frames, and an ad version for the organic-to-paid loop (ORGANIC-OS 7.7).
