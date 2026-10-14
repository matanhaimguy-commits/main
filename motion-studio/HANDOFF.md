# Motion reel machine: handoff from the StraightScale studio session

This is for the session building a system that generates motion-design reels on its own. It holds what the
studio session built, proved, measured and learned across three client reels (four deliveries) and a bank of
viral references, so the machine starts from that instead of from zero. Written 14 Oct 2026.

Everything below exists as working code and documents in the GitHub repo **`matanhaimguy-commits/main`**, on its
default branch **`claude/discovery-engine-v16-ms5mxf`**. If your session can read that repo, treat this file as the
map and open the files it points to. If it can't, this file is written to stand on its own.

---

## 0. Read order (if you have the repo)

1. `motion-studio/HANDOFF.md`: this file.
2. `.claude/skills/motion-reel/SKILL.md`: the A-to-Z workflow (13 stages, gates, engine table, licences).
3. `motion-studio/CLAUDE.md`: house rules (render contract, banned looks, sound, review loop, tools).
4. `motion-studio/refbank/README.md`: the reference bank (cards of proven viral reels plus a per-client usage
   ledger). Then run `python3 motion-studio/refbank/tools/refbank.py stats`.
5. `motion-studio/knowledge/README.md`: index of 7 guides (about 4,300 lines) distilled from five reference repos.
   - The craft rules with numbers are in `onetake-principles.md`.
   - What broke before is in `our-pipeline.md` §3.
6. `motion-studio/projects/straightscale-03/`: the best finished project, worth reading end to end.
   - Its `index.html` is the reference implementation of a voice-timed, two-language canvas film.
   - It also holds `audio/score.py`, `audio/mix.py`, `finish.sh`, `docs/treatment.md` and `docs/review_log.md`.

---

## 1. What exists and is proven

| Piece | Status | Where |
|---|---|---|
| A-to-Z workflow skill `motion-reel` | Used for reels 02 and 03 | `.claude/skills/motion-reel/SKILL.md` |
| Canvas film engine | Production use; 60 fps with true subframe motion blur | `motion-studio/render.mjs`, `stills.mjs`, `lib/motion.js` |
| QA tools | All used on the deliveries | `motion-studio/tools/` |
| Voice chain | ElevenLabs voice → word timings → film and mix clock | see §8 |
| Score and mix chain | Real-instrument sampler score, effects from the film's own event times, word-timed ducking, two-pass loudnorm | `projects/straightscale-03/audio/`, `finish.sh` |
| Reference bank | 92 breakdown cards (81 viral reels, median 8.1M plays, plus 11 craft films), tag vocabulary, device catalogue, picker, usage ledger | `motion-studio/refbank/` |
| Knowledge base | 7 guides plus 5 complete reference repos | `motion-studio/knowledge/`; repos via `bash references/fetch.sh` |
| Project template | Brief, brand, treatment, review log, manifest, credits | `motion-studio/templates/project/` |

**QA tools in detail**

| Tool | What it checks |
|---|---|
| `seekcheck.mjs` | determinism |
| `pacing.py` | rhythm, rests, slideshow detection |
| `audio_qa.py` | loudness, dropouts, mud, voice vs music gap |
| `safezone.mjs` | text inside the platform UI safe zones and at minimum sizes |
| `events.mjs` | exports sound-cue times from the film |
| `vectorize_mark.py` | traces a real logo to SVG for macro zooms |

**The deliveries**, all for client StraightScale, an Albanian marketing agency. Every reel is 1080x1920 at 60 fps,
with voiceover and mastered audio.

| Reel | Idea | Signature device | Engine | Paid cost |
|---|---|---|---|---|
| 01 "Marketing copë-copë", 50 s | "Everyone says 'quality', so clients compare price." Problem on charcoal, gold-thread wipe to ivory, three steps, patches stitched into one set | shape wipe, word-by-word | canvas | voice reused |
| 02 "Klientët që kthehen", 41 s | A gold client token rides the S-path of the real logo at macro scale: leaks out, returns, loops; pull-back reveals the logo | one-take camera, object carries camera | canvas | ≈ $0.4 |
| 03 "Qartësia", 37 s, Albanian | "Attention is expensive; winners are clearer, not louder." Built from a viral reference's grammar. A crimson focus bracket finds what matters in every beat, on an ivory field | focus brackets | canvas | ≈ $0.92 for both languages |
| 03 English cut, 36 s | Same film source, English voice and copy | same | canvas, `?lang=en` | (included above) |

Reel 03 is the one the user called perfect. §6.6 explains what made it work.

---

## 2. The pipeline the machine should run

Every stage writes an artifact to the project folder `motion-studio/projects/<client>-<piece>/`, so a run can be
resumed and audited. The gates are where a person may approve. In unattended mode the machine decides at each
gate and logs the decision.

| # | Stage | Output | Tools | Gate / check |
|---|---|---|---|---|
| 0 | Setup | Tools installed | `bash motion-studio/setup.sh music` (+ `lemo`, `voice`) | `node -e "require('playwright')"`, `ffmpeg -version` |
| 1 | Intake | `PROJECT.md` Brief (the job brief, §3) | none | All required fields present, or stop and report |
| 2 | Research | `brand.md`, `manifest.json`, facts table with sources | client files (Drive), HyperFrames `capture <url>`, Firecrawl, Apify, Meta Ads Library | Every on-screen number has a source and a date |
| 3 | References | `docs/treatment.md` §1 (grammar to take and content to leave, with measured pacing) | `refbank.py pick/search`; capture new ones (§7.4) | At least 2 references, none already used by this client |
| 4 | Concepts | 3 concepts with different central visual ideas; one picked | `knowledge/onetake-principles.md` P3; the bank's devices | `refbank.py check` passes (no repeats) |
| 5 | Script and voice | Script, then `audio/vo_takeN.mp3` and `audio/words.json` | ElevenLabs (§8) | Word budget ≈ 2.4 words/s; transcript matches the script |
| 6 | Treatment | Beat sheet on the voice clock | `docs/treatment.md` §5 | Beat CV ≥ 0.25, longest ≥ 4x shortest, rest after hook, a survivor at every transition |
| 7 | Styleframes | 3-4 key frames rendered | `node stills.mjs --at ...` | Every rubric axis 8+ |
| 8 | Build | `index.html` (canvas engine) or HyperFrames `film/` | engine table, §9 | `seekcheck` and `safezone` pass |
| 9 | Sound | `audio/music.wav`, `sfx.wav`, `mix.wav` | `score.py`, `mix.py`, `finish.sh` | `audio_qa.py`: -14 LUFS, -1.5 dBTP, voice 10-20 dB over music |
| 10 | Review (≥ 3 rounds) | `docs/review_log.md` | contact sheets, strips, rubric, all checks | Every axis 8+, all checks pass, or the blemish is logged and reported |
| 11 | Render and master | `out/silent.mp4` → muxed master | `render.mjs --fps 60 --sub 4` in 2-3 parallel segments | Frame count = duration x 60; seams; loudness after AAC |
| 12 | Deliver | `deliver/vN/` (§10) | ffmpeg, SendUserFile or Drive | Files present and sized; commit and push |
| 13 | Log usage | `refbank/ledger.json` entry | `refbank.py log` | Required, so the next film for this client differs |

Times measured here on 4 CPUs and 15 GB RAM, no GPU:
- A full reel is about 1.5-2 hours of agent time, including about 25 minutes of final render for a 36-40 s film
  (3 parallel segments).
- A HyperFrames DOM film renders at about 3.3 s per output second.

---

## 3. The job brief: the machine's input contract

The interactive skill asks one round of questions. Unattended, the brief must already answer them. Suggested
schema:

```yaml
client: straightscale                 # slug; also the ledger key and the project folder prefix
piece: reel-04                        # project folder = motion-studio/projects/<client>-<piece>
goal: "Get comments 'ANALIZA' for a free 45-min analysis"   # what the viewer should do (the CTA)
audience: "Albanian SMB owners who run their own ads"
platform: instagram-reels             # 9:16 master; re-layouts: [4x5, 1x1, 16x9] only if listed
length_s: [30, 45]
languages: [sq]                       # first = master; others become ?lang= variants of the same film
voiceover: true                       # ALWAYS explicit. Never decide silently.
voice: { provider: elevenlabs, voice_id: 8oGKUMljR779HzpZBiE4, model: eleven_v4 }
brand:
  logo: drive://<file-id> or repo path   # the official file, never redrawn
  fonts: [Montserrat, Playfair Display]  # self-hosted
  colours: { primary: "#BE0F18", gold: "#DD9A10", ivory: "#F8F6EF", charcoal: "#1F1F1F" }
  rules: ["no gold text on ivory", "no crimson text on charcoal", "no em dashes", "no hype words"]
facts:                                 # every number that may appear on screen
  - { claim: "~1,800 active ads in Albania say 'cilësi'", source: "Meta Ad Library", date: 2026-10-11 }
offer: "Free 45-minute analysis"
must_say: []
must_not_say: ["prices", "invented clients or reviews", "deadlines", "founder name or face"]
references: []                        # optional URLs the client loves; else the machine picks from refbank
angle: null                           # optional pain point or idea; else pick one not in the ledger
budget_usd: 3                         # hard cap on paid APIs for this job
deliver_to: { drive_folder: <id>, notify: telegram }
approval: unattended                  # unattended | guided (pause at concepts, voice, styleframes, draft)
```

**Defaults when a field is missing**
- 9:16 at 30-45 s.
- The client's own language first.
- Voiceover `true` only if the brief says so. Otherwise stop and ask, because a film without voiceover is a
  different film.
- References are picked from the bank, avoiding the ledger.
- No paid image or video generation unless `budget_usd` covers it and the brief allows it.

---

## 4. Unattended-mode rules

- **Never ask mid-run.** Decide at each gate and write the decision and its reason in `PROJECT.md`.
- **Stop and report**, without guessing, when:
  - a required brief field is missing;
  - brand files can't be fetched;
  - a fact has no source;
  - the next step would exceed `budget_usd`;
  - any automatic check still fails after 3 fix rounds.
- Before every paid call, estimate first. ElevenLabs supports `estimate_only`.
  - Log each paid call and its cost in `PROJECT.md`.
  - Never retry a paid generation call blindly: retrying starts and charges a second job.
- **One human gate before posting, always.** A native-language check and someone listening with sound.
  - We cannot listen, so loudness and mud are measured, not heard.
  - Deliver to the human for a thumbs-up; never auto-post.
- **Version, never overwrite.** Use `deliver/v1`, `v2`, … with a changelog. Commit and push at the end of every
  stage; containers are wiped.
- **Log the film in the ledger** (`refbank.py log`) before reporting done.

---

## 5. Quality bar

### 5.1 House rules (from `motion-studio/CLAUDE.md`)

**Render contract**
- Every frame is a pure function of time.
  - Canvas engine: `window.seek(t)` paints frame t. HyperFrames: one paused GSAP timeline.
  - No `Math.random` (seeded noise only), no `setTimeout`/rAF/CSS transitions in render mode, and no state carried
    between frames.
  - `tools/seekcheck.mjs` must pass.
- Self-host every font and script. CDNs (jsDelivr, unpkg, cdnjs) are blocked in the cloud containers.

**Banned looks**
- centred title on a gradient;
- everything fading in;
- corner labels and frame borders;
- glow on UI;
- generic particle bursts or confetti;
- grey-bar placeholder cards;
- generic avatar circles;
- redrawn logos;
- fake UI or invented screens;
- an empty lower half for no reason;
- "cards on a flat background" as the whole idea.

**Look rules**
- One display font and one UI font, from the brand. One accent colour.
- **One signature device per film, present throughout.**
- Something new on screen every 2-4 s, and real rests (≥ 1 s) planned, not accidental.

**Safe zones and text sizes on 9:16 (1080x1920)**
- Keep text out of the top 250 px, the bottom 400 px and the right 140 px (the platform UI). Left margin is 96.
- Body text is never under 44 px. Fine print used purely as texture may go down to 26 px.
- Check every beat at 360 px wide.

**Content rules**
- Only real brand material.
- No invented numbers, reviews, clients, testimonials or deadlines.
- Examples are labelled as examples on screen (e.g. "SHEMBULL").

### 5.2 Pacing targets (measured; `tools/pacing.py` prints them)
- Beat lengths vary: coefficient of variation ≥ 0.25, and the longest beat ≥ 4x the shortest.
  - Accepted references sit at CV 0.6-0.8 and spread 7-14x.
- About a quarter of frames truly still, and at least one calm run ≥ 1 s. A rest must be frozen; a slow push-in
  still counts as motion.
- No frozen stretch over 3 s, and no quiet run over 5 s.
- A long lull right before the climax.
- Flurries (≥ 3 big changes within 1.5 s) never on a fixed interval.
- Never the same exit twice in a row (spring away, blur away, hard cut).
- Reel 03 measured about 20 visual beats in 24 s, a new picture about every 1.2 s, beat CV 0.70.
- **The viral bank agrees (§7.3).** Across 81 viral reels, something big changes every 0.5-1.5 s (median), mostly
  inside continuous shots rather than through cuts. So treat "every 2-4 s" as the longest allowed gap, not the
  target.
- The viral bank's medians by category are in §7.3.

### 5.3 The review rubric (each round, logged in `docs/review_log.md`)

Score 1-10, with evidence timestamps, on these axes:
- hook in the first 2 s;
- readability at phone size;
- motion quality;
- continuity;
- variety and pacing;
- composition;
- brand accuracy;
- sound;
- message with the sound off.

Each round:
1. Render a phone-size contact sheet with one frame per beat, plus strips around every fast moment.
2. Run every automatic check.
3. Fix the three worst problems.

Ship only when every axis is 8+ and every check passes, or the remaining issue is logged and reported.

### 5.4 Automatic checks (commands)

```bash
node motion-studio/tools/seekcheck.mjs [--page index.html?lang=en]   # same frame on revisit; seeks every 0.1 s
python3 motion-studio/tools/pacing.py out/draft.mp4                   # still share, quiet runs, transitions, CV, spread, energy map
node motion-studio/tools/safezone.mjs [--page ...]                    # boxes from window.__boxes; flags out-of-zone or < 44 px (fine < 26)
python3 motion-studio/tools/audio_qa.py deliver/v1/film.mp4            # LUFS, true peak, dropouts, low-mid mud, voice-over-music gap
node motion-studio/tools/events.mjs [--page ...] > audio/events.json   # {duration, cues, events[]} for score.py and foley
./review.sh out/final.mp4 4.1                                         # contact, strip and phone sheets
```

---

## 6. Creative doctrine: what makes a reel not look generic

### 6.1 Pick the idea before writing beats
- Write three concepts with **different central visual ideas**. Three orderings of the same cards count as one
  concept.
- A concept is one line describing the picture, not the product.
- Idea families that work:
  - one element transforms through every beat and lands as the brand mark;
  - one continuous push through nested scales;
  - a chain reaction where each event triggers the next;
  - before/after halves;
  - a material that floods in and recedes to reveal each scene;
  - one interface element that spawns each section;
  - a process that hides the message until it aligns;
  - an image that resolves as pieces join;
  - a world built from the brand's own material (reel 02 rode inside the logo).
- For each concept, specify:
  - the first 2 s;
  - the survivor at each transition;
  - what the idea forbids;
  - the engine;
  - the risk and the render cost.
- A template is not a concept. A recycled idea is rejected even when executed perfectly.

### 6.2 Continuity beats pacing
"Feels like slides" has two causes:
- **Monotonous rhythm:** fix it with the numbers in §5.2.
- **Substitution:** each scene replaces the last, and nothing travels between them.
  - Give every transition an explicit **survivor**: an object that persists and transforms. In reel 02 the gold
    token survives every beat.
  - Only two hard cuts are allowed unbridged: within a staccato run, and the cut to the end card.

### 6.3 Put the message inside the image
- Make the claim a physical event in the picture, not a caption. Examples:
  - The client token turns grey when it leaks.
  - "Cilësi" multiplies into a grey crowd behind the number 1,800.
  - The path was the logo all along.
- Decorative effects the brand doesn't actually do (sparkles, specks) read as stock templates.

### 6.4 Motion with weight
- Use springs, not easing curves. `lib/motion.js` has closed-form `spring()` and `track()`.
  - Rising word: ζ≈0.6, ω≈22, about 26 px travel, scale 0.94→1.
  - Card arrival: ζ≈0.62, ω≈18.
  - Logo letters: ζ≈0.5, ω≈26.
- Text arrives physically: a springy upward move, with opacity full early. It never just fades in.
- Operate the camera like a person:
  - Lead a tracked subject by about 0.1 s.
  - Interpolate zoom logarithmically.
  - Add a small decaying jolt on landings (not under narrated UI).
- Motion blur comes from a simulated shutter. `render.mjs --sub 4` averages subframes.
  - Strobing past about 80 px/frame is a failure.
  - Never blur through a cut.
- Typing runs at 28-38 chars/s with a steady caret. Staccato words last 0.22-0.36 s.

### 6.5 Sound as one room
- Fewer sounds than beats; drop one of any two sounds within 40 ms of each other.
- Use one shared reverb, and plan silences. Impacts are the loudest moments.
- Place effects from the film's exported event times, never retyped.
- Music follows the argument's harmony. Reel 03 stays in A minor while attention leaks, falls to near-silence on
  "they aren't louder", moves to C major when clarity arrives, and resolves on the payoff word.
- No cliché closers (vibraphone chord with a shimmer). Close on the cadence or a film-specific impact.
- Keep melodic runs at F4 or above, with short decays, to avoid low-mid mud under a male voice.

### 6.6 Why reel 03 was the best, and what to repeat
1. **It started from a measured viral reference**, not from a blank page.
   - The reference was divyansh.fx_'s "faceless" reel: 26 s, 348K plays.
   - We took its *grammar*: a clean light field, one accent, words focusing out of blur, a prop sequence (stopwatch,
     focus brackets, closing ring, linked hexagons, pills, a typed payoff with a hand-drawn ellipse, a logo sting),
     and a new picture about every 1.2 s.
   - We left its *content*: green, its English text, its pictograms, its creator mark.
   - Then we rebuilt it entirely in the brand: ivory, crimson, Montserrat plus Playfair italic, and the real logo.
2. **One signature device carries meaning.** A crimson focus bracket "finds" what matters in every beat, which is
   literally the film's argument (clarity).
3. **The voice is the master clock.**
   - Every visual cue is bound to a *word index* in the transcript, through the cue table `K`: for example
     `b2: 2` means beat 2 starts at word 2.
   - Re-voicing or translating moves the whole film automatically.
   - The English cut was the same `index.html` with `?lang=en`, its own `K` table and copy table `TXT`, and its own
     words file. 100/100 sampled Albanian frames stayed bit-identical after the refactor.
4. **One sourced, client-specific beat** the reference didn't have: the 1,800 ads saying "cilësi", with its source
   on screen.
5. **A planned silence** on "nuk janë më të zhurmshme" ("they aren't louder"). The music drops out, so the line
   lands.
6. **Craft details:**
   - Focus pulls are blur radius driven by a spring.
   - The renderer adds real subframe motion blur.
   - The noise crowd is rendered once as a sprite cache, then blurred as one layer on exit.
   - `fitSize()` only ever shrinks a line to fit its safe width, so no language overflows.

### 6.7 Hooks that work (first 2 s), from the bank
- An impossible object in a real place (fake out-of-home CGI).
- A scale shock.
- A question aimed at a pain ("Every month you start from zero?").
- A bold claim ("Attention is expensive").
- A number ladder ("0% to 100%").
- A guess challenge.
- A series hook ("which brand next?").
- A relatable POV.
- Starting mid-action.
- A "wait for the end" curiosity gap.

The hook must be visual too, because it has to work muted: motion within 0.5 s, and the first frozen hold only
*after* the hook. §7 lists the devices with their real examples and plays.

### 6.8 Never the same film twice (anti-repetition)
- The bank's ledger records, per client and per film: references used, category, devices (the first is the
  signature), hook, palette, camera language, engine and music.
- `refbank.py pick` and `refbank.py check` enforce these rules:
  - Never reuse a reference already used for this client.
  - Never repeat the previous film's category.
  - Never reuse the signature device of any of the last 3 films.
  - Share at most one device with the previous film.
- Also vary palette and camera language film to film, as reels 01 → 02 → 03 did:
  - 01: charcoal to ivory, wipes.
  - 02: dark macro world, one-take ride.
  - 03: light field, locked camera with focus pulls.
- Tools and pipelines are reused; looks are not.

---

## 7. The reference bank (`motion-studio/refbank/`)

### 7.1 What it is
- One Markdown card per proven reel, at `refbank/cards/<id>.md`, with YAML front matter. Each card holds:
  - plays, likes and shares, and the creator's followers;
  - category, hook, devices, energy, palette and hex colours, sound;
  - our build engine, difficulty (1-5), business fit, wow (1-5) and relevance (1-5);
  - pacing metrics measured from frames.
- Each card body covers:
  - the film in one line;
  - why it stops the scroll in the first 2 s;
  - a timed beat map;
  - the signature device;
  - a pacing read and the look;
  - why it works (retention mechanics);
  - steal this / leave this;
  - how to build it in our studio;
  - three business translations.
- `refbank/index.json` is built from the cards, so it can be searched without reading them.
- `refbank/TAGS.md` is the controlled vocabulary: 17 categories, about 20 hook types, about 90 devices, plus
  engines and business fits.
- `refbank/devices.md` is the catalogue of signature devices across the bank. Each entry says what the device is,
  which cards show it, how to build it in our engines, and business uses.
- `refbank/ledger.json` is the per-client usage memory, already seeded with reels 01-03.

**What's in it** (14 Oct 2026):
- **92 cards in total.** 81 are viral social reels: 75 from TikTok and 6 from Instagram (including the reel behind
  reel 03). The other 11 are award-level onetake craft films (study only).
- **Reach.** Every social reel except one has 1M+ plays; 38 have 10M+. The median is 8.1M plays.
- **Categories** (17): lyric-mograph 12, ui-saas 12, story-comedy 7, vfx-edit 7, brand-ad 6, cgi-fooh 6,
  explainer-2d 6, product-motion 6, satisfying-sim 6, data-infographic 5, explainer-3d 5, beat-sync 3,
  kinetic-type 3, logo-reveal 3, spectacle-world 3, asmr-care 1, brand-identity 1.
- **Usefulness.** 60 cards score relevance 4-5 for client marketing, and 48 of those are buildable at difficulty
  3 or less in our stack.
- **Build routes:**

  | Engine | Cards |
  |---|---|
  | canvas | 42 |
  | HyperFrames | 22 |
  | client footage | 19 |
  | paid gen-video | 8 |

- **Business fit** (cards can fit several):

  | Fit | Cards |
  |---|---|
  | agency | 51 |
  | e-commerce | 46 |
  | personal brand | 38 |
  | SaaS | 37 |
  | local service | 35 |
  | events | 32 |
  | B2B | 27 |
  | health | 25 |
  | education | 24 |
  | restaurant | 24 |
  | finance | 21 |
  | real estate | 19 |

**Start here.** These have relevance 5 and are easy to build:
- **tt-foil-finance:** a step chart driven by a ticking date.
- **tt-explainedbyalistair:** "This is A. This is B. What's the difference?", looped.
- **tt-hellobossfilms:** a TV remote swaps the product on the table on every beat.
- **tt-greenscreencut:** a branching tube shows who can receive what.
- **tt-chartosaur:** one dashboard fixed letter by letter through an acronym.
- **tt-clearmindtalks:** one glowing pictogram per spoken phrase.
- **ig-divyansh-fx-attention:** focus pulls, one prop per phrase (StraightScale reel 03).
- **tt-rafaellfreitaas:** three dots squash-and-stretch into the logo.
- **tt-maxmill-ae:** one morphing pill that runs a whole UI story.
- **tt-martaraile:** a green-screen phone as an x-ray window.
- **tt-bymike0404:** the camera dives into the wordmark, which becomes a city, then the app.
- **tt-madebyoddly:** the logo's arrow becomes a train riding the order steps.
- **onetake-knockon:** a chain reaction whose track is the product icon.
- **onetake-one-dot:** one dot plays every role.

**Highest wow:**
- **tt-thequinettos:** a numb arm becomes a stone arm (136M).
- **tt-why-cgi:** a giant bra as a mall trampoline (98M).
- **tt-blick-thegobbler:** bow vs hug (140M).
- **tt-arts-help:** a marker that draws grass (76M).
- **tt-brknsergio:** trampoline portals into other worlds (46M).

### 7.2 Using it
```bash
python3 motion-studio/refbank/tools/refbank.py stats
python3 motion-studio/refbank/tools/refbank.py search --category explainer-2d --fit agency --max-difficulty 3
python3 motion-studio/refbank/tools/refbank.py pick --client straightscale --fit agency --n 6   # skips used refs and recent signatures
python3 motion-studio/refbank/tools/refbank.py check --client straightscale --category data-infographic --devices chart-grow,word-stack
python3 motion-studio/refbank/tools/refbank.py log --client straightscale --project straightscale-04 --refs <ids> \
  --category data-infographic --devices chart-grow,word-stack --hook question --palette dark --camera "..." --engine canvas
python3 motion-studio/refbank/tools/refbank.py build    # after adding or editing cards (validates tags)
```

How a job uses the bank:
1. In stage 3, `pick` for the client and fit, then open 2-3 cards.
2. Take each card's grammar and write the "steal / leave" table into the treatment.
3. In stage 4, `check` the chosen concept.
4. In stage 13, `log` the finished film.

### 7.3 What the bank says about pacing by category
Medians over the 81 social reels, measured from frames sampled at 2 fps or slower:

| Category | n | median plays | cuts / 10 s | s between big changes | hook energy 0-2 s |
|---|---|---|---|---|---|
| lyric-mograph | 12 | 6.1M | 5.3 | 1.00 | 0.71 |
| story-comedy | 7 | 13.2M | 0.0 | 1.50 | 0.24 |
| vfx-edit | 7 | 45.7M | 1.4 | 0.51 | 0.47 |
| cgi-fooh | 6 | 69.7M | 0.0 | 0.51 | 0.64 |
| brand-ad | 6 | 2.3M | 0.9 | 0.62 | 0.34 |
| satisfying-sim | 6 | 8.4M | 0.0 | 1.18 | 0.10 |
| explainer-2d / -3d | 10 | 8-23M | 1.1 | 1.50 | 0.28 / 0.56 |
| data-infographic | 5 | 4.7M | 0.7 | 3.75 | 0.16 |
| product-motion | 5 | 12.5M | 1.9 | 1.35 | 0.17 |

How to read the columns:
- **Cuts** need a jump in the colour distribution, so camera moves and morphs don't count.
- **Big change** means at least 12% of the picture changes within half a second.
- **Hook energy** is the share of the picture changing in the first 2 s.

What this means for the machine:
1. **Viral reels change something big about every 0.5-1.5 s.** That is faster than our older "something new
   every 2-4 s" rule; treat 2-4 s as the *maximum* gap, not the target.
   - Most of them use few or no hard cuts. Change comes from motion inside one continuous shot or camera move.
   - That is the one-take, carry-a-survivor doctrine of §6.2, seen from the data side.
2. **Hook energy splits two ways:**
   - **Spectacle formats open in heavy motion** (0.5-0.7): CGI, VFX, lyric edits.
   - **Explainers, data and product films open calmer** (0.1-0.3), with a clear question or a clean first image.
   - Pick the style of hook that matches the format; don't force a frantic open on a data film.
3. **True stillness is rare in viral social reels.** Quiet share at 2 fps is about 0.
   - onetake's "about 25% still" is a craft target for brand and product films. In a hook-driven reel, a rest is a
     short freeze on a payoff word or number (0.5-1.5 s), placed after the hook and before the CTA.

### 7.4 Adding references: the capture recipe (blocked hosts included)
Instagram, fbcdn and TikTok video hosts **cannot be reached** from these cloud containers, and `api.apify.com` is
blocked too. Everything goes through the **Apify MCP connector**, which works.

1. **Find candidates** by plays.
   - `clockworks/tiktok-hashtag-scraper`: `{hashtags:[...], resultsPerPage: 60-80}`, $0.002 per video. Its results
     are popularity-sorted, so it is where the 10M+ motion reels are.
   - `apify/instagram-hashtag-scraper`: `{hashtags, resultsType:"reels", resultsLimit}`, $0.0023 per result. Its
     results are mostly recent, not top, so it is weak for finding hits.
   - Rank by plays and by plays / followers (the breakout factor). Floor: 1M plays.
2. **Read results without flooding context.** Read the dataset through `ReadMcpResourceTool` (server `Apify`) at
   `http://api.apify.internal:3333/v2/datasets/<id>/items?format=xlsx&clean=true&fields=...`.
   - **xlsx is saved to disk as a blob**, while JSON would be pasted into the conversation.
   - The limit is about 256 KB per read. Nested arrays only appear when you omit `fields` (they become columns like
     `videoMeta/aiVideoDescription/0/description`).
3. **Scene descriptions and transcripts.**
   - `clockworks/tiktok-scraper` with `{postURLs:[...], aiVideoDescription:true}` gives a time-segmented "what is
     seen and heard" for $0.001 per video-second.
   - Add `downloadSubtitlesOptions:"TRANSCRIBE_ALL_VIDEOS"` ($0.041 per started minute) for voiceover reels.
     Transcripts land as `transcription-*.txt` records in the run's key-value store.
   - For Instagram, `apify/instagram-reel-scraper` takes `{username:[<reel url>], includeTranscript:true}`.
4. **Frames.** `seemuapps/video-frame-extractor` accepts TikTok, Instagram, YouTube and MP4 URLs, up to 100 per run.
   - Input: `{videoUrls:[...], mode:"interval", intervalSeconds:0.5, maxWidth:200, maxFramesPerVideo:48, proxyMode:"auto", maxDownloadMbPerVideo:40}`.
   - Keep the download cap at 40 MB or more. At 6 MB, videos longer than about 60 s were skipped without an error.
   - Price: $0.01 per video plus $0.002 per frame. It handles about one video per minute.
   - Frames land in the run's key-value store as `v<N>-<videoId>-frame-0001.jpg`. Read each one with
     `ReadMcpResourceTool`; each read saves a file to disk (frames are 3-8 KB).
   - Contact sheets from the actor are over 256 KB, so they can't be read. Build your own.
5. **Metrics and sheet.** Run `python3 motion-studio/refbank/tools/frames_metrics.py <frames_dir> --step 0.5 --id <id> --out refbank/metrics/<id>.json`.
   - It reports cuts per 10 s, mean seconds between big changes, change rhythm CV and spread, quiet share, hook
     energy, an energy curve, luma, saturation and a palette.
   - It also writes `sheet.jpg` (hook at full rate, then one frame per second) to look at.
6. **Write the card** from `refbank/TEMPLATE.md` using `TAGS.md` slugs, then run `refbank.py build`.
   - Frames are third-party media: keep them out of git (`refbank/frames/` is ignored).
   - Study the grammar and never ship their pixels, words, characters or music.

**Cost**: about $0.10-0.15 per reference, all in. The first bank of about 80 cost about $20 in Apify.

**Weekly refresh job** (good for the machine):
1. Run the two hashtag scrapes.
2. Drop anything already in `index.json`.
3. Take the top 10-15 by plays and breakout factor, spread across categories.
4. Capture, write cards, build, and commit.

---

## 8. Voice chain (ElevenLabs MCP connector)

1. **Voice**: "StraightScale - Strategist (male, 45)", `voice_id 8oGKUMljR779HzpZBiE4`, model `eleven_v4`.
   - It handles both Albanian and English. For a new client, pick or design a voice
     (`creative_list_voices` / `creative_design_voice` → `creative_save_designed_voice`).
2. **Generate.** Call `creative_generate_speech` with `estimate_only` first, then for real.
   - It returns 4 takes on a flow, about 2,000 credits (about $0.35) for a 37 s script.
   - Poll `creative_get_flow_run_status`.
   - Downloads come from `storage.googleapis.com`, which is reachable.
3. **Pick a take**, pin it with `creative_add_flow_asset_node`, then call `creative_transcribe_audio`
   (`eleven_scribe_v1`). This gives word timings for free.
4. **Write `audio/words.json`** as `{source, duration, words:[{w, s, e}]}`, plus a `words.js` ES-module copy so the
   page can `import` it. This file is the master clock.
5. **Script rules:**
   - About 2.4 words per second.
   - Hook in the first 2 s.
   - One idea per line.
   - Teach or show one thing before the CTA.
   - Client-language lines get an English check line, and are flagged for a native speaker.

---

## 9. Engines and the canvas film pattern

### 9.1 Choosing the engine by the look
| Look or job | Engine |
|---|---|
| Kinetic type, UI and product demos, launch and brand reels, data, captions (most reels) | **HyperFrames**: HTML plus GSAP, one paused timeline, 447-item registry. `npx -y hyperframes@0.8.150`. GSAP must be vendored locally |
| Custom drawing, generative or physical motion, macro worlds, true motion blur | **Canvas engine**: `window.seek(t)` plus `render.mjs`. All three StraightScale reels used it |
| Painterly or illustrated looks (watercolour, ink, impasto, whiteboard, iso-infographic, toon, art deco, silkscreen) | **Lemo-Opuscar** style engines (`setup.sh lemo`), ported to a 9:16 page |
| Character acting (mascot, host, reaction) | **Claude Animation Base** (p5.brush). Use the client's own character, never Anthropic's mascot |
| Abstract-line B-roll | **Collage** route C, code-only halftone collage |
| Photoreal, product 3D, footage | Client footage first. Paid generation (ElevenLabs/Higgs image, video, 3D) only with budget approval |

### 9.2 Canvas engine contract and commands
```bash
node motion-studio/stills.mjs --from 0.25 --step 0.5 --dur 20 [--page "index.html?lang=en"]   # contact sheet from the page
node motion-studio/render.mjs --fps 15 --sub 1 --dur 37 --out out/draft.mp4                     # draft
# final: 2-3 parallel segments, then concat, then check the seams
node motion-studio/render.mjs --fps 60 --sub 4 --from 0  --dur 13 --out out/s1.mp4 &
node motion-studio/render.mjs --fps 60 --sub 4 --from 13 --dur 12 --out out/s2.mp4 &
node motion-studio/render.mjs --fps 60 --sub 4 --from 25 --dur 12 --out out/s3.mp4 &
wait; printf "file s1.mp4\nfile s2.mp4\nfile s3.mp4\n" > out/list.txt && ffmpeg -f concat -i out/list.txt -c copy out/silent.mp4
```
- The renderer averages subframes in the page with a canvas running mean (`globalAlpha = 1/(k+1)`), about 2x
  faster than reading pixels back.
- Seam check: compare frame differences at each join with their neighbours.

### 9.3 The voice-timed, multi-language page pattern (from `projects/straightscale-03/index.html`)
```js
const LANG = new URLSearchParams(location.search).get('lang') === 'en' ? 'en' : 'sq';
const WORDS = (await import(LANG === 'en' ? './audio/en/words.js' : './audio/words.js')).default;
const K = { sq: { b2: 2, b3: 5, hex: [20, 22, 25], pills: [44, 47, 49, 51, 53, 55], payoff: 65 /*...*/ },
            en: { b2: 2, b3: 5, hex: [17, 19, 22], pills: [45, 48, 49, 51, 55, 59], payoff: 68 /*...*/ } }[LANG];
const at = i => WORDS.words[i].s;          // cue time = start of word i
// TXT[LANG] holds every on-screen string; fitSize(text, font, size, maxW) only ever shrinks a line to fit.
window.CUES = {...}; window.EVENTS = [...]; window.DURATION = T_END;   // exported for the score and foley
```
- `score.py` reads `events.json` (`{duration, cues, events}`) and places every note and effect from it, so a
  re-voice moves the music too.
- Text helpers push their boxes to `window.__boxes` so `safezone.mjs` can check them.

### 9.4 Sound chain
1. **Score.** `audio/score.py` uses the Lemo sampler (VSCO2CE plus VCSL packs, CC0, about 667 MB,
   `setup.sh music`), run with `~/lemo/.venv/bin/python`.
   - Harmony is planned per section; effects are procedural foley from `sfx.py`, low-passed.
   - Timpani needs a pitch, and stereo buffers need a custom `add`.
2. **Voice EQ:** high-pass 75 Hz, -3 dB at 230 Hz, +1.5 dB at 3.5 kHz.
3. **Music EQ:** high-pass 45 Hz, -6 dB at 220 Hz, -2 dB at 3.2 kHz.
4. **Duck** (`mix.py`) from the word timings.
   - Voice spans are padded 0.12 s in and 0.3 s out; gaps under 0.7 s are bridged; ramps are 0.18 s.
   - The duck is -13 dB, with the unducked music 1 dB under the voice, so the music sits about 14 dB under while
     ducked.
   - Effects go in at 0.5 gain.
5. **Master** with two-pass `loudnorm` to I=-14, TP=-1.5, LRA=11. Mux AAC at 320k with `+faststart`, then re-check
   loudness after AAC.

---

## 10. Delivery package (`deliver/vN/`, never overwrite)
- `<client>_<piece>_9x16.mp4`: master, H.264 yuv420p, CRF 21 preset slow, AAC 320k, faststart.
- `<...>_view.mp4`: viewing copy under 30 MB (CRF 23).
  - Film grain on light backgrounds bloats files badly: CRF 16 gave 250 MB segments.
- `poster.png`, `contact_sheet.png`, `captions_<lang>.srt`, `CREDITS.md` (fonts, samples, voice, licences),
  `CHANGELOG.md`.
- The report to the human says what was checked, what wasn't (nobody listened; native check pending), and the two
  unused concepts as alternatives.
- Re-layouts (4:5, 1:1, 16:9) are separate layouts sharing scenes, never crops, and only when asked.

---

## 11. Environment facts and gotchas (hard-won)

**Network**
- **Blocked:** instagram.com, fbcdn, TikTok and YouTube video hosts, api.apify.com, font and JS CDNs, and some
  client sites (straightscale.com).
- **Reachable:** storage.googleapis.com, GitHub raw, the Apify / ElevenLabs / Drive MCP connectors.
- Firecrawl ran out of credits once, so don't depend on it.

**Container and processes**
- 4 CPUs, 15 GB RAM, ffmpeg 6.1, Chromium at `/opt/pw-browsers` (never `playwright install`). Writable disk is a
  fixed per-session allowance.
- Containers are wiped. `setup.sh` is idempotent: run it at the start of every job, and commit and push often.
- Never `pkill -f <pattern>`: it can match and kill your own shell. Kill by PID.
- Never wait with `pgrep -f`: it matches itself. Wait on `/proc/<pid>`.

**Canvas pitfalls**
- A blur filter on an element moved far off-canvas can blank the whole frame. Hide off-screen elements.
- Many individually blurred elements are slow. Cache them as a sprite, then blur once as a layer.
- Measure text only after fonts load. A late font invalidates every measured position.

**Refactors and code edits**
- When refactoring a film, prove zero regression with frame hashes (we compared 100 sampled frames) and
  bit-identical audio.
- Use Python, not `sed`, for multi-line code edits; quoting breaks.

**Licences**
- onetake is PolyForm Noncommercial: study its principles, never run, copy or adapt its code or text.
- HyperFrames is Apache-2.0. Avoid its 24 named text effects from an unlicensed outside repo.
- Lemo, CAB and collage are MIT. Strip "LemoLab" sign-offs and fan content.

**Repo rules**
- Never run `hyperframes skills update`.
- Never commit tokens. API keys live in `.env` and are never pasted into prompts.

---

## 12. Cost and time model (per reel, measured)

| Item | Cost |
|---|---|
| ElevenLabs voice: 4 takes, about 37 s | ≈ $0.35 per language |
| ElevenLabs Scribe word timings | $0 |
| Studying one external reference (frames, transcript, scene description) | ≈ $0.10-0.25 |
| Music (CC0 sampler), fonts (OFL), rendering (in-session) | $0 |
| **Paid services per reel** | **≈ $0.40-0.90** |
| Claude usage | Not measured here; about 1.5-2 h of agent time per reel |

---

## 13. Automation architecture (researched; pick one)

**A. Claude Code Routine plus API trigger (recommended)**
- Create a Routine on this repo. Its prompt is: "Run motion-reel in unattended mode with the brief in the payload;
  deliver; log the ledger; commit; notify."
- Fire it with `POST https://api.anthropic.com/v1/claude_code/routines/<id>/fire`:
  - header `Authorization: Bearer <per-routine token>`;
  - header `anthropic-beta: experimental-cc-routine-2026-04-01`;
  - body `{"text": "<the job brief YAML>"}`.
- Each run is a fresh cloud session with the repo's skills loaded and your claude.ai connectors.
- Limits:
  - It is a research preview.
  - 30 fires per hour per Routine.
  - The maximum run length is undocumented, so test a full 2-hour job first.

**B. Your own worker**
- A Docker image with the tools pre-installed (Node, Chromium, ffmpeg, Python audio, the 667 MB sample packs), at
  least 4 CPUs, 8 GB RAM and 10 GB disk.
- Command: `claude -p "<brief>" --permission-mode dontAsk --allowedTools ... --max-turns N --max-budget-usd X --mcp-config mcp.json --output-format json`.
- Bills to an API key. claude.ai connectors don't carry over, so ElevenLabs and Apify need their own MCP servers or
  keys.
- The Agent SDK equivalent needs `settingSources` to load project skills.

**C. GitHub Actions** (`claude-code-action`) on a schedule or dispatch. Runners are smaller, so renders are slower.

**Not an engine:** Cowork. It supports plugins and skills, but has no API or headless mode, and its scheduled
tasks need the desktop app open.

**Still to build for unattended runs**
1. The job-brief parser and the "never ask" rule (§3-4).
2. Auto-setup on session start.
3. A delivery step (Drive upload plus a notification).
4. The human thumbs-up gate before posting.
5. A weekly refbank refresh (§7.4).

---

## 14. Client rules: StraightScale (if the machine makes more for them)
- **Language:** Albanian first; English cut available.
- **Copy:**
  - No em dashes and no hype words.
  - No prices.
  - No invented numbers, reviews, client names, testimonials or deadlines.
  - No founder name or face.
  - Don't say "we chase or follow up leads", and don't lead with "1 hour".
- **CTA:** "Shkruaj ANALIZA në komente" (free 45-minute analysis). The English cut kept ANALIZA; switching to an
  English keyword is a pending decision.
- **Brand:**
  - Colours: red #BE0F18, gold #DD9A10, ivory #F8F6EF, charcoal #1F1F1F, crimson #B31217 on light fields.
  - Never gold text on ivory, and never crimson text on charcoal.
  - Fonts: Montserrat plus Playfair Display. Use the real logo files from Drive, never redrawn.
- **Sourced facts available:** about 1,800 active Albanian ads say "cilësi" (Meta Ad Library, 11 Oct 2026). The
  three growth figures from the brief: €15K→€55K, €30K→€100K and €0→€140K per month.
- **Used so far:** see `refbank.py history --client straightscale`. The next film must differ in category, signature
  device, palette and camera language.

---

## 15. File map
```
.claude/skills/motion-reel/SKILL.md        the workflow
motion-studio/
  HANDOFF.md                               this file
  CLAUDE.md                                house rules + tool list
  setup.sh                                 session setup (tiers: lemo, voice, music)
  render.mjs  stills.mjs  review.sh  beats.py  lib/motion.js
  tools/      seekcheck.mjs pacing.py audio_qa.py safezone.mjs events.mjs vectorize_mark.py lemo_fonts.py
  knowledge/  README + 6 guides (onetake-principles, hyperframes, lemo-opuscar, claude-animation-base,
              gbro-collage-broll, our-pipeline)
  refbank/    README, TAGS, TEMPLATE, devices.md, cards/, metrics/, index.json, ledger.json,
              tools/refbank.py, tools/frames_metrics.py
  templates/project/                       PROJECT.md brand.md manifest.json CREDITS.md docs/{treatment,review_log}.md
  projects/straightscale{,-02,-03}/        the three reels (source, audio, docs, deliver/)
references/   five complete reference repos (gitignored; bash references/fetch.sh)
social-agent/ separate project: Instagram/Facebook comment-to-DM and AI sales DMs (can carry the CTA keyword)
```
