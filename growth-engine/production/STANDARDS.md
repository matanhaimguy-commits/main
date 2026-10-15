# Production standards (v1.0, 15 Oct 2026)

**The one place every production number lives.** Every production skill, reviewer and the generation gate read it.
Machine values are in `standards.json` (same folder); the gate (`growth-engine/tools/pipeline.py`) enforces the model
rules from there. Built from a full read of readymerce-ads-machine v13.4, hook-lab v1.1, script-lab v1.1,
animation-ads, song-ads, podcast-ads, drama-ads, carousel-machine, motion-video-director, claymation, and this repo's
motion-reel and growth-engine skills, with every one of the 18 issues in `AI-VIDEO-PIPELINE.md` section 5 checked
against the skill text (section 13 below).

**Precedence.** On a number (model, length, words, loudness, safe zone, pass rule) this file wins over any skill file.
On method (how to write a hook, how to cast a voice, how to build a sheet) the skill wins. A skill change that needs a
new number changes this file first, with a dated line in the changelog.

---

## 1. Models

| Use | Model | Settings | Why |
|---|---|---|---|
| Every AI video clip | MiniMax H3 `minimax_h3` | `resolution: "2K"`, `aspect_ratio: "9:16"`, `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`, 2 credits/s | Hub G1. Looked more real than FLUX 3 at a third of the price (Oct 2026). |
| Silent start-to-end transformation after an H3 keyframe take failed | Kling 3.0 `kling3_0` | start + end frame, same `declined_preset_id`, 10 credits per 5 s | Hub G2. Needs G-FALLBACK (Director or owner) on the asset. |
| Talking shot H3 can't sync after a split into 2 clips | Keyframe render + Sync Lipsync 3 | | The pipeline's second fallback (AI-VIDEO-PIPELINE step 10). Needs G-FALLBACK. |
| Any other video model (Seedance, Veo, Omni, Sora, Grok, Wan, Hailuo, FLUX video) | none | | Banned (hub G1). Drama's v2 routing (X5) is not adopted for organic until the owner decides (decision D9, section 14); a one-off needs G-EXCEPTION from the owner, recorded on the asset. The claymation style skill's "Seedance 1.5 Pro for transitions" default is not used: take its style block only. |
| Realistic people: character stills, start frames, sheets | GPT Image 2 `gpt_image_2` | `quality: high`, `resolution: 2k`, **always with a reference photo** (media role `image`) | Hub G7. GPT Image 2.5 made skin plastic on the round 5 UGC people. |
| Carousels, single images, statics, the client style reference | GPT Image 2.5 `gpt_image_2_5` | `aspect_ratio: "4:5"`, `resolution: 2k`, `quality: medium` (1 credit), media role `image_references` | Tested 11 Oct and in daily use since 15 Oct for Albanian text. |
| Stylized sheets and storyboards (animation, song, crochet, clay) | Nano Banana 2 `nano_banana_2` (default) | `resolution: 2k`, media role `image_references` | What the animation and song skills use. **Re-test R1** against GPT Image 2.5 on one sheet and one storyboard before the first animated series (section 14). |
| Narrator and character voices | ElevenLabs `eleven_v4` (default), audition `eleven_v3` beside it | `creative_generate_speech`, 4 takes per beat | Hub G8. `eleven_v3` ran Albanian lines together. StraightScale narrator: voice `8oGKUMljR779HzpZBiE4`. |
| Music beds | ElevenLabs `eleven_music_v2_5` | instrumental, 2 takes, length = VO + 3 to 5 s | Hub G8. |
| Songs | ElevenLabs `eleven_music_v2_5` with custom lyrics (default); Suno only when the owner makes it | 2 to 3 takes, picked by Whisper match to the lyrics (0.88 to 0.95) | Our StraightScale song runs used ElevenLabs Music; the song skill still says Suno (issue 6). |
| Sound effects | ElevenLabs `eleven_text_to_sound_v2` | 4 takes, never under hook words | Hub G8. |
| Higgsfield speech or audio (`seed_audio`, `text2speech_v2`) | none | | Retired for our content (hub G8: robotic). The gate blocks it. |
| ElevenLabs image or video models | none | | Stills come from Higgsfield, video from H3. The gate blocks them without G-EXCEPTION. |

## 2. H3 clips

| Rule | Number | Notes |
|---|---|---|
| Clip length | **5 to 15 s** | H3 accepts 4 to 15, but a 4 s render failed (hub G1). Pad short slices with silence. |
| Duration vs audio (**interim, re-test R2**) | Audio slice at most 14 s; `duration` = the slice rounded up to a whole second **plus 1 s**, within 5 to 15 | The hub says duration = padded slice; drama's newer test (11 Oct) says a duration equal to the audio fails and uses stem + 1 s. The interim rule satisfies the newer test. Re-test on a 5 s and a 14 s slice, then write one rule here. |
| Modes | Reference mode when a mouth moves (storyboard image 1, then character, state and set sheets, then the ElevenLabs slice as audio 1); keyframe mode (start image, optional end image) for silent shots | Never mixed in one generation. Never reference mode **without** audio (drama: failed in testing); silent shots use keyframe mode (worked on 15 Oct for the StraightScale quote reel) or the Kling fallback. |
| Words per clip | Monologue **30 to 35 per 15 s**; dialogue with listening gaps **about 20** per character clip (10 per line at most) | Issue 4: both are right for their case. |
| Shots per take | **2 to 3 reliable, 4 at most** | Issue 5. Song's 3 to 6 is overruled. |
| Speakers | One speaker per generation; one voice per character, locked for the series | Hub G4. |
| Filler | No clip without a line or a story action | Hub G5. Drama's silent story-action clips are story action. |
| Prompt card | The 9-part video card (VISUAL-QA 4.2) on every clip; storyboard always image 1 when talking or multi-shot | The gate enforces image 1. |
| Gestures | One small gesture per shot at most | Hub G1. |
| Takes | Batch 2 takes on the hook and on talking sequences; retakes keep the same references in the same order | |
| Attempts | 3 takes per clip (2 retakes), then simplify the shot or escalate | VISUAL-QA 7.1. The gate counts versions. |

## 3. Stills, sheets, storyboards

- Prompt card: the 11 blocks of VISUAL-QA 4.1, in order. Story props get content, text gets quotes + surface +
  position + occlusion, actions are contact points, negatives are targeted (never a blanket "no text").
- Realistic stills are written as an iPhone 15 Pro photo with real skin texture; the background is already
  mid-action; hands empty unless the script uses an object (hub G7).
- Sheet order in the look bible: hero, human, group, product, setting, key prop, then state sheets. Every
  story-critical prop gets a prop sheet (VISUAL-QA 4.4). Podcast start frames come only from the one master two-shot.
- Storyboards: one per sequence, 2 to 3 panels on a 16:9 canvas of 9:16 panels, or 2x2 on 4:5; built from the sheets,
  never from text alone; the hook storyboard first, checked at phone size with the text hook on it.
- Placements: Reels 1080x1920 (9:16); feed images and carousels 1080x1350 (4:5; the publishing API refuses 3:4);
  carousel 7 to 12 slides.
- Concept frames (hook step) are stills serving the hook shot's Shot Spec (`H-01`).

## 4. Audio

| Rule | Number |
|---|---|
| Pace before casting | 2.5 words/s (2.4 for characters who savour words); after casting, the measured pace decides the word budget |
| Storyteller pace band (per take score) | 4.3 to 5.5 syllables/s; pitch range 7+ semitones; flat lines flagged |
| Takes | Beats of 2 to 7 lines, 4 takes each; lowest score wins; every take transcribed against the script |
| Speed-up | Never past 1.05x; a long take is fixed by cutting words or moving up a tier |
| Pauses (issue 8) | **Human-style voices (UGC, podcast, talking head, narrator speaking as a person): never cap or compress pauses.** Check pause spread (SD 0.1 s or more) and a few pauses of 0.45 s or more at sentence ends. Animation characters may use gap codes (S 0.15, B 0.4, H 0.8 s) as **minimums**: `vo_build2.py`'s 0.4 s cap is not used for them either. |
| Conversation | Turn gaps 0.08 to 0.3 s, an occasional 0.1 to 0.2 s overlap; pitch within 1.5 semitones per character across clips |
| Music bed | 14 to 18 dB under the voice; dropped further under the hook, the turn, the reveal and the payoff |
| SFX | Never under the hook words |
| Loudness (issue 9) | **-14 LUFS integrated (±1), true peak -1 dBTP or lower**, every social delivery and every format (songs too). Measure with `vqa_crops.py loudness`. |
| Transcript check | Whisper (or ElevenLabs Scribe) word for word on every take and every speaking clip; a bad line is regenerated before any video. **Albanian and every non-English voice: a multilingual faster-whisper model (`small` or `medium`, `language="sq"`), never the `.en` models the animation checker names**; Whisper small mangles Albanian spelling, so use it for word presence and timing, and read spelling against the script. |

## 5. Picture and edit

- **Frame rate (issue 10): 30 fps** for everything; drama may choose 24 fps for its look, stated in the run.
- Export: H.264 High, 1080x1920, AAC 48 kHz; the ElevenLabs master (or the song) is the only audio; clip audio muted.
- Speed changes: silent clips may be trimmed or sped up (animation allows up to about 2.5x); **never a lip-synced
  clip** (it breaks sync with the master). First word at 0.0 s means within 0.1 s of the first frame.
- Picture change: every 2 to 4.5 s (songs 1.5 to 3.5 s; UGC and B-roll 1.5 to 3 s; a strong talking head may hold 4 to
  6 s); in the first 5 s something changes every 1 to 1.5 s; motion in the first second.
- Drift (hub G6): fix in the edit: cut at each lag step inside a pause, or one median offset when steps are under
  0.15 s; retake only when drift sits inside a word or correlation stays under about 0.5.
- Podcast cut map: in point 0.08 s before onset, gaps 0.08 to 0.2 s (never over 0.35 s), a reaction shot at least every
  10 s, punch-in 112 to 118% as a second camera.
- End card 2.5 to 3 s with the music under it; the organic end card is the CTA (keyword, follow, save), never an offer.

## 6. Text, captions and safe zones

| Element | Rule |
|---|---|
| Text hook / carousel cover headline | **4 to 10 words**, top third, frame 1 to about 3 s, never over the frame-1 subject; optional label of 6 words or fewer. Drama: optional, 6 words at most (X7). |
| Captions | 1 to 4 words per card, bold sans, contrast 4.5:1 or more, timed to the word |
| Supers | 2 to 6 words, never the transcript |
| Text in AI video | Never rendered by the video model; added in the edit |
| **Reels safe zone (issue 11)** | **Top 14% and bottom 35% clear of key content, plus the right 21% of the width in the lower half** (the Instagram UI: username, caption, audio row, buttons). Drama's 35 to 40% is the strict end. |
| Feed images and carousel slides | Text and logo inside a 4% margin; the cover headline readable at 200 px wide |
| Punctuation | No em dashes anywhere (spoken, super, caption, slide) |

## 7. AI disclosure (issue 12)

One policy for every format, aligned with Instagram's AI label (Organic Growth OS section 13):
- Turn on **Instagram's own AI label** for every post with a photoreal AI person, an AI voice speaking as a person, or
  realistic AI footage. No burned-in "AI DRAMATIZATION" tag (the podcast skill's tag is retired).
- Stylized animation (clay, crochet, 3D family-film, 2D storybook) also gets the label until the owner decides
  otherwise (decision D1).
- An AI person is never presented as a real customer or client, and never carries a real or invented result.
- The final reviewer checks this (V26, F7); the hub draft's notes say "AI label: on" when it applies.

## 8. Lengths

| Tier | Seconds | Use |
|---|---|---|
| O15 | 10 to 20 | one point: a quote reel, a stop-doing-X |
| O30 | 20 to 35 | compact shapes: myth buster (ST6), short mistake list (ST7), compact hidden cause (ST3), demo (ST14); the animation short |
| O60 | 45 to 75 | **the organic story tier:** POV day (ST4), hidden cause (ST3), two futures (ST5), a challenge episode (ST17), drama POV, song, podcast |
| O90 | 75 to 100 | only with a stated reason (an unaware audience, a new mechanism) |
| Podcast C45 (issue 18) | **35 to 45 s, 8 to 12 turns, 80 to 110 words** | One range for conversations. The router's 40 to 50 s C45 stays for single-voice problem demos (paid). |

No full discovery story under 45 s (organic); never over 3 minutes. Paid ads keep Script Lab's D15 to V300 router.

## 9. Pass rules

| Gate | Pass |
|---|---|
| Hook (G-HOOK) | All 9 Hook Lab gates; every channel A or A+ (an A- is rewritten); organic: a fresh grader agrees on the master stack |
| Script (G-SCRIPT) | 85/100 or more and no critical fail, after a fresh cold read (two from O60 up: listen and sound-off); 3 FIX loops, then the owner |
| Spec (G-SPEC) | Lint clean (`pipeline.py spec-check`) and a fresh prompt-reviewer PASS for the file's current version |
| Prompt (G-PROMPT-IMG / -VID) | P1 to P12 all PASS for that exact prompt; 2 loops, then the Director |
| Visual (G-VIS, -SHEET, -BOARD, -SLIDE) | Hero assets (frame 1, storyboard image 1, sheets, covers, thumbnails, start frames, the style reference): zero defects. Others: zero critical, zero major, at most 2 minor. 3 attempts per asset, then the owner. |
| Take (G-TAKE) | Zero critical, zero major; drift fixable in the edit; every scripted word present |
| Motion (G-MOTION-FRAMES) | M1 to M7 pass on preview frames every 0.5 s and at every transition |
| Final (G-FINAL) | F1 to F8, then the Director's pass, then the owner on the hub |

## 10. Budget

- Prices: H3 2 credits/s (a 15 s clip is 30); Kling 10 per 5 s; GPT Image 2.5 at 2k medium 1 credit; other stills
  1 to 6.5 credits (price them with `get_cost`); ElevenLabs about 177 credits per 4-take narrator beat (15 Oct).
- Preflight before the first render: every planned clip and still + 25% for retakes; `pipeline.py budget` records it
  against the client's monthly cap (brain.json) and the live balance. Re-check the balance right before every submit:
  credits are shared with every other session. The gate refuses a budget record older than 24 hours.
- Tier A pieces only with a proven angle or the month's wildcard (Organic Growth OS 7.7).

## 11. QA methods

- Stills: `vqa_crops.py image` (full, 3x3 tiles at 2x, region crops, panels, 200 px thumbnail; OCR only as a second
  opinion: it misreads ë and ç). The reviewer opens every file in the manifest.
- Video takes: frames at 1 per second (2 per second under 6 s) plus the first and last 0.1 s, contact sheets
  (`vqa_crops.py frames`); drift (`vqa_crops.py drift`); Whisper words.
- Motion renders: frames every 0.5 s plus each cut's start, middle and end (`vqa_crops.py motion`).
- Final cut: frames every 1.5 s plus every cut (`vqa_crops.py final`), sound-off watch, transcript, loudness.

## 12. What each skill keeps, and what this file overrides

| Skill | Keeps (method) | Overridden here |
|---|---|---|
| readymerce-ads-machine (hub) | Module 0, Part L, Section G method, C3 order | Loudness, fps, safe zones, AI label, the C10b "3 to 8 s per shot" clip line (clips are 5 to 15 s), the drama exception list (D9) |
| readymerce-hook-lab | The stack, 9 gates, rubric, H0 to H7 | B2B profile, carousel mode, organic metrics, the fresh grader (adapters/hook-lab-organic.md) |
| readymerce-script-lab | Everything in WRITE/GRADE/FIX | Organic tiers and rungs, scorecard re-weight, sound-off read, organic LEARN (adapters/script-lab-organic.md); the C45 podcast range |
| readymerce-animation-ads | Phases, style bible, shot ledger, 12 shot-logic tests | Image model pending R1, pause cap, loudness, clip duration, shots per take |
| readymerce-song-ads | Phases, lyric gate, 10 shot-logic tests | Song route (ElevenLabs Music default), H3 settings and prompt card, drift method, loudness, shots per take |
| readymerce-podcast-ads | Pinterest refs, master two-shot, speaker map, cut map | AI tag (label instead), loudness, C45 range |
| readymerce-drama-ads | Templates, concept card, beat sheet, shot list and 15 rules, film test | Model routing beyond H3/Kling (D9), safe zone (adopted for all reels), fps by choice |
| carousel-machine | Steps, idea score, story positions, style locks | Hook via Hook Lab carousel mode; fresh visual reviewer and G-SET replace its self-critic; cover 4 to 10 words |
| motion-video-director | (retired for our work) | Use motion-reel: it already follows our pipeline (issue 13) |
| motion-reel | The HyperFrames workflow | Hook Lab + Script Lab for its words, M1 to M7 review, loudness |

## 13. The 18 issues, checked and resolved

Every claim was checked against the skill text by a reader agent on 15 Oct 2026 (quotes and line numbers in
`audit/skill-audit-2026-10-15.md`).

| # | Issue | Checked | Rule now |
|---|---|---|---|
| 1 | Image model differs | True (hub G7 GPT Image 2 for faces, song and animation Nano Banana 2, carousels GPT Image 2.5) | Section 1: faces GPT Image 2 + reference; carousels and statics GPT Image 2.5; stylized Nano Banana 2 until R1 |
| 2 | H3 duration | True (hub: padded slice; drama 11 Oct: stem + 1 s) | Section 2 interim rule (slice up to 14 s, duration + 1 s); re-test R2 |
| 3 | Minimum clip | True (drama lists 4 to 15 s) | 5 s |
| 4 | Words per clip | True (hub and podcast 30 to 35; drama about 20) | 30 to 35 monologue, about 20 dialogue |
| 5 | Shots per take | True (song 3 to 6; animation 2 to 3 reliable and also "2 to 4"; hub 2 to 4) | 2 to 3, 4 at most |
| 6 | Song skill lags the hub | Partly true (no 2K, preset id or prompt card in the song skill; the hub itself still says Suno) | Section 1 song route; song runs use the H3 card and the drift method |
| 7 | Drama exceptions vs hub ban | Partly true (hub lists X1 to X4 with a stale X2; drama v2 has X5 to X10 routing to other models) | Not adopted for organic until the owner decides (D9); G-EXCEPTION per asset meanwhile |
| 8 | Pause handling | True (hub bans caps; animation's `vo_build2.py` caps at 0.4 s and the hub sends every module to it) | Section 4: never capped |
| 9 | Loudness | True (-16 animation and podcast, -14 drama and motion, song none, hub none) | -14 LUFS, -1 dBTP |
| 10 | Frame rate | True (drama 24 fps) | 30 fps, drama by choice |
| 11 | Safe zones | True (14/20 vs drama 14/35-40 + right 21%) | The drama zone for every reel |
| 12 | AI tag | True (podcast burns a tag; drama bans it) | Section 7: Instagram's label |
| 13 | motion-video-director conflicts | True (result-first hooks, em dashes as pause marks, user-made MP3, Freesound) | Retired; motion-reel |
| 14 | Carousels skip Hook Lab and the cold read | True | Hook Lab carousel mode + fresh cold read of the slide copy + fresh visual reviewer (adapters/carousel-machine-organic.md) |
| 15 | Hook Lab tuned to DTC health | True | B2B profile (adapters/hook-lab-organic.md) |
| 16 | Learning is paid-only | True (H8 and LEARN read Meta ads data only) | Organic LEARN (adapters, analyst agent) |
| 17 | Script Lab caller table misses drama and motion | True | adapters say how drama and motion-reel call Script Lab; the table itself lives in the synced skill (owner edits it on claude.ai) |
| 18 | Podcast C45 vs router C45 | True (35 to 45 vs 40 to 50, and the hub contradicts itself) | Section 8 |

Found beyond the 18 (details in the audit file): the hub's C10b "one shot = 3 to 8 s" contradicts its own G1; Hook Lab
names no image model for concept frames; Hook Lab self-grades (now a fresh grader); the Hook Library and
HOOK-LIBRARY-B2B-AL are not on disk (now `clients/<slug>/research/hook-library.md`); Script Lab's per-beat word budgets
don't add up to its tier ranges (budget words at the measured pace, per beat, and check the total); `vo_build2.py` is
fetched from a URL at run time and isn't in any skill folder.

## 14. Open re-tests and owner decisions

| ID | What | Cost | Status |
|---|---|---|---|
| R1 | Side-by-side for stylized sheets and storyboards: Nano Banana 2 vs GPT Image 2.5, one character sheet and one 3-panel storyboard per style used | about 10 credits | Before the first animated series; needs G-HUMAN-TEST |
| R2 | H3 duration rule: a 5 s and a 14 s talking slice, duration = slice vs slice + 1 s | about 80 credits | Before the next talking-head or story piece; needs G-HUMAN-TEST |
| D1 | AI label policy for the account (existing decision in brain.md) | | Default in section 7 until decided |
| D9 | Drama model routing (X5 to X10: Kling/Omni, Seedance, Cinema Studio, Veo, Gemini Omni) for organic drama | | H3 + Kling only until the owner decides |

## Changelog
- 2026-10-15 v1.0: first version from the skill audit and the two owner specs.
