# AI Video Production Pipeline (v1, 15 Oct 2026)
### One gated pipeline for every AI video we make: talking heads, UGC, podcasts, animations, songs, drama, motion reels, plus carousels

> Saved verbatim from the owner's spec (15 Oct 2026). Implementation and the single numbers file: `STANDARDS.md`
> and `standards.json` in this folder; the run tool: `growth-engine/tools/pipeline.py`; visual QA: `VISUAL-QA.md`.
> Note: `motion-reel` and `growth-engine` ARE installed in this repo (`.claude/skills/`); they were checked against
> section 5 when this was built (see `STANDARDS.md`, "Audit").

Built from a full read of the current skills: readymerce-ads-machine v13.4 (Part C and Section G), readymerce-hook-lab v1.1, readymerce-script-lab v1.1, readymerce-animation-ads v3.6, readymerce-song-ads (last change 4 Oct), readymerce-podcast-ads v5.0, readymerce-drama-ads v2.2, carousel-machine v3, motion-video-director.

**Note:** `motion-reel` and `growth-engine` are not installed in this environment, so they are not covered here. If they live in your other Claude Code session, check them against section 5 of this document.

---

## 1. The correct order (and why it differs from idea → script → hook → audio → characters...)

Your list has the right pieces. Four of them are in the wrong order, and four steps are missing.

| # | Step | What changes from your list | Why |
|---|---|---|---|
| 0 | **Foundation and brief** | Missing | Every later gate checks against it: avatar, buyer words, beliefs, proof, the one offer. Without it the hook and script gates have nothing to test against. |
| 1 | **Idea, angle and THE PICTURE** | Same | One idea, one angle, one visual metaphor the whole video is built on. |
| 2 | **Hook** | **Before the script** | The hook decides who watches. Script Lab writes line 2 to pay off an approved hook, not the other way round. No script line is written before the hook passes. |
| 3 | **Script** | After the hook | Gated with a cold read by a fresh agent and a 100-point score. |
| 4 | **Audio** (voice, conversation or song) | Same place | Audio sets the real timing. Every shot is cut to it, so it must exist before any picture. |
| 5 | **Audio analysis and timeline** | Missing | Word timestamps, beats, pauses and slices. This is what turns a script into a shot-by-shot clock. |
| 6 | **Visual plan (scenes and shots)** | **Before characters and settings** | You decide what each moment must show before designing people and places. Otherwise you design assets you don't need and miss ones you do. |
| 7 | **Look bible: characters, settings, props** | After the visual plan | Built from what the shots need, locked once, reused every episode. |
| 8 | **Storyboards** | Same | One image per sequence. It becomes image 1 in every video generation. |
| 9 | **Budget preflight** | Missing | Price every clip before the first render. Never start a video you can't finish. |
| 10 | **Video generation** | Same | MiniMax H3 at 2K, one speaker per clip, prompt card. |
| 11 | **Per-take QA** | Missing | Frames, lip-sync drift, words. Most quality is won or lost here, before the edit. |
| 12 | **Edit** | Same | The audio master is the timeline. Clip audio is muted. |
| 13 | **Final QA** | Missing | Sound-off watch, transcript, loudness, safe zones, policy. |
| 14 | **Package and approval** | Missing | A human approves before anything is posted. |
| 15 | **Learn** | Missing | Results go back into the hook library and the script lessons list. |

The rule behind the order: **words before sound, sound before pictures, plan before assets, look before you cut.** Each step locks something the next step depends on. Changing a locked step sends you back through its gate.

---

## 2. The pipeline, step by step, with gates

Each step lists: what it does, the skill and tools, the gate (pass criteria), who checks, and what happens on fail.

**Who checks:**
- **Claude**: self-check against numbers.
- **Fresh agent**: a new agent that has never seen the brief or earlier drafts. Used where self-grading is blind.
- **Human**: you or the operator, at the few points where taste or hearing matters.

### Step 0 · Foundation and brief
- **Does:** loads the client brain: avatar, VOC (exact buyer words), awareness stage, beliefs, mechanism, proof bank, offer, voice card, constraints. For organic posts, it also loads the Post Card (job, belief, CTA, format tier).
- **Skill:** ads-machine Module 0 (A1 to A3, B1 Voice Card with 10+ verbatim phrases, B2 Conviction Map), Script Lab brief card (2a) and persona card (2b).
- **Gate:**
  - One avatar confirmed.
  - At least 10 verbatim buyer phrases.
  - Every fact the video might use is on the facts sheet with a source.
  - The persona card holds only what the viewer knows before the ad: never the cause, mechanism, product or angle.
- **Who:** Claude.
- **On fail:** stop and ask for the missing fact. Never invent it.

### Step 1 · Idea, angle and THE PICTURE
- **Does:** picks one angle (one outcome in the buyer's words), the awareness stage, the load-bearing belief, the length tier and THE PICTURE (the one visual metaphor or demo that makes the cause visible).
- **Skill:** ads-machine C3 steps 1 to 6; Script Lab length router (section 3) and structure pick (3b, ST1 to ST18); animation Phase 3; song Phase 3.
- **Gate:**
  - THE PICTURE passes the one-second read: a stranger gets it in one look.
  - The tier fits the job. No story under 55 s; D30 and C45 are demos or conversations.
  - Every concept gets a short tier and a story tier, each written on its own.
  - The structure's required facts exist (no case-study structure without a real case).
- **Who:** Claude. For organic, the Organic Director checks fit with the Content Map.
- **On fail:** pick another picture or structure.

### Step 2 · Hook (three channels: visual, text, spoken)
- **Does:** writes the hook stack, grades it, renders concept frames.
- **Skill:** readymerce-hook-lab H0 to H7.
  - H0: Hook Library fresh (under 60 days) or run H1 research.
  - H3: generate (format-matched list plus 5 originals).
  - H4: grade; keep 3 stacks (master and 2 variants, at least 2 hook types).
  - Concept frame per finalist, viewed at phone size with the text hook on top.
- **Gate:**
  - All 9 gates pass:
    1. Buyer lock within 2 s with sound off.
    2. One claim across all three channels.
    3. Problem in frame 1 and in spoken sentence 1.
    4. Sound-off makes sense.
    5. Seam into line 2.
    6. A question still open at 10 s.
    7. No product, brand, price or offer in the first 3 s.
    8. Every fact is the brand's own.
    9. Meta check.
  - **Every channel grades A or A+.** An A- always goes back for a rewrite.
  - Text hook 4 to 10 words in the top third.
  - Spoken: first word at 0.0 s, problem in the first 6 words, sentence 1 of 8 to 14 words.
- **Who:** Claude grades. **Human:** you pick the master stack together with the script spine (step 3).
- **On fail:** H6 rewrite by three different routes, then grade again.

### Step 3 · Script
- **Does:** writes the script as speech, inside the tier's word budget, on a chosen structure.
- **Skill:** readymerce-script-lab WRITE:
  - Pre-write pack: a belief ladder with a "because" test between every rung, a question chain, a script bible (speakers, timeline, picture map, word list, setups and payoffs, facts) and a reveal plan.
  - 2 to 3 spines of about 80 words, using at least 2 structures.
  - Write as speech.
  - A line table.
  - Format adapters: 18a animation, 18b song, 18c podcast, 18d UGC, 18e text on screen, 18f VSL. Drama sends its own adapter.
- **Gate (12A to 12C):**
  - **16 mechanical tests**, each with line-number evidence, plus the 24-question lessons list.
  - **Cold read:** a fresh agent gets only the persona card and the numbered spoken lines. It writes a 5-sentence retell, the doubt left, "would you tap?", and the most confusing moment. From S90 up, a second skeptic reader.
  - **100-point score; release at 85+ with no critical fail.** Critical fails: major confusion on a core rung, a missing rung, a speaker or timeline break, an invented fact.
  - Hook seam (test 12): every stack is read stitched onto line 2.
- **Who:** Claude for the tests; **fresh agent** for the cold read. **Human:** you pick the spine and master stack. If you said "run without stopping", Claude picks and says which.
- **On fail:** FIX loop, rewriting only the failing lines, with **new readers every loop. Maximum 3 loops, then it comes to you** with the remaining fails.
- **Song extra (4f lyric gate):**
  - Speech is written and released first, then turned into lyrics.
  - Lyrics are graded read flat, with tests 3, 5, 7, 8, 9, 12 and 13 plus a lyric cold read.
  - Tests 1, 6 and 16 are run against the released speech.
  - The chorus carries THE PICTURE at least twice; the turn and CTA are spoken lines.
  - Aim at the low end of the tier, because music runs 10 to 25 s long.
- **Organic adapter:** the ending follows the organic CTA ladder (follow, save, send, keyword), not an offer close.

### Step 4 · Audio (the timing master)
Audio is made before any picture. Pick the route by format:

| Route | Used by | How | Gate |
|---|---|---|---|
| **Narrator / character VO** | Animation, talking head, UGC, motion | ElevenLabs `eleven_v4` default (audition `eleven_v3` beside it). 5a casting: voice brief, shortlist 4 to 6, audition the hook and mechanism lines at 4 takes, **15 s pilot first**, length calibration, then lock voice ID, model, tags and IPA for the brand name. 5b: beats of 2 to 7 lines, 4 takes each. | **Score per take** (vo_build2.py): word errors, pace band (4.3 to 5.5 syllables/s for a storyteller), pitch range (7+ semitones), flat lines flagged. Lowest score wins. **Human: four short listens** (audition, pilot, master, bed). Never speed the voice past 1.05x. Never cap human pauses: the 0.30 s cap made the U2 voice robotic. Check pause spread (standard deviation 0.1 s or more, some pauses 0.45 s or more). |
| **Conversation** | Podcast, drama | One locked voice per character on `eleven_v4`, beats at 4 takes. Turn gaps 0.08 to 0.3 s, occasional 0.1 to 0.2 s overlap. Packed stem per character per clip. | **Transcript check before any video:** ElevenLabs Scribe or Whisper word for word against the script. A bad line is regenerated and the master rebuilt. Pitch within 1.5 semitones per character. |
| **Song** | Song ads | Our StraightScale runs used ElevenLabs Music v2.5 with custom lyrics, 2 to 3 takes, picked by Whisper match to the lyrics (0.88 to 0.95). The skill still says Suno, generated by you. | **Human listen gate before any video.** Whisper match to the lyrics. If the first problem line arrives after 3 s, regenerate the opening before any visuals. |
| **Music bed and SFX** | All except song | `eleven_music_v2_5` (2 takes, length = VO + 3 to 5 s), `eleven_text_to_sound_v2` (4 takes, never under the hook words) | Bed 14 to 18 dB under the voice and dropped under the hook, turn, reveal and payoff. |

**On fail:** rerun the beat with changed text, or go back to casting if the voice sounds robotic.

### Step 5 · Audio analysis and timeline
- **Does:** turns the audio master into a clock.
  - Word timestamps: faster-whisper with `word_timestamps`, aligned to the script with difflib.
  - Line table and pause map.
  - Songs: BPM with librosa; vocal stem isolated (ElevenLabs isolation or UVR MDX-Net); re-time on the stem.
  - **Slices:** one per talking sequence, starting on the sequence's first frame, faded 0.03 s, padded to whole seconds, max 15 s.
- **Gate:**
  - Every scripted word is found in the timeline.
  - Every slice is between 5 and 15 s.
  - One speaker per slice.
  - Voice arrives within 0.3 s of the start.
- **Who:** Claude.
- **On fail:** fix the master in step 4.

### Step 6 · Visual plan (scenes and shots)
- **Does:** decides what each moment shows, timed to the audio.
  - "Show what is said or sung." The picture changes every 2 to 4.5 s (songs 1.5 to 3.5 s).
  - Shots are grouped into sequences of 2 to 4 shots, max 15 s each, sharing one audio slice.
  - **Shot ledger (animation 7b):** mode per shot (H3-REF talking, H3-KEY silent, KLING fallback, STILL, REAL, CARD) and links (CHAIN or CUT).
  - **Drama shot list:** shot sizes, 30-degree rule, continuity-state column, retention map.
- **Gate:**
  - **Shot-logic table:** 10 tests for song, 12 for animation. It starts with the one-second read per shot, and adds "talking mouth at least a third of the frame" and orientation for inside-the-body shots. A shot that fails is redesigned before it reaches a storyboard.
  - **Drama:**
    - 15 hard rules, including: at least 50% of shots move; geography established by 8 s; something changes every 2 to 4 s (every 1 to 1.5 s in the first 5 s); adjacent shots differ in length by 25%.
    - An event in every 10 s window.
  - Frame 1 of the video = the approved hook concept frame.
- **Who:** Claude.

### Step 7 · Look bible: characters, settings, props
- **Does:** a style bible plus sheets in a fixed order: hero, human, group, product, setting, key prop, then state sheets (a character's different states). Realistic people come from a real reference photo (podcast: Pinterest search, 8-point score, keep 13+ of 16), written as an iPhone 15 Pro photo with real skin texture.
- **Gate:**
  - Every sheet viewed at full size: identity matches across sheets, hands empty unless the script uses an object, backgrounds already mid-action (a posed background stays frozen in video), no readable text unless intended.
  - **Human approves every sheet** (song GATE 5, animation GATE 6).
  - Podcast: start frames come from one master two-shot only. A second close-up made from the master plus the original photo produced a different man.
- **On fail:** regenerate before storyboards.
- **Reuse:** the bible and sheets are built once per client and reused for every episode and the short tier.

### Step 8 · Storyboards
- **Does:** one storyboard image per sequence: 2 to 3 shots on a 16:9 canvas, or a 2x2 / 2x3 grid. Hook storyboard first.
- **Gate:**
  - Every panel opened at full size.
  - **Hook storyboard checked at phone size with the text hook on it, sound off.** It must keep the concept frame's subject.
  - No cloned characters, impossible poses or random text. All three slipped through on the Pillow Pool song before this gate existed.
  - **Human approves** (song GATE 6, animation GATE 7; drama animatic when you are present).
- **On fail:** regenerate the panel.

### Step 9 · Budget preflight (hard gate G3)
- **Does:** prices every planned clip in Atlas USD (STANDARDS.md 10; history in credits there).
  - H3 on Atlas at 768P = $0.024 per second asked for.
  - Stills = $0.059 each (`openai/gpt-image-2` at medium, the dearest named size).
  - Voices = $0.10 per 1,000 characters (`elevenlabs/v3/text-to-speech` on Atlas).
  - Add 25 to 30% for retakes, then check the balance (`atlas account balance`) **right before submitting**, because the Atlas account is shared across sessions.
- **Gate:** the balance covers the whole video plus retakes. For organic, also the client's monthly cap (Organic Growth OS 7.7).
- **On fail:** agree the scope with you before spending anything.

### Step 10 · Video generation (hard gates G1, G2, G4, G5)
- **Model:** MiniMax H3 at 2K, 9:16, `declined_preset_id` on every call.
  - **Reference mode** when a mouth moves: storyboard as image 1, then character and state sheets, then setting; the ElevenLabs slice as audio 1.
  - **Keyframe mode** for silent shots.
  - The two modes can't be mixed.
- **The 7-part prompt card (every clip):**
  1. Realism line.
  2. Reference tokens (`<<<image_1>>>` is..., `<<<audio_1>>>` is his voice).
  3. Hands and props: which hand holds what, or "hands empty".
  4. Timeline of 2 to 4 shots, one action per shot, timed to words.
  5. Background line in every shot: 2 or 3 named people doing named actions.
  6. Lip-sync block, including "use the audio exactly, same timing". That line fixed an out-of-sync retake.
  7. Negatives: no text, no logos, no morphing.
- **Rules:**
  - One speaker per generation, about 30 to 35 words per 15 s clip.
  - No filler clips with no line and no story action.
  - Batch 2 takes on the hook and on talking sequences. Retakes keep the same references in the same order.
- **Fallbacks:** split the sequence into 2 clips; then keyframe render plus Sync Lipsync 3; Kling 3.0 only for a silent start-to-end transformation after H3 fails the frame check.

### Step 11 · Per-take QA (before any edit)
- **Frame check:** contact sheets for every clip, at one frame per second for talking takes (every 0.5 s for short drama takes), looked at before cutting. Reject list: identity change, vanished props, frozen background, gibberish text, extra limbs, wrong framing.
- **Lip-sync drift check (G6):**
  - Compare the clip's audio envelope with its slice in 2 s windows every 0.25 s; find the lag and where it steps. H3 drifted 0.1 to 1.1 s in 9 of 13 clips.
  - **Fix in the edit:** cut at each step inside a pause, or use one median offset when steps are under 0.15 s.
  - Retake only if the drift sits inside a word, or correlation is under about 0.5 with no clear lag.
- **Transcript:** Whisper every speaking clip against the script word for word. Retake only for a missing, wrong or added word the edit can't cut around.
- **Who:** Claude. Failing shots are listed to you before the retake.

### Step 12 · Edit
- **Timeline:** the ElevenLabs master (or the song) is the only audio; clip audio is muted.
- **Picture:** normalize to 1080x1920. Apply drift offsets.
  - Podcast cut map: in point 0.08 s before onset, gaps 0.08 to 0.2 s (never over 0.35 s), a reaction shot at least every 10 s, punch-in of 112 to 118% as a second camera.
- **Supers and captions:**
  - Hook super held from frame 1 to about 3 s, exactly as approved.
  - Captions 1 to 4 words, inside safe zones: top 14% and bottom 20% clear (drama: bottom 35 to 40%).
  - End card 2.5 to 3 s, with the music under it.
- **Mix:** bed ducked under the voice, SFX in time with picture, loudness normalized (see 5, unify).

### Step 13 · Final QA
Every item must pass. Never deliver with a known failure.
- **Sound-off watch:** the story is understood from picture and text alone.
- **Sound-on watch.**
- **Voice-alone listen:** if it sounds robotic, go back to step 4.
- **Final transcript:** every word present.
- **Hook timing:** first word at 0.0 s (song: first sung word by about 1 s, problem sung by about 3 s).
- **Technical:** safe zones and caption contrast; loudness and true peak; no generated gibberish text; no banned model used.
- **Credits:** within the preflight.
- **Policy:** no side-by-side before and after; no "your [condition]"; AI disclosure rules followed.
- **Drama only:** film-test score card out of 100, release at 85, with a fresh agent running checks 2 to 6 for high-stakes work.

### Step 14 · Package and approval
- **Deliverables:**
  - Final cuts: story tier and short tier.
  - 3 hook variants. Each runs as its own ad, or its own trial reel in organic.
  - Captions, alt text and the posting package.
  - Organic: every Tier A piece also makes its 6 derived assets (Organic Growth OS 7.7).
- **Gate:** **human approval before anything is posted or launched.** Non-English copy is marked for a native read.

### Step 15 · Learn
- **Paid:**
  - Hook Lab H8 after about 1,000 impressions per stack. Hook rate (3 s plays ÷ impressions): floor 30%, target 40%. Hold rate (15 s plays ÷ 3 s plays): floor 25%, target 35%.
  - Script Lab LEARN: map the 3 steepest drop-offs to script lines and add 1 or 2 lessons to the lessons list.
- **Organic (missing today, see 5):** skip rate, average watch time, sends and saves per reach, follows and keyword comments per post, read at 72 hours and 7 days.

---

## 3. How each format runs through the pipeline

| Step | Talking head / UGC | Podcast | Animation | Song | Drama | Motion reel | Carousel |
|---|---|---|---|---|---|---|---|
| 0 to 1 | Module 0, C3 1 to 6 | Module 0 | Phases 1 to 3 | Phases 1 to 3 | Concept card | Brief | Brand kit, brief, idea score (6 tests) |
| 2 Hook | Hook Lab | Hook Lab (title bar 8 words max) | Hook Lab | Hook Lab (sung problem by about 3 s) | Hook Lab with exceptions (text hook optional, first line by 1.5 s) | Not connected to Hook Lab (gap) | Own 4 PASS/FAIL gates, 5 variants (gap: not on Hook Lab) |
| 3 Script | Script Lab 18d | Script Lab 18c (8 to 12 turns, 80 to 110 words) | Script Lab 18a + 4f | Speech, then lyrics, then 4f lyric gate | Script Lab + drama adapter + 2 cold reads (listen and picture) | Own script rules (gap: conflicts with Script Lab) | Six story positions + 8-question self-check (no cold read) |
| 4 Audio | VO (5a to 5d) | Conversation master + transcript check | VO + pilot + 4 listens | Song + listen gate | Voices per character, scene master | VO MP3 | n/a |
| 5 Timeline | Slices | Packed stems per character | Slices, pause map | BPM, vocal stem, slices | Stems + listening gaps | beats.json | n/a |
| 6 Plan | Shot timeline | Speaker map, frame plan F0 to F2 | Shot ledger + 12 tests | Shot logic + 10 tests | Shot list + 15 rules | Storyboard and shot list | Continuity plan, one scene line per slide |
| 7 Look | iPhone-style stills from a reference | Pinterest refs, one master two-shot | Sheets (GATE 6) | Sheets (GATE 5) | Location master, sheets | Style board (approve plan) | Style bible, 3 locks, test slide |
| 8 Storyboard | Optional | Start frames | GATE 7 | GATE 6 | Animatic | Preview sheets (approve preview) | Cover (4 options), then slide 2 as anchors |
| 9 Preflight | G3 | G3 | G3 + 30% | G3 | Cost check | n/a (code render) | Balance + get_cost |
| 10 Generate | H3 ref mode | H3 ref mode, one character per clip | H3 ref / key, Kling fallback | H3 ref with vocal stem | Multi-model routing (exception) | Canvas, Three.js, GSAP | GPT Image 2.5, anchored batch |
| 11 Take QA | Frames + drift + words | Take sheet 1 frame/s + pitch + drift | Frame PDF + drift | Frame sheets + sync | Frames 0.5 to 1 s + correlation | Preview loop | Letter-by-letter at full size, thumbnail test at 200 px |
| 12 to 13 | Edit + final QA | Cut map + final QA | Edit + QA | Edit + QA | Picture lock, score, sound, grade, mix + 85/100 film test | QA checklist (15 items) | Two critic passes, grid test |

---

## 4. The house rules that make every generation accurate

1. **Nothing generates before its inputs are locked.** Hook before script, script before audio, audio before pictures, sheets before storyboards, storyboards before video.
2. **Fresh eyes where self-grading is blind.** The script cold read and the drama picture read always use a new agent, and a new one every loop.
3. **Humans only where taste or hearing matters:** pick the spine and hook, listen to voice and song, approve sheets and storyboards, approve the final cut. Everything else is measured.
4. **Measure, don't eyeball:**
   - Word match on every take.
   - Lip-sync lag on every clip.
   - Pitch spread and pace band on every voice take.
   - Loudness on every master.
   - Text checked letter by letter.
5. **Every rule has a number:** clip 5 to 15 s, 30 to 35 words per clip, 2 to 4 shots per take, picture change every 2 to 4.5 s, A or A+ hooks, 85/100 scripts.
6. **Retake only what the edit can't fix.** Drift steps get cut at pauses; only drift inside a word is retaken.
7. **References in the same order on every retake;** storyboard always image 1.
8. **One speaker per clip, one voice per character, locked for the whole series.**
9. **Lessons become rules.** Every failure gets a dated line in the skill's lessons list or changelog, so it never happens twice.

---

## 5. What's broken or inconsistent today (fix before automating)

The skills drifted as they were updated on different days. An automated agent will follow whichever file it reads, so these must be unified. The fix: **one shared production-standards file that every skill reads**, so numbers live in one place.

| # | Issue | Where | Recommended single rule |
|---|---|---|---|
| 1 | **Image model differs:** Nano Banana 2 (song, animation sheets and storyboards) vs GPT Image 2 (podcast and hub G7; GPT Image 2.5 rejected as plastic for faces) vs GPT Image 2.5 (carousel) | Song, animation, podcast, hub, carousel | Realistic faces: GPT Image 2 with a reference. Stylized sheets and storyboards: pick one after a side-by-side test. Carousels: GPT Image 2.5 (tested 11 Oct for Albanian text). |
| 2 | **H3 duration:** "= padded slice" (hub, song, animation, podcast) vs "stem + 1 s, equal to audio fails" (drama, newest test 11 Oct) | All video skills | Re-test once on a 5 s and a 15 s slice, then write one rule into G1. |
| 3 | **Minimum clip:** 5 s (hub, podcast) vs 4 s (drama) | Hub, drama | 5 s until re-tested. |
| 4 | **Words per clip:** 30 to 35 (hub, podcast) vs about 20 (drama) | Hub, drama | 30 to 35 for monologue, about 20 for dialogue with listening gaps. |
| 5 | **Shots per H3 take:** 3 to 6 (song) vs 2 to 3 (animation) vs 2 to 4 (hub) | Song, animation, hub | 2 to 3 reliable, 4 max. |
| 6 | **Song skill lags hub v13.3:** no 2K, no `declined_preset_id`, no prompt card, old sync check; says Suno generated by you, while our runs used ElevenLabs Music | readymerce-song-ads | Update to G1 card, G6 drift method and the ElevenLabs Music route (Suno as an option). |
| 7 | **Drama exceptions vs hub ban:** drama routes to Seedance, Veo, Omni and Kling (X5); hub G1/G2 says never. Hub still lists only X1 to X4. | Hub, drama | Decide: either record X5 to X10 in the hub as approved drama exceptions, or remove them. |
| 8 | **Pause handling:** hub G8 bans capping human pauses; animation's vo_build2.py caps pauses at 0.4 s | Hub, animation | Narrators may use gap codes; human-style voices (UGC, podcast, talking head) never capped. Write it down. |
| 9 | **Loudness:** -16 LUFS (animation, podcast) vs -14 LUFS (drama, motion), song none | All | -14 LUFS, -1 dBTP for all social delivery. |
| 10 | **Frame rate:** 30 fps vs 24 fps (drama) | All | 30 fps, except drama by choice. |
| 11 | **Caption safe zones:** bottom 20% clear vs drama's 35 to 40% | All | Use the stricter drama zone for anything posted as a Reel (the UI covers more of the bottom). |
| 12 | **AI tag:** podcast burns in "AI DRAMATIZATION"; drama bans a tag | Podcast, drama | One policy, aligned with Instagram's AI label rule (Organic Growth OS section 13). |
| 13 | **Motion-video-director conflicts:** result-first hooks, its own word budgets, em dashes as pause marks, you generate the MP3 by hand, Freesound SFX, missing helper scripts (preflight.sh, preview.mjs and others) | motion-video-director | Bring it under Hook Lab, Script Lab and G8, or retire it in favour of motion-reel. |
| 14 | **Carousels skip Hook Lab and the cold read** | carousel-machine | Add a carousel mode to Hook Lab (cover = text and visual stack) and a fresh-agent cold read of the slide copy. |
| 15 | **Hook Lab is tuned to DTC health** (body-part rules, medical-severity checks) | Hook Lab | Add a B2B/services profile using HOOK-LIBRARY-B2B-AL (person + one real prop, one countable fact). |
| 16 | **Learning is paid-only:** H8 and LEARN read only Meta ads data | Hook Lab, Script Lab | Add an organic LEARN mode: skip rate, watch time, sends, saves, follows and keyword comments per post. |
| 17 | **Script Lab caller table is missing** drama ads and motion skills | Script Lab | Update the table and adapters. |
| 18 | **Podcast C45 is 35 to 45 s,** router C45 is 40 to 50 s | Podcast, Script Lab | Align to one range. |

---

## 6. Build order for automating it in the Social Agent

1. **Production-standards file** with every number from sections 2 and 5 in one place. Every skill reads it.
2. **A pipeline runner** that moves each Post Card through steps 0 to 15, storing each step's output and gate result in the post's folder, so any step can be re-run without redoing earlier ones.
3. **Gate records:** for every gate, store pass or fail, the evidence (scores, lags, word matches) and who checked. A post can't move forward with an open fail.
4. **Human checkpoints as a queue:** spine and hook pick, voice and song listen, sheets, storyboards, final approval. Batch them so you approve once a day, not once per step.
5. **Organic LEARN** writing back into the Hook Library and the Script Lab lessons list.
