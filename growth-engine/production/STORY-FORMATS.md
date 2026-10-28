# Story formats for organic posts (v1.1, 16 Oct 2026)

The playbook for organic **story** posts (AI animation, the POV day in the buyer's life, drama, songs, podcast clips,
talking heads, UGC): the ideal customer's day and known pains, then the mechanism revealed, made to be sent and followed.
It answers the owner's question "how can we combine it in a smart and right way for the postings?"

**Precedence.** Numbers (models, lengths, words, loudness, safe zones, pass rules) come from `STANDARDS.md` and
`standards.json`; they win over every skill file and over this file. Method comes from the skills and the adapters in
`growth-engine/adapters/`. Facts come only from `clients/<slug>/brain.json` and `brand-kit.md`. Where a skill and
STANDARDS.md disagree, this file follows STANDARDS.md and says so (table in section 6.3).

**Sources.** Kallaway (`audit/research_kallaway.json`, 14 transcripts, cited by video id); the skill digests in `audit/`
(`story_structures`, `organic_adaptation`); `config/organic.json`; ORGANIC-OS 6 and 7. **(inference)** marks our own
rules: his transcripts give no cut rate and no POV template.

---

## 1. What a story post is here

A story post is three choices on one Post Card:

| Field on the card | What it decides | Where the ids live |
|---|---|---|
| `story_template` | the narrative: whose day, which pains, where the mechanism lands | `config/organic.json` `story_templates` |
| `format` | the production: who or what is on screen, which skill, which tier and credit range | `config/organic.json` `formats` (`production` = the pipeline family) |
| `animation_style` | the locked look, animated formats only | `config/organic.json` `animation_styles` |

Plus `series` and `series_character` (a CH- id from the series' LIB run) when the piece is an episode, `length_target_s`
(the tier), and `angle_proven` or `wildcard` for tier A.

| Format | Tier | Credits | Jobs | Story templates it renders | Adapter (plus hook-lab-organic and script-lab-organic, always) |
|---|---|---|---|---|---|
| `reel_story_narrated` | B | 210-445 | reach, trust, convert | pov_day, two_days, hidden_villain, overheard | this file, section 6.4 (POV camera, silent keyframe clips under the narrator) |
| `reel_animation` | A | 150-220 | reach, trust | pov_day, hidden_villain, two_days, object_speaks | `animation-organic.md` |
| `reel_animation_short` | B | 70-100 | reach, trust | hidden_villain, object_speaks, pov_day | `animation-organic.md` (short tier) |
| `reel_drama_pov` | A | 180-495 | reach, trust | pov_day, two_days, overheard | `drama-organic.md` |
| `reel_song` | A | 140-355 | reach, trust | song_day, pov_day | `song-organic.md` |
| `reel_podcast` | B | 220-320 | trust, convert | podcast_disagreement | `podcast-organic.md` |
| `reel_ugc_pov` | B | 80-200 | reach, trust | pov_day, two_days | `ugc-talking-head-organic.md` |
| `reel_strategist_prop` | B | 80-200 | trust, convert, reach | none listed | `ugc-talking-head-organic.md` (the strategist as a presenter in his staged studio set) |
| `reel_talking_head_real` | C | 0-10 | trust, convert, reach | none listed; needs real footage | `ugc-talking-head-organic.md` |

**Credits** are organic.json's ranges, which `route` and `card-check` read. They come from each adapter's computation
at STANDARDS 10 prices (section 4 of each adapter; `reel_story_narrated` from section 6.4 here) and include about 25%
retakes; the cast sheets of a new series are extra, once.

All of them are the `ai_video` family (every pipeline step) except `reel_song` (`song`: every step, and step 4 adds
G-HUMAN-SONG) and `reel_talking_head_real` (`real`: no look bible, storyboard, credits or generation). Run the skill
with its adapter, this file, STANDARDS.md and the hook and script adapters, and apply the overrides in section 6.3.

**What `organic.py` does with a story card** (read from the code, 15 Oct 2026):
- `card-check`: a `story_template` that is not in organic.json, or that the format doesn't render, is an ERROR; a belief
  outside the template's beliefs is a WARN. `confession_pov` needs real footage (STANDARDS 7; organic.json
  `needs_real_footage`) and no AI-person format renders it, so a card that puts it on one fails (section 3.6). A tier A
  or B story format without a template is a WARN (podcast exempt). `reel_animation` and `reel_animation_short` without
  an `animation_style` (or with an unknown one) are an ERROR; a style on a non-animated format is ignored with a WARN.
  Tier A without `angle_proven` or `wildcard` is an ERROR. `reel_talking_head_real` is an ERROR while the brain has
  `real_footage: false`. The CTA must be one of the card's job CTAs (organic.json `jobs`); a keyword CTA needs a live
  keyword (StraightScale: only ANALIZA). A `series` that is not on the content map is an ERROR, so a new series is added
  to `content-map.json` first.
- `route`: keeps only formats that render the card's template (+2), gives a tier B story without a proven angle +1 ("story
  lab: test at tier B first"), drops tier A without `angle_proven` or `wildcard`, drops formats whose top credits exceed
  what is left of the month's cap, and drops yesterday's family.
- `week-check`: a 5+ post week with no card carrying a `story_template` is a WARN; more than one tier A is a WARN.
- `reel_strategist_prop` and `reel_talking_head_real` carry story structure through Script Lab's ST code only: a
  `story_template` on them fails `card-check`, so they don't count as the week's story reel. (Open for the owner: add
  `confession_pov` to `reel_talking_head_real`, its only renderer, once the owner films.)

---

## 2. The storytelling engine

Kallaway's frameworks, each tied to where it runs in our 16 steps: **step 2** Hook Lab (`hook-lab-organic.md`),
**step 3** Script Lab (`script-lab-organic.md`, ST codes), **step 6** the visual-planner's shot plan.

| Framework (source) | The rule | Where it runs | Meets |
|---|---|---|---|
| **The dance: but / therefore** (t5Z-Q1bg1tU; oRYfJ_yxz6M) | Alternate context and conflict; join beats with BUT or THEREFORE, never AND THEN. His benchmark short has 4 "but" loops in its first 30 s. | Step 3: every beat join in the line table is "por", "kështu që" or "prandaj", never "dhe pastaj". Step 6: each BUT or THEREFORE is a picture change. | Every ST; Hook Lab gate 5 (seam into line 2) |
| **Addiction loop: stakes, big question, head fake, rehook** (KyC8r-zitVE) | Before the story: who it happens to, what is at risk, why now. Give just enough to predict. Break the prediction in a way that is surprising but logical, with clues planted. Open the next loop as one closes. | Step 2: the big question is the hook's open question still live at 10 s (gate 6). Step 3: stakes by 5 s; the head fake breaks a false belief from the brain (AV-01 `false_beliefs`). Step 6: each rehook lands on a cut with a new picture; section ends are danger zones. | HL-T5 fear moment, HL-T13 misdirection; ST3, ST6 |
| **Dopamine ladder** (jtmstMt4WLc) | 1 stimulation (0 to 2 s: colour, motion, brightness in your own look), 2 captivation, 3 anticipation, 4 validation with a non-obvious answer, 5 affection, 6 revelation. Faceless content struggles at 5 and 6. | Step 2/6: motion in the first second and a change every 1 to 1.5 s in the first 5 s (STANDARDS 5), in the client's own world (StraightScale: Tirana after dark, the red-case phone). Levels 5 and 6 are a series job: recurring cast plus real human posts (D1). | HL-STACK visual channel; ST3 rung 4 |
| **Modern story arc** (wgXGimZvDa4) | Start at about 70/100 intensity, spike to about 90 with early conflict, release to about 30, peak again at about 75; after each release the viewer must "rebuy" with new stakes. Hook order: what and why, then who and how, then when and where. | Step 3: the beat sheets in section 3 carry these targets. In 45 to 75 s the peaks come every 15 to 25 s **(inference, from the research file)**. A clock time is colour after the what/why line, never the opener. | ST4 without the slow setup; drama BS11 |
| **Contrast A vs B** (2byPP_9F0-Q; pcnrzBwoVUk; p4W23V_LLvE) | A = what the viewer believes, B = the alternative that solves it better. Topic in line 1, contrast in lines 2 and 3. | Step 2: the card's `belief` names the A to B move; A from AV-01 `false_beliefs` or `tried`, B from the contrarian vault (C1 to C5). | HL-T4 hidden cause, HL-T12 two futures; ST5, ST6, ST9 |
| **Six story locks** (pcnrzBwoVUk) | Term branding, embedded truths (cut if/maybe/might), thought narration, negative frames, loop openers every 20 to 30 s in shorts, contrast words. Not all six in every short. | Step 3 polish pass. Term brand = "Patchwork Marketing". Thought narration = the owner's own excuse. Contrast words: "por", "në fakt", "në vend të", "rezulton se", "megjithatë". Embedded truths apply to the problem only, never to outcomes (no guarantees). | HL-T9 workaround reveal, HL-T3 stop doing X; ST9 |
| **Value = contrast x relevance** (p4W23V_LLvE; 7I50PECz7SU) | Make reality beat the expectation, aimed at the buyer's bullseye. Say the topic and the first contrast in 3 to 5 s. Cut lines, not frames. Keep one format fingerprint. | Step 1: the idea gate's shock score. Step 3: green, yellow, red line cut. Step 6: same set, same recurring object, same caption style every episode. | Idea gate 7.2 |
| **Hero vs villain, something to root for, atomic shareability** (wgXGimZvDa4) | Give the viewer a villain (a person, the status quo, a rival approach) and a hero to root for; shrink the message to one retellable line; say hard points twice (once plainly, once as a picture). | Step 1: the villain is the mistake or Patchwork Marketing, never the owner. Step 3: the last dab is a C1 to C5 line. Step 6: THE PICTURE is the "say it twice" moment. | HL-T1, HL-T2; `hidden_villain`; drama T8 |
| **Direction: write the last line first** (t5Z-Q1bg1tU) | Write the last line ("last dab") first, so memorable it is shared alone; then line 1; then the middle. In short form the last line sets up the first on replay. | Step 3: the line table starts with the last dab. Step 6: the last shot matches frame 1 so the loop is seamless. Matches the organic adapter's "payoff in the last 3 to 5 s, loop back to the hook". | Script Lab test 12 |
| **Buyer triangle and 6-step playbook** (oRYfJ_yxz6M; 94ezZMYPzls) | Map the buyer's workflow, pick one high-pain step and its baseline solve, bring a novel solve; every video carries pain, solution and trust. Substance one level above the buyer's knowledge. | Steps 0 and 1: the pain is one moment in AV-01's day, the baseline solve comes from `tried` (more ads, boosting, a freelancer or an agency), the novel solve is one step of the Only Choice System. | ST2, ST3 |

**Timing for a 60 s story.** Kallaway's own numbers: topic in 1 to 2 s (3 to 5 s in p4W23V_LLvE), stimulation in the
first 1 to 2 s, a rehook every 20 to 30 s. STANDARDS 5 adds the picture cadence per format and for the first 5 s.
**(inference)** A micro-turn (one BUT or THEREFORE) every 5 to 8 s; conflict spike by about 5 s,
head fake and rehook 1 at about 20 to 28 s, the reveal at about 32 to 45 s, the last dab at about 55 s.

**Hook rules that matter most for stories.** Topic clarity and on-target curiosity in 1 to 3 s (2byPP_9F0-Q); show while
you tell, visual hooks first (t5Z-Q1bg1tU); "you/your", never "I/people"; no vague teaser. **(inference, research file)**
A "POV:" label with "ti" meets the relevance rule. The text hook follows STANDARDS 6 (drama: X7 in STANDARDS 7b); Hook
Lab gate 7 keeps the brand, the mechanism name and any offer out of the first 3 s.

---

## 3. The story templates

**Rules every template follows.**
- **The buyer is the hero:** competent and busy, never lazy or foolish. Blame the mistake, never the viewer (OS 6.1).
- **Pains only from the brain** (AV-01: `words`, `keeps_up`, `tried`, `false_beliefs`, `fears`). The avatar's Albanian
  words are "written in Albanian by us"; confirm with real buyer words (demand map gap).
- **Numbers:** where a template wants a number, use only a number from the brain's proof bank with `permission: yes`,
  else none. StraightScale has none (IP-01 is internal only), so no counts, prices, amounts or results. Screens show
  states (a silent phone, an unread dot, "Seen", a pile of unanswered messages), never counts, and never a real
  platform's logo or name: "the inbox", "the phone" (STANDARDS 6; the style bible bans invented UI with fake numbers).
- **Anecdotes** in the brand's voice only as a clearly framed POV dramatization ("POV: ..."), never stated as something
  that happened (STANDARDS 7).
- **The mechanism:** the cause (Patchwork Marketing) is named after the open question is set; the method (the Only
  Choice System: Find, Own, Attract, Convert, Close) is given away; the agency is named lightly or not at all.
- **The payoff shows a process, not a result:** the same message, this time answered with one question and a next
  step. Never a speed promise ("we answer within 1 hour"), never "we chase the client's leads", never a guarantee.
- **AI people and the AI label** follow STANDARDS 7 (D1 decides whether to extend it). AI people are never real clients
  and never carry a result. Until D1: the StraightScale strategist may face the camera only as a presenter in his
  clearly staged studio set (the whiteboard), AI label on, never as a client, owner or customer. AI business owners (POV,
  UGC, the split screen of `two_days`), podcast hosts and drama characters who could pass as real owners are shown from
  behind, as hands only (a POV camera), at a distance, or as stylized animation.
- **One organic CTA** that fits the job (ORGANIC-OS 6.2; STANDARDS 5 end card): follow, save, send, comment (an answer
  to a question), keyword (only a keyword live in brain.json; StraightScale: ANALIZA), dm, or book. "Book" only on a
  convert post, said as the keyword or DM path ("comment ANALIZA; the booking button comes in the DM"). Never a link,
  price, discount, guarantee or urgency. Albanian, "ti", numbers as words, no em dashes, a native read before posting.

### 3.1 `pov_day`: POV, a day in the buyer's life
**Purpose:** the core story post; the viewer lives their own day and meets the hidden cause. **Beliefs** B1, B2, B3.
**Jobs** reach, trust. **Script Lab** ST3, ST4 (with M4.18-1 failed-solution journey and M4.18-2 discovery). **Hook Lab**
HL-T9 workaround reveal, HL-T5 fear moment.

| s (O60) | Beat | Kallaway mechanic |
|---|---|---|
| 0-3 | Cold open on the pain moment, in the buyer's words | Stimulation + topic + A vs B; intensity about 70 (jtmstMt4WLc, 2byPP_9F0-Q) |
| 3-15 | The day so far: 2 or 3 accommodations, one picture each | Stakes by 5 s; BUT/THEREFORE joins; spike to about 90 (KyC8r-zitVE, t5Z-Q1bg1tU) |
| 15-25 | The failed fix and why it failed | Thought narration of the baseline belief, then the head fake (pcnrzBwoVUk, KyC8r-zitVE) |
| 25-32 | The breaking point | Rehook 1 with a contrast word; rebuy: new stakes (pcnrzBwoVUk, wgXGimZvDa4) |
| 32-45 | Revelation: the hidden cause as THE PICTURE, then the UMS in one line | Term branding; validation; said twice, plainly then as a picture; release to about 30, rise to 75 (jtmstMt4WLc, wgXGimZvDa4) |
| 45-55 | The same moment, lived differently | Show while you tell; rehook 2 (t5Z-Q1bg1tU) |
| 55-60 | Last dab, then one organic CTA | Last line written first, loops to frame 1; native-embed CTA (t5Z-Q1bg1tU, 7I50PECz7SU) |

**O30 cut** (`reel_animation_short`; a compact hidden cause ST3, since no full discovery story runs under 45 s): 0-3 cold
open · 3-10 one accommodation + BUT · 10-16 failed fix + thought narration · 16-26 THE PICTURE + UMS line · 26-30 last
dab + CTA. **Formats:** `reel_story_narrated` (POV camera, no face), `reel_animation` and `_short`, `reel_ugc_pov`,
`reel_drama_pov`, `reel_song`. **Number slot** (a count of unanswered messages, a lost job's value): only a number from
the brain's proof bank, else none. **StraightScale** (a "POV:" dramatization, never a real owner): a kitchen and
furniture showroom owner in Tirana; enquiries arrive while he is on the floor ("mesazhet mbeten pa përgjigje kur jam në punë"); he adds ads; he tells
himself they only asked for the price; at night "klientët nuk kthehen". Reveal: the ad, the page and the inbox drawn as
separate pieces with gaps, the enquiry falling through, named Patchwork Marketing. Last dab (C3): "Reklamat e tua nuk po
dështojnë. Kërkesat po vdesin pas klikimit." (Your ads aren't failing. Your enquiries are dying after the click.)

### 3.2 `two_days`: same morning, two owners
**Purpose:** contrast in the picture itself; makes the viewer pick a side. **Beliefs** B2, B3, B5. **Jobs** reach,
trust. **Script Lab** ST5. **Hook Lab** HL-T12 two futures.

| s (O60) | Beat | Kallaway mechanic |
|---|---|---|
| 0-3 | Split screen: two owners, the same moment (the same message arrives on both phones) | Contrast A vs B as a picture; stimulation |
| 3-20 | Their days diverge on one decision | The dance, cutting left and right on each BUT; stakes |
| 20-28 | The owner you would bet on (more ads, nicer posts) is not the one ahead | Head fake + rehook 1 (KyC8r-zitVE) |
| 28-42 | The one difference named: the mechanism | Term branding; validation |
| 42-55 | Where each is at night | Rebuy and peak; picture contrast (wgXGimZvDa4) |
| 55-60 | Last dab + CTA | Loops to the split frame |

**O30 cut:** none (the divergence needs the time); test the angle as a carousel (cover = two futures, slide 2 pays it).
**Formats:** `reel_story_narrated`, `reel_animation`, `reel_ugc_pov`, `reel_drama_pov`. **Truth:** neither owner is a
client; the difference is process; night is a state, never a number outside the proof bank. Until D1, photoreal owners
are seen from behind, by their hands or at a distance (STANDARDS 7); faces only in stylized animation.
**StraightScale:** two private-school owners get the same enquiry. One says "më thirr më vonë" (call me later) and
boosts a post; the other's pieces are joined, so the enquiry gets an answer, one question and a next step. Last dab
(C1): "Nuk të duhet më shumë marketing. Të duhet marketing që punon bashkë."

### 3.3 `hidden_villain`: the problem is a character
**Purpose:** comic reach and sends; the most natural recurring animated character. **Beliefs** B1, B2. **Job** reach. **Script
Lab** ST3 through device DEV-F2 (villain mocking the fixes). **Hook Lab** HL-T2 villain mockery, HL-T1 character in place.

| s (O60) | Beat | Kallaway mechanic |
|---|---|---|
| 0-3 | The villain speaks from where it lives (on the desk, in the inbox) | Character in place; topic in line 1; no name yet (gate 7) |
| 3-15 | It mocks failed fix 1 and 2 | Dance; mock the fix, never the owner (wgXGimZvDa4) |
| 15-28 | It brags about what it costs the owner (his fears) | Stakes; negative frame (pcnrzBwoVUk) |
| 28-35 | "You know what I'm scared of?" | Rehook 1; head fake (animation F2) |
| 35-50 | It gives its name; the mechanism arrives and the villain loses | Term branding; validation; show the fix working |
| 50-60 | Last dab + CTA | Loop to frame 1 |

**O30 cut:** 0-3 villain line · 3-10 two fixes mocked · 10-16 the cost · 16-26 name + the mechanism arrives · 26-30 last
dab + CTA. **Formats:** `reel_animation_short` (lab), `reel_animation`, `reel_story_narrated`. **Truth:** comic, never
shaming the owner; no real business, product or competitor as the villain. **StraightScale:** pilot 1 (section 7).

### 3.4 `object_speaks`: an object in the business tells its story
**Purpose:** a cheap, gentle hidden cause told by a prop the buyer owns. **Beliefs** B1, B3. **Jobs** reach, trust.
**Script Lab** ST3 through DEV-F1 (talking part). **Hook Lab** HL-T1.

| s (O30, its natural tier) | Beat | Kallaway mechanic |
|---|---|---|
| 0-3 | The object introduces itself | Stimulation; character in place |
| 3-15 | What it sees every day (the pains) | Thought narration in the object's mouth; BUT joins |
| 15-25 | The day it saw the change (the mechanism) | Head fake, then validation |
| 25-30 | CTA | Last dab loops to the object |

**O60:** add the failed fixes (15-30 s) and a rehook at about 25 s before the change. **Formats:** `reel_animation_short`,
`reel_animation`. **StraightScale:** the red-case phone (the brain's recurring object): "Unë jam telefoni yt. Mesazhet
vijnë gjithë ditën. Askush nuk më hap deri në mbrëmje." (I'm your phone. Messages come all day. Nobody opens me until
evening.) The change: the pieces get joined and every message gets its next step. CTA: save.

### 3.5 `overheard`: witness or overheard line
**Purpose:** peer insight from outside the owner's head; drives comments. **Beliefs** B2, B3. **Jobs** reach, trust.
**Script Lab** ST4 with M4.18-3 (transformation with a witness). **Hook Lab** HL-T10.

| s (O60) | Beat | Kallaway mechanic |
|---|---|---|
| 0-3 | Someone else noticed: the overheard line | Big question (KyC8r-zitVE) |
| 3-12 | The surprising detail | Captivation |
| 12-25 | What you would assume | Thought narration, then head fake; rehook 1 by 25 s |
| 25-40 | The cause | Term branding; THE PICTURE |
| 40-55 | The lesson as the mechanism | Validation; rehook 2 |
| 55-60 | CTA | Last dab |

**Formats:** `reel_story_narrated`, `reel_drama_pov`. **Truth:** the witness and the speakers are staged, never a real
business by name, and the scene is framed as a POV dramatization ("POV: ..."), never told as something that happened.
Until D1 the people at the table are seen from behind or at a distance (STANDARDS 7). **StraightScale:** "POV: at a
café in Tirana you hear an owner at the next table say he pays for ads, a page and someone for posts, and 'telefoni nuk
bie'." The detail: every piece he pays for is there, and none of them connects to the next. The cause: nobody owns the connection. Lesson (C2): "Agjencitë të shesin pjesë. Ne ndërtojmë gjithë sistemin, duke filluar nga blerësit e tu."
(Agencies sell you pieces. We build the whole system, starting with your buyers.)

### 3.6 `confession_pov`: owner confession
**Purpose:** trust through an honest admission. **Beliefs** B3, B7. **Job** trust. **Script Lab** ST4, M4.18-4. **Hook
Lab** HL-T8 (first person + a number + an edge): only a number from the brain's proof bank, else none.

| s (O60) | Beat | Kallaway mechanic |
|---|---|---|
| 0-3 | First person, an edge: what I got wrong | Negative frame; topic |
| 3-20 | What it cost | Stakes; dance |
| 20-40 | What I saw that changed it (the mechanism) | Head fake; rehook 1; term branding |
| 40-55 | What I do now | Validation; affection (jtmstMt4WLc) |
| 55-60 | CTA | Last dab |

**Formats:** real footage only (STANDARDS 7: a confession POV needs real footage). An AI owner saying in the first
person that the method changed his business is an implied testimonial, so `reel_ugc_pov` and `reel_drama_pov` no
longer render it, and drama's T10 quiet monologue no longer maps to it. The one renderer is the real owner
(`reel_talking_head_real`), which organic.json doesn't list for it yet. **Truth:** a confession is someone's real story,
in his own words, with no result he can't show. **StraightScale:** waits for real footage (`real_footage: false`) and
D7 (the owner ramble); write it only from his real words.

### 3.7 `song_day`: song of the buyer's day
**Purpose:** reach and memory (sends, rewatches); judge on sends and follows, not DMs. **Beliefs** B1, B2, B7. **Job**
reach. **Script Lab** ST3; song 4c-NP (named person, three tiny scenes) or 4c-PR (problem rap).

| s (O60) | Beat | Mechanic |
|---|---|---|
| 0-3 | First sung line by 1 s, the problem sung by 3 s | Stimulation; topic |
| 3-20 | Verse: the day's pains, three tiny scenes | Dance; stakes |
| 20-30 | Chorus: THE PICTURE | Term branding; atomic line (wgXGimZvDa4) |
| 30-40 | Verse 2: failed fixes, each with its reason | Head fake; rehook |
| 40-48 | The turn, spoken: the mechanism | Validation |
| 48-56 | Chorus again (THE PICTURE at least twice) | Rebuy |
| 56-60 | Outro: spoken CTA | Last dab |

**O30 cut:** hook plus one chorus (song 4c-PR shape). **Format:** `reel_song`. **STANDARDS:** speech first, then lyrics,
then the lyric gate; low end of the tier; picture change 1.5 to 3.5 s; ElevenLabs Music; the owner hears every song
master before any picture (G-HUMAN-SONG). **Number slot** (a climbing counter, a count payoff): only a number from the
brain's proof bank, else none. **StraightScale chorus draft:** "Reklama këtu, faqja atje, mesazhet askund" (Ads here,
the page there, the messages nowhere). Turn (C1), spoken. Waits for a proven angle (tier A).

### 3.8 `podcast_disagreement`: two hosts disagree
**Purpose:** trust through a real argument; the viewer takes a side in the comments. **Beliefs** B3, B4, B5, B8 (B8: no
"what happens in the analysis" lines until D3). **Jobs** trust, convert. **Script Lab** ST2, with the 18c two-host
conversation and podcast beat template PC-2H. **Length:** C45 (STANDARDS 8).

| s (C45) | Beat | Mechanic |
|---|---|---|
| 0-4 | A real disagreement in line 1 (turns 1-2) | Contrast A vs B; cold open |
| 4-14 | Host A's case: the common belief (turns 3-4) | Thought narration |
| 14-26 | Host B's case: the hidden cause in one picture line (turns 5-6) | Head fake; term branding |
| 26-36 | The moment A gets it (turns 7-8) | Validation; payoff in 6 words or fewer |
| 36-42 | Organic CTA (turns 9-10) | Native embed |

**Format:** `reel_podcast` (a master two-shot, start frames only from it, one speaker per clip, a reaction shot every
10 s). **Truth:** "needs a real disagreement" (organic.json); the hosts are presenters of a staged conversation,
labelled, and never presented as real owners or clients: a host argues the owner's common belief in the third person
or to "ti", never as "I, the owner". Until D1 the hosts are shown only from behind, at a distance or as stylized
animation (STANDARDS 7), so a podcast card runs steps 0 to 3 only (`podcast-organic.md` 3). **StraightScale:** pilot 3
(section 7).

---

## 4. Animation styles

| Style id | When it fits a B2B audience | Templates it suits | Watch out |
|---|---|---|---|
| `claymation` | Tactile and comic without looking childish; handmade texture reads as care; no uncanny faces | hidden_villain, object_speaks, pov_day | Stop-motion texture costs nothing extra in H3; never use the claymation skill's video routing |
| `crochet` | Only when the material is the metaphor: Patchwork Marketing is literally squares stitched together, and the fix is one thread | hidden_villain, object_speaks | Can read as soft or childish for owners aged 35 to 60; keep the lines sharp and the pains real |
| `family_film_3d` | When a character must carry feeling across a day: the owner's face at night | pov_day, two_days | Most exposed to the generic AI look (desensitisation, jtmstMt4WLc) and to studio imitation |
| `storybook_2d` | Calm, fable-like explaining (fits the "calm, direct" voice); good for drawing THE PICTURE | object_speaks, song_day | Slower cadence; keep the STANDARDS 5 picture change |

**Locked style blocks** (organic.json, word for word in every sheet, storyboard and clip prompt):
```
claymation:      Handmade claymation stop-motion look: plasticine characters with visible thumbprints and slight tool marks, soft rounded forms, miniature handmade set pieces, warm practical lighting, shallow depth of field like a tabletop set, gentle stop-motion texture.
crochet:         Crochet amigurumi look: characters and props knitted from soft yarn with visible stitches, safety-bead eyes, felt details, a cosy miniature yarn world, soft daylight, shallow depth of field.
family_film_3d:  Polished 3D family-film animation look: expressive stylised characters with large eyes and soft subsurface skin, rounded shapes, warm cinematic lighting with soft bounce, rich but controlled colour, gentle depth of field.
storybook_2d:    Classic hand-drawn 2D animation look: clean ink lines, painted watercolour backgrounds, expressive squash-and-stretch poses, warm storybook palette, soft vignette.
```
- **Image model (STANDARDS 1, re-test R1):** Nano Banana 2 at 2k for stylized sheets and storyboards until R1 (one sheet
  and one 3-panel storyboard per style used, Nano Banana 2 vs GPT Image 2.5, about 10 credits, G-HUMAN-TEST) is run
  before the first animated series; until then GPT Image 2.5 makes stylized sheets only inside the R1 test. Video:
  MiniMax H3 only (STANDARDS 1 and 2); Kling 3.0 only with G-FALLBACK; Seedance and every other video model are banned
  for organic (a one-off needs G-EXCEPTION).
- **Trademark rule (V24):** the ids `family_film_3d` and `storybook_2d` are config keys (renamed on 16 Oct 2026). An older
  card with the earlier studio-named ids fails card-check: rename them to `family_film_3d` / `storybook_2d`. Prompts say "3D family-film animation"
  and "hand-drawn 2D storybook animation"; never a studio's name, characters, logos or look-alikes.
- **The recurring cast is built once per series** on a LIB run, `clients/<slug>/runs/<CODE>-LIB-<SERIES>/` (StraightScale:
  `SS-LIB-PATCHWORK`): a hero or mascot, 2 or 3 recurring characters, 1 or 2 sets, and a prop sheet for every story prop
  (the red-case phone as `PR-PHONE-CHAT`). `pipeline.py budget` (G-BUDGET) runs before the first sheet (STANDARDS 10). 4
  to 7 sheets, each with a G-PROMPT-IMG PASS before its call and G-VIS-SHEET with hero rules (zero defects) after,
  approved once (G-HUMAN-LOOK). Episodes name the character in `series_character` and reference the sheets: the first
  episode of a new cast adds about 15 credits for the sheets (`animation-organic.md` 4), later episodes don't. One
  series, one style: a new style is a new series and a new LIB run.

---

## 5. How story formats fit the posting system

### 5.1 The weekly rhythm
7 posts a week: 3 reels, 3 carousels, 1 image. `week_rules`: 1 image at most, no family or job two days in a row, 1+
contrarian and 1+ B7 post, a conversion CTA at least every 5 posts, 1 tier A at most, 1 story reel at least.

| Day | Post | Job · belief | Story role |
|---|---|---|---|
| Mon | **Story reel** (pov_day, hidden_villain or two_days) | reach · B1 or B2 (two_days: B2) | Opens the week's question; CTA send or follow |
| Tue | Carousel "One Step": the method step the reel revealed | trust · B4 | Pays the mechanism as a saveable how-to |
| Wed | Reel (C1 to C5): contrarian quote reel (B1), motion reel (B2), or the strategist prop at his whiteboard (B1 or B2) | reach · B1 or B2 | Second angle on the same cause; CTA send |
| Thu | Carousel: owner self-check | trust · B3 | Comment ANALIZA |
| Fri | Reel: motion reel, or podcast_disagreement once D1 allows host faces | convert · B5 | Comment ANALIZA |
| Sat | Image: owner question | reach · B7 | Comment: an answer to the question |
| Sun | Carousel: a retelling of the week's tier A piece (section 5.5), or a One Step episode | trust · B3 or B4 | Follow for the series |

Each slot's format carries that belief in organic.json, so `route` offers it and `card-check` gives no format WARN
(`reel_motion`: B2 to B5; `reel_quote_broll`: B1, B7; `reel_strategist_prop`: B1, B2, B4, B6, B8; `two_days`: B2, B3, B5).

### 5.2 Which job each story format serves, and the chain
**Reach** (sends, follows): animated `hidden_villain` and `pov_day`, `reel_story_narrated`, `song_day`, drama; CTA send
or follow. **Trust** (saves, keyword comments): `object_speaks`, `overheard`, `confession_pov` (real footage only),
podcast; CTA save or ANALIZA. **Convert** (qualified DMs): `podcast_disagreement` on B5 or B8 (no "what happens in the
analysis" B8 post until D3); CTA ANALIZA, DM, or book said as the keyword path (section 3 rules). A hard offer post
(about 3% of output, at most 1 a month on a new account, ORGANIC-OS 6.2) is a convert post about the one free offer,
with the same limits.

The chain: the story reel names the cause; the next carousel teaches the step that fixes it; the keyword posts send
people to the hub funnel `analiza`. The keyword DM must continue the reel's promise in the same words (Script Lab organic
scorecard, "DM-funnel match"). Only ANALIZA is live; PATCHWORK and HARTA may not be used until their flows exist.

### 5.3 Lab, then factory
- **Lab:** a new story angle is tested cheaply first: as a carousel (`carousel_mistakes`, `carousel_teardown`), a quote
  reel (`reel_quote_broll`, about 25 to 40 credits) or an animation short (`reel_animation_short`, 70 to 100). `route`
  scores tier B stories up for this.
- **Promote by the job metric:** an angle that beats the account median on its card's job metric gets `angle_proven:
  true` and may go to a tier A piece (OS 7.7 rule 1). A 3x+ median post with good sends or saves moves its format into
  the factory: variations on the same structure until it stops working (OS 9.5).
- **One wildcard a month:** one untested tier A piece (`wildcard: true`), never more.
- **Kill rule:** a premium format under the median on its job metric 3 times in a row pauses for 60 days (OS 7.7 rule 7).

### 5.4 Series and recurring characters
A series is one template, format, style and cast that repeat (10 episodes before judging, OS 6.4). Binge viewing of
one account drives follows ("content minutes", OS 6.4 citing Kallaway); the LIB run, the locked voice and the same set
make each episode cheaper; the same set, object and captions are the format fingerprint (p4W23V_LLvE). AI series stall
at affection (jtmstMt4WLc), so each week also needs real human proof once D1 is decided.

### 5.5 The 6 derived assets of a tier A piece
(OS 7.7 rule 2): **1** main cut (O60); **2** short cut (O30, about 35 credits, reusing shots) as a later story reel or
a trial re-test after 14 to 30 days; **3** three hook variants as trial reels (not among the 7 posts); **4** a carousel
that retells the piece (one of the week's 3): a normal carousel run per `carousel-machine-organic.md` (4:5 slides in the
account's carousel style, slide text from the slide prompt, G-VIS-SLIDE and G-SET). The storyboard panels are never
posted as slides: they are 9:16 panels on a board canvas with no text (STANDARDS 3); **5** 2 or 3 frames for the daily
Stories; **6** an ad version.

### 5.6 A worked month for StraightScale (cap 1,300 Higgsfield credits)
Ranges are organic.json per-piece credits (they include about 25% retakes); the narrated POV is priced at 60 s from
section 6.4 and the strategist at O30 (`ugc-talking-head-organic.md` 4). Reel 2 is Wednesday's slot and Reel 3
Friday's (section 5.1). ElevenLabs credits are outside the cap.

**Carousels and images.** STANDARDS 10 prices a 7 to 12 slide carousel at about 16 to 33 credits (3 concept frames,
cover rounds of 4, slides at 2k medium, +25%), so 12 a month would be 192 to 396. The plan holds each carousel to its
floor: about 13 (7 slides: 3 concept frames, one cover round of 4, then slides 2 to 7 once at medium), 3 a week = 39.
The brand kit allows carousels up to 30 Higgsfield credits a week, so even the floor is over that line: an open owner
question (raise the line, or fewer carousels a week). A second cover round or a slide retake also needs the owner's yes
until the owner raises that line. Single images: 1 credit at medium, 2.75 at high.

| Week | Story reel | Reel 2 (Wed) | Reel 3 (Fri) | Reels, low to high |
|---|---|---|---|---|
| W1 | `reel_animation_short`, hidden_villain ep 1 (pilot 1), lab: 70-100 | `reel_quote_broll`: 25-40 | `reel_motion`: 0-30 | 95-170 |
| W2 | `reel_story_narrated`, pov_day (pilot 2, 60 s), lab: 280-445 | `reel_quote_broll`: 25-40 | `reel_motion`: 0-30 | 305-515 |
| W3 | `reel_animation`, the winning angle or the wildcard, W1 cast reused: 150-220 | `reel_quote_broll`: 25-40 | `reel_motion`: 0-30 | 175-290 |
| W4 | `reel_animation_short`, hidden_villain ep 2, cast reused: 70-100 | `reel_strategist_prop` O30, the staged studio presenter (flex slot): 80-110 | `reel_motion`: 0-30 | 150-240 |

| Line | Arithmetic | Credits |
|---|---|---|
| 12 reels | 95 + 305 + 175 + 150 ; 170 + 515 + 290 + 240 | 725 to 1,215 |
| 12 carousels | 12 x 13 (39 a week, over the brand kit's 30: owner question) | 156 |
| 4 images | 4 x 1 ; 4 x 2.75 | 4 to 11 |
| One-time this month | R1 about 10 + R2 about 80 + crochet cast sheets on Nano Banana 2 (about 15 to 20, `animation-organic.md` 4 and `song-organic.md` 4) | 105 to 110 |
| **Total** | 725 + 156 + 4 + 105 ; 1,215 + 156 + 11 + 110 | **990 to 1,492** |

W2's second reel is a quote reel, not the strategist, because the narrated POV is the month's priciest piece. The top
of the range is 192 over the cap, so two controls are written into the plan (month-to-date spend from `organic.py
ledger straightscale`):
1. Before W3 cards are made, if 1,300 minus month-to-date spend is below W3's top + W4's top with its flex slot as a
   motion reel + two weeks of carousels and images (290 + 160 + 78 + 6 = 534), W3's story reel becomes hidden_villain
   ep 2 as a `reel_animation_short` (70 to 100, and W4 takes ep 3) and the tier A piece moves to next month: top
   1,492 - 120 = **1,372**.
2. Before W4 cards are made, if 1,300 minus month-to-date spend is below W4's top (240 + 39 + 3 = 282), the strategist
   reel becomes a `reel_motion` (0 to 30): top 1,372 - 80 = **1,292**, under the cap.

Expected spend at midpoints: reels 970 + carousels 156 + images 8 + one-time 108 = **about 1,242**, and neither control
fires. Mix: 7 tier C, 4 tier B, 1 tier A, as OS 7.7 says month 1 should lean on B and C. Budget timing follows
STANDARDS 10: `pipeline.py budget` (G-BUDGET, +25%, under 24 h old, against the live balance) runs before each run's
first generation and again within 24 h of each later batch, and step 9 re-prices the whole video before the first video
call.

### 5.7 How to judge a story post (72 h and 7 d)
| Read | Look at | Decision |
|---|---|---|
| 72 h | Skip rate, average watch time, sends per reach; the hook variants' trial reels | High skip: the hook failed (rewrite, re-test as a trial). Drop at 20 to 30 s: rehook 1 failed (fix that line in the lessons). |
| 7 d | The card's job metric vs the account median: reach = sends per reach and follows per 1k reach; trust = saves per reach and keyword comments; convert = qualified DMs. Plus average watch time. | Beats the median: `angle_proven: true`. 3x+: factory. Under: log one reason (topic, packaging, delivery, CTA). Good hold but few sends: the last dab isn't retellable. |

The baseline is empty in the brain: the first 6 posts set it, and the Learn loop needs Insights access (D6). The analyst
maps drop-offs to beat and line numbers and adds 1 or 2 lessons to `clients/<slug>/analytics/learnings.md` (G-LEARN).

---

## 6. The production path for one story piece

### 6.1 Steps (tools in `growth-engine/tools/`)
| Step | What happens for a story piece | Gates |
|---|---|---|
| Card | `cards/<yyyy-mm>-W<n>/<post_id>.yaml` with format, story_template, animation_style, series, series_character, length, angle_proven or wildcard, CTA; `organic.py card-check`, `route`, `week-check` | card-check clean |
| Once per series | `pipeline.py init straightscale SS-LIB-<SERIES> --format <format>`; `pipeline.py budget` before the first sheet (STANDARDS 10); style, character, set and prop sheets | G-BUDGET, G-PROMPT-IMG per sheet, G-VIS-SHEET, G-HUMAN-LOOK |
| Run | `pipeline.py init straightscale <post_id> --format <format> --card <card>` opens `runs/<post_id>/ledger.json` | |
| 0 to 3 | Brief and THE PICTURE; hook stack with a fresh grader; script from the template's beats and ST code, last dab first, listen and sound-off cold reads (drama: both at every length, X10). A concept frame made here is the run's first generation, so `pipeline.py budget` runs before it | G-BRIEF, G-IDEA, G-HOOK, G-SCRIPT 85+, G-HUMAN-SPINE |
| 4 to 5 | `pipeline.py budget straightscale <post_id> --planned <USD> --balance <live Atlas USD>` before the first voice call (the voice is a generation; STANDARDS 10). ElevenLabs voice (4 takes per beat, pauses never capped) or song master (STANDARDS 1 and 4); each voice, slice, song, music and SFX asset gets its own G-AUDIO; word map; slices per STANDARDS 2 | G-BUDGET, G-AUDIO per audio asset, G-AUDIO-MASTER, G-HUMAN-VOICE (new voice), G-HUMAN-SONG (every song master, before any picture), G-TIMELINE |
| 6 | visual-planner: one Shot Spec per shot, every beat and rehook on a cut; `pipeline.py spec-check`; prompt-reviewer | G-PLAN, G-SPEC |
| 7 to 8 | Sheets from the LIB run; storyboards, hook board first at phone size with the text hook; every storyboard is hero (STANDARDS 3); `pipeline.py budget` again if the last G-BUDGET is over 24 h old | G-PROMPT-IMG per sheet and storyboard, G-VIS-SHEET, G-VIS-BOARD, G-CONTINUITY, G-HUMAN-HOOKBOARD |
| 9 | `pipeline.py budget straightscale <post_id> --planned <USD> --balance <live Atlas USD>` re-prices the whole video (every planned clip and still + 25%); step 9 closes only on a G-BUDGET recorded after steps 0 to 8 closed, and the gate refuses every video call until it does (STANDARDS 10) | G-BUDGET |
| 10 to 11 | Generation through the gate; fresh reviewers per asset (frames, drift, every word); 3 attempts per asset (an edit pass of a still, with its own previous version as the single `edit_source` reference, is one attempt and gets its own full review: STANDARDS 1), then the owner; 2 failed prompt loops, then the Organic Director | G-PROMPT-VID (G-PROMPT-IMG for any start frame or still), G-VIS, G-TAKE, G-AUDIO, G-ASSETS, G-HUMAN-ESCALATE |
| 12 to 13 | Edit on the audio master, loudness per STANDARDS 4, captions in the STANDARDS 6 safe zone; final review, then the Organic Director | G-FINAL, G-DIRECTOR |
| 14 to 15 | `hub.py push <item.json>` as a draft, "AI label: on" in the notes; owner approves on the Content page; analyst at 72 h and 7 d | G-HUMAN-FINAL, G-LEARN |

### 6.2 The owner's checkpoints (batched daily in `queue/<date>.md` by `pipeline.py queue --write`)
Look bible once per series (G-HUMAN-LOOK) · the hook storyboard of every piece (G-HUMAN-HOOKBOARD) · each new voice
once (G-HUMAN-VOICE) · every song master before any picture (G-HUMAN-SONG) · the final post on the hub (G-HUMAN-FINAL).
Only when needed: an asset after 3 failed attempts (G-HUMAN-ESCALATE), the R1 and R2 tests (G-HUMAN-TEST), a model
outside the standards (G-EXCEPTION). The Organic Director decides Kling fallbacks (G-FALLBACK) and a prompt after 2
failed loops (and may send it to the owner). STANDARDS 9 lists them all.

### 6.3 Where a skill disagrees with STANDARDS.md (STANDARDS wins)
| Skill or source says | We do |
|---|---|
| Script Lab, pipeline step 1: no story under 55 s | No full discovery story under 45 s; under 45 s use compact shapes (STANDARDS 8) |
| Drama: S90 default; v2's X5 routes shots to Seedance, Veo, Omni and others | O60 or shorter; H3 for every shot, Kling 3.0 only with G-FALLBACK, until D9; a one-off needs G-EXCEPTION (STANDARDS 7b) |
| Song: Suno, generated by hand; 3 to 6 shots per take | ElevenLabs Music default; shots per take and sequence length per STANDARDS 2 and 5; the owner hears every master (G-HUMAN-SONG) |
| Podcast: burned "AI DRAMATIZATION" tag; router C45 40 to 50 s | Instagram's AI label, no burned tag (STANDARDS 7); C45 per STANDARDS 8 |
| Animation: `eleven_multilingual_v2` for Albanian; `vo_build2.py` 0.4 s pause cap; -16 LUFS | `eleven_v4`; pauses never capped (gap codes are minimums); loudness per STANDARDS 4 |
| Claymation style skill: Seedance 1.5 Pro for transitions | Style block only; H3 keyframe chains, Kling with G-FALLBACK (STANDARDS 1, claymation row) |
| Skills and pipeline step 12: bottom 20% safe zone | The STANDARDS 6 safe zone on every reel |
| Drama: 24 fps | 30 fps; drama may choose 24, stated in the run (STANDARDS 5) |
| Kallaway POV template (research file): enquiry counters, a priced kitchen, "dramatised numbers" | Brain rule: no number outside the proof bank; screens show states, not counts (STANDARDS 6) |
| Adapter examples with counts or platform names on screens | Out for every client: no count unless it is in brain.json, no real platform's logo or name (STANDARDS 6) |
| Kallaway: captions don't matter (8cQidXgtGmU) | OS 8.2 caption rules stay; treated as a hypothesis |

### 6.4 The narrated POV (`reel_story_narrated`)
A narrator (the brand's locked voice, "ti") over a POV camera: hands, the phone, the room, never a face. No mouth moves
on screen, so every clip is a silent H3 keyframe clip (STANDARDS 2): one shot per clip, a start frame (and an optional
end frame), 5 s rendered and trimmed or sped up to its slot (at most 2.5x, STANDARDS 5). A chain of shots is several
one-shot clips cut in the edit on the voice master. No reference mode and no storyboard as image 1 (nothing talks); the
hook board still goes to the owner (G-HUMAN-HOOKBOARD) and the boards to G-CONTINUITY (STANDARDS 3 and 9).
- **Words:** Script Lab at the narrator's measured pace (STANDARDS 4), the tier per STANDARDS 8 (pov_day is O60).
- **Shots:** one picture per 3 s on average (STANDARDS 5's 2 to 4.5 s band; `song-organic.md` 4 uses the same
  story-seconds rule), the first 5 s per STANDARDS 5, every BUT and rehook on a cut. 2 takes on the hook clip, 1 take on
  the others (STANDARDS 2).
- **Stills:** one start frame per clip. A frame with hands in it is a realistic person: GPT Image 2 with a reference photo
  (STANDARDS 1); a frame with no person (the phone on the worktop, THE PICTURE) is GPT Image 2.5 in the client's style.
- **Credits** (our computation at STANDARDS 10 prices): clips = (runtime minus the 3 s end card) ÷ 3, plus the second
  hook take, at 10 credits each (H3, 2 per second); stills = one start frame per picture plus about 5 more (concept
  frames, the hook board, the end-card still) at 1 credit with no person up to 6.5 with hands (price with `get_cost`);
  then +25%.

| Piece | Clips | Stills | Total with +25% |
|---|---|---|---|
| O60 at 45 s | 14 pictures + 1 hook take = 15 clips = 150 | 19 stills = 19 to 124 | **about 210 to 340** |
| O60 at 60 s | 19 pictures + 1 hook take = 20 clips = 200 | 24 stills = 24 to 156 | **about 280 to 445** |

organic.json's `reel_story_narrated` range (210 to 445) is this table.

---

## 7. Three pilot concepts for StraightScale (idea cards only, nothing produced)

Hooks are drafts for Hook Lab (10 hooks, fresh grader, A or A+ on every channel) and need a native read.

### Pilot 1: "Patchwork" (the villain short)
- **Card:** `hidden_villain` · `reel_animation_short` (B) · `crochet` · pillar Own · **B2** · **reach** · CTA **send** ·
  hidden_cause · "telefoni nuk bie" · 30 s (O30) · series null until it beats the median, then it joins the content map.
- **Hook stack:** visual: a crochet blanket stitched from mismatched squares lies over an owner's desk, the red yarn phone
  silent under it, one square twitching. Text: "Ja pse telefoni yt nuk bie" (This is why your phone doesn't ring).
  Spoken (the villain): "Telefoni yt nuk bie, dhe ti ende fajëson reklamat." (Your phone doesn't ring, and you still
  blame the ads.)
- **Beats:** 0-3 the villain's line · 3-10 mocks the fixes: "Më shumë reklama? Bukur. Një freelancer tjetër? Edhe më
  bukur." (More ads? Nice. Another freelancer? Even nicer.) · 10-16 the cost: messages unanswered while he works, ad money
  disappearing · 16-26 "Më quajnë Patchwork Marketing" (They call me Patchwork Marketing), then one thread pulls the
  squares into one line (the five steps as supers) and the villain unravels · 26-30 last dab (C1) + "Dërgoja një pronari
  që paguan disa furnitorë për marketing." (Send it to an owner who pays several suppliers for marketing.)
- **Credits:** 70 to 100, plus about 15 for the first cast sheets, about 10 for R1 and about 80 for R2 (both once).
- **True first:** R1 run (G-HUMAN-TEST); R2 run (G-HUMAN-TEST: the villain talks, and STANDARDS 14 puts R2 before the
  next talking-head or story piece); `SS-LIB-PATCHWORK` built and approved (G-HUMAN-LOOK); the villain's voice cast
  (G-HUMAN-VOICE); AI label on per STANDARDS 7 (D1 decides whether to extend it); "ti" until D2.

### Pilot 2: "Të shkruajnë, por nuk blejnë" (POV day)
- **Card:** `pov_day` · `reel_story_narrated` (B) · no style · pillar Convert · **B1** · **reach** · CTA **send** ·
  hidden_cause · "na shkruajnë po nuk blejnë" · 60 s (O60).
- **Hook stack:** visual: POV over the owner's hands at a kitchen showroom counter after dark; the red-case phone on the
  worktop lights up again and again while his hands hold a sample door. Text: "POV: të shkruajnë, por nuk blejnë" (POV:
  they message you, but don't buy). Spoken (narrator, "ti"): "Të shkruajnë, por nuk blejnë, dhe ti mendon se problemi
  është çmimi." (They message you, but don't buy, and you think the problem is the price.)
- **Beats:** 0-3 hook · 3-15 morning to afternoon: a client on the floor, BUT the phone keeps lighting up, SO "do t'u
  shkruaj më vonë" (I'll write back later) · 15-25 he adds ads; thought narration "pyesnin vetëm për çmimin" (they only
  asked about the price) · 25-32 rehook "Por ja ku është problemi" (But here's the problem): more ads, more messages
  nobody catches · 32-45 THE PICTURE: the ad, the page and the inbox as separate pieces, the enquiry falling through the
  gap: "Nuk është çmimi. Nuk je ti. Ky është Patchwork Marketing." Then the UMS in one line · 45-55 the same worktop, the
  same message, this time answered with one question and a next step (process only) · 55-60 last dab (C3) + "Dërgoja
  një pronari që u përgjigjet mesazheve më vonë." (Send it to an owner who answers messages later.)
- **Credits:** about 280 to 445 at 60 s (section 6.4); R2 is already paid in W1.
- **True first:** R2 run (before pilot 1); the AI-people rule (STANDARDS 7) met by the POV camera: hands only, no face;
  AI label on (an AI voice speaks as a person); the narrator voice `8oGKUMljR779HzpZBiE4` (STANDARDS 1) has its
  G-HUMAN-VOICE record, with the Albanian pace band measured on the approved audition in its note (STANDARDS 4); the
  Albanian names of the five steps (the brain names them in English only); the buyer phrase confirmed if possible.

### Pilot 3: "Agjenci tjetër apo një sistem?" (podcast disagreement)
- **Card:** `podcast_disagreement` · `reel_podcast` (B) · pillar Own · **B5** · **trust** · CTA **keyword ANALIZA** ·
  comparison · "mesazhet mbeten pa përgjigje kur jam në punë" · 40 s (C45), 10 turns, about 90 words.
- **Hook stack:** visual: host A's calm F1 medium close-up at the night podcast table in Tirana, with the title bar (frame
  1 is F1, never the master two-shot: `podcast-organic.md` 3). Text (title bar): "Agjenci tjetër apo një sistem?"
  (Another agency or a system?). Spoken (A): "Nëse nuk të bie telefoni, merr një agjenci më të mirë." (If your phone
  doesn't ring, get a better agency.)
- **Turns:** host A argues the owner's common belief in the third person, never as "I, the owner" (section 3.8). B "Jo.
  Merr pjesë që punojnë bashkë." (No. Get pieces that work together.) · A "Pronari paguan reklama, faqe, dikë për
  postimet." (The owner pays for ads, a page, someone for posts.) · B "Pikërisht. Çdo pjesë punon vetëm. Askush nuk i
  lidh." (Exactly. Each piece works alone. Nobody connects them.) · A "Po mesazhet që i vijnë kur është në punë?" (And
  the messages that come while he's at work?) · B "Mbeten mes pjesëve. Ky është Patchwork Marketing." · A "Pra një
  agjenci tjetër do t'i shiste edhe një pjesë." (So another agency would sell him one more piece.) · B, to the viewer:
  "Po. Të duhet sistemi i plotë, duke filluar nga blerësit e tu." (C2) · A "Nga fillon?" · B: the five steps in one line
  + "Komento ANALIZA dhe të shkruajmë në DM." (Comment ANALIZA and we'll write to you in DM.) The three A lines changed
  on 16 Oct need the native read first.
- **Credits:** about 220 to 320 with the cast built, plus about 25 to 33 once for the new cast (`podcast-organic.md` 4).
- **True first:** D1 decided (host faces on screen; until then the card runs steps 0 to 3 only); D7 confirms owners
  argue this; R2; a second voice (G-HUMAN-VOICE); `SS-LIB-PODCAST` with the master two-shot (G-HUMAN-LOOK); no "what
  happens in the analysis" lines until D3.

---

## 8. Checklist before a story card goes to production

**Content-strategist**
- [ ] `story_template`, `format` and `animation_style` use organic.json ids; the format renders the template; `card-check` has no ERROR.
- [ ] Tier A has `angle_proven: true` or is the month's only `wildcard`; one tier A a week at most; one story reel at least.
- [ ] The pain is one moment from AV-01, in the brain's words; the baseline fix comes from `tried`; A vs B is named.
- [ ] The last dab is written (C1 to C5 or the mechanism lines); no number outside the proof bank (StraightScale: none).
- [ ] The CTA is one of the section 3 asks and fits the job; a keyword CTA uses a live keyword (ANALIZA only); "book"
  only on a convert post, as the keyword or DM path; no link, price, discount, guarantee or urgency.
- [ ] AI people per STANDARDS 7: label on, never a client, no results; until D1 only the strategist in his staged studio
  set faces the camera, and AI owners, hosts and drama characters are seen from behind, as hands, at a distance or as
  animation; `confession_pov` only with real footage of the real owner, in his own words.
- [ ] No count, anecdote or platform name breaks section 3's rules (numbers only from brain.json; "POV: ..." framing).
- [ ] The credit range fits what is left of the month (section 5.6 controls) and the series is on the content map.
- [ ] The decisions the piece needs (D1, D3, D7, R1, R2) are done, or the card says which interim rule it follows.

**Visual-planner**
- [ ] Frame 1 is the approved concept frame: the problem where it lives in the business, motion in the first second.
- [ ] Picture changes per STANDARDS 5 for the format and for the first 5 s; each BUT and rehook on a cut.
- [ ] THE PICTURE has its own Shot Spec with `must_read_in_1s`; the payoff shows a process; the last shot matches frame 1.
- [ ] Screens and story props have content lines and prop sheets; screens show states, never invented counts.
- [ ] The style block is copied word for word; no studio names; cast from the series' LIB run with `series_character`.
- [ ] Shots per take, clip length, speakers and modes per STANDARDS 2 (silent keyframe clips are one shot each); every
  storyboard is image 1 on a talking or multi-shot clip and is hero; the STANDARDS 6 safe zone is kept clear.
