# Format library (v1.0, 28 Oct 2026)

**What this file is.** Every video, carousel and static format we can make, what each one is for, which skill makes
it, how it runs on Atlas, what it costs, and what StraightScale already made in it. The Strategist picks a format from
here, by the card's load-bearing beat; the router (`growth-engine/tools/organic_os/router.py`) does the ranking.

**Why it exists.** Matan, 28 Oct 2026: "Why all of the generations you make are literally just motion graphics… it's
not what we want to make for each client." "You're not using the actual readymerce-ads-machine system to generate UGC,
PODCAST, ANIMATION, or anything we can actually make." The cause was ours: the router gave a bonus to the cheapest
tier ("cheap: test the angle first"), so November's slate became 7 `reel_motion` cards out of 12. Cost no longer ranks.

**Precedence.** A number (model, length, price, pass rule) comes from `STANDARDS.md` and `standards.json`; this file
cites them. A method (how to write a hook, cast a voice, build a sheet) comes from the skill named in each entry. The
machine values (families, funnel, L19 levels, Atlas units, USD) are in `growth-engine/config/organic.json` `formats`
and `beats`. Written from a read of readymerce-ads-machine v13.4 (L19, Part C, Section G), readymerce-animation-ads
v3.6, readymerce-podcast-ads v5.0, readymerce-drama-ads v2.2, readymerce-song-ads, readymerce-script-lab,
readymerce-hook-lab, ugc-video-script-and-storyboard-designer, ad-video-factory, claymation and storyboard-ai-ad, plus
`STORY-FORMATS.md`, `STANDARDS.md` and `organic.json`.

---

## 1. How a format is chosen

**Message first, format last** (ads-machine 0.4, L19). A Post Card names its idea, job, belief and story first. Then:

1. **Name the load-bearing beat** (`load_bearing_beat` on the card): the beat that does most of the selling.
   - `mechanism`: the edge is invisible (a system, a cause, software, anything internal). StraightScale's own offer is
     a mechanism business: the pieces built in order.
   - `proof`: the edge is visible and needs a believable face or a demonstration.
   - `offer`: the deal itself is different.
   - `list`, `data`, `type`: the idea is a list in a fixed order, a number or chart, or one sentence that works as type.
     These three are the only beats `reel_motion` may carry.
2. **Score the formats on L19's six properties** (each format holds 0 no, 1 partly, 2 yes in `organic.json`):

   | Property | Needed for |
   |---|---|
   | Face: can it carry a believable human face? | the problem and the proof |
   | Invisible: can it show what a camera can't? | the mechanism |
   | Order: do we control the order the viewer takes it in? | every beat; lists most |
   | Sound: can we count on sound? | voice, dialogue, song |
   | Attention: can it hold attention long enough? | stories and mechanisms |
   | Person: does it read as a person, not an ad? | proof and offer |

   Each beat weights what it needs (`organic.json` `beats.needs`): mechanism = invisible 3, order 1, attention 1,
   person 1; proof = face 3, person 2, sound 1; offer = order 2, person 2, face 1, sound 1; list = order 3, attention
   1; data = invisible 2, order 2; type = order 2, attention 1. Fit = weighted levels over the most possible, 0 to 5
   (`organic_os/l19.py`).
3. **Funnel stage.** Reach is TOF, trust MOF, convert BOF. A format built for the card's stage (first in its `funnel`)
   ranks up 1, one that also fits ranks up 0.5.
4. **Evidence.** Formats that win with this client's buyers (`content-map.json` `buyer_formats`) +3; the proven
   convert formats (strategist with a prop, podcast, comparison carousel) +2 on convert cards; the story template the
   card names +2.
5. **Variety** against the other planned cards (`organic_os/variety.py`):
   - no format family more than **twice in a week** (Monday to Sunday);
   - at least **4 families in a month** (from 6 posts up); a family not used yet this month ranks up 1, each earlier
     use ranks it down 1;
   - **`reel_motion` at most 1 post in 6** (1 in any smaller set), and only for a `list`, `data` or `type` beat.
   - `organic.py week-check` fails a slate that breaks these; `card-check` fails a motion card with any other beat.
6. **Cost only filters.** A format whose top price is over what is left of the month's USD cap is skipped. Price never
   adds or subtracts a point. Tier A still needs a proven angle or the month's wildcard (ORGANIC-OS 7.7).
7. **The map can block.** `content-map.json` `blocked_formats` (for example face-on AI people until D1) and a surface
   with 0 in `formats_per_week` (no carousels this month) are skipped.

**Mixed formats are allowed inside one piece** (L19): a real or presenter face for the hook and proof, a stylized
cutaway for the mechanism (animation F10 mixed media). Route by the beat that carries the most weight.

**Run it:**
```
python3 growth-engine/tools/organic.py route <slug> <card.yaml> --prev-family <yesterday's family> \
  --plan clients/<slug>/cards/<month folders>
```
Take the top format unless a written reason says otherwise (an existing released script, a template the card needs, a
family already full); the reason goes in the card's `notes`.

**Families** (`format_family`, what the variety rules count): ugc, presenter, podcast, drama, story, song, animation,
quote_broll, real, carousel, static, motion.

---

## 2. The library

Each entry: what it is for (beat, funnel, job, story shapes), the L19 levels (face, invisible, order, sound,
attention, person), the skill and its gates, the Atlas route, the USD per piece (`organic.json` `usd`, STANDARDS 10
prices + 25% retakes), and what StraightScale already made (section 4 has the files).

**Every video entry also obeys** the hub's Section G as STANDARDS restates it: the H3 prompt card (realism line, one
reference line per token, hands and props, a 2 to 4 shot timeline with one action per shot, background action in every
shot, the lip-sync block, negatives; ads-machine G1, VISUAL-QA 4.2); one speaker per generation (G4); no filler clips
(G5); the transcript and drift check on every talking clip (G6); realistic stills from GPT Image 2 with a reference,
written as iPhone photos (G7); every voice from ElevenLabs, now `elevenlabs/v3/text-to-speech` on Atlas, natural
pauses never tightened (G8); the budget preflight (G-BUDGET); Hook Lab A or A+ on every channel and Script Lab 85+
before any generation; AI label per STANDARDS 7.

**Atlas routes in short** (`standards.json` `models.atlas.allowed`): video on `minimax/h3-developer/reference-to-video`
(a mouth moves: stills + the voice slice as references) or `/image-to-video` (keyframe mode, silent), 768P, 4 to 15 s,
$0.024/s; stills on `openai/gpt-image-2/text-to-image` or `/edit` at quality medium, $0.059; voices on
`elevenlabs/v3/text-to-speech`, $0.10 per 1,000 characters; songs on `suno/chirp-v6`, $0.132 a call; talking objects on
`bytedance/avatar-omni-human-v2.0`, $0.0896 per second of audio; word timings on `xai/stt-v1`. Section 5 lists what
these don't cover yet.

### 2.1 UGC POV (`reel_ugc_pov`, family ugc, tier B)
- **For:** proof of the problem in the buyer's own day; TOF, MOF; reach and trust; `pov_day`, `two_days`.
- **L19:** face 1 (until D1 the AI owner is from behind, hands only or at a distance), invisible 0, order 2, sound 2,
  attention 1, person 2. Best beat: proof or a lived mechanism; weak alone on an invisible cause.
- **Skill and gates:** readymerce-ads-machine Part C (UGC formats) via `adapters/ugc-talking-head-organic.md`; Hook Lab,
  Script Lab (UGC adapter); Section G. A staged POV ("POV: ..."), never a real customer, never a confession (that needs
  real footage, `confession_pov`).
- **Atlas:** GPT Image 2 stills from a candid reference (G7), the set already moving in the still; H3 keyframe mode for
  silent hands and room shots; H3 reference mode only if a mouth is on screen.
- **USD:** $1.58 to $4.15.
- **StraightScale:** EN 04's POV hands-only spine (planned); the w43-3 v2 "22:47 race" used H3 B-roll of a POV
  (vetoed: invented facts, face-on AI people).

### 2.2 UGC talking head (`reel_ugc_talking`, family ugc, tier B)
- **For:** a creator talks to the phone: a confession-style problem, a failed fix, a peer recommendation; TOF to BOF.
- **L19:** face 2, invisible 0, order 2, sound 2, attention 1, person 2. Best beat: proof, offer.
- **Skill and gates:** readymerce-podcast-ads section 13 (solo creator variant: one Pinterest reference, 1 to 3 real
  settings, one locked voice, clips up to 15 s, jump cuts); Script Lab UGC adapter (D30, C45 or S60, organic O30 to
  O60). G1 prompt card, G4, G6 drift check.
- **Atlas:** GPT Image 2 master frame from a real candid photo (G7, needs quality high: F5), H3 reference mode with the
  creator's ElevenLabs slice (lip-sync on Atlas H3 is untested: F2).
- **USD:** $1.58 to $4.15.
- **StraightScale:** U1 aesthetic clinic (15 s), U2 real estate (13.2 s, H3 2K, eleven_v4) and U3 accounting (13.7 s),
  Albania round 3; the round 5 H3 set had 4 realistic UGC presenters. U2 failed (frozen office, a phone that vanished
  mid-gesture, a skipped cut, a pause-capped robotic voice) and is why the H3 prompt card and FL-08, FL-09 exist.
- **Blocked on the StraightScale EN map until D1:** a face-on AI creator reads as a real owner or client (STANDARDS 7).

### 2.3 Strategist with a prop (`reel_strategist_prop`, family presenter, tier B)
- **For:** the proven paid winner. A presenter explains one idea with one real prop (a sheet, an org chart, a phone);
  MOF and BOF first, TOF too; trust, convert, reach.
- **L19:** face 2, invisible 1 (the prop shows part of it), order 2, sound 2, attention 1, person 1. Best beat:
  mechanism with a physical stand-in, offer.
- **Skill and gates:** Hook Lab + Script Lab + H3 via `adapters/ugc-talking-head-organic.md` (O30 or O60); G1 prompt
  card with the hands-and-props line (which hand holds what in every shot). The strategist faces the camera only as a
  presenter in his clearly staged set, AI label on, never a client, owner or customer (STANDARDS 7). Rotate props.
- **Atlas:** GPT Image 2 presenter still from the locked identity reference (F5), H3 reference mode with his voice
  slice (F2), one cutaway still per setting.
- **USD:** $1.58 to $4.15.
- **StraightScale:** IP-01 (`clients/straightscale/brain.json`, internal only): all 4 paid winners in Albania used a
  strategist at a whiteboard with one real prop, about ILS 19 per lead. V3 "three questions" (UGC presenter, 39.8 s,
  Seedance 2.0) made the strategist identity reused later.

### 2.4 Talking head at a whiteboard or chalkboard (`reel_whiteboard`, family presenter, tier B)
- **What it is:** an **H3 presenter with drawn board inserts.** The strategist stands at a whiteboard or chalkboard in
  his staged set (H3 reference mode, his voice slice), cut every 3 to 6 s with full-frame inserts of the board itself:
  the mechanism drawn one stroke at a time (a box, an arrow, a crossed-out fix, the buyer's sentence written word for
  word). The presenter carries trust; the board shows what a camera can't.
- **For:** mechanism (the strongest presenter fit), list, offer; MOF and BOF first, TOF too; trust, convert, reach.
- **L19:** face 2, invisible 2, order 2, sound 2, attention 1, person 1.
- **Skill and gates:** Hook Lab + Script Lab + H3 presenter via `adapters/ugc-talking-head-organic.md`; board inserts as
  progressive states (ad-video-factory ANIMATION.md style 3: "whiteboard is the same idea with progressive draw-in
  states"), or the code-rendered Whiteboard Explainer style in lemo-opuscar; G-VIS on every board state (no
  pseudo-text, FL-10), G-MOTION-FRAMES when the inserts are rendered in code. Board text only from the released script;
  no counts the brain doesn't hold (STANDARDS 6).
- **Atlas:** presenter as 2.3; board states as GPT Image 2 `/edit` chains from one empty-board still (each state the
  previous plus one stroke), animated with H3 keyframe mode start to end, or rendered in code at $0.
- **USD:** $2.02 to $4.74.
- **StraightScale:** IP-01 (above: the winning ads were a strategist at a whiteboard); V1 "one-hour rule" (chalkboard
  animation, 55 s, Albania round 4, Final Ads doc).

### 2.5 Podcast clip (`reel_podcast`, family podcast, tier B)
- **For:** a real disagreement between two hosts; the second host is the viewer's proxy and asks the objection out
  loud; offer and objections; MOF, BOF; trust, convert; `podcast_disagreement`.
- **L19:** face 2, invisible 0, order 2, sound 2, attention 2, person 2. Best beat: offer, proof.
- **Skill and gates:** readymerce-podcast-ads v5.0 via `adapters/podcast-organic.md`: one Pinterest photo per host and an
  empty set photo, one master two-shot, one start frame per character, one locked voice each, one character per
  generation, frame-by-frame QA. C45 only: 35 to 45 s, 8 to 12 turns, 80 to 110 words (STANDARDS 8). Until D1 the
  hosts are shown from behind, at a distance or as stylized animation (STANDARDS 7).
- **Atlas:** GPT Image 2 master frame and start frames (F5), H3 reference mode per host with that host's packed stem (F2).
- **USD:** $3.49 to $5.12.
- **StraightScale:** none made. STORY-FORMATS.md 7 has a pilot idea card ("Agjenci tjetër apo një sistem?").

### 2.6 Drama POV, 2 to 4 characters (`reel_drama_pov`, family drama, tier A)
- **For:** a scene from the buyer's day with a conflict in the first line and the mechanism as the answer near the end;
  TOF, MOF; reach, trust; `pov_day`, `two_days`, `overheard`; templates T1 to T13 (drama-ads 2).
- **L19:** face 1 (until D1), invisible 0, order 2, sound 2, attention 2, person 2. Best beat: proof by someone else's
  reaction, a lived mechanism.
- **Skill and gates:** readymerce-drama-ads v2.2 via `adapters/drama-organic.md`: concept card, beat sheet, screenplay in
  Script Lab's drama adapter with two cold reads (X10), shot list with retention rules, set bible, animatic gate, film
  test at 85/100. Exceptions X1 to X10 (STANDARDS 7b). Its multi-model routing (X5) is not adopted for organic (D9):
  every shot on H3, silent ones in keyframe mode.
- **Atlas:** GPT Image 2 cast and set stills, H3 reference mode for lip-synced close-ups (one speaker per clip), H3
  keyframe mode for reactions, inserts and establishing shots.
- **USD:** $3.21 to $8.28. Tier A: a proven angle or the wildcard.
- **StraightScale:** none made. hush_ads (another brand, vault) has 5 scene mp4s with no notes.

### 2.7 Skit (`reel_skit`, family drama, tier B)
- **For:** one scene, 2 characters, one overheard line that reframes the problem (C7 "skit / overheard line"); the lab
  version of a drama; TOF; reach; `overheard`, `two_days`. O30.
- **L19:** face 1, invisible 0, order 2, sound 2, attention 2, person 2. Best beat: proof, offer.
- **Skill and gates:** readymerce-drama-ads (a single-scene short) via `adapters/drama-organic.md`; one lip-synced
  speaker per clip (X1); the carrier speaks the reframe; STANDARDS 7 for people who could pass as real owners.
- **Atlas:** as 2.6, fewer shots.
- **USD:** $1.64 to $3.25.
- **StraightScale:** none made.

### 2.8 Narrated story (`reel_story_narrated`, family story, tier B)
- **For:** a narrator tells one buyer's day or two owners side by side over AI scenes; TOF to BOF; reach, trust,
  convert; `pov_day`, `two_days`, `hidden_villain`, `overheard`.
- **L19:** face 1, invisible 1, order 2, sound 2, attention 2, person 2. Best beat: offer, mechanism told as a story.
- **Skill and gates:** Hook Lab + Script Lab (organic) + H3 + the narrator voice; story beats from STORY-FORMATS.md
  (6.4: O60 at 45 to 60 s).
- **Atlas:** GPT Image 2 stills, H3 keyframe mode for the scenes, the narrator on `elevenlabs/v3/text-to-speech`.
- **USD:** $4.00 to $5.23.
- **StraightScale:** w43-3 v2 "The 22:47 race" (60 s, script 91/100; vetoed by the Director for a reply-time promise,
  invented facts, face-on AI people and the English voice; 16 defects at final QA). EN 04 "decided before you quoted"
  (planned).

### 2.9 Song ad (`reel_song`, family song, tier A)
- **For:** a sales letter set to music; reach and memory (sends, rewatches); TOF, MOF; `song_day`, `pov_day`. Judge on
  sends and follows, not DMs.
- **L19:** face 0, invisible 2, order 2, sound 2, attention 2, person 1. Best beat: mechanism in a picture.
- **Skill and gates:** readymerce-song-ads via `adapters/song-organic.md`: speech released by Script Lab, then lyrics
  graded flat; G-HUMAN-SONG (Matan listens to every master before any picture); Whisper match 0.88 or more.
- **Atlas:** `suno/chirp-v6` (custom lyrics, 20 to 90 s); character sheets and storyboards (stylized: F6); H3 reference
  mode with the vocal stem for every sung shot (F2).
- **USD:** $2.48 to $5.93. Tier A.
- **StraightScale:** S1 "Likes Don't Pay the Rent" (hip-hop, 3D, 74 s), S2 "Two Weeks Away" (claymation, 72 s), S3
  "Keep Your Price" (needle-felt, 77.7 s), S4 sung in Albanian (crochet, 72 s), all H3 lip-synced (song docs). Team
  note: "songs earn replays and shares; then run the best one as a paid ad". ORGANIC-OS 7.7: our song ads got paid
  leads at 2 to 3x the cost of the talking-head winners. EN 03 "Maya's quilt" (claymation, Atlas Suno, masters made).

### 2.10 Animation: claymation, crochet, 3D, skeleton, anime, 2D (`reel_animation` tier A, `reel_animation_short` tier B; family animation)
- **For:** showing the invisible cause as one picture (the patch sewn on alone, the leak in the funnel); TOF, MOF;
  reach, trust; `pov_day`, `hidden_villain`, `two_days`, `object_speaks`. The short is O30 (one character, 2
  sequences), the full piece O60.
- **L19:** face 0, invisible 2, order 2, sound 2, attention 2, person 2 (with a human voice). Best beat: mechanism.
- **Styles** (`organic.json` `animation_styles`, one locked block per series): `claymation` (the claymation skill's
  sub-style blocks, physicality and motion guard word for word), `crochet`, `family_film_3d`, `storybook_2d`,
  `skeleton_xray` (new: the A7 gym look) and `anime_2d` (new). Formats from animation-ads A2: F1 talking part, F2
  villain, F3 roll-call, F4 timeline, F5 anatomy explainer, F6 one-character story, F7 witness, F9 absurd metaphor,
  F10 mixed media.
- **Skill and gates:** readymerce-animation-ads v3.6 via `adapters/animation-organic.md`: audio first, style bible and
  sheets, storyboard per sequence timed to the voice, Phase 7a shot logic (no slop), G-HUMAN-LOOK once per series.
- **Atlas:** stylized sheets and storyboards (F6), H3 keyframe mode for actions and chained transitions, H3 reference
  mode where a mouth moves (F2).
- **USD:** short $1.35 to $2.05; full $2.73 to $4.15 (tier A).
- **StraightScale:** Albania round 3: A1 physio (claymation talking calendar, 21 s), A2 real estate (3D villain, 24 s),
  A3 law firm (crochet, 23 s), A4 language school (flat 2D, 23 s), A5 renovation (glossy 3D money pipe, 25 s), A6
  accounting (retro comic, 24 s), A7 gym (X-ray skeleton, 19.6 s); V2 "two weeks away" (papercraft, 49.7 s). English:
  EN 05 and EN 06 (claymation cloth world, planned).

### 2.11 Talking object (`reel_talking_object`, family animation, tier B)
- **For:** an object from the business speaks (the boosted post, the calendar, the unanswered DM, the newest patch):
  F1 talking part or F2 villain; TOF, MOF; `object_speaks`, `hidden_villain`. O30.
- **L19:** face 0, invisible 2, order 2, sound 2, attention 2, person 2. Best beat: mechanism.
- **Skill and gates:** readymerce-animation-ads (F1, F2) via `adapters/animation-organic.md`; animation-ads A4b: "a
  speaker who shouldn't talk" was in 10 winners and 0 losers.
- **Atlas:** mouth shots on `bytedance/avatar-omni-human-v2.0` (talking objects only: every Shot Spec subject a `PR-`
  prop; the clip is as long as its slice, 4 to 15 s); silent shots on H3 keyframe mode.
- **USD:** $3.14 to $5.97 (OmniHuman is about 3.7 times an H3 second).
- **StraightScale:** A1 physio's talking calendar (claymation); the round 5 set's 3 cartoon talkers.

### 2.12 Quote with B-roll (`reel_quote_broll`, family quote_broll, tier C)
- **For:** one point in one line over one moving shot; O15; TOF; reach; B1, B7.
- **L19:** face 1, invisible 0, order 2, sound 2, attention 1, person 1. Best beat: type, proof of a feeling.
- **Skill and gates:** the `clients/straightscale/content/2026-w42-6-reel/script.md` recipe: one H3 keyframe shot from a
  passed start frame, voice and captions in the edit; G-HUMAN-VOICE until the narrator's record exists.
- **Atlas:** one GPT Image 2 still, one H3 keyframe clip, the narrator voice.
- **USD:** $0.75 to $1.19.
- **StraightScale:** w42-6 quote reel (13.6 s; v1 to v3 failed on loudness, pseudo-text and the caption zone; v4 passed).

### 2.13 Lived authority (`reel_lived_authority`, family presenter, tier B)
- **For:** a composite person whose job is the context (an agency account manager, a front-desk lead) talks from where
  she works; TOF, MOF; reach, trust; `overheard`, `pov_day`.
- **L19:** face 2, invisible 0, order 2, sound 2, attention 1, person 2. Best beat: proof, a lived mechanism.
- **Skill and gates:** ads-machine C7 (lived-authority talking head; B3 POV library) with podcast-ads 13; no credentials
  the brain doesn't hold; a staged person, AI label on.
- **Atlas:** as 2.2.
- **USD:** $1.58 to $4.15.
- **StraightScale:** none made. **Blocked on the StraightScale EN map until D1** (a face-on AI person).

### 2.14 Real talking head and behind the scenes (`reel_talking_head_real`, `reel_bts_real`, family real, tier C)
- **For:** the owner on camera; the strongest trust format once the owner films; MOF, BOF, TOF; B3, B4, B7, B8.
- **L19:** talking head face 2, invisible 0, order 2, sound 2, attention 1, person 2.
- **Skill and gates:** talking-head-recut + embedded-captions (the owner films on a phone); Script Lab (organic);
  steps 11 to 13 still check the takes, words and final cut.
- **Atlas:** none (real footage); word timings on `xai/stt-v1`.
- **USD:** $0 to $0.59 (talking head and BTS reel), BTS carousel $0 to $1.70.
- **StraightScale:** none: `brain.json` `visual.real_footage` is false (E8, E12).

### 2.15 Carousel (`carousel_*`, family carousel, tier C)
- **For:** saves and depth: framework, self-check, mistakes, teardown, comparison, opinion, BTS; mostly MOF.
- **L19:** face 0, invisible 1, order 2, sound 0, attention 2, person 1 (BTS: face 2, person 2). Best beat: list, data.
- **Skill and gates:** carousel-machine via `adapters/carousel-machine-organic.md`; 7 to 10 slides; G-VIS-SLIDE, G-SET.
- **Atlas:** GPT Image 2 at medium (4:5 made at 1024x1536 and cropped, STANDARDS changelog 28 Oct).
- **USD:** $0.96 to $1.92.
- **StraightScale:** w43-1 carousel (7 slides, self-check, published 15 Oct, https://www.instagram.com/p/DehkW3EDa0B/,
  no results logged); w43-1b framework carousel (hub draft).

### 2.16 Static, single image (`image_question`, `image_review_quote`, family static, tier C)
- **For:** only a strong self-check question, a real review quote or an announcement; 1 a week at most.
- **L19:** face 0, invisible 0, order 1, sound 0, attention 0, person 1 (review quote: person 2).
- **Skill and gates:** carousel-machine (1 slide); paid statics follow ads-machine Part A (V1 designed, V2 native, V3
  story) and winning-statics.
- **Atlas:** one GPT Image 2 image.
- **USD:** $0.07 to $0.89.
- **StraightScale:** paid (Albania): the founder letter (best, ILS 32.5 per lead, 24 leads) and money math (ILS 40.7, 23
  leads) beat the call-back ads (ILS 94.3 and 101.6); 15 statics O1 to O5 x A1 to A3 planned on 6 Oct with no results
  recorded (static test doc). Organic: w42-5, w42-7, w43-2 images (hub drafts).

### 2.17 Motion graphics (`reel_motion`, family motion, tier C)
- **One option among many, never a default.** At most 1 post in 6, and only when the load-bearing beat is a `list`,
  `data` or a `type`-led idea. Always voiced (owner, 15 Oct), so the AI label is on.
- **L19:** face 0, invisible 1, order 2, sound 1, attention 1, person 0. Weak at emotion and at reading as a person.
- **Skill and gates:** motion-reel (HyperFrames) via `adapters/motion-reel-organic.md`; G-MOTION-TEXT before any
  render, G-MOTION-FRAMES on preview frames.
- **Atlas:** code-rendered; the voice on ElevenLabs v3; optional stills.
- **USD:** $0.08 to $2.34.
- **StraightScale:** Albanian reels 01 to 06 (motion, 14 to 50 s); w43-3 v1 "Fat apo sistem" (kinetic type, rejected by
  Matan: "boring, too much text, no voice"); EN 01 (killed: "generic advice, off-offer"); EN 02 (kinetic type, retired
  28 Oct: its beat was a mechanism).

---

## 3. The library at a glance

| Format | Family | Tier | USD per piece | Best beats | Funnel |
|---|---|---|---|---|---|
| `reel_ugc_pov` | ugc | B | 1.58 to 4.15 | proof, offer | TOF, MOF |
| `reel_ugc_talking` | ugc | B | 1.58 to 4.15 | proof, offer | TOF, MOF, BOF |
| `reel_strategist_prop` | presenter | B | 1.58 to 4.15 | mechanism, offer | MOF, BOF, TOF |
| `reel_whiteboard` | presenter | B | 2.02 to 4.74 | mechanism, list, offer | MOF, BOF, TOF |
| `reel_lived_authority` | presenter | B | 1.58 to 4.15 | proof | TOF, MOF |
| `reel_podcast` | podcast | B | 3.49 to 5.12 | offer, proof | MOF, BOF |
| `reel_drama_pov` | drama | A | 3.21 to 8.28 | proof, offer | TOF, MOF |
| `reel_skit` | drama | B | 1.64 to 3.25 | proof, offer | TOF |
| `reel_story_narrated` | story | B | 4.00 to 5.23 | offer, mechanism | TOF, MOF, BOF |
| `reel_song` | song | A | 2.48 to 5.93 | mechanism | TOF, MOF |
| `reel_animation` | animation | A | 2.73 to 4.15 | mechanism | TOF, MOF |
| `reel_animation_short` | animation | B | 1.35 to 2.05 | mechanism | TOF, MOF |
| `reel_talking_object` | animation | B | 3.14 to 5.97 | mechanism | TOF, MOF |
| `reel_quote_broll` | quote_broll | C | 0.75 to 1.19 | type | TOF |
| `reel_talking_head_real`, `reel_bts_real` | real | C | 0 to 0.59 | proof, offer | MOF, BOF |
| `carousel_*` | carousel | C | 0.96 to 1.92 (BTS 0 to 1.70) | list, data | MOF |
| `image_*` | static | C | 0.07 to 0.89 | type, proof | TOF to BOF |
| `reel_motion` | motion | C | 0.08 to 2.34 | list, data, type only | any |

---

## 4. What StraightScale already made

Sources: the Drive doc "StraightScale - Final Ads (Albanian text) - Oct 2026"
(https://docs.google.com/document/d/19gsV73aBaJg83siK5QeZTd73Sv2pd0vfK78600ClLSM, 13 videos, 9:16, English voice,
Albanian hook, subtitles and end card); the song docs (v1
https://docs.google.com/document/d/1yHHqWQf6X0FjoHHnu2KVvLzJYOFOO3Go2vaF9IGbXl0, FINAL
https://docs.google.com/document/d/1Ums8XqPqQJAIQlljD7sfo_bfOdb6coRsLTSvm5COSBA); the static test doc
(https://docs.google.com/document/d/1YutxttR7wK0YjGynFldXS_QbQ1tKs0j2qz2vDfwAUQA); this repo; the skills' lessons. The
vault's "StraightScale Growth Engine" notes (M1 to M8) are prompt templates and hold no ad results. Funnel stage is not
stated for the paid ads; rounds 3 and 4 ran on cold traffic (inferred).

| Piece | Format | Stage | Tools | What the notes say | Where |
|---|---|---|---|---|---|
| Founder letter (paid, rounds 1 to 2) | static, long text signed Matan | not stated | not stated | best: ILS 32.5 per lead, 24 leads | static test doc 1 |
| Money math (paid) | static | not stated | not stated | second: ILS 40.7 per lead, 23 leads | static test doc 1 |
| Missed calls, Lock screen (paid) | static | not stated | not stated | worst: ILS 94.3 and 101.6 per lead; the "we answer within the hour" message was dropped | static test doc 1 |
| Campaign "Albania B2B 28/09" | mixed | cold | | ILS 5,545, 96 leads, ILS 57.8 per lead; "the offer and the form are where the money leaks, not the hook" | static test doc |
| Strategist at a whiteboard (paid winners) | presenter with a prop | not stated | not stated | all 4 paid winners, about ILS 19 per lead (IP-01, internal only) | `clients/straightscale/brain.json` proof_bank |
| O1 to O5 x A1 to A3 (15 statics, 6 Oct) | V1 designed, V2 native, V3 story + founder letter | planned test | Higgsfield stills 4:5 | no results recorded | static test doc 2 to 4 |
| V1 "one-hour rule" (round 4) | chalkboard animation, 55 s | organic and paid | not stated | cites HBR 2011 | Final Ads doc |
| V2 "two weeks away" | papercraft animation, 49.7 s | | not stated | | Final Ads doc |
| V3 "three questions" | UGC presenter, 39.8 s | | Seedance 2.0 | the strategist became the identity reference | Final Ads doc |
| A1 to A7 (round 3) | claymation talking calendar, 3D villain, crochet, flat 2D, glossy 3D, retro comic, X-ray skeleton (19.6 to 25 s) | | not stated | A7: "likes, not clients" angle | Final Ads doc |
| U1, U2, U3 | UGC talking head, 13.2 to 15 s | | U2: H3 2K, eleven_v4 | U2 failed: frozen office, vanishing phone, skipped cut, pause-capped robotic voice (FL-08, FL-09) | Final Ads doc; ads-machine G1, G8 |
| Round 5 set | 13 H3 clips: 4 UGC presenters, 3 cartoon talkers, Kling transformations | | H3 2K, Kling 3.0, GPT Image 2 | H3 looked more real than FLUX 3 at 2K for about a third of the price; Kling transformations worked first time; GPT Image 2.5 gave plastic skin; lip-sync drift up to 1.1 s fixed by re-cuts | ads-machine G1, G7; animation-ads lessons |
| S1 to S4 songs | song ads: 3D, claymation, needle-felt, crochet (71.7 to 77.7 s) | | H3 lip-synced, every second | "songs earn replays and shares; then run the best one as a paid ad" | song docs |
| Reels 01 to 06 (organic, Albanian) | motion graphics | TOF | code; ElevenLabs strategist voice | delivered | `motion-studio/projects/straightscale*` |
| w42-6 quote reel | quote with B-roll, 13.6 s | TOF | GPT Image 2.5, H3 2K keyframe, eleven_v4 voice `8oGKUMljR779HzpZBiE4` | v4 passed after 3 fails | `clients/straightscale/content/2026-w42-6-reel/` |
| w43-1 carousel | self-check carousel, 7 slides | MOF | image model | published 15 Oct, no results logged | `clients/straightscale/content/2026-w43-1-carousel/` |
| w43-3 v1 / v2 | kinetic type / narrated story with H3 | MOF | v2: GPT Image 2, H3 2K, eleven_v4, eleven_music_v2_5 | v1 rejected by Matan; v2 vetoed by the Director | `motion-studio/projects/straightscale-2026-w43-3-reel*/` |
| EN 01 / EN 02 | voiced explainer / kinetic type | MOF / TOF | EN 02: Kokoro voice | EN 01 killed by Matan; EN 02 retired 28 Oct | `motion-studio/projects/straightscale-en-01`, `-02` |
| EN 03 "Maya's quilt" | claymation song, O60 + O30 | TOF | Atlas `suno/chirp-v6` | masters made, waiting on Matan's listen | `motion-studio/projects/straightscale-en-03-song/` |
| EN 04 to EN 06 | narrated POV, claymation shorts | TOF | none generated | hooks below A after 4 rounds; scripts 76, 80, 76 | `motion-studio/projects/straightscale-en-04*`, `-05*`, `-06*` |

**What this says.** The only measured paid results favour a person with a letter or a prop (the founder letter, the
strategist at a whiteboard) over offer-led call-back statics, and talking-head winners over songs on cost per lead
(ORGANIC-OS 7.7). Organic has no results yet (`results-log.md` is empty). Every motion piece so far was delivered,
rejected or killed without a result.

---

## 5. Model gaps: owner decisions

Only Matan names Atlas models (`standards.json` `models.atlas.allowed`). Facts below were read on 28 Oct 2026 with the
free `atlas models get`, `atlas models list` and `atlas generate cost` (no generation, $0 spent). Each item has a
recommendation; nothing changes until Matan decides.

**F1. H3 resolution: 2K vs the Atlas 768P entry.** The hub's G1 says every clip at 2K (decided on the round 5 ads).
Atlas: `minimax/h3-developer/*` offers 480P, 768P, `1440p-sr` and `4k-sr` (no 2K); our entry pins 768P at $0.024/s (30%
of the $0.08/s list). Estimates for a 10 s reference-mode clip: developer 768P $0.24, developer `1440p-sr` $0.45; the
non-developer `minimax/h3/reference-to-video` offers 2K at $1.30 (no discount) and 768P at $0.80.
*Recommendation:* keep 768P for drafts and silent B-roll; add `1440p-sr` on the developer entry for final clips with a
face or a mouth (about 1.9x the 768P price), after one G-HUMAN-TEST of the same 10 s talking clip at 768P, `1440p-sr`
and full H3 2K (about $1.99 for all three). Name full H3 2K only if the test shows `1440p-sr` falls short.

**F2. Lip-sync with an audio reference on Atlas H3.** The `reference-to-video` schema takes `refers`: any mix of image,
video and audio URLs, at least one image or video (audio alone is refused). The gate already reads audio as a reference
kind (`atlas_rules.py`). Not yet shown: that H3-developer moves the mouth to the slice the way Higgsfield H3 did, and
whether the drift check (G6) holds. Every talking format here (2.2 to 2.9, 2.13) depends on it.
*Recommendation:* one 10 s G-HUMAN-TEST clip ($0.24 at 768P) with a known slice, transcript and drift check, before any
talking piece is scheduled. If it fails, talking formats wait; talking objects keep OmniHuman 2.0.

**F3. Music beds.** No Atlas model is named; STANDARDS 1 says no bed until one is. The catalog has
`minimax/music-3.0` (`is_instrumental: true` ignores lyrics; estimate $0.15 a call), `minimax/music-2.6`, and the Suno
family (`suno/chirp-v6` is named for songs with `instrumental: false` locked).
*Recommendation:* name `minimax/music-3.0` with `is_instrumental: true` for beds (2 takes, about $0.30 a piece), or
allow `suno/chirp-v6` with `instrumental: true` as a second entry; first a G-HUMAN-TEST listen of 2 beds.

**F4. Sound effects.** No model in the Atlas audio catalog makes effects: its 18 audio models are TTS, speech-to-text,
lyrics and music (`bytedance/seed-audio-1.0` takes text, speech rate, pitch and loudness: a voice model).
*Recommendation:* nothing to name; keep the repo's synthesised or licensed effects (STANDARDS 1).

**F5. GPT Image 2 at high quality for realistic people.** G7 says realistic people on GPT Image 2 at quality high with
a reference; the Atlas entry pins quality medium. With the same reference image, the `/edit` estimate at 1152x2048 is
$0.149 at medium and $0.276 at high (1.9x).
*Recommendation:* allow `quality: high` on `/edit` only for the asset types of realistic people (`character_sheet`,
`start_frame`, `still` when the Shot Spec is ugc, talking_head, podcast or drama); keep medium for everything else.
About 4 hero stills a piece, so roughly +$0.50 a talking piece.

**F6. Stylized sheets and storyboards.** STANDARDS 1 names Nano Banana 2 for stylized sheets (animation, song, clay,
crochet), but it is not on the Atlas list, so every animated format is limited to GPT Image 2 (which the claymation
skill found flatter for clay). Atlas has `google/nano-banana-2/edit` (2k estimate $0.12; 1k $0.08, 4k $0.16).
*Recommendation:* run re-test R1 (STANDARDS 14) on Atlas, one character sheet and one 3-panel storyboard per style on
both models (about $1.50), then name the winner for `character_sheet`, `prop_sheet`, `set_sheet` and `storyboard` in
stylized formats.

**F7. Start-to-end transformations.** The hub's G2 fallback (Kling 3.0) is not on Atlas's list. Atlas has
`kwaivgi/kling-v3.0-pro/image-to-video` with `end_image` ($0.1428/s at 1080p).
*Recommendation:* keep H3 keyframe mode with start and end frames; name Kling only after an H3 transformation fails
its frame check twice on a real piece.

**F8. Face-on AI people (D1).** Not a model, but it decides two formats: `reel_ugc_talking` and `reel_lived_authority`
are blocked on the StraightScale EN map because STANDARDS 7 shows AI people only from behind, hands only, at a
distance or stylized until D1 (the strategist presenter is the one exception).
*Recommendation:* decide D1 for the EN page: allow face-on AI creators and lived-authority people as clearly staged
characters with the AI label, never as clients or owners, or keep them blocked.

---

## 6. November 2026, re-routed (StraightScale EN)

Run by session F1 on 28 Oct with the new router over `clients/straightscale-en/cards/`; each card's `notes` has the
reason. Before: 7 of 12 `reel_motion`. After: 7 families, 1 motion.

| Slot | Card | Idea | Beat | Format | Family |
|---|---|---|---|---|---|
| Mon 2 Nov | W1-01 | EN 03 song, part one | mechanism | `reel_song` (wildcard) | song |
| Wed 4 Nov | W1-02 (new) | the WORDS Sheet, part two: a buyer's sentence on the board, where it was found, the hook | mechanism | `reel_whiteboard` | presenter |
| Fri 6 Nov | W1-03 | built or patched: the newest patch brags it learned nothing | mechanism | `reel_talking_object` (claymation) | animation |
| Mon 9 Nov | W2-01 | EN 04 two offers side by side | offer | `reel_story_narrated` | story |
| Wed 11 Nov | W2-02 | the order I'd build in | list | `reel_motion` | motion |
| Fri 13 Nov | W2-03 | what will this leave me if I stop paying | offer | `reel_podcast` | podcast |
| Mon 16 Nov | W3-01 | EN 05 the boosted post explains | mechanism | `reel_animation_short` (claymation) | animation |
| Wed 18 Nov | W3-02 | three questions an offer answers | list | `reel_whiteboard` | presenter |
| Fri 20 Nov | W3-03 | the week the third client signs | mechanism | `reel_ugc_pov` (hands only) | ugc |
| Mon 23 Nov | W4-01 | EN 06 the page that changed the subject | mechanism | `reel_animation_short` (claymation) | animation |
| Wed 25 Nov | W4-02 | tried everything | offer | `reel_podcast` | podcast |
| Mon 30 Nov | W5-01 | a post vs an ad | mechanism | `reel_whiteboard` | presenter |

EN 02 (`SSEN-2026-10-W5-02`, kinetic type) is in `cards/retired/`. The month's budgets add up to $44.40 against the
$100 cap. The talking formats here (whiteboard, podcast) wait on F2's lip-sync test; the strategist's face-on presenter
is allowed by STANDARDS 7; the podcast hosts and the POV owner are shown from behind until D1.

---

## Changelog
- 2026-10-28 v1.0 (session F1): first version. New formats `reel_ugc_talking`, `reel_whiteboard`,
  `reel_lived_authority`, `reel_skit`, `reel_talking_object`; new styles `skeleton_xray`, `anime_2d`; every format
  carries `format_family`, `funnel` and `l19`; `beats` in `organic.json`; the router ranks by L19 fit, funnel and
  variety, and cost only filters; `week-check` enforces the variety rules; Post Cards name `load_bearing_beat`.
