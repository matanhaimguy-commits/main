# Podcast ads, organic adapter

Pass this file, the Post Card and `growth-engine/production/STANDARDS.md` with every `readymerce-podcast-ads` call for an
organic piece (`reel_podcast`, story template `podcast_disagreement`). The skill's method stays: Pinterest references and
their score, the one master two-shot, one start frame per host made only from it, the speaker map, packed stems, the H3
prompt and behaviour lock, the take reject list, the cut map. Where this file or STANDARDS.md disagrees with the skill,
they win (section 7). Built from podcast-ads v5.0 and `production/audit/` (`podcast-ads.json`,
`skill-audit-2026-10-15.md`). "Line" means a SKILL.md line.

## 1. The skill's phases on the 16-step pipeline
Sound comes before pictures: the voices, the conversation master (skill 6b) and the transcript check (skill section 10,
printed after generation, line 431) all run at step 4, before any image or clip.

| Skill phase (section) | Step | Gate in the ledger | Who |
|---|---|---|---|
| Module 0, autonomy rule (0) | 0 | G-BRIEF | Claude, from brain.json and the card; a missing fact stops the run |
| The disagreement: A's belief against B's cause (2, rules 2 and 5) | 1 | G-IDEA | Claude; the Organic Director checks Content Map fit and that the disagreement is real (section 3) |
| Title bar + cold-open line 1 (2 rule 3, 11.11) | 2 | G-HOOK | hook-agent + a fresh grader (hook-lab-organic.md); Hook Lab is required, not "if it ran" (line 60) |
| Write the conversation, Script Lab 18c (2, 2b) | 3 | G-SCRIPT 85+, G-HUMAN-SPINE | script-agent with script-lab-organic.md; listen and sound-off cold reads by fresh agents; spine pick delegated with the reason |
| Casting cards (voice part), voices, master, transcript check (3, 6b, 10) | 4 | G-AUDIO-MASTER, G-HUMAN-VOICE; G-AUDIO per voice asset | `pipeline.py budget` first: the voices are the run's first generation (STANDARDS 10). The owner listens once per new voice (audition + 15 s pilot); that note records the voice's pace band (STANDARDS 4) |
| Packed stems, speaker map (6b.5, 7) | 5 | G-TIMELINE; G-AUDIO per stem | Claude: line table, stem map, every stem 4 to 14 s and every clip 5 to 15 s (STANDARDS 2) |
| Frame plan, one Shot Spec per clip, cut plan (6) | 6 | G-PLAN, G-SPEC per clip | visual-planner + fresh prompt-reviewer |
| Set card, Pinterest, master two-shot F0 (3, 4, 5.1) | 7 | G-PROMPT-IMG, G-VIS-SHEET (hero), G-HUMAN-LOOK once per series | on the LIB run (`pipeline.py budget` before its first image, STANDARDS 10); fresh visual-reviewer |
| Start frames F1, F2 (5.2, 5.4) | 8 | G-PROMPT-IMG, G-VIS-BOARD (hero rules), G-CONTINUITY, G-HUMAN-HOOKBOARD | fresh visual-reviewer; the owner sees the line-1 host's frame with the title bar |
| Budget preflight (7.5) | 9 | G-BUDGET | `pipeline.py budget` re-prices the whole video after steps 0 to 8 close; no video call before step 9 closes (STANDARDS 10); balance re-checked right before submit |
| Prompt per clip, one batch (8, 9.1) | 10 | G-PROMPT-VID per clip | the gate checks every call |
| Take sheets, reject list, pitch, drift (9) | 11 | G-TAKE per clip, then G-ASSETS | fresh take-reviewer; G-ASSETS closes the step once every asset's latest version passed its gate (STANDARDS 9) |
| Cut map, edit (11) | 12 | (none) | Claude |
| QA before delivery (14) | 13 | G-FINAL, G-DIRECTOR | take-reviewer in final mode, then the Organic Director |
| Hook variants, package (12, 15) | 14 | G-HUMAN-FINAL | the owner on the hub |
| LEARN (0b item 6) | 15 | G-LEARN | analyst at 72 h and 7 d |

On fail (replaces line 43): 3 FIX loops per script, then G-HUMAN-ESCALATE; 2 prompt loops, then the Organic Director;
3 asset attempts, then G-HUMAN-ESCALATE, also when every Pinterest route fails (line 185). Sync Lipsync 3 after a failed
split needs G-FALLBACK; other models G-EXCEPTION.

## 2. Structures for a service business
| Skill structure | Organic re-cast | Format · story_template | Tier |
|---|---|---|---|
| PC-2H two-host cold open (lines 80 to 93) | **Main use.** A opens on the owner's common belief in the avatar's words, B disagrees with a position from the brain, B's picture line names the cause, A gets it, CTA. Beats 6, 8 and 10 change (section 5) | `reel_podcast` · `podcast_disagreement` | C45 |
| PC-3P panel (line 114) | A host asks; one guest holds the common belief, one holds the cause. One more casting card, photo, start frame and set of clips | `reel_podcast` · `podcast_disagreement` | C45 |
| PC-HV hook variants (section 12) | 3 openings cut from the same clips, run as trial reels; no line plays twice | variants of the card | C45 each |
| PC-SOLO solo creator (section 13) | An owner's day in 1 to 3 settings: route to `ugc-talking-head-organic.md`. Until D1 an AI owner is shown from behind, hands only or at a distance, never talking to the lens (STANDARDS 7) | `reel_ugc_pov` · `pov_day` (`confession_pov` needs real footage: the owner films) | O30 or O60 |
| PC-L150 long cut (line 75), or a 20 to 30 s two-host cut | Not made: C45 is the one range for conversations (STANDARDS 8), and 2 to 3 min is over O90. Owner decision | | |

**C45 beats for `podcast_disagreement`** (STORY-FORMATS 3.8 laid over the skill's 10 beats):

| s | Turns | Beat | Skill beats it replaces |
|---|---|---|---|
| 0 to 4 | 1-2 | A states the common belief to "ti" or in the third person (never as "I, the owner"), the avatar's world named; B disagrees in a few words | 1, 2 |
| 4 to 14 | 3-4 | A's case: what the owner pays for and what he tried (brain `tried`, `words`) | 3 |
| 14 to 26 | 5-6 | B's case: the hidden cause in one picture line, then its name (Patchwork Marketing) | 4, 6 |
| 26 to 36 | 7-8 | A gets it; his line ends on a payoff phrase of 6 words or fewer | 5, 7, 10 |
| 36 to 42 | 9-10 | B: the method in one line, then the organic CTA | 8, 9 |
| 42 to 45 | | End card (2.5 to 3 s), no speech (section 4 word budget) | |

**StraightScale example** (STORY-FORMATS pilot 3: B5, trust, CTA ANALIZA, 10 turns, about 90 words; native read first).
Title bar: "Agjenci tjetër apo një sistem?" A: "Nëse nuk të bie telefoni, merr një agjenci më të mirë." B: "Jo. Merr
pjesë që punojnë bashkë." A: "Pronari paguan reklama, faqe, dikë për postimet." B: "Pikërisht. Çdo pjesë punon vetëm.
Askush nuk i lidh." A: "Po mesazhet që i vijnë kur është në punë?" B: "Mbeten mes pjesëve. Ky është Patchwork
Marketing." A: "Pra një agjenci tjetër do t'i shiste edhe një pjesë." B, to the viewer: "Po. Të duhet sistemi i plotë,
duke filluar nga blerësit e tu." A: "Nga fillon?" B: the method line + "Komento ANALIZA dhe të shkruajmë në DM." Host A
argues the owner's belief to "ti" or in the third person, never as "I, the owner"; the three A lines changed on 16 Oct
need the native read first. The five steps have no Albanian names yet: until the owner gives them, the method line is C1
("Nuk të duhet më shumë marketing...").

## 3. Look, cast and reuse
**Who is on screen (truth first).**
- StraightScale has no real hosts (`visual.face: ai_character`, `real_footage: false`). The AI hosts are presenters of a
  staged conversation, never owners, clients, customers or reviewers. Host A argues the common belief (brain
  `false_beliefs`, `tried`, avatar `words`) to "ti" or in the third person ("the owner pays for..."), never as "I, the
  owner" or "my clients"; host B holds a vault position (C1 to C5) and the mechanism. Neither names a real business,
  says StraightScale worked for them, or carries a result or a number (the proof bank has none). AI label on per
  STANDARDS 7 (D1 decides whether to extend it).
- **D1 first** (STANDARDS 7): until D1 is decided, AI podcast hosts are shown only from behind, hands only, at a
  distance or as stylized animation. This format needs two faces and is built to pass as a real podcast (5.4 check 7),
  so pilot 3 needs "D1 decided (faces on screen)". Until then a podcast card runs steps 0 to 3 only: no voice, image or
  clip.
- **Waits for D7** (the owner's 15 to 20 minute voice note): episodes on what clients always ask or what everyone gets
  wrong; lines told as the owner's or team's own experience; a host saying owners keep arguing this (pilot 3); a real
  voice in place of an AI host. Case stories wait for proof (B6 `not_held`, D5); analysis lines wait for D3.
- **A real disagreement** (organic.json): A's belief is one the avatar holds, argued in his words, not a straw man; B
  answers with a vault position; A turns because of B's picture line, not because he gives up. Nobody lectures (60% cap).

**References and frames (the skill's method, kept).**
- Casting card per host and a set card (section 3): AV-01's age band (35 to 60), Albanian, everyday business clothes,
  hosts clearly different; voice description = timbre, age, gender, accent, pace only (line 158). Set: a small podcast
  table in Tirana after dark (brain `visual.set`), dynamic mics, 3 to 5 real props, the brand's deep red phone face down
  (no screen, no text to go wrong: FL-10); no logos, show sign or screens with text.
- Pinterest (4.1 to 4.4): 3 to 5 searches per host, 3 for the set, 15 to 30 image URLs each (Apify, then the built-in
  browser, then Firecrawl); contact sheets of about 12; the 8 points scored 0 to 2 (candid, ordinary light, real skin,
  matches the card, wardrobe fits, clean, face clear near eye level, a real photo: not AI, stock or famous); keep 13+ of
  16; reject on sight per line 204. One photo per host plus a backup never attached with it; an empty set photo;
  `media_import_url`; the reference board. **Organic adds** a fresh visual-reviewer who re-scores pick and backup blind;
  each pick is registered on the LIB run as a `still` with that verdict as its G-VIS.
- **F0, the master two-shot:** GPT Image 2 (`quality: high`, `resolution: 2k`, media role `image`), 16:9, attached: the
  empty set photo + one photo per host; never shown. "Create new, different people. Do not copy the reference people's
  faces." goes in this prompt only (4.5). A `character_sheet` on the LIB run (hero by type): G-VIS-SHEET at hero rules
  (zero defects, 5.4 check 3 included), then G-HUMAN-LOOK.
- **Likeness check (organic adds; VISUAL-QA V24: no real people unless approved):** at G-VIS-SHEET the fresh
  visual-reviewer opens F0 beside every host reference photo (pick and backup) and fails F0 as critical when a face could
  be taken for the reference person. The same check runs on F1 and F2 at G-VIS-BOARD. A fail is a new F0 attempt (an
  edit pass on the face counts as one, STANDARDS 1 and 9), never a waiver.
- **F1, F2:** one 9:16 medium close-up per host, F0 the only attachment (5.2): calm, eyes on the friend, hands resting,
  the face 15 to 55% from the top (STANDARDS 6), head below the title-bar band (top third, under the top 14%), mouth
  above the caption band (above the bottom 35%).
  **For the gate they are storyboards:** a talking clip needs a storyboard as image 1 (VISUAL-QA 6, `pipeline.py
  check-call`) and the skill allows one image per clip (line 364): `pipeline.py asset <slug> <post_id> F1 --type
  storyboard` (every storyboard is hero, STANDARDS 3; add `--hook` for the line-1 host); hero rules plus 5.4 checks;
  G-CONTINUITY over F0, F1, F2.
- Frame plan: hosts + 1 images (line 291). A frame that drifts twice becomes the upscaled crop of F0 (line 228).
- **Concept frame (exception to hook-lab-organic.md):** a concept still of a host is a second image of that person (line
  30), so the fresh grader reads the H-01 Shot Spec (episode 1) or the approved F1 with the new title bar. Pilot 3's "two
  hosts, host A leaning in" puts F0 on screen (line 233) and breaks the behaviour lock: frame 1 is host A's calm F1.

**Reuse.** Once per series on `clients/straightscale/runs/SS-LIB-PODCAST/`: cards, reference board, F0, F1, F2, voice
IDs. Each episode registers the same F1 and F2 media as its storyboards (`pipeline.py media ... --id`), reviewed with its
own title bar; dry-run the first clip with `pipeline.py check-call`. A new wardrobe, room or host is a new G-HUMAN-LOOK.

## 4. Words, lengths, shots, credits
- **Length:** C45 per STANDARDS 8 (35 to 45 s, 8 to 12 turns, 80 to 110 words; Script Lab test 14 counts against it).
  **The word budget that fits (our computation):** speech time = runtime minus the end card (2.5 to 3 s) minus the turn
  gaps (7 to 11 gaps of 0.08 to 0.2 s, up to about 2 s). At 45 s: 45 - 3 - 2.2 = about 40 s of speech, about 100 words
  at 2.5 words/s. At 35 s: 35 - 3 - 1.4 = about 31 s, about 77 words, so 80 words need about 36 s. Write 80 to 100 words
  before casting; the top of STANDARDS 8's range (110) fits only when the cast voices measure about 2.75 words/s or
  faster (110 words in 40 s). After casting, each voice's measured pace sets the budget (STANDARDS 4). This is why the
  beat table ends the last turn at 42 s.
- **Turns** (STANDARDS 8, from lines 66 to 68): 20 words or fewer, one turn up to 25; the listener speaks every other
  turn and at least every 8 s; no host has two turns in a row or more than 60% of the words; core lines under 12 words,
  none over 17 (line 42). Numbers as words with a noun between two numbers (line 78); StraightScale has no numbers to
  use.
- **Speaker map** (section 7 with STANDARDS 2): one host per clip, that host's lines in script order, never a line
  split. Stem (the slice) = the lines joined by 0.8 to 1.0 s listening beats + about 1 s tail, padded to a whole second,
  **4 to 14 s**; `duration` = stem + 1 s on top of the tail, within 5 to 15 (interim until R2). A stem under 4 s folds
  its pull lines into that host's other clip (line 353). Words per clip come from time (STANDARDS 2, podcast row): about
  27 to 30 at 2.5 words/s (proposed, confirm on first run); the skill's 30 to 35 (line 337) is a ceiling. Two hosts: 4
  to 6 clips.
- **Shots:** one continuous shot per take, static camera locked to the start frame (lines 373, 379), inside STANDARDS'
  4 at most; the second camera is a punch-in in the edit, never a new image. Motion in the first second; in the first
  5 s a change every 1 to 1.5 s (angle A, punch-in B at 112 to 118%, a 0.8 to 1.5 s listener reaction); then every 2 to
  4.5 s; a reaction shot at least every 10 s (STANDARDS 5, line 455). Never cut a pause out of one take in the same
  framing (line 454).
- **G-PLAN passes when:** images = hosts + 1; every clip holds one host at 5 to 15 s; no line is split; the cut plan
  meets the change and reaction rules; one Shot Spec per clip (`format: podcast`, hands, props, `text_in_image: none`,
  static medium close-up at chest height, 9:16, safe zones, `must_read_in_1s`), the line-1 clip with `hero: true`.

**Credits** (STANDARDS 10 prices). Video seconds = speech seconds + 3 to 4 s per clip (a beat, the tail, padding, the
+1 s duration), at 2 credits/s; 2 takes of every clip, as every clip talks (STANDARDS 2); then +25% for retakes. Speech
seconds come from the length bullet: 32 s for 80 words, about 40 s at most (the 45 s cut).

| Piece | Low end | High end |
|---|---|---|
| Episode, cast built | 80 words, 4 clips: 32 + 4x3 = 44 s; 2 takes = 88 s = 176; +25% = **about 220** | 45 s cut (about 40 s of speech), 6 clips: 40 + 6x4 = 64 s; 2 takes = 128 s = 256; +25% = **about 320** |
| New cast, once per series | F0, F1, F2 at 6.5 (GPT Image 2, 2k, high) = 19.5; +25% = **about 25** | 3 hosts, 4 images = 26; +25% = **about 33** (the skill's "two retakes per frame", line 359: about 60 to 80) |
| Once, before the first talking piece | R2 duration re-test, about 80 (G-HUMAN-TEST) | |
| ElevenLabs credits | about 177 per 4-take beat; one beat per host = about 350 | two beats per host = about 710 |

An episode is 220 to 320 (`organic.json` `reel_podcast`), at most about a quarter of the 1,300 monthly cap; one take
per clip would be 110 to 160.

## 5. Copy and the close
- **Out:** the end card's offer, cost line and URL (line 467); "offer before the CTA" (line 42); a guarantee or prices in
  a friend's mouth (line 124); hedged numbers (line 125); the brand as a friend's tip with a lived result (beats 6, 8,
  10; lines 71 to 73, 89 to 93). The example payoff "every message gets an answer in minutes" (line 110) is banned.
- **In:** the "product" is the method: B names the cause after A's case, then one line of the Only Choice System.
  StraightScale is named lightly or not at all; if spoken, write "Strejt Skejl" for ElevenLabs (line 410).
- **One organic CTA** from the ORGANIC-OS list (STANDARDS 5) that fits the card's job, spoken by B in the last turn and
  on the end card. Trust: save ("Ruaje këtë postim."), follow, send, comment (an answer to the episode's question: which
  host is right), or the live keyword. Convert: "Komento ANALIZA dhe të shkruajmë në DM." or DM; "book" is said only as
  this path (the booking button comes in the DM, brand kit "One path"), never as a link. ANALIZA is the only live
  keyword (PATCHWORK and HARTA wait for flows). No price, offer, guarantee, urgency, "falas" or "45 minuta": the DM
  carries the next step. Never "we answer within 1 hour", never "we chase your leads".
- **End card** 2.5 to 3 s: the CTA in large type, music under it, the real logo file only; no offer, URL or fine print.
- **Instagram caption** instead of primary text and headlines (line 525): hook line, the disagreement as a question, the
  CTA; a pinned comment for ANALIZA. "Ti" (D2 interim); all Albanian marked for a native read; facts checked at the cold
  read.

## 6. Voice, audio and checks
- **Voices:** one locked `eleven_v4` voice per host (`eleven_v3` auditioned beside it), clearly different (line 296).
  Host B may use the strategist voice `8oGKUMljR779HzpZBiE4`; host A needs a new voice and G-HUMAN-VOICE (audition + 15
  s pilot). One low-intensity tag per line; a laugh only on "(small laugh)" (line 406); negations in full (hub G8).
- **Takes:** beats of 2 to 7 lines, 4 takes each, picked on every word, pause spread SD 0.1 s or more (at least one
  pause of 0.45 s or more per 3 sentence ends, STANDARDS 4, proposed) and a moving pitch. Pauses are never capped:
  `vo_build2.py` (line 295) is not used (0.4 s cap, no overlaps, one stem per speaker). Never speed a voice past 1.05x.
- **Conversation master:** script order, turn gaps 0.08 to 0.2 s (inside STANDARDS 4 and 5), a 0.1 to 0.2 s overlap now
  and then, pitch within 1.5 semitones per host, every line timed in the line table. The edit never retimes it.
- **Transcript check before any image or clip:** Scribe or faster-whisper `small`/`medium` with `language="sq"`, word for
  word, spelling read against the script; a bad line is regenerated and master and stems rebuilt. Clips: T8 at G-TAKE.
- **H3 call:** `minimax_h3`, `"2K"`, `"9:16"`, `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"` (missing in
  the skill, line 364); image 1 = the host's start frame (its storyboard), audio 1 = the packed stem; nothing else.
- **Prompt:** the section 8 text on the 9-part card (VISUAL-QA 4.2): realism; reference per token; one panel, one
  continuous shot; hands resting on the table or mug; line time spans, one softened tone note of 5 words or fewer each;
  background object motion (steam, a curtain), never other people (the skill's own prompt, line 389: "No other people
  appear"; STANDARDS 2 prompt card row); the lip-sync block with beat times and "use `<<<audio_1>>>` exactly, word for
  word, at the same timing"; the behaviour lock (line 375); no cinematic words (247).
- **G-TAKE:** frames 1 per second (2 under 6 s) plus first and last 0.1 s, face crops 190 px or more; T1 to T9 plus the
  reject list in used lines (lines 418 to 423: lens look, profile, eyes down or shut over 1 s, gestures, a smile on a
  problem line, frozen over 4 s, drift from the start frame). `vqa_crops.py drift`, fixed in the edit; retake only for
  drift inside a used word or correlation under about 0.5, as the same prompt plus one fix with its own G-PROMPT-VID.
- **Edit from the cut map** (one row per line: clip, in, out, angle A or punch-in B, reaction over it; line 440): clips
  muted, the master the only audio (line 439); in 0.08 s before onset, out 0.12 to 0.2 s after (line 452); J-cuts of 0.1
  to 0.2 s; line spread under 2 dB, 20 to 80 ms fades, very low room tone; loudness per STANDARDS 4 (-14 LUFS ±1, true
  peak -1 dBTP or lower, the range and short-term limits: the pass flag of `vqa_crops.py loudness`); 30 fps, H.264 High
  1080x1920, AAC 48 kHz. Native framing (line 458) is its own crop step.
- **Title bar** = the text hook, per STANDARDS 6's podcast title bar row: 4 to 8 words, 2 lines at most, about 44 to
  50 px type at 1080 wide, top third below the top 14%, frame 1 to about 3 s, over no head; then only an optional label
  of 6 words or fewer. No burned-in tag, which also clears the top-left clash (line 468).
- **Captions** per STANDARDS 6 (podcast 1 to 3 words, 80 to 100 px, about 55 to 62% down): bold white sans with
  outline, contrast 4.5:1+, word-timed, clamped to their line's segment (line 463), no gap over 0.4 s in speech, above
  the bottom 35%, out of the right 21% of the lower half, inside the 6% side margins.
- **G-FINAL** (STANDARDS 9): frames every 1.5 s plus every cut (`vqa_crops.py final`), F1 to F8, the sound-off and
  sound-on watches, the voice-alone listen, the banned-model check on the run's `calls.jsonl`, plus the skill's tables
  (lines 496 to 502): pitch, line spread under 2 dB, seams 0.08 to 0.35 s, hook and conversation checks, each caption on
  the speaking face; AI label (V26, F7). G-DIRECTOR: is the disagreement real, does the CTA fit the job.

## 7. What this adapter overrides in the skill, and why
| Skill (line) | Organic rule | Why |
|---|---|---|
| "AI DRAMATIZATION" tag burned in top-left (33, 468) | No burned tag; Instagram's AI label on; hub notes "AI label: on" | STANDARDS 7 |
| Card C45 = 40 to 50 s (40) | 35 to 45 s, 8 to 12 turns, 80 to 110 words (80 to 100 at 2.5 words/s, section 4) | STANDARDS 8 |
| About -16 LUFS, true peak -1.5 (299, 457, 470) | -14 LUFS (±1), true peak -1 dBTP or lower; the 2 dB line spread stays | STANDARDS 4 |
| Duration = padded stem, stems to 15 s, 30 to 35 words (300, 336, 337, 364) | Stem 4 to 14 s, duration = stem + 1 s; words sized by time (about 27 to 30); beats join lines, the tail follows the last | STANDARDS 2 interim (R2); lines 300 and 336 disagree |
| Full autonomy, no human gate (32); "the user decides" (43) | G-HUMAN-LOOK, G-HUMAN-VOICE, G-HUMAN-HOOKBOARD, G-HUMAN-FINAL; G-HUMAN-ESCALATE | Nothing posts without approval (CLAUDE.md); AI-VIDEO-PIPELINE 4 |
| Self-review of picks, frames, takes and final (4.3, 5.4, 9, 14) | Fresh visual, prompt and take reviewers; the skill's checks become their extras; the likeness check on F0, F1, F2 | VISUAL-QA 1, V24 |
| Hook Lab optional (60) | Required; every channel A or A+; a fresh grader | hook-lab-organic.md, STANDARDS 9 |
| Transcript check after generation (431); clip audio not transcribed (435) | At step 4, before any image or clip; every clip transcribed at G-TAKE | AI-VIDEO-PIPELINE 1, STANDARDS 4 |
| Voice method and builder from animation Phase 5 (295) | `vo_build2.py` not used; pauses never capped; overlaps kept | STANDARDS 4 (issue 8) |
| Gaps 0.08 to 0.3, 0.08 to 0.2, 0.35 (299, 453, 500); ffmpeg on clip audio (470) | Master at 0.08 to 0.2, kept by the edit; QA flags seams over 0.35; clip audio muted | One timeline (line 439), STANDARDS 5 |
| Start frame as the only image (364) | The start frame is registered as its host's one-panel storyboard | The gate's image-1 rule (VISUAL-QA 6, STANDARDS 2) |
| Captions lower middle, title bar "top safe area" (461, 466) | Top 14%, bottom 35%, right 21% of the lower half and 6% sides kept clear | STANDARDS 6 |
| End card: 3-word CTA, offer, cost line, URL (467) | 2.5 to 3 s, one organic CTA, music under it | STANDARDS 5, ORGANIC-OS 6.2 |
| Brand line, peer result, guarantee, prices, hedged numbers (71 to 73, 89 to 93, 124, 125) | Method turn; no result, guarantee, price or invented number | STANDARDS 7, brand kit "Never" |
| Primary text and 2 headlines (525) | Instagram caption and pinned comment | ORGANIC-OS 8.2 |
| Budget: one retake of the longest clip, two retakes per image (358, 359) | 2 takes per talking clip, then +25% | STANDARDS 2, 10 |
| Hub G1 card "2 or 3 named people" against "No other people appear" (389) | No other people; the background action (VISUAL-QA 4.2 item 6) is object motion | The skill's own prompt (389); STANDARDS 2 prompt card row |

## 8. Package (tier B)
- Main cut (C45) + 3 hook variants from the same clips (section 12): the main, the same open with title bar B, a later
  start that re-runs Script Lab tests 3, 5 to 10, 13, 14 (line 477). Variants run as trial reels; a later start still
  lasts 35 s or more (test 14), so a card that wants one plans the main cut near 45 s.
- `runs/<post_id>/`: card, hook stacks, numbered script with release and cold reads, line table, speaker and stem maps
  with voice IDs, Shot Specs, prompts, take sheets with drift, cut map, section 14 tables, credits against the preflight.
- Hub draft with `hub.py push`: notes "AI label: on", caption, pinned comment; nothing posts before G-HUMAN-FINAL.
  Optional: an ad version with the ad CTA (ORGANIC-OS 7.7 rule 5), never posted organically.
- G-LEARN at 72 h and 7 d: skip rate, average watch time, saves per reach (trust) or qualified DMs and ANALIZA comments
  (convert), drops mapped to lines through the master's line table; lessons to the client's
  `analytics/learnings.md`, the opening's result to its `research/hook-library.md`.
