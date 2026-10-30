# Drama ads, organic adapter

Pass this file, the Post Card and `growth-engine/production/STANDARDS.md` with every `readymerce-drama-ads` call for an
organic piece (`reel_drama_pov`). The skill's method stays: templates, concept card, beat sheet, screenplay format,
shot list and its 15 rules, set bible, animatic, film test. Where this file or STANDARDS.md disagrees with the skill,
they win for organic posts (section 7). Built from drama-ads v2.2 (11 Oct 2026), `production/audit/drama-ads.json`
and `production/audit/skill-audit-2026-10-15.md`. "Line" means a SKILL.md line.

## 1. The skill's phases on the 16-step pipeline
The pipeline plans before assets (AI-VIDEO-PIPELINE 1): the shot list (skill 0a step 7) comes before the set bible.

| Skill phase (0a order, section) | Step | Gate in the ledger | Who |
|---|---|---|---|
| 1 Module 0, concept card (0, 3) | 0-1 | G-BRIEF, G-IDEA | Claude from brain.json and the card; the Organic Director checks Content Map fit |
| 2 Hook Lab in drama (7.4, X7, X8) | 2 | G-HOOK | hook-agent + a fresh grader (hook-lab-organic.md); concept frames are hero H-01 stills (G-PROMPT-IMG, G-VIS; `--hero`, STANDARDS 3), and the first one needs `pipeline.py budget` first (the run's first generation, STANDARDS 10) |
| 3 Screenplay, Script Lab gate (5) | 3 | G-SCRIPT 85+, G-HUMAN-SPINE | script-agent with script-lab-organic.md + the drama adapter (5.1 to 5.3); two fresh cold readers; spine pick delegated |
| 4 Voices, scene master, transcript (10) | 4 | G-AUDIO-MASTER, G-HUMAN-VOICE; G-AUDIO per voice asset | a G-BUDGET PASS from the last 24 h before the voices (STANDARDS 10); the owner listens once per character voice (audition + 15 s pilot), and that note records the voice's pace band (STANDARDS 4) |
| 4 Line table, packed stems (10) | 5 | G-TIMELINE; G-AUDIO per stem | Claude; stems 4 to 14 s (STANDARDS 2) |
| 5 Treatment, floor plan, 7 shot list + retention map (6, 8.2, 7.6, 7.7) | 6 | G-PLAN (15 rules + retention map), G-SPEC per shot | visual-planner + fresh prompt-reviewer |
| 6 Set bible (8.2) | 7 | G-PROMPT-IMG, G-VIS-SHEET per sheet, G-HUMAN-LOOK once per series | on the client's LIB run (section 3); `pipeline.py budget` before its first sheet |
| 8 Shot frames, frame QA (8.3) | 8 | G-PROMPT-IMG, G-VIS-BOARD per board, G-VIS per start frame, G-CONTINUITY | fresh visual-reviewer; frame QA 8.3.4 and VISUAL-QA 10.5 as extras |
| 9 Animatic (9) | 8 | G-CONTINUITY on its frame sheet, G-HUMAN-HOOKBOARD | the animatic and the cost estimate ride with the hook board in the queue (STANDARDS 9); that approval is the skill's "go" (line 522) |
| 10 Cost preflight (11.5) | 9 | G-BUDGET | `pipeline.py budget` re-prices the whole video after steps 0 to 8 close; no video call before step 9 closes (STANDARDS 10) |
| 11 Generation (11) | 10 | G-PROMPT-VID per clip; G-FALLBACK; G-EXCEPTION | the gate checks every call; still prompts (G-PROMPT-IMG) sit at steps 7 and 8 |
| 12 Per-take QA (11.6) | 11 | G-TAKE per clip, then G-ASSETS | fresh take-reviewer; G-ASSETS closes the step once every asset's latest version passed its gate (STANDARDS 9) |
| 13 to 20 Cut, score, sound, grade, mix, captions, export (12 to 15) | 12 | (none) | Claude; jump-cut re-check after every edit change (14.9b) |
| 21 Film test, score card (16) | 13 | G-FINAL (F1 to F8 + film test), G-DIRECTOR | fresh take-reviewer in final mode, then the Organic Director |
| 22 Deliver, series (17, 18) | 14-15 | G-HUMAN-FINAL, G-LEARN | the owner on the hub; the analyst at 72 h and 7 d |

On fail (replaces line 72): 3 FIX loops per script, then G-HUMAN-ESCALATE; 2 prompt loops, then the Organic Director;
3 asset attempts, then G-HUMAN-ESCALATE.

## 2. Templates for a service business (T1 to T13)
`reel_drama_pov` renders only `pov_day`, `two_days`, `overheard` (`confession_pov` needs real footage, so no AI-person
format renders it: STANDARDS 7). **POV day-in-the-life scenes are the main use.** The payoff is a change in what the hero
does or understands, never a result (STANDARDS 7).

| Template | Organic re-cast (StraightScale, AV-01) | story_template | Tier |
|---|---|---|---|
| T2 Someone else notices first | **Main use.** His daughter sees the unanswered messages on the deep red phone before he admits it ("Babi, e pe këtë mesazh?"). A fellow owner names the cause: pieces that don't work together. The same evening, lived differently | `pov_day` | O60 (short O30) |
| T12 The secret plan / the bet | The daughter bets her father that the people who wrote this week never heard back; he checks the phone; the bet teaches the cause. "The Bet" example facts (agency fee, "10 ditë", "1,800 ads", "afraid of delays", lines 172 to 191, 435) are not in the brain: structure only | `pov_day` | O60 |
| T13 The misjudgment | We judge an owner on his phone at his kid's dinner, then learn he is answering messages that came in while he worked all day, because his marketing pieces don't connect | `pov_day` | O60 |
| T5 The family dare | A kid dares the parent at the table, stake named by 6 s; comic wrong answers; the kid teaches the cause | `pov_day` | O60 |
| T4 The old-school archetype | A grandfather who sold on his name in the neighbourhood, beside the grandson paying several suppliers (brain AV-01, no count); same counter, two ways | `two_days` | O30 or O60 |
| T3 The viewer is the exhibit | A future museum guide shows visitors today's business page: boosted posts, nobody answering; the guide gives the cause | `overheard` | O30 or O60 |
| T7 Dramatic irony | Two owners at a café mock a third for spending an evening on how his pieces connect instead of boosting again; one calm line names the cause. No full calendar or numbers on him | `overheard` | O30 |
| T9 The moral dilemma | "Should he cut the price again to keep this client?" A fellow owner reverses the expected answer with the brain's false belief ("they compare me on price because my price is too high"). The paid ban (line 168) is lifted | `overheard` | O30 |
| T10 The quiet monologue | An owner's own voice over his night moments is a confession: someone's real story. It waits for the owner to film or record it (D7), never an AI owner | (waits for real footage) | |
| T1 The result causes trouble | Needs a documented client result (hub B15d); the proof bank is empty (B6 `not_held`) | (waits for proof) | O60 |
| T11 Fall, then rebuild | Needs real facts: becomes The Build or a real-owner story (D5), never AI people | (waits for proof) | O60 or O90 |
| T6 The old habit as a person | The boost button as a clingy partner: route to `reel_animation` (animation-organic.md); never a real competitor | `hidden_villain` (animation) | O30 |
| T8 The villain's point of view | The skill already sends it to animation (section 2) | `hidden_villain` or `object_speaks` (animation) | O30 or O60 |

Kept as method: the beat sheet (section 4, beats 1 to 9 and 11) for O60; the C45 shape for O30 (question, geography,
friction, the turn with the mechanism, payoff on a face, CTA); "man in a hole"; E16 (8 shots, about 20 s) as the O30
block; C1, C2 as density models; E17 as the closest `pov_day`; E11-D, E11-E as the cheapest; 7.2 as the opening menu.

## 3. Look, cast and reuse
- **People:** GPT Image 2 (`quality: high`, `resolution: 2k`) with a reference photo (STANDARDS 1), not the skill's
  "GPT Image 2 or Nano Banana Pro" (line 462). Stills are written as an iPhone 15 Pro photo with real skin texture
  (STANDARDS 3); the "shot on 35mm film" phrase bank (line 1265) stays out of image prompts (hub G7). The film look
  (one grade per act at 60 to 80%, 35mm grain 8 to 15%, a 0.3 to 0.6 px blur, the phone shadow floor) is an edit step.
- **Identity rule kept (8.2):** a person comes only from the location master plus their sheet; one match-on-action
  hop. Adjacent close-ups keep the same model and references in the same order (FL-12).
- **Set bible once per series** on `clients/straightscale/runs/SS-LIB-<SERIES>/`: floor plan, 16:9 location master,
  character sheets, anchor lines, a prop sheet per story prop (the brand's deep red smartphone, each screen state with
  exact text: a state, never a count), lighting bible, coverage plates from GPT Image 2 with the master as reference
  (STANDARDS 1; 3D Jutsu is a preset: owner-approved test first). G-VIS-SHEET at hero rules, G-HUMAN-LOOK once; the cast
  file (section 18) lives there.
- **Cast and truth:** lived-in, clearly different people in AV-01 places in Tirana (clinic reception, kitchen workshop,
  salon); 2 or 3 named background people. Every person is a composite in a clearly staged scene, never a real client,
  never a result; AI label on per STANDARDS 7 (D1 decides whether to extend it). **Until D1 (STANDARDS 7):** a
  character who could pass as a real owner (the hero, a fellow owner) is shown from behind, hands only, at a distance or
  as stylized animation. His lines play over those shots or over another character's reaction, so visible lip-sync goes
  only to a character who can't pass as a real owner (the daughter, a guide). Screens show states, not counts, and no
  real platform logo or name: "the inbox", "the phone" (STANDARDS 6, 8.3). Episodes reuse the bible (8.1).

## 4. Words, lengths, shots, credits
- **Tiers** (STANDARDS 8): O60 by default; O30 is one scene with one turn; O90 only with a stated reason; no O15 drama
  (a scene needs geography and a turn). The skill's S90 and C45 (line 108) are paid tiers.
- **Words:** runtime x (1 minus the no-dialogue share) x the measured pace (2.5 words/s before casting); no-dialogue
  share 25 to 40% (O60), 20 to 35% (O30): about 70 to 140 words for O60, 30 to 70 for O30. Core lines 3 to 10 words,
  none over 17, one turn up to 25; doubter questions 6 words or fewer; no two turns in a row; numbers as words.
- **Clips** (STANDARDS 2): H3 5 to 15 s; one speaker per generation; about 20 words per lip-synced clip, 10 per line,
  and a line over 10 words never on visible H3 lip-sync (play part of it over the listener); stems 4 to 14 s,
  `duration` = stem rounded up + 1 s (the skill's line 542 = the STANDARDS interim until R2). A lip-synced clip
  (reference mode) holds 2 to 3 shots, 4 at most, one camera move per shot. A silent shot is its own keyframe clip: one
  shot, rendered at 5 s and trimmed to its slot (X6).
- **Shots:** O60 16 to 24, O30 8 to 12, an average of 2 to 3 s (inside STANDARDS 5's 2 to 4.5 s, so a 45 s O60 holds
  21 shots at most); in the first 5 s a change every 1 to 1.5 s, so opening shots run 1 to 1.5 s (STANDARDS 5 has no
  drama exception to this). Visible lip-sync on 60% of lines at most: plan up to 3 or 4 lip-synced clips for O60, up to
  2 for O30. **R2 first:** the H3 duration re-test (about 80 credits, G-HUMAN-TEST) precedes the first lip-synced drama,
  in place of the 3-shot pilot (line 657).
- **Row to Shot Spec:** size, angle, lens → `camera`; blocking → `pose`, `action_physics`; eyeline → `eyeline`;
  continuity state → `continuity`, `props.state`; line → `line_text`; the shot's job → `must_read_in_1s`.

**The 15 shot-list rules (7.6), all kept; G-PLAN fails on any break.** 1. No two adjacent shots with the same size and
angle. 2. 50% or more of shots move, each with a named reason; never two frozen tableaux in a row. 3. Size mix (given
for S90, the target here): wides 15 to 20%, mediums and over-the-shoulders 25 to 30%, close-ups about 30%, inserts 20
to 25%. 4. Listener on screen 35 to 50% of dialogue time; visible lip-sync on 60% of lines at most. 5. Geography by 8 s
in every new scene; one marked turn per scene. 6. Screen side and eyeline per character per setting in every row.
7. Every row names its light source, true to the floor plan. 8. Adjacent shot lengths differ by 25% or more; cuts
quicken into the turn, then one held shot of 3 to 6 s. 9. One entrance or exit per scene; one prop business per
character. 10. Handles: "generate 5 to 8 s, use 2 to 4 s" becomes takes of 5 to 15 s with a 1.5 to 4 s window per
shot. 11. The 30-degree rule: the same subject twice in a row changes angle 30 degrees or size one step. 12. A change
every 2 to 4 s, every 1 to 1.5 s in the first 5 s, a new beat and sonic state about every 15 s. 13. The continuity
state column is filled for every row and copied into its frame and video prompts. 14. The person carrying the mechanism
never faces the lens. 15. Runtime fits the organic tier on the scene master before any frame. Plus 7.7: proof on screen
when a line states it (brain facts only), the payoff insert held 1.5 to 2.5 s, a new event in every 10 s window.

**Credits (Higgsfield, STANDARDS 10 prices; our computation).** Count clips from the shot list. A lip-synced clip
(reference mode, 2 to 3 shots) renders about 8 s (stem + 1 s) and gets 2 takes. Every other shot is a silent keyframe
clip at the 5 s floor with 1 take, and the hook clip gets a second take (STANDARDS 2). H3 at 2 credits/s. One image per
clip at 6.5 (GPT Image 2, 2k, high): a start frame per silent clip, a storyboard per lip-synced clip. Then +25%.
ElevenLabs is billed apart (about 177 per 4-take beat).

| Piece | Low end | High end |
|---|---|---|
| O30 | 20 s, 8 shots, no lip-sync: 8 silent clips (40 s) + the hook's second take (5 s) = 45 s (90) + 8 images (52) = 142, +25% = about 180 | 35 s, 12 shots, 2 lip-synced clips holding 4 of them: 8 silent clips (40 s) + 2 x 8 s x 2 takes (32 s) + 5 s = 77 s (154) + 10 images (65) = 219, +25% = about 275 |
| O60 | 45 s, 16 shots, 1 lip-synced clip holding 2: 14 silent clips (70 s) + 8 s x 2 takes (16 s) + 5 s = 91 s (182) + 15 images (98) = 280, +25% = about 350 | 75 s, 24 shots, 4 lip-synced clips holding 10: 14 silent clips (70 s) + 4 x 8 s x 2 takes (64 s) + 5 s = 139 s (278) + 18 images (117) = 395, +25% = about 495 |
| New cast, once per series | master, 2 sheets, a prop sheet, 2 plates: 6 x 6.5 = 39, +25% = about 50 | 8 stills: 52, +25% = about 65 |

With one shot per silent clip (STANDARDS 2) an O30 costs about 180 to 275 and an O60 about 350 to 495 (`organic.json`
gives `reel_drama_pov` 180 to 495), up to about 40% of the
1,300 monthly cap (brain.json). To spend less, cut silent shots (each one is a 5 s clip and a 6.5 still) or ship as
O30. The skill's 3,000 to 4,500 per S90 (line 656) assumes multi-model drafts and 3 to 4x the footage kept (line 1572);
log rendered against kept seconds on the first two episodes and correct this model.

## 5. Copy and the close
- Beat 10 (line 226) and check 10 (line 292) are deleted: no price, guarantee, scarcity or conversion on screen.
  **The "product" is the mechanism:** the cause line (Patchwork Marketing: pieces that don't work together) after 25%,
  the fix (one step of the Only Choice System) carried in after 40% and shown before it is named (5.3). StraightScale is
  named lightly on the end card at most. The "no logo test" becomes the insight test. Cause lines (ti, from the
  contrarian vault): "Nuk të duhet më shumë marketing. Të duhet marketing që punon bashkë." / "Reklamat e tua nuk po
  dështojnë. Mesazhet po humbasin pas klikimit."
- **One organic CTA fitted to the card's job** (the ORGANIC-OS list, STANDARDS 5): send ("Dërgoja një pronari
  biznesi."), follow ("Na ndiq për pjesën e dytë.", only when part 2 is planned), save ("Ruaje këtë postim."), comment
  (an answer to the dilemma the scene asks), the live keyword ("Shkruaj ANALIZA në komente.") or DM. The digest's
  "comment HOW / CALLS" keyword asks are out: no live funnel.
- The CTA line L-cuts over the button shot (7.7); the end card is a softened still of the story's final world with the
  CTA in large type, 2.5 to 3 s, music under it. No offer, no lead-form cue (line 441), no fine print. AI label on.
- Facts only from brain.json; the brand kit's Never list holds (no answer-time promise, no claim that we work the
  client's leads; we build them a system). Text hook: X7. Captions: 1 to 4 words, bold sans (STANDARDS 6, not the
  skill's sans or serif) with a soft shadow, no box, 80 to 100 px, 55 to 62% down, contrast 4.5:1, never over a face,
  key prop or screen, none over the silent opening; keywords stay white, not the skill's "warm yellow" and not gold
  (#DD9A10 is kept for the small counter, brand kit colours).
- The Instagram caption replaces primary text and headline (lines 911 to 914): a first line that passes Hook Lab, the
  dilemma as a question, the CTA, no offer; a pinned comment when the CTA is ANALIZA; marked for a native read.

### The two cold reads (X10, 5.4)
- **Listen read:** a fresh agent gets the persona card (AV-01 at night, phone in hand) and the spoken lines only, as
  "Voice 1", "Voice 2": the 5-sentence retell, the doubt left, "would you follow, save or send it?", the most confusing
  moment, who wanted what and who stood in the way, why the other person changed their mind, any moment it couldn't
  tell who spoke. Pass: it retells problem, cause, method, why it works, what to do; a missed fact goes into a line.
- **Picture read:** a second fresh agent gets the persona card, the V-beats and S-cues and the planned supers and
  caption keywords, no dialogue: a 5-sentence retell (who, want, obstacle, turn, change). Pass: it names want,
  obstacle, turn, change; else give the turn a visible action. It is also the sound-off read. New readers every loop.

## 6. Voice, audio and checks
- **Voices:** one locked `eleven_v4` voice per character (not "v3 or v4", line 528), cast from timbre, age, accent and
  pace; one audio tag per line; 4 takes per beat; a narrator close uses the StraightScale narrator
  `8oGKUMljR779HzpZBiE4` (its G-HUMAN-VOICE record is needed once, STANDARDS 9).
- **Takes:** reject no energy above 8 kHz, a wrong word or a rushed line (10.3), plus the STANDARDS take score. Pauses
  inside a line are never capped; turn gaps 0.08 to 0.3 s (0.08 to 0.2 s after the mechanism enters), overlaps 0.1 to
  0.2 s, gap codes S 0.15, B 0.4, H 0.8 s as minimums, pitch within 1.5 semitones per character across clips.
- **Transcript:** multilingual faster-whisper (`small` or `medium`, `language="sq"`) on the master and every
  lip-synced clip; spelling read against the script. **Stems:** per character, listening gaps 0.8 to 3 s, a 0.3 s head
  handle, a whole second, 4 to 14 s (STANDARDS 2), MP3; never split a line across clips.
- **Music and SFX:** `eleven_music_v2_5` on the cue sheet, 14 to 18 dB under the voice (STANDARDS 4), a hook bed 20 dB
  or more under with no melody; `eleven_text_to_sound_v2` with `duration_seconds` set; one bed per location; foley 3 to 6
  dB (featured) and 10 to 16 dB (touch) under dialogue peaks; the hook sound lands before the first line, never under it.
- **Mix:** clip audio muted; loudness per STANDARDS 4: -14 LUFS (±1), true peak -1 dBTP or lower, LRA 6 to 11 LU,
  short-term never above about -9 LUFS (the pass flag of `vqa_crops.py loudness`). No upscale for H3 (2K is above
  1080x1920; line 798 is for a Kling clip). **G-TAKE:** frames 1 per second (2 under 6 s) plus the first and last 0.1 s,
  face crops 190 px or more (STANDARDS 11); `vqa_crops.py drift` (cut at lag steps in pauses); retake only for drift
  inside a word, correlation under about 0.5, or a wrong word.
- **Frame rate:** 30 fps by default (STANDARDS 5). 24 fps may be chosen for the film look, written in the run at step
  6; then conform every clip, never interpolate dialogue, and redo the beat math (line 1419 is at 30 fps).
- **Safe zone** (STANDARDS 6, which took this zone from the skill for every reel): top 14% and bottom 35% clear plus
  the right 21% of the lower half, 6% side margins (40% at the bottom is the strict end); faces and key props 15 to 55%
  from the top, not the skill's 60%, because captions start at 55%.

### The 85/100 film test (section 16, at G-FINAL)
The fresh take-reviewer runs all 13 checks on every drama, not only "high-stakes work" (line 888): frame sheet, shot,
opening (X8), story, sound and music audits, transcript, loudness and gaps, facts against brain.json, the mute and
eyes-closed watches, the film test ("a clip from a series?"), continuity with the 90x160 jump-cut scan, retention.
G-FINAL adds (STANDARDS 9 and 11): frames every 1 s plus each cut's first and last frame, the sound-on watch, the
voice-alone listen, the banned-model check on the run's `calls.jsonl` and the phone shadow floor.

| Area | Points | Full marks (organic) |
|---|---|---|
| Hook (first 3 s) | 15 | A readable action with a real sound; the problem clear sound-off by 2 s; the first line by 1.5 s |
| Story and script | 15 | The Script Lab release holds on screen: question, turn, payoff, button |
| Picture / Continuity | 10 / 10 | One film in light, faces and coverage; no prop, wardrobe, position or eyeline break across a cut |
| Pacing and retention | 15 | 7.7 passes; no sag window; runtime inside the organic tier |
| Proof and payoff | 10 | Every brain fact shown when spoken; the payoff insert lands |
| Sound and music / Captions | 10 / 5 | Beds, foley, silence, cue map, -14 LUFS / 80 to 100 px, white keywords, inside the safe zone |
| Ending and CTA | 10 | The L-cut CTA, the final-world end card with one organic CTA, 2.5 to 3 s, no offer (line 884) |

Release at 85 or more with F1 to F8 passing; below 85, fix the lowest areas and re-render; then G-DIRECTOR.

## 7. What this adapter overrides in the skill, and why
**Exceptions X1 to X10 (0b, lines 114 to 128).** STANDARDS 7b is the rule; this table gives it in the skill's words.

| X | What it says | Organic |
|---|---|---|
| X1 | One speaker per lip-synced clip; fast exchanges from per-character stems with listening gaps, cut in the edit; a second character may be visible but silent | Adopt now (STANDARDS 2) |
| X2 | Removed in v2 ("they replace v1's X2", line 116); the hub's X2 "silent story-action clips" is stale | Nothing to adopt |
| X3 | Hook Lab gate 9 holds for the first 3 s; then a character may feel embarrassed, kept private and resolved by the payoff; no medical severity; the brand never mocks the hero | Adopt now (hook-lab-organic.md tone rules) |
| X4 | The hero may share the credit for a result, only when shown, at full strength, at most 2 credit lines | Not adopted: AI people carry no results; the proof bank is empty |
| X5 | Routing by shot type: H3 for lip-synced close-ups; Kling 3.0 and Omni, Seedance 2.5, Cinema Studio 4.0, Veo 3.1, Gemini Omni Flash for moving, silent, establishing, insert shots; Sync Lipsync 3 after the move | Waits for D9. Until then H3 for every shot; Kling 3.0 or Sync Lipsync 3 under G-FALLBACK; any other model under G-EXCEPTION from the owner, per asset |
| X6 | Silent shots are coverage (reactions, inserts, cutaways, establishing, entrances, exits), each with one job; mood b-roll still banned | Adopt now on H3 keyframe mode, one shot per clip (STANDARDS 2); other models for them wait for D9 |
| X7 | Text hook optional, off by default; if used, 6 words at most, small type, no box, never over a face, gone by 3 s | Adopt now (STANDARDS 6) |
| X8 | First line by 1.5 s (up to 4.0 s only after a strong readable action showing the problem sound-off within 1 s); a real sound by 0.3 s; a story event by 1.0 s; no greeting, title card or near-static shot in the first 4 s | Adopt now (AI-VIDEO-PIPELINE section 3), for drama only; 1.5 s also where the skill still says 4 s (lines 217, 283, 391, 842, 929) |
| X9 | No burned-in AI tag; Meta's disclosure when Meta asks; never claim the footage is real, live or a real customer | Adopt now in the STANDARDS 7 form: the label is always on |
| X10 | The story survives on mute; the selling facts survive listening only or ride on supers and captions; both cold reads pass | Adopt now (section 5) |

Characters who could pass as real owners follow STANDARDS 7's AI-people rule (section 3).

**Other overrides (STANDARDS.md wins on every number):**

| Skill (line) | Organic rule | Why |
|---|---|---|
| Silent shots to Kling; drafts on cheap tiers (567, 649) | H3 keyframe mode, one shot per clip; Kling only after an H3 frame-check fail; no drafts | STANDARDS 1-2; H3 Max takes no references (1491) |
| `declined_preset_id` only when Higgs names one (568) | The fixed id on every H3 and Kling call | Hub G1, STANDARDS 1 |
| H3 "4 to 15 s", reactions 4 to 5 s, stems to 15 s (1490, 555, 541) | Clips 5 to 15 s, stems 4 to 14 s | A 4 s render failed; stem + 1 s must fit 15 s (STANDARDS 2) |
| Music 10 to 18 dB, video-to-music, a kept clip sound (726, 730, 579) | 14 to 18 dB; `eleven_music_v2_5` (video-to-music needs G-EXCEPTION); clip audio muted | STANDARDS 1, 4, 5 |
| 24 fps; AI disclosure "when Meta asks" (799, 127) | 30 fps, 24 by choice; label always on | STANDARDS 5, 7 |
| Offer beat, conversion check, offer end card (226, 292, 441, 884) | One organic CTA, no offer | ORGANIC-OS 6.2 |
| Animatic waits for the user; fresh film-test agent for high stakes only (522, 888) | G-HUMAN-HOOKBOARD; fresh reviewers on every frame, take and final | VISUAL-QA 1, 6; STANDARDS 9 |
| T6 and T9 never lead a first test; S90 and C45 (168, 108) | Lifted (T6 to animation); O30 and O60 | Paid test rules; STANDARDS 8 |
| Primary text, ads, hook and hold rates (911 to 921); S90 at 3,000 to 4,500 credits (656) | Caption, trial reels, organic LEARN; section 4 budget | ORGANIC-OS 8.3, 9; one video model |
| End card 2 to 3 vs 2.5 to 3 s; window 2 to 4 vs 1.5 to 4 s (227, 442, 424, 672) | 2.5 to 3 s; 1.5 to 4 s | STANDARDS 5; the skill contradicts itself |

## 8. Package (tier A)
- Main cut (O60); a short (O30) with its own script and release, never trimmed (line 244), reusing the main cut's
  shots; 3 hook variants (first 3 to 4 s only) as trial reels; a carousel that retells the piece: a normal carousel run per `carousel-machine-organic.md` (4:5 slides, G-VIS-SLIDE, G-SET); storyboard panels are never posted (STORY-FORMATS 5.5); 2 or 3 story
  frames; an ad version with the ad CTA (ORGANIC-OS 7.7 rule 5), never posted organically.
- `runs/<post_id>/` holds the concept card, graded hook stacks, screenplay with release and cold reads, treatment, shot
  list with retention map, frame sheet, animatic, stem map, prompts, generation log, cue sheet, cut map, score card.
- Hub draft (`hub.py`) with notes "AI label: on"; nothing posts before G-HUMAN-FINAL; one tier A piece a week at most,
  on a proven angle or the month's wildcard (ORGANIC-OS 7.7).
- G-LEARN at 72 h and 7 d: skip rate, average watch time, sends, saves, follows and ANALIZA comments per reach. A drop
  where the mechanism enters means the bridge broke the spell (section 18); asks for part 2 flag a series. Lessons to
  `clients/straightscale/analytics/learnings.md`, the opening's result to the client's Hook Library.
