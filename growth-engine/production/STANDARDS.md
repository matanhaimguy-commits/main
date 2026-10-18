# Production standards (v1.2, 18 Oct 2026)

**The one place every production number lives.** Every production skill, reviewer and the generation gate read it.
Machine values are in `standards.json` (same folder); the gate (`growth-engine/tools/pipeline.py`) enforces the model
rules from there. Built from a full read of readymerce-ads-machine v13.4, hook-lab v1.1, script-lab v1.1,
animation-ads, song-ads, podcast-ads, drama-ads, carousel-machine, motion-video-director, claymation, and this repo's
motion-reel and growth-engine skills, with every one of the 18 issues in `AI-VIDEO-PIPELINE.md` section 5 checked
against the skill text (section 13 below). Numbers marked **proposed, confirm on first run** have thin evidence: use
them, measure, and change them here after the first run.

**Precedence.** On a number (model, length, words, loudness, safe zone, pass rule) this file wins over any skill file.
On method (how to write a hook, how to cast a voice, how to build a sheet) the skill wins. A skill change that needs a
new number changes this file first, with a dated line in the changelog. Other docs cite these sections by number
instead of restating the numbers.

---

## 1. Models

| Use | Model | Settings | Why |
|---|---|---|---|
| Every AI video clip | MiniMax H3 `minimax_h3` | `resolution: "2K"`, `aspect_ratio: "9:16"`, `declined_preset_id: "24bae836-2c4a-48e0-89b6-49fcc0b21612"`, 2 credits/s | Hub G1. Looked more real than FLUX 3 at a third of the price (Oct 2026). |
| Silent start-to-end transformation after an H3 keyframe take failed | Kling 3.0 `kling3_0` | start + end frame, same `declined_preset_id`, 10 credits per 5 s | Hub G2. Needs G-FALLBACK (Director or owner) on the asset. |
| Talking shot H3 can't sync after a split into 2 clips | Keyframe render + Sync Lipsync 3 | | The pipeline's second fallback (AI-VIDEO-PIPELINE step 10). Needs G-FALLBACK. |
| Any other video model (Seedance, Veo, Omni, Sora, Grok, Wan, Hailuo, FLUX video) | none | | Banned (hub G1). Drama's X5 routing is not adopted for organic until the owner decides (decision D9, section 14; table in 7b); a one-off needs G-EXCEPTION from the owner, recorded on the asset. Claymation: see the claymation row below. |
| Realistic people: character stills, start frames, sheets, storyboards | GPT Image 2 `gpt_image_2` | `quality: "high"`, `resolution: "2k"`, **always with a reference photo** (media role `image`). No 4:5 output (ratios 1:1, 4:3, 3:4, 16:9, 21:9, 9:16, 3:2, 2:3) | Hub G7. GPT Image 2.5 made skin plastic on the round 5 UGC people. The gate checks the settings, the reference and the ratio. |
| Carousels, single images, statics, the client style reference, and stills or start frames with no person in the client's style | GPT Image 2.5 `gpt_image_2_5` | Always pass `aspect_ratio: "4:5"` (feed; 9:16 for a reel still), `resolution: "2k"`, `quality: "medium"` (1 credit) and `variant: "flare"` (the model defaults are 1k, low and an unpinned variant); media role `image_references` with job ids, never URLs | Tested 11 Oct and in daily use since 15 Oct for Albanian text. The gate checks resolution and quality (medium, or high for a cover polish) and refuses a variant other than flare. It refuses 2.5 for a still or start frame whose Shot Spec is a realistic-people format (ugc, talking_head, podcast, drama). |
| A photoreal person on a carousel slide, cover or static | GPT Image 2.5 at 4:5 with the person's approved `gpt_image_2` still (or the real founder photo, used only for face and build) as `image_references` | as the carousel row | `gpt_image_2` has no 4:5. The visual reviewer checks skin and face against that still. If the skin goes plastic, make the slide in `gpt_image_2` at 3:4 and re-fit it to 1080x1350 with the growth-engine blurred-edge method; pick one route after a side-by-side (G-HUMAN-TEST). The 3:4 route needs a G-EXCEPTION (model `gpt_image_2`) on the slide, cover or static asset: the gate's `gpt_image_2` list has no slide types and no 4:5. |
| Stylized sheets and storyboards (animation, song, crochet, clay) | Nano Banana 2 `nano_banana_2` (default) | `resolution: "2k"`, media role `image_references` | What the animation and song skills use. **Re-test R1** against GPT Image 2.5 on one sheet and one storyboard before the first animated series (section 14). Until then GPT Image 2.5 makes stylized sheets and storyboards only inside the R1 test (G-HUMAN-TEST). Nano Banana Pro is not on the list (drama's "GPT Image 2 or Nano Banana Pro" for sheets is not used). |
| Claymation | from the claymation style skill take the sub-style block, the physicality block and the motion guard (one motion action per shot; 12 fps stepped stop-motion cadence, no motion blur), word for word | | Not its models: clay images on Nano Banana 2 (Seedream 4.5 is not on the list); clay transitions (start frame to end frame) run on H3 keyframe mode with start and end images, Kling 3.0 only with G-FALLBACK after an H3 frame-check fail; its "Seedance 1.5 Pro for transitions" is banned. A melt or morph transition carries its own transition guard, kept apart from the in-scene guard that bans morphing. |
| Narrator and character voices | ElevenLabs `eleven_v4` (default), audition `eleven_v3` beside it | `creative_generate_speech`, 4 takes per beat | Hub G8. `eleven_v3` ran Albanian lines together. StraightScale narrator: voice `8oGKUMljR779HzpZBiE4`. |
| Music beds | ElevenLabs `eleven_music_v2_5` | instrumental, 2 takes, length = VO + 3 to 5 s | Hub G8. |
| Songs | ElevenLabs `eleven_music_v2_5` with the released lyrics as custom lyrics (default), run as a flow node: read `creative_get_model_schema` for the lyrics and length fields before the first call, and never repeat a call to retry (each call is charged). Suno only when the owner makes it by hand from the same lyrics; that song takes the same checks | 2 to 3 takes. Music prompt under 25 words, always with "clear lead vocal, lyrics up front", plus the series genre and singer. Pick the take with the highest Whisper match to the lyrics (multilingual faster-whisper in the song's language, `language="sq"` for Albanian); a take under **0.88** is not used (**proposed, confirm on first run**: the low end of the 0.88 to 0.95 band seen in our runs). Measure each take's length against the tier (Suno ran 10 to 25 s long; the ElevenLabs overrun is not measured yet). | AI-VIDEO-PIPELINE step 4 says StraightScale song runs used ElevenLabs Music; no run files for them are in the repo. The song skill and the hub still say Suno (issue 6). |
| Sound effects | ElevenLabs `eleven_text_to_sound_v2` | 4 takes, never under hook words | Hub G8. |
| Higgsfield speech or audio (`seed_audio`, `text2speech_v2`) | none | | Retired for our content (hub G8: robotic). The gate blocks it. |
| ElevenLabs image or video models | none | | Stills come from Higgsfield, video from H3. The gate blocks them without G-EXCEPTION. |
| Atlas Cloud models (`atlas generate image`, `video`, `audio`) | none named yet | | The owner names each Atlas model in `standards.json` `models.atlas.allowed`: an entry with its exact id, kind, the parameters it must pass, the duration bounds (video) and any extra text fields, which are reviewed with the prompt. A parameter carrying text that the entry does not list blocks the call. While the list is empty the gate blocks every Atlas generation. A family banned above stays banned on Atlas unless the owner names that exact model; G-EXCEPTION does not open Atlas. `atlas generate 3d` and `atlas chat` are blocked. Atlas runs only through the gated `atlas` command (`growth-engine/tools/atlas/README.md`). |

**Edit pass (VISUAL-QA 5.5 route 1).** The gate allows an image asset's **own previous version** (same asset id, same
run, registered with its job id, any gate status) as the **single** image reference: register it with
`pipeline.py prompt ... --media <previous job id>:edit_source` and pass it in the call as `image_references` (or
`image` on `gpt_image_2`). The edit is a new version of the asset, counts as one attempt, and gets its own full review.
Any other reference still needs its own passed review.

## 2. H3 clips

| Rule | Number | Notes |
|---|---|---|
| Clip length | **5 to 15 s** | H3 accepts 4 to 15, but a 4 s render failed (hub G1). Pad short slices with silence. |
| Duration vs audio (**interim, re-test R2**) | The slice is the whole audio file attached as audio 1, padded to a whole second: podcast = the speaker's lines joined by 0.8 to 1.0 s listening beats plus about 1 s tail; drama = the character's lines with listening gaps of 0.8 to 3 s and a 0.3 s handle before the first word; song = the vocal stem from the sequence's first frame with a 0.03 s fade-out. Slices run **4 to 14 s**; `duration` = the slice rounded up to a whole second **plus 1 s**, within 5 to 15; the +1 s comes on top of any tail already inside the file. A slice under 4 s folds its lines into the same speaker's other clip. | The hub says duration = padded slice; drama's newer test (11 Oct) says a duration equal to the audio fails and uses stem + 1 s. The interim rule satisfies the newer test. Re-test on a 5 s and a 14 s slice, then write one rule here. `pipeline.py` checks only 5 to 15 s, so the prompt reviewer checks duration = slice + 1 s (P10). AI-VIDEO-PIPELINE step 5's "every slice is between 5 and 15 s" reads 4 to 14 s. |
| Modes | Reference mode when a mouth moves (storyboard image 1, then character, state and set sheets, then the ElevenLabs slice as audio 1); keyframe mode (start image, optional end image) for silent shots | Never mixed in one generation. Never reference mode **without** audio (drama: failed in testing); silent shots use keyframe mode (worked on 15 Oct for the StraightScale quote reel) or the Kling fallback. **Silent keyframe clips are one shot each** (start, optional end frame); a chain of silent shots is several one-shot clips cut in the edit; multi-shot sequences are reference mode with audio only. |
| Words per clip | Monologue **30 to 35 per 15 s**. Podcast packed stem (one host, listening beats inside): words come from time, (stem length, 14 s at most, minus the beats and the tail) x the voice's measured pace, **about 27 to 30** at 2.5 words/s (**proposed, confirm on first run**); Script Lab's 30 to 35 is a ceiling. Drama lip-synced clip: **about 20**, 10 per line at most, and a line over 10 words never goes to visible H3 lip-sync (play part of it over the listener). Sung clips: no word count; lyrics follow section 4. | Issue 4. "Dialogue" alone did not tell an agent which rule a podcast follows. |
| Shots per take | **1 to 3, 4 at most** (2 to 3 is the reliable range when a take has cuts). Podcast: exactly 1 continuous shot, static camera locked to the start frame; the second camera is a 112 to 118% punch-in made in the edit. Drama: one camera move per shot, two compatible moves at most, each with an end state. Claymation: one motion action per shot. | Issue 5. Song's 3 to 6 is overruled; the podcast's 1 shot is a fourth value the issue missed. |
| Speakers | One speaker per generation; one voice per character, locked for the series | Hub G4. |
| Filler | No clip without a line or a story action | Hub G5. Drama's silent coverage shots (X6, section 7b) are story action. |
| Prompt card | The 9-part video card (VISUAL-QA 4.2) on every clip; storyboard always image 1 when talking or multi-shot. A one-shot talking clip with a locked camera (podcast) uses the speaker's approved 9:16 start frame as a one-panel storyboard: registered as `storyboard` (`--hook` for the line-1 speaker), passed at G-VIS-BOARD and G-CONTINUITY together with the master two-shot, and it is the only image in the call (audio 1 = the packed stem). For podcast, card item 3 reads "one panel, one continuous shot" and item 6 is object motion (steam, a curtain), never people. | The gate enforces image 1 (`pipeline.py check-call`). |
| Gestures | One small gesture per shot at most | Hub G1. |
| Takes | Batch 2 takes on the hook and on every talking or singing sequence; other silent keyframe clips 1 take; retakes keep the same references in the same order and change one thing in the prompt | |
| Attempts | 3 takes per clip (2 retakes), then simplify the shot or escalate | VISUAL-QA 7.1. The gate counts versions. |

## 3. Stills, sheets, storyboards

- Prompt card: the 11 blocks of VISUAL-QA 4.1, in order. Story props get content, text gets quotes + surface +
  position + occlusion, actions are contact points, negatives are targeted (never a blanket "no text").
- Realistic stills are written as an iPhone 15 Pro photo with real skin texture; the background is already
  mid-action; hands empty unless the script uses an object (hub G7).
- Sheet order in the look bible: hero, human, group, product, setting, key prop, then state sheets. Every
  story-critical prop gets a prop sheet (VISUAL-QA 4.4). Podcast start frames come only from the one master two-shot.
- Storyboards: one per sequence, built from the sheets, never from text alone; the hook storyboard first, checked at
  phone size with the text hook on it. Layout: 2 or 3 shots on a 16:9 canvas of 9:16 panels side by side; 4 shots in a
  2x2 grid of 9:16 panels, which makes a 9:16 canvas (four 9:16 panels in 2 rows and 2 columns can't fill a 4:5 canvas;
  the song skill's 4:5 canvas holds 2 rows of 3). Thin white gutters; no text, numbers or speech bubbles in any panel.
- **Hero status.** Every storyboard is image 1 in its H3 call, so every storyboard is hero (VISUAL-QA 5.3 "storyboard
  image 1"): `standards.json` sets `storyboard.hero: true`. The hook concept frame is frame 1, so it is hero too:
  register it with `--hero` (or as a `start_frame`).
- Placements: Reels 1080x1920 (9:16); feed images and carousels 1080x1350 (4:5; the publishing API refuses 3:4);
  carousel 7 to 12 slides (carousel-machine's 12 to 15 slide "Start here" and 4 to 8 slide "Tool or news drop" formats
  are fitted to 7 to 12). Delivery files: slides JPEG 1080x1350 under 8 MB each (not the skill's 1080x1440 under
  250 KB); reels MP4 H.264 + AAC under 100 MB, 3 to 90 s.
- Concept frames (hook step) are stills serving the hook shot's Shot Spec (`H-01`).

## 4. Audio

| Rule | Number |
|---|---|
| Pace before casting | 2.5 words/s (2.4 for characters who savour words); after casting, the measured pace decides the word budget |
| Storyteller pace band (per take score) | **English:** 4.3 to 5.5 syllables/s. **Other languages (Albanian):** the band is measured on the approved audition and written in that voice's G-HUMAN-VOICE note; takes are scored against it. Pitch range 7+ semitones; flat lines flagged |
| Takes | Beats of 2 to 7 lines, 4 takes each; lowest score wins; every take transcribed against the script |
| Speed-up | Never past 1.05x; a long take is fixed by cutting words or moving up a tier |
| Pauses (issue 8) | **Human-style voices (UGC, podcast, talking head, narrator speaking as a person): never cap or compress pauses.** Check pause spread (SD 0.1 s or more) and at least one pause of 0.45 s or more per 3 sentence ends (**proposed, confirm on first run**). Animation characters may use gap codes (S 0.15, B 0.4, H 0.8 s) as **minimums**: `vo_build2.py`'s 0.4 s cap is not used for them either. |
| Audio tags (`eleven_v4`) | At most one low-intensity tag per line, at its start ([quietly], [a little tired]); a laugh tag only where the script writes a laugh; negations written in full; brand names spelled the way they are said |
| Conversation | The master sets every gap and the edit never retimes it (the master is the only audio). Turn gaps 0.08 to 0.3 s (podcast 0.08 to 0.2 s; drama 0.08 to 0.2 s once the mechanism enters), an occasional 0.1 to 0.2 s overlap; G-FINAL fails any seam gap over 0.35 s. Pitch within 1.5 semitones per character across clips. Per-line loudness spread under 2 dB before the master loudness pass. |
| Music bed | 14 to 18 dB under the voice (drama's 10 dB and motion-reel's 10 to 20 dB ends are overruled); under the hook only a tension bed 20 dB or more under the voice, with no melody; ducking 6 to 12 dB on lines (attack 5 to 20 ms, release 250 to 500 ms) or hand rides; dropped further under the turn, the reveal and the payoff |
| SFX | Never under the hook words. `eleven_text_to_sound_v2` defaults to about 2 s, so always set `duration_seconds`. Featured foley peaks 3 to 6 dB and touch foley 10 to 16 dB under the dialogue peaks. |
| Loudness (issue 9) | **-14 LUFS integrated (±1), true peak -1 dBTP or lower** (motion-reel's -1.5 passes), loudness range 11 LU or less (drama 6 to 11 LU), short-term never above about -9 LUFS; two-pass `loudnorm` (measure, then apply); every social delivery and every format (songs too). `vqa_crops.py loudness` reports all four and a pass flag against these numbers. |
| Song listen | **G-HUMAN-SONG:** the owner listens to every song master before any picture is made (per piece; the gate blocks song pictures without it). Sung Albanian can't be fully measured by Whisper. |
| Lyrics (songs) | The speech is released at 85+ first, then turned into lyrics with every rung in order. 8 to 14 syllables a line. The chorus carries THE PICTURE and its name and is sung at least twice. The turn and the CTA are lines Whisper finds word for word. Lines per tier: O60 23 to 37 (the skill's S60 row); 18 to 27 when the song runs 40 to 50 s; O30 about 11 to 19 (the 40 to 50 s row scaled at 0.45 to 0.54 lines per second; **proposed, confirm on first run**). The brand is named at most once (the skill's "at least twice" is a paid rule). |
| Transcript check | Whisper (or ElevenLabs Scribe) word for word on every take and every speaking clip; a bad line is regenerated before any video. **Albanian and every non-English voice: a multilingual faster-whisper model (`small` or `medium`, `language="sq"`), never the `.en` models the animation checker names**; Whisper small mangles Albanian spelling, so use it for word presence and timing, and read spelling against the script. |

## 5. Picture and edit

- **Frame rate (issue 10): deliver 30 fps** for AI video. Drama's model table lists H3 output at 24 fps (check with
  ffprobe on the first take): conform to 30 by repeating frames (ffmpeg `fps=30`), never by motion interpolation of a
  dialogue shot. Drama may deliver 24 fps for its look, stated in the run, and then redoes its beat math (written at
  30 fps). Code-rendered motion (motion-reel) delivers 30 or 60 fps (canvas engine 60 fps with 4 subframes; HyperFrames
  `--fps 60`); Lemo-Opuscar and Claude Animation Base pages render and deliver at 24 fps. Claymation's 12 fps stepped
  cadence is a look inside the clip, not the file rate: the dropped-frame check reads the container rate only.
- Export: H.264 High, 1080x1920, AAC 48 kHz; the ElevenLabs master (or the song) is the only audio; clip audio muted.
- Speed changes: silent clips may be trimmed or sped up to 2.5x at most (the song skill's "up to about 2.7x" is
  overruled); **never a lip-synced clip** (it breaks sync with the master).
- **Hook timing, one rule per format.** Spoken formats (talking head, UGC, narrator, motion voice-over, podcast line 1):
  first word at 0.0 s, meaning within 0.1 s of the first frame. Song: after the intro trim the voice arrives within
  0.3 s; the first sung word by about 1 s; the problem sung by about 3 s, inside the first 6 words; more than 3 s to the
  first problem line means regenerating the opening before any picture, and a slow hook never ships. Drama (X8): the
  first spoken line by 1.5 s (up to 4.0 s only after a strong readable action that shows the problem sound-off within
  1 s), a real sound by 0.3 s, a story event by 1.0 s, no near-static shot in the first 4 s; the drama skill's older
  "first line by 4 s" lines are stale. Motion: motion in the first second and the hook text on screen by 0.3 s (M5).
- Picture change: every 2 to 4.5 s (songs 1.5 to 3.5 s; UGC and B-roll 1.5 to 3 s; a strong talking head may hold 4 to
  6 s); in the first 5 s something changes every 1 to 1.5 s; motion in the first second.
- Songs: one H3 take holds 2 to 3 shots (4 at most), each 1.5 to 3.5 s, so a sung sequence covers 4 to 10.5 s of song
  (14 s at most with 4 shots; 4 s is the slice floor, section 2); the skill's 15 s sequences of 3 to 6 shots are not
  used. The beat grid comes from `librosa.beat.beat_track` and every cut snaps to the nearest beat. The vocal stem
  (ElevenLabs isolation or UVR MDX-Net Voc_FT) is checked at about 30 dB under the mix in instrumental parts, and
  phrases are re-timed on the stem (RMS above about -38 dB).
- Drift (hub G6): fix in the edit: cut at each lag step inside a pause, or one median offset when steps are under
  0.15 s; retake only when drift sits inside a word or correlation stays under about 0.5.
- Podcast cut map: in point 0.08 s before onset, out point 0.12 to 0.2 s after the last word's energy drops; J-cuts of
  0.1 to 0.2 s; a 0.8 to 1.5 s reaction shot at least every 10 s; punch-in 112 to 118% as a second camera; 20 to 80 ms
  fades at each cut. Turn gaps come from the master (section 4).
- End card 2.5 to 3 s with the music under it. The organic end card carries the card's one CTA from ORGANIC-OS: follow,
  save, send, comment (an answer to a question), keyword (only a keyword live in brain.json), dm, or book (convert
  posts only, said as the keyword or DM path: "comment ANALIZA; the booking button comes in the DM"). Never a link,
  price, discount, guarantee or urgency.

## 6. Text, captions and safe zones

| Element | Rule |
|---|---|
| Text hook / carousel cover headline | **4 to 10 words**, top third, frame 1 to about 3 s, never over the frame-1 subject; optional label of 6 words or fewer. Drama: optional, 6 words at most (X7). |
| Podcast title bar (its text hook) | 4 to 8 words (the skill's 8-word cap inside the 4 to 10 rule), 2 lines at most, about 44 to 50 px type at 1080 wide, in the top third below the top 14%, frame 1 to about 3 s, checked against every start frame so it covers no head; it carries the ICP and the pain, never a summary. With no burned-in tag (section 7), nothing else sits in that band. |
| Captions | 1 to 4 words per card (songs and podcast 1 to 3), bold sans, contrast 4.5:1 or more, timed to the word; songs: the words as sung with about 0.3 s tail; podcast: each card clamped inside its own line's segment, never across a cut, and no gap over 0.4 s while someone talks. Size 80 to 100 px at 1080x1920 (4.5 to 5.5% of frame height). Placed about 55 to 62% down: above the bottom 35%, below the faces, inside the side margins, out of the right 21% of the lower half; never over a face, a key prop or in-frame text; none over a silent opening. |
| Supers | 2 to 6 words, never the transcript |
| Text in AI video | Never rendered by the video model; added in the edit |
| **Reels safe zone (issue 11)** | **Top 14% and bottom 35% clear of key content, plus the right 21% of the width in the lower half, and 6% side margins** (at 1080x1920: top 269 px, bottom 672 px, right 227 px in the lower half, sides 65 px). Faces and key props sit 15% to 55% from the top (drama says 60%, but captions start at 55%), eyes about 30 to 40% down. Body text never under 44 px on a 1080-wide frame, checked at 360 px wide. Drama's 35 to 40% is the strict end. motion-reel's house zone (top 250, bottom 400, right 140 px) is overruled: run `node motion-studio/tools/safezone.mjs <dir> --top 269 --bottom 672 --right 227 --left 65 --min 44` (it applies the right margin at every height, which is stricter) and check HyperFrames pages against the same zone. |
| Feed images and carousel slides | Text and logo inside a 4% margin; the cover headline readable at 200 px wide |
| Carousel slides | Cover headline 4 to 10 words in 2 or 3 lines of about 12 characters, readable at 200 px wide. Body: one idea per slide; headline 7 words or fewer, then 1 or 2 short lines; list items 5 words or fewer; SHORT lane 5 to 15 words or DENSE lane up to 30 words in 5 lines at most (only the turn slide may break its lane; past 30 words, split the slide). Slide 2 answers the cover in under a second and works alone. Counters 1/NN to NN/NN. One ask, on the last slide, which has no arrow. Proof every 2 to 3 slides only from the proof bank; with no proof, show the process. |
| Numbers and screens | No counts on screens, phones or in lines unless the number is in brain.json: screens show states ("a pile of unanswered messages"), not counts. No real platform logos or names on screen: "the inbox", "the phone". A count of the post's own items ("7 gjëra" on a 7-item post) is structure, not a claim, and must match the post. |
| Punctuation | No em dashes anywhere (spoken, super, caption, slide) |

## 7. AI disclosure (issue 12)

**This section is the rule** (other docs say "per STANDARDS 7 (D1 decides whether to extend it)"). One policy for every
format, aligned with Instagram's AI label (Organic Growth OS section 13):
- Turn on **Instagram's own AI label** for every post with a photoreal AI person, an AI voice speaking as a person, or
  realistic AI footage. This includes a voiced motion reel with an ElevenLabs narrator (reel_motion is always voiced)
  and carousel slides or single images with a photoreal AI person or scene. No burned-in "AI DRAMATIZATION" tag (the
  podcast skill's tag is retired); the song, carousel and motion-reel skills have no disclosure rule, so this section is
  theirs.
- Stylized animation (clay, crochet, 3D family-film, 2D storybook) also gets the label until the owner decides
  otherwise (decision D1).
- **AI people, until D1 is decided** (brain.json D1 interim, verbatim: "AI people are only shown from behind or as
  clearly staged scenes; no AI person is presented as a real client."). The StraightScale strategist may face the
  camera only as a presenter in his clearly staged studio set (the whiteboard), AI label on, never as a client, owner or
  customer. AI business owners in POV or UGC, AI podcast hosts and drama characters who could pass as real owners are
  shown from behind, hands only, at distance, or as stylized animation. A confession POV needs real footage.
- An AI person is never presented as a real customer or client, and never carries a real or invented result.
  Anecdotes in the brand's voice only as clearly framed POV dramatizations ("POV: ..."), never stated as fact.
- The final reviewer checks this (V26, F7); the hub draft's notes say "AI label: on" when it applies.

## 7b. Drama exceptions (drama-ads 0b, X1 to X10)

X1 to X4 were approved by the owner on 11 Oct 2026 (drama v1); X5 to X10 came with drama v2 and replace v1's X2. They
apply inside the drama skill only. This table says which ones organic drama adopts.

| X | Rule it relaxes | Exception | Limits | Organic |
|---|---|---|---|---|
| X1 | G4 one speaker per generation | Holds for every lip-synced clip; fast exchanges are built from per-character stems with listening gaps and cut in the edit | A second character may be visible but silent; never two lip-synced speakers in one generation | Adopted (section 2) |
| X2 | v1 "silent story-action clips" | Removed in drama v2; the hub's X2 line is stale | | Nothing to adopt |
| X3 | Hook Lab gate 9 (never ashamed) | Gate 9 holds for the first 3 s; after that a character may feel embarrassed when the story needs it | Shame stays private and is resolved by the payoff; no medical severity; the brand never mocks the hero | Adopted |
| X4 | B15c never hedge the result | The hero may share the credit | Only when the change is shown; at most 2 credit lines per ad | Not adopted: an AI person never carries a result (section 7) |
| X5 | G1 H3 for every human clip | Routing by shot type to Kling 3.0 and Omni, Seedance 2.5, Cinema Studio 4.0, Veo 3.1, Gemini Omni Flash; Sync Lipsync 3 after the move | Every shot from a set-bible frame; per-take QA; cost preflighted per model | Not adopted until D9: H3 for every shot (silent ones in keyframe mode); Kling 3.0 or Sync Lipsync 3 only with G-FALLBACK; any other model only with G-EXCEPTION per asset |
| X6 | G5 no filler | Silent shots are coverage: reactions, inserts, cutaways, establishing shots, entrances and exits | Every shot has one named job; mood b-roll with no story job stays banned | Adopted on H3 keyframe mode (one shot per clip, section 2); needs no G-EXCEPTION |
| X7 | Text super from frame 1 to about 3 s | The text hook is optional in drama and off by default | If used: 6 words at most, small type, no box, never over a face, gone by 3 s | Adopted (section 6) |
| X8 | First spoken word at 0.0 s | First spoken line by 1.5 s; up to 4.0 s only after a strong readable action | No greeting, establishing-only opener, title card or near-static shot in the first 4 s | Adopted for drama (section 5 hook timing) |
| X9 | "AI DRAMATIZATION" tag on screen | No AI tag burned in | Never claim the footage is real, live or a real customer | Adopted in the section 7 form: Instagram's AI label always on |
| X10 | Followable with sound on and picture off | The story survives on mute; the selling facts survive listening only or ride on supers and captions | Both cold reads in drama 5.4 pass | Adopted: G-SCRIPT for drama needs both cold reads at every length |

Organic drama characters who could pass as real owners follow section 7's AI-people rule.

## 8. Lengths

**This section is the single source for lengths** (other docs point here).

| Tier | Seconds | Use |
|---|---|---|
| O15 | 10 to 20 | one point: a quote reel, a stop-doing-X |
| O30 | 20 to 35 | compact shapes: myth buster (ST6), short mistake list (ST7), compact hidden cause (ST3), demo (ST14); the animation short; the song short (hook + one chorus); the drama short (one scene, one turn) |
| O60 | 45 to 75 | **the organic story tier:** POV day (ST4), hidden cause (ST3), two futures (ST5), a challenge episode (ST17), drama POV, song |
| O90 | 75 to 90 | only with a stated reason (an unaware audience, a new mechanism); 90 s is the longest reel the growth-engine hand-off takes |
| Podcast C45 (issue 18) | **35 to 45 s, 8 to 12 turns, 80 to 110 words**; a turn is 20 words or fewer (one may reach 25); the listener speaks at least every other turn and at least every 8 s; no host has two turns in a row or more than 60% of the words; line 1 is the pain, with the ICP and the pain clear within 3 s; the payoff line ends on 6 words or fewer | One range for conversations. The router's 40 to 50 s C45 (100 to 140 words) stays for single-voice problem demos (paid). |

Podcast runs only at C45 (35 to 45 s). No full discovery story under 45 s (organic); never over 90 s until the owner
confirms a longer hub and publishing limit (then never over 3 minutes). Paid ads keep Script Lab's D15 to V300 router.

The card's tier decides the length: the `script` gate's length check passes when the runtime fits that tier (O15 10 to
20, O30 20 to 35, C45 35 to 45, O60 45 to 75, O90 75 to 90). The "30 to 60 s for reach" in GATES.md and
script-lab-organic.md is the default range for a reach reel, not a fail for an O15 quote reel or an O30 short.

## 9. Pass rules

| Gate | Pass |
|---|---|
| Hook (G-HOOK) | All 9 Hook Lab gates; every channel A or A+ (an A- is rewritten); organic: a fresh grader agrees on the master stack |
| Script (G-SCRIPT) | 85/100 or more and no critical fail, after a fresh cold read (two from O60 up, and on every drama at any length (X10): listen-only, and sound-off with only the picture beats, sound cues and supers). Songs: the speech passes first, then the lyrics pass the lyric gate read flat (tests 3, 5, 7, 8, 9, 12, 13 plus a fresh lyric cold read; tests 1, 6 and 16 against the released speech; chorus at least twice; line count fits the tier); the run's one G-SCRIPT record is written only after both, its note naming both scores. 3 FIX loops with new readers every loop, then the owner (G-HUMAN-ESCALATE) |
| Spec (G-SPEC) | Lint clean (`pipeline.py spec-check`) and a fresh prompt-reviewer PASS for the file's current version |
| Prompt (G-PROMPT-IMG, G-PROMPT-VID) | P1 to P12 all PASS for that exact prompt; 2 loops, then the Organic Director (who may send it to the owner as G-HUMAN-ESCALATE) |
| Visual (G-VIS, G-VIS-SHEET, G-VIS-BOARD, G-VIS-SLIDE) | Hero assets (frame 1 and the hook concept frame, every storyboard, sheets, covers, thumbnails, start frames, the style reference): zero defects. Others: zero critical, zero major, at most 2 minor. 3 attempts per asset (an edit pass is one attempt), then the owner (G-HUMAN-ESCALATE). |
| Continuity (G-CONTINUITY) | Across all storyboards of the piece: same faces, outfits and prop states; screen direction and geography hold; the story reads in order with no missing beat (VISUAL-QA 6). The record names the board versions it covers. |
| Set (G-SET) | The whole carousel: one visual world, swipe bridges line up, the turn looks different, slide 2 works alone, no slide could swap with another (VISUAL-QA 10.7) |
| Audio (G-AUDIO) | **Per audio asset** (voice, audio slice, song, music, SFX): the take check passed (transcript against the script or lyrics, take score, song Whisper floor 0.88). Record it with `pipeline.py gate <slug> <post_id> G-AUDIO --status PASS --by <who> --asset <ID>@v<n> --note "<what was checked>"`. An audio file with no G-AUDIO PASS can't be a reference in an H3 call. |
| Assets (G-ASSETS) | **Step 11's gate:** every asset's latest version passed its own gate (G-VIS*, G-TAKE, G-MOTION-FRAMES or G-AUDIO). `pipeline.py status` lists what is open. A losing hook finalist's concept frame passed G-VIS before grading; one the owner dropped after 3 failed attempts is closed by the owner's G-VIS OVERRIDE ("dropped finalist", `hook-lab-organic.md`). |
| Take (G-TAKE) | Zero critical, zero major; drift fixable in the edit; every scripted word present |
| Motion text (G-MOTION-TEXT) | Before any render (motion step 8): a fresh prompt-reviewer checks the code's text constants, layout positions, timing table and brand colours against the Shot Spec and the released script (VISUAL-QA 7.2; checks M1, M3, M4, M6), recorded on the `motion_render` version with `pipeline.py record`. G-MOTION-FRAMES fails on a version without it. |
| Motion (G-MOTION-FRAMES) | A fresh take-reviewer passes M1 to M7 on preview frames every 0.5 s plus each transition's start, middle and end (`vqa_crops.py motion`), and motion-reel's automatic checks pass on the same render: `tools/seekcheck.mjs`, `tools/pacing.py` against the references, `tools/audio_qa.py`, `tools/safezone.mjs` with the section 6 zone, HyperFrames `check --caption-zone`, Lemo `readcheck.mjs` for Lemo pages. motion-reel's 9-axis self-score is the builder's check before review, not the gate. M5 means the hook text is on screen by 0.3 s (motion-reel's "hook in the first 2 s" is overruled). Nothing important frozen more than 4 s. Fix in code, re-render the preview, review again; final render only after PASS. |
| Final (G-FINAL) | F1 to F8 on frames every 1.5 s plus every cut (drama: every 1 s plus every cut's first and last frame), plus the sound-on watch, the voice-alone listen (robotic means back to step 4) and the banned-model check (the run's `calls.jsonl` shows only standard models or a recorded G-EXCEPTION or G-FALLBACK); then the Director's pass (G-DIRECTOR), then the owner on the hub (G-HUMAN-FINAL). Drama also needs the film-test score card at 85/100 or more, run by the fresh take-reviewer on every drama: Hook 15, Story 15, Picture 10, Continuity 10, Pacing and retention 15, Proof and payoff 10, Sound and music 10, Captions 5, Ending and CTA 10; below 85, fix the lowest areas and re-render. |

**Human checkpoints** (standards.json `human_checkpoints`): G-HUMAN-SPINE (delegable), G-HUMAN-VOICE (once per voice:
audition and 15 s pilot; the keyframe quote reel's step 4 needs it until the narrator's record exists), **G-HUMAN-SONG**
(every song master, before any picture), G-HUMAN-LOOK (once per series), G-HUMAN-HOOKBOARD (every hook board; drama
adds the animatic and cost preflight, podcast the line-1 start frame with the title bar, motion the hook styleframe),
G-HUMAN-ESCALATE (an asset after 3 failed attempts, a script after 3 FIX loops), G-HUMAN-FINAL (every post; Albanian strings marked for a native
read), G-HUMAN-TEST, G-FALLBACK (Director), G-EXCEPTION.

## 10. Budget

- Prices: H3 2 credits/s (a 15 s clip is 30); Kling 10 per 5 s; GPT Image 2.5 at 2k medium 1 credit (high 2.75);
  other stills 1 to 6.5 credits (price them with `get_cost`); ElevenLabs about 177 credits per 4-take narrator beat
  (15 Oct). A carousel of 7 to 12 slides at medium is 3 concept frames (one per finalist hook stack, 1 each) + 1 to 3
  cover rounds of 4 (4 to 12) + slides 2 to N (6 to 11) + 25% = about 16 to 33 credits; organic.json's carousel range 7 to 90 and ORGANIC-OS 7.7's 60 to 90 come from GPT
  Image 2 at 2k high (6.5 per slide) and are stale. Cover rounds: `count: 4` per round, one round is one attempt (3 at
  most, then G-HUMAN-ESCALATE). A batch holds at most 12 requests and takes no cost preflight: price with one single
  `generate_image` call with `get_cost: true`.
- **When G-BUDGET runs.** `pipeline.py budget` (gate G-BUDGET) runs before the **first** generation of a run: at step 4
  for voiced pieces (the ElevenLabs voice is a generation), before step 7 on a LIB run, and again within 24 h of each
  later batch: the gate refuses any gated generation without a G-BUDGET PASS from the last 24 hours. **Step 9 then
  re-prices the whole video** (every planned clip and still + 25% for retakes, against the client's monthly cap in
  brain.json and the live balance): step 9 closes only on a G-BUDGET recorded after the earlier steps closed, and the
  gate refuses every video call until step 9 is closed. Re-check the balance right before every submit: credits are
  shared with every other session. G-PROMPT-IMG sits at steps 7 and 8 (sheets, storyboards), G-PROMPT-VID at step 10.
- Tier A pieces only with a proven angle or the month's wildcard (Organic Growth OS 7.7).

## 11. QA methods

- Stills: `vqa_crops.py image` (full, 3x3 tiles at 2x, region crops, panels, 200 px thumbnail; OCR only as a second
  opinion: it misreads ë and ç). The reviewer opens every file in the manifest.
- Video takes: frames at 1 per second (2 per second under 6 s) plus the first and last 0.1 s, contact sheets
  (`vqa_crops.py frames`); drift (`vqa_crops.py drift`); Whisper words. Talking takes: face crops at least 190 px wide at
  viewing size; a used line is rejected on a lens look, a profile, eyes down or shut over 1 s, leaving frame, a gesture,
  a smile on a problem line, a frozen pose over 4 s, or drift from the start frame. Song takes: every sung word against
  the lyrics, never one middle frame per shot.
- Motion renders: frames every 0.5 s plus each cut's start, middle and end (`vqa_crops.py motion`).
- Final cut: frames every 1.5 s plus every cut (`vqa_crops.py final`), sound-off watch, sound-on watch, voice-alone
  listen, transcript, loudness (`vqa_crops.py loudness`: integrated, true peak, range, short-term), banned-model check.
  Drama adds the jump-cut scan (the last and first frame of each cut at 90x160 grey; every pair with correlation above
  about 0.6 is reviewed) and the phone shadow floor (average frame luma under about 0.10, or a lit face under about
  0.25, is lifted).

## 12. What each skill keeps, and what this file overrides

| Skill | Keeps (method) | Overridden here |
|---|---|---|
| readymerce-ads-machine (hub) | Module 0, Part L, Section G method, C3 order | Loudness, fps, safe zones, AI label, the C10b "3 to 8 s per shot" clip line (clips are 5 to 15 s), the drama exception list (7b, D9) |
| readymerce-hook-lab | The stack, 9 gates, rubric, H0 to H7 | B2B profile, carousel mode, organic metrics, the fresh grader (adapters/hook-lab-organic.md) |
| readymerce-script-lab | Everything in WRITE/GRADE/FIX | Organic tiers and rungs, scorecard re-weight, sound-off read, organic LEARN (adapters/script-lab-organic.md); the C45 podcast range |
| readymerce-animation-ads | Phases, style bible, shot ledger, 12 shot-logic tests | Image model pending R1, pause cap, loudness, clip duration, shots per take, the 4-shot board canvas |
| readymerce-song-ads | Phases, lyric gate, 10 shot-logic tests | Song route (ElevenLabs Music default), Whisper floor, G-HUMAN-SONG, H3 settings and prompt card, sequence length, drift method, loudness, shots per take, speed-up cap, brand at most once |
| readymerce-podcast-ads | Pinterest refs, master two-shot, speaker map, cut map | AI tag (label instead), loudness, C45 range, words per stem, one-panel storyboard |
| readymerce-drama-ads | Templates, concept card, beat sheet, shot list and 15 rules, film test | X4 not adopted; X5 routing (D9); X8 first line by 1.5 s; X10 both cold reads; the film test on every drama at G-FINAL; music 14 to 18 dB under the voice; 30 fps by default; safe zone (adopted for all reels) |
| carousel-machine | Steps, idea score, story positions, style locks | Hook via Hook Lab carousel mode; fresh visual reviewer and G-SET replace its self-critic; cover 4 to 10 words; quality medium for every slide (its `low` for body slides is overruled); 4:5 and 1080x1350 delivery |
| claymation | Sub-style block, physicality block, motion guard | Its models (section 1 claymation row) |
| motion-video-director | (retired for our work) | Use motion-reel: it already follows our pipeline (issue 13) |
| motion-reel | The HyperFrames workflow, the engines, the refbank no-repeat check, native re-layouts | Hook Lab + Script Lab for its words (its 2.4 words/s budget and one alternative hook line give way to the Script Lab gate and 10 graded hooks); G-MOTION-TEXT, then M1 to M7 by a fresh reviewer plus its automatic checks (section 9); the safe zone (its 250/400/140 px house zone, section 6); frame rate (section 5); music 14 to 18 dB under the voice (not 10 to 20); a transcript check of the voice against the script; the AI label (section 7); no em dashes |

## 13. The 18 issues, checked and resolved

Every claim was checked against the skill text by a reader agent on 15 Oct 2026 (quotes and line numbers in
`audit/skill-audit-2026-10-15.md`).

| # | Issue | Checked | Rule now |
|---|---|---|---|
| 1 | Image model differs | True (hub G7 GPT Image 2 for faces, song and animation Nano Banana 2, carousels GPT Image 2.5) | Section 1: faces GPT Image 2 + reference; carousels and statics GPT Image 2.5; stylized Nano Banana 2 until R1 |
| 2 | H3 duration | True (hub: padded slice; drama 11 Oct: stem + 1 s) | Section 2 interim rule (slice 4 to 14 s, duration + 1 s on top of any tail); re-test R2 |
| 3 | Minimum clip | True (drama lists 4 to 15 s) | 5 s |
| 4 | Words per clip | True (hub and podcast 30 to 35; drama about 20) | 30 to 35 monologue; podcast stem from time (about 27 to 30); drama about 20 |
| 5 | Shots per take | True (song 3 to 6; animation 2 to 3 reliable and also "2 to 4"; hub 2 to 4; podcast 1) | 1 to 3, 4 at most |
| 6 | Song skill lags the hub | Partly true (no `minimax_h3` id, 2K, `declined_preset_id` or 5 s floor; its own 7-part prompt lacks the hub card's hands-and-props and background lines; a single cross-correlation instead of the G6 drift check; the hub itself still says Suno; the ElevenLabs Music song runs are stated in AI-VIDEO-PIPELINE step 4 but no run files are in the repo) | Section 1 song route; song runs use the H3 card and the drift method |
| 7 | Drama exceptions vs hub ban | Partly true (hub line 78 lists X1 to X4 with a stale X2; drama v2 replaced X2 with X5 to X10, and only X5 routes shots to other models; X6 to X10 cover silent coverage, the text hook, first-line timing, the AI tag and two cold reads; hub G2 already allows Kling 3.0 as a fallback; the claymation skill's Seedance 1.5 Pro default is another off-hub route) | Section 7b; X5 not adopted for organic until the owner decides (D9); G-EXCEPTION per asset meanwhile |
| 8 | Pause handling | True (hub bans caps; animation's `vo_build2.py` caps at 0.4 s and the hub sends every module to it) | Section 4: never capped |
| 9 | Loudness | True (-16 animation and podcast, -14 drama and motion, song none, hub none) | -14 LUFS, -1 dBTP, LRA 11 LU or less |
| 10 | Frame rate | True (drama 24 fps; motion-reel 60 fps; Lemo and Claude Animation Base 24 fps) | 30 fps for AI video, conformed by repeating frames; motion 30 or 60; code styles 24 |
| 11 | Safe zones | True (14/20 vs drama 14/35-40 + right 21%; motion-reel 250/400/140 px) | The drama zone plus 6% sides for every reel, in px in section 6 |
| 12 | AI tag | True (podcast burns a tag; drama bans it) | Section 7: Instagram's label |
| 13 | motion-video-director conflicts | True (result-first hooks, em dashes as pause marks, user-made MP3, Freesound) | Retired; motion-reel |
| 14 | Carousels skip Hook Lab and the cold read | True | Hook Lab carousel mode, a fresh cold read of the slide copy, and fresh G-VIS-SLIDE and G-SET reviewers in place of the skill's self-critic loop (adapters/carousel-machine-organic.md, sections 2 and 3) |
| 15 | Hook Lab tuned to DTC health | True | B2B profile (adapters/hook-lab-organic.md) |
| 16 | Learning is paid-only | True (H8 and LEARN read Meta ads data only) | Organic LEARN (adapters, analyst agent) |
| 17 | Script Lab caller table misses drama and motion | True | adapters/drama-organic.md routes drama through Script Lab; adapters/motion-reel-organic.md section 2 says how motion-reel calls Hook Lab and Script Lab; the table itself lives in the synced skill (owner edits it on claude.ai) |
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
| D1 | AI label policy and AI people for the account (existing decision in brain.json) | | Section 7 until decided |
| D9 | Drama model routing (X5 only: Kling 3.0 and Omni, Seedance 2.5, Cinema Studio 4.0, Veo 3.1, Gemini Omni Flash, Sync Lipsync 3 after the move) for organic drama | | H3 for every shot (silent ones in keyframe mode); Kling 3.0 and Sync Lipsync 3 with G-FALLBACK; others with G-EXCEPTION per asset |
| H1 | Human listens. AI-VIDEO-PIPELINE step 4 asks for four listens (audition, pilot, master, bed). In force: G-HUMAN-VOICE once per voice (audition and pilot) and G-HUMAN-SONG on every song master; the spoken master and the bed pass on the measured take checks and G-FINAL's voice-alone listen | | The owner may restore the four listens |

## Changelog
- 2026-10-15 v1.0: first version from the skill audit and the two owner specs.
- 2026-10-16 v1.1, models: GPT Image 2.5 settings (2k, medium or high, variant flare) and GPT Image 2 settings and reference checked by the gate; 2.5 refused for realistic people in reel stills; the 4:5 photoreal slide route; Nano Banana Pro removed; claymation row; song route with a 0.88 Whisper floor (proposed).
- 2026-10-16 v1.1, edit pass: an asset's own previous version is allowed as the single reference (role `edit_source`), with its own full review.
- 2026-10-16 v1.1, clips: slice 4 to 14 s with +1 s on top of any tail; podcast stem words 27 to 30 (proposed); drama 20; shots per take 1 to 3; silent keyframe clips one shot; podcast one-panel storyboard; takes on singing sequences.
- 2026-10-16 v1.1, stills: 4-shot board is a 9:16 canvas; every storyboard and the hook concept frame are hero; carousel delivery files.
- 2026-10-16 v1.1, audio: non-English pace band from the audition; long pauses 1 per 3 sentence ends (proposed); audio tags; conversation gaps from the master; bed, ducking, SFX levels; LRA and short-term loudness; G-HUMAN-SONG; lyrics.
- 2026-10-16 v1.1, picture: frame rates by engine; speed-up 2.5x; hook timing per format; song sequences; podcast cut map; organic CTAs on the end card.
- 2026-10-16 v1.1, text: podcast title bar; caption size and band; safe zone in px with 6% sides and the face band; carousel slide text; no counts or platform names on screens.
- 2026-10-16 v1.1, AI label and drama: section 7 is the rule, voiced motion and photoreal slides included, AI people interim rule; new section 7b (X1 to X10).
- 2026-10-16 v1.1, lengths: podcast only C45; O30 song short; O90 75 to 90 s and a 90 s outer limit; tier decides the script length check.
- 2026-10-16 v1.1, gates: G-AUDIO and G-ASSETS explained; G-CONTINUITY, G-SET rows; new G-MOTION-TEXT and G-HUMAN-SONG; G-HUMAN-VOICE at the quote reel's step 4; prompt loops go to the Organic Director; G-FINAL adds sound-on, voice-alone and banned-model checks, and the drama film test; budget timing (step 9 re-prices before any video call).
- 2026-10-16 v1.1, verifier fixes: the 3:4 photoreal-slide route needs G-EXCEPTION; a count of the post's own items is structure; O30 adds the drama short; a script after 3 FIX loops goes to G-HUMAN-ESCALATE; a dropped hook finalist's frame closes by the owner's G-VIS OVERRIDE; the carousel price adds the 3 concept frames (about 16 to 33).
- 2026-10-18 v1.2, Atlas Cloud: the `atlas` CLI runs behind the gate (`growth-engine/tools/atlas/`); the Atlas allowlist is `standards.json` `models.atlas.allowed` (entries with id, kind, parameters, duration bounds and text fields), empty until the owner names a model, so every Atlas generation is blocked; `atlas generate 3d` and `atlas chat` are blocked.
