# Onboarding: from "accepted" to "active"

How a new brand is taken from a signed client to a weekly content engine, by sessions, with Matan deciding only what is
his. Written 28 Oct 2026 for the Client OS plan (session C4). It sits under `ORGANIC-OS.md` (what to make and why) and
`production/` (how it is made and checked), and it uses `clients/_template/` as the starting folder.

A brand's `status` in `tools/clients/registry.json` and in the hub's Client OS dashboard follows these stages:
`onboarding` (O1) then `research` (O2 to O4) then `active` (after O5). `paused` is outside this path.

## How the stages run

Every stage has a **producer** (a session or agent that does the work), an **evaluator** (a fresh session that never saw
the producer's reasoning and checks the files cold), a **gate** (the check that must pass) and a **decider** (who says go).

- The main session runs the other sessions (CLAUDE.md, Sessions). It decides the internal gates.
- A session started by another session never passes an owner checkpoint, never publishes and never touches the live hub
  business.
- Owner checkpoints go to the hub's Studio page as one question each, with a recommendation.
- At most 3 rounds per step. After 3 failed rounds the producer replaces its work (a new angle, a new source), it does
  not escalate to Matan.
- No real client data goes in this repo's tools, tests or fixtures. Real client files live in `clients/<slug>/`, which
  this repo's CLAUDE.md already treats as the working folder. Never put a token or key in a file.
- Nothing is published, and no Apify, Atlas or other paid tool runs, until the stage that needs it says so. Apify runs
  only through the gate (`config/apify-actors.json`), always with `maxTotalChargeUsd` set.

Start of every onboarding: `cp -r clients/_template clients/<slug>`, add the brand to `tools/clients/registry.json` with
status `onboarding`, and add `Agency OS/Clients/<Name>/` in the vault (`tools/brain_note.py <slug>` writes its profile).

## O1 Intake and draft (docs first)

Quick onboarding, approved by Matan on 29 Oct 2026. The client is not asked 50 questions. They upload the documents they
already have, the machine drafts the brain from them, and Matan edits about 10 important fields by hand (O3).

| | |
|---|---|
| **Inputs** | The client's name and contact. The intake link (the hub app's `/intake/$token`): business name, website, Instagram, one offer line, up to 5 competitors, two consents (AI-made people and faces, public use of proof) and the foundation documents (brand guide, price list, decks, past posts, reviews export, anything they have). |
| **Outputs** | `clients/<slug>/intake/slim.json` (the form, with no signed links). `clients/<slug>/foundation/` with the client's documents and `manifest.json` (**gitignored: private client documents never go into git**). A drafted `clients/<slug>/brain.json` where **every field has a source** in `field_sources` (document name and page, website URL, Instagram post, review) or says `unknown: <what is missing>`. `research/seeds.json` and, after the draft check, `research/o2-queue.json`. |
| **Producer** | The main session pulls the intake (`hub.py intake-pull <slug>`, right away: the document links expire after 10 minutes), then `braindraft` seeds it (`draft.py seed <slug>`) and `brain-builder` drafts the rest (see its agent file). The 38 old questions are the drafter's internal checklist (`draft.py checklist <slug>`), never asked of the client. |
| **Evaluator** | A fresh session. It opens 5 fields chosen by it, not by the producer, and checks that the cited page or URL says what the brain says. It also checks that no number, result, client or review appears without a source, and that every `unknown:` says what is missing. It writes `intake/draft-review.md`, ending with `PASS` or `FAIL`. |
| **Gate** | **Sourced draft.** `hub.py intake-pull <slug>` prints `O1 gate: ready`, `draft.py check <slug>` prints `PASS` (every drafted field has a source or `unknown: <what>`, the schema passes), and the evaluator's report ends with `PASS`. The check also queues O2: research starts automatically after the draft. |
| **Decides** | The main session. |

Notes:
- **Slim intake shape.** `intake-pull` calls `GET /api/clients/intakes?brand=<slug>` with the studio token and reads
  `{brand, business_name, website, instagram, offer_line, competitors, consents: {ai_people, proof}, docs: [{name, mime,
  size, signed_url}], submitted_at}`. It downloads each document into `foundation/` at once (no token goes to the storage
  host) and lists any that failed, so the gate says which document to ask for again. The old 38-question shape is still
  read (`answers.json` and `files.json`), for brands that already used it.
- `hub.py intake-pull <slug> --fixture file.json --dry-run` runs the same checks from a saved response with no network
  and writes nothing.
- **The draft reads, in this order:** the foundation documents, the website, the Instagram account, public reviews. A fact
  that only the client's own words can give (price, capacity, who approves) and that no document holds is written
  `unknown: <what>`; it is never guessed and never asked of the client in a form. Matan fills the few that matter in O3.
- **Consents set rules.** `ai_people` false: `visual.face` is `faceless`. `proof` false: no proof line is made public
  (permission stays `pending`).
- `onboarding/intake-questions.json` stays as the checklist data (ids never change); the app no longer shows it to new
  clients.

## O2 Research

| | |
|---|---|
| **Inputs** | The drafted `brain.json` and `research/seeds.json` (website, Instagram, competitors, consents) from O1; `research/o2-queue.json` says it is queued. For a brand on the old shape: `intake/answers.json` (G1 to G3). |
| **Outputs** | In `clients/<slug>/research/`: the voice of the customer (`voc-master.csv`, with a source on every row), competitors and their ads (`competitors.csv`, `ads.csv`), the outlier set (`outliers.csv` from `organic.py outliers`), page facts (`page-facts.md`), the demand map (`demand-map.csv`, 20 to 40 buyer phrases tagged direct, bridge or off_map) and the Hook Library (`hook-library.md`). These are Client Foundation v3 steps 01 (business snapshot and research map), 02 (VOC harvest) and 03 (competitors and market messages). |
| **Producer** | `research-scout`, running Foundation steps 01 to 03, **started automatically once `draft.py check` passes**. Scrapers only through `config/apify-actors.json`: Instagram, Facebook posts, Meta Ad Library (`apify/facebook-ads-scraper`, counts only unless more is needed), Google reviews, Trustpilot (`memo23/trustpilot-scraper-ppe`). Each call must carry `maxTotalChargeUsd`, which the gate enforces. The actor's `max_items` is the item cap to put in the input; the gate does not check it, so the USD cap is the hard limit. YouTube Shorts come from TranscriptAPI and carry views only (see below). |
| **Evaluator** | A fresh session. It opens the files and checks evidence and counts: every VOC row has a quote, a source URL and a date; rows are real quotes, not summaries; at least 80 coded VOC rows per problem lane on `standard` budget (50 on `lean`) and at least 3 lanes; at least 8 competitors with their ad counts, or the reason an Ad Library scan was not possible; the outlier file has at least 10 trusted outliers or says why not; the demand map has 20 or more direct or bridge phrases; the Hook Library has at least 20 hooks with a source each. It re-computes three counts by hand and compares. |
| **Gate** | **Evidence and counts.** The evaluator's report `research/review.md` ends with `PASS`. A FAIL names the missing counts and the producer fills only those. |
| **Decides** | The main session. |

Notes:
- **YouTube outliers:** a Shorts listing has no comment counts, and TranscriptAPI's metadata call returns views and likes
  text only. `organic.py yt-import` therefore marks every short `views_only`, and `organic.py outliers` skips the comment
  and engagement checks for them. It says why on the row (`skipped`) and in its summary, and never trusts them: they can
  show as `partial_outlier` (views 3x the median) for a check by hand. If someone reads the comment counts another way,
  `yt-import --counts counts.json` gives those shorts the full check.
- Foundation step output names above are this repo's names for the Foundation files; keep them stable so the
  evaluator and the brain-builder find them.

## O3 Strategy

| | |
|---|---|
| **Inputs** | O2's research folder and the drafted brain. |
| **Outputs** | `research/strategy.md`: 2 or 3 offer directions, each with its evidence (VOC row ids, competitor gaps, the price and margin when known), ICP avatars (1 to 3), awareness stage and sophistication, the mechanism (problem name and solution name), the belief ladder B1 to B8, the voice, and the few claims the client must approve. A filled `clients/<slug>/brain.json`, `brain.md` and the first `decisions_open`. This is Foundation steps 04 (desire, identity, sophistication), 05 (avatars, objections), 06 (mechanism), 07 (offer), 08 (brand and messaging) and 09 (beliefs and proof). |
| **Producer** | `brain-builder`, running Foundation steps 04 to 09 on top of the O1 draft. Never guesses: a missing fact is written `unknown: <what>` with its source field kept, and listed in `decisions_open`. |
| **Evaluator** | A fresh session. It reads `brain.json` cold and checks: `organic.py brain-check <slug>` has no errors (the six blocking fields are filled and the schema passes); `draft.py check <slug>` still passes; every avatar phrase, fear and desire traces to a VOC row; each offer direction has at least 3 pieces of evidence; no number, result, client or review appears that is not in a foundation document, the website or the proof bank; no claim breaks `constraints.cannot_say`. |
| **Gate** | `brain-check` passes **and** the evaluator's report ends with `PASS` **and** the owner steps below are done (and the client's, if the optional step ran). |
| **Decides** | **Matan edits the Brand card** (about 10 fields) and **picks the direction** (checkpoint **G-HUMAN-OFFER**, STANDARDS 9). The client confirms only the claims in the optional step. The main session records the answers in the brain and in `decisions_open`. |

**The Brand card (Matan, by hand).** In the hub, Matan edits about 10 fields: `offer`, `icp`, `promise`, `mechanism`,
`voice`, `never_say`, `proof_bank`, `cta_keyword`, `monthly_cap_usd`, `cadence`. Then the main session runs
`hub.py brand-pull <slug>` (read-only `GET /api/clients/brand-overrides?brand=<slug>`). Each field is written into
`brain.json` with the source `Matan (Brand card, <date>)` in `field_sources`, the result must pass the brain schema or
nothing is written, and the vault note is regenerated with `tools/brain_note.py` when the vault exists. **`brain.json`
stays the source of truth**: the card is an input form, and a field Matan did not touch is not changed.

| Brand card field | Lands in `brain.json` |
|---|---|
| `offer` | `offer.main_offer` |
| `icp` | `avatars[0].situation` (AV-01 is created if there is no avatar) |
| `promise` | `offer.delivers` |
| `mechanism` | `mechanism.ums` |
| `voice` | `voice.adjectives` (split on commas or lines) |
| `never_say` | `constraints.cannot_say` (one per line) |
| `proof_bank` | `proof_bank` (each line gets a P-id; permission is the card's, else `pending`; document proof is kept) |
| `cta_keyword` | `offer.keyword` |
| `monthly_cap_usd` | `package.monthly_usd_cap` (this is also the O5 cap, set only by Matan) |
| `cadence` | `package.posts_per_week` |

**Client confirm (optional).** Skip it when the drafted brain has nothing the client must approve. When it runs, the
confirm link carries only the claims that need the client's yes: names they will be called by, results and numbers to be
published, testimonials and proof permissions, and anything the brain says about them that no document backs. It never
repeats the intake questions.

How G-HUMAN-OFFER is asked: the pipeline has no per-brand run to hang it on (its runs are per post, and the look bible's
run is per series), so it has no step wiring. It is a Studio question: the main session pushes the brand's onboarding
run (`hub.py studio-push <slug> <post_id>`), writes a decision file with the 2 or 3 directions, the recommendation and
`research/strategy.md` as context, and sends it with `hub.py studio-ask <slug> <post_id> decision.json`. Matan answers
on the Studio page. The main session reads it with `hub.py studio-answers`, records it with
`pipeline.py gate <slug> <post_id> G-HUMAN-OFFER --status PASS --by Matan --note "<his words>"`, and marks it with
`hub.py studio-synced`. Producer and evaluator sessions never record it.

## O4 Plan

| | |
|---|---|
| **Inputs** | The approved `brain.json`, the research folder, the chosen offer. |
| **Outputs** | `clients/<slug>/content-map.json` (and `.md`): theme, pillars, series, the TOF, MOF and BOF mix for the brand's stage. A 4-week slate of Post Cards in `clients/<slug>/cards/<yyyy-mm>-W<n>/`, each card with a `funnel_stage`, a `load_bearing_beat` and a format chosen by the format router. A 6-idea bank in `cards/bank/`. |
| **Producer** | `content-strategist` (map and cards) and `organic-director` (approves the map and each week). |
| **Evaluator** | A fresh session. It re-runs the checks below and reads three cards cold for a hook that fits the brand's buyers' own words. |
| **Gate** | `organic.py card-check <slug> cards/<week>` passes for every card, `organic.py week-check <slug> cards/<week>` passes for every week, and the router's choice is recorded on each card. |
| **Decides** | The main session. |

Rules for the slate:
- **The mix follows the brand's stage** (`config/organic.json` `stage_mix`, set by `package.account_stage`): `new` is
  reach 50 percent, trust 35, convert 15 with one hard offer post a month; `growing` is 40, 40, 20; `mature` is 35, 40,
  25. Reach is the TOF job, trust is MOF, convert is BOF (`funnel_stage` on the card).
- **Every card goes through the format router** (`organic.py route <slug> <card>`, `production/FORMATS.md`). The router
  scores each format on how well its L19 properties fit the card's load-bearing beat, then funnel stage, what wins with
  this brand's buyers, the story template and variety. Cost only filters against the monthly USD cap. Motion graphics is
  one format among many: it is picked only for a list, data or type-led beat, at most 1 post in 6, and it is never the
  fallback when a better-fitting format is over the cap. If nothing fits the beat, the card is rewritten or swapped for
  the next bank idea.
- Plan only 4 weeks in detail, with the first 2 weeks fully carded. The bank keeps 6 ideas, each with a job, a beat and a
  buyer sentence from the demand map.
- Max 3 rounds per week. After that the next bank idea replaces the failing card.

## O5 Set-up

| | |
|---|---|
| **Inputs** | The approved plan. The brand's Instagram or Facebook access. |
| **Outputs** | The narrator's voice (once, G-HUMAN-VOICE) and the look bible (once per series, G-HUMAN-LOOK) with the brand's `LIB` run. The hub business: profile, lead-magnet keyword funnel(s) in `lead_magnets` with `hub.py funnel`. `package.monthly_usd_cap` and the weekly cadence in `brain.json` and `registry.json`. The brand's `status` set to `active`. |
| **Producer** | `conversion-agent` (profile, funnel, lead magnet and its five checks), `visual-planner` and `video-producer` for the look bible, the main session for the hub business and the registry. |
| **Evaluator** | A fresh session checks the lead-magnet checks, the `LIB` run's gates (`pipeline.py status`) and `hub.py client-sync <slug> --dry-run`. |
| **Gate** | `brain-check` has no gaps left in `package.monthly_usd_cap`, `lead_magnets` or `voice`; a `G-HUMAN-VOICE` PASS exists; `G-HUMAN-LOOK` has a PASS; `hub.py client-sync <slug> --dry-run` passes the contract. |
| **Decides** | **Matan listens to the voice** (G-HUMAN-VOICE, Matan only). **The look bible is delegated** (G-HUMAN-LOOK): the main session may record it after a fresh evaluator's report (STANDARDS 9, delegated owner checkpoints). **Matan sets the monthly USD cap** and confirms the cadence. A session started by another session never records any of these. |

When the gate passes, the main session sets `status: active` in `registry.json`, runs `hub.py client-sync <slug>`, and the
weekly engine (`growth-engine` skill) takes over: scout, plan, make, check, draft to the hub, learn. Nothing is posted
without Matan's approval on the hub (G-HUMAN-FINAL).

At the end of each stage the main session adds an entry to the vault's `Agency OS/Log/` and updates the client's
decisions and content log. Client facts change only in `clients/<slug>/brain.json`.

## Checkpoints at a glance

| Stage | Checkpoint | Who |
|---|---|---|
| O1 | Sourced draft | code (`intake-pull`, `draft.py check`) and a fresh evaluator |
| O2 | Evidence and counts | fresh evaluator, main session decides |
| O3 | **G-HUMAN-OFFER** (new): the offer direction | Matan, on the Studio page |
| O3 | Brand card (about 10 fields) | Matan, in the hub, pulled with `brand-pull` |
| O3 | Claims confirmed (optional) | the client, on the confirm link |
| O4 | card-check and week-check | code, main session decides |
| O5 | G-HUMAN-VOICE | Matan only |
| O5 | G-HUMAN-LOOK | delegated after a fresh evaluator |
| O5 | Monthly USD cap | Matan |

## Files this kit added

`onboarding/intake-questions.json` (and `.schema.json`, `test_intake_questions.py`; now the drafter's checklist), `tools/intake/` (the
`intake-pull` command, slim and old shapes), `tools/braindraft/` and `tools/draft.py` (seed, checklist, check), `tools/brand/` (the
`brand-pull` command), `tools/brainio/` (brain.json paths, saving, schema check), `clients/_template/`, the YouTube views-only handling in `tools/organic_os/`, the Trustpilot and
Ad Library entries in `config/apify-actors.json`, and G-HUMAN-OFFER in `production/STANDARDS.md` and `standards.json`.
