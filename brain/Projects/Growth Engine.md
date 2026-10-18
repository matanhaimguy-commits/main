---
type: project
updated: 2026-10-18
tags: [project, growth-engine, organic, instagram, content]
---

# Growth Engine

The system that grows a client's Instagram and Facebook from research to booked calls. The studio side (this repo,
Claude sessions) researches, plans, makes and checks posts; the hub ([[Social Agent hub]]) holds them as drafts,
publishes what a person approved and runs the DM bot. How each picture and video is made and checked is in
[[Production layer]]; motion reels are built in [[Motion Studio]]. The only client so far is [[StraightScale]].
Back to [[00 Index]].

## What it is, in one screen

- Chain: onboard, research, plan, produce, approve, publish, engage, measure; winners become templates.
- Two halves. Hub (Lovable app, always on): clients, funnels, DMs, leads, content calendar, publishing, results.
  Studio (Claude Code sessions, in bursts): brand kits, research, plans, renders, QA.
- The bridge is the hub's Content API (`/api/content/*`, one studio token). `growth-engine/tools/hub.py` talks to it.
- Strategy spec ("what to make, for whom, why"): `growth-engine/ORGANIC-OS.md` (Organic Growth OS v1, 15 Oct 2026).
  Where the OS and older steps disagree, the OS wins; where the OS gives a production number, STANDARDS.md wins.
- Phases (PLAN.md, written 14 Oct 2026): phase 1 (Content API, Content page, studio skill, StraightScale pilot) in
  progress; phase 2 (publisher, insights pull, onboarding link) next; phase 3 (weekly scheduled session per client,
  template library, automatic results log) after 2; phase 4 (ads: boost winners) later. Whether phase 1 is now
  closed is not written anywhere I found.

Source: growth-engine/PLAN.md, growth-engine/ORGANIC-OS.md (header and section 3), .claude/skills/growth-engine/SKILL.md

## Where things live

| What | Path |
|---|---|
| Strategy spec | `growth-engine/ORGANIC-OS.md` |
| Plan and phases | `growth-engine/PLAN.md` |
| Daily run instructions | `growth-engine/DAILY.md` |
| Pre-publish gates, Director review, weekly memo | `growth-engine/GATES.md` |
| Beliefs, jobs, CTAs, mixes, week rules, formats, story templates, animation styles | `growth-engine/config/organic.json` |
| Schemas (brain, Post Card, scorecard) | `growth-engine/schemas/` |
| How each production skill runs for organic posts | `growth-engine/adapters/*-organic.md` (9 files) |
| Checks and numbers | `growth-engine/tools/organic.py` |
| Hub CLI | `growth-engine/tools/hub.py` |
| Agents | `.claude/agents/` (16 files) |
| Skill | `.claude/skills/growth-engine/SKILL.md` |
| Per client | `clients/<slug>/`: `brain.json`, `brain.md`, `brand-kit.md`, `style-bible.md`, `competitors.md`, `content-map.json`, `cards/`, `content/`, `runs/`, `research/`, `analytics/`, `reviews/`, `ledger.csv` |

Source: growth-engine/ORGANIC-OS.md (implementation map), .claude/skills/growth-engine/SKILL.md, ls of clients/straightscale

## The cycle: daily and weekly

**Daily run (StraightScale since 15 Oct 2026).**
- A scheduled task named "StraightScale daily content" runs every morning at 06:49 Europe/Tirane. It wakes the
  studio session that holds the Lovable, Higgsfield and ElevenLabs connectors and runs `growth-engine/DAILY.md`.
  A task that starts a fresh session gets no connectors, so it cannot do this job. The task id and the hub's Lovable
  project id are in DAILY.md.
- Goal: keep the hub **4 days ahead**. Every day from today to today+3 has exactly one post for the client, as a
  **draft** with its time. Times: 19:30 Tirana, Sundays 18:00.
- A person approves on the hub's Content page. The hub publishes approved items at their time (Auto-publish is on
  for StraightScale) and alerts about drafts due within 24 hours.
- From the cloud network `hub.py` cannot reach the hub host, so the daily run writes drafts with SQL through the
  Lovable connector (`query_database`). Never insert with status `scheduled` or `published`.
- Order: `organic.py brain-check`; the day's Post Card (write one if missing, pick the format with `route`);
  `card-check` and `week-check`; the full production run ([[Production layer]]); insert the hub draft; write
  `clients/<slug>/content/<key>/`; commit and push.
- Report: three lines (what was made, what waits for approval, the spend), then one line per asset version that failed
  review, then anything that blocked.
- Story reels, animation, drama, song and podcast pieces are made in a normal session, not in the daily run; the
  daily run only places them when their run shows step 13 done.

**Weekly rhythm inside the daily run.**
- Monday: research refresh (research-scout, 3-month window, `organic.py outliers`) and the Director memo
  (`organic.py score`: top 3 and bottom 3 by job metric, a diagnosis line per bottom post, three decisions: keep,
  kill, test).
- Friday: next week's Post Cards and the Director batch review (written to `clients/<slug>/reviews/<week>.md`).

**Weekly mode (the skill).** Steps 1 to 7 for one client in one session: research, learn, plan, produce, QA, ship to
the hub as drafts, hand over. A scheduled fresh session every Monday per client is phase 3 and is not built.

Source: growth-engine/DAILY.md (intro, sections 0 to 5), growth-engine/GATES.md, .claude/skills/growth-engine/SKILL.md (Modes), growth-engine/PLAN.md

## Post Cards

- Every post starts as a Post Card: the contract between strategy and production. Path:
  `clients/<slug>/cards/<yyyy-mm>-W<n>/` (week of the month by Monday). Schema:
  `growth-engine/schemas/post-card.schema.yaml`.
- Fields: post_id, client, account_language, pillar, series, episode, job (reach, trust, convert), belief (B1 to B8),
  avatar, awareness, demand_phrase, idea_source, narrow_product, format, format_tier (A, B, C), angle_proven,
  credit_budget, length_target_s, hook_type, emotion, cta_type, cta_keyword, lead_magnet, proof_used, hypothesis,
  success_metric, target, status. Story pieces add story_template, animation_style, series_character, wildcard.
- Status flow: planned, scripted, produced, approved, scheduled, live, scored.
- Each card carries a `gates:` map; the owning agent writes pass or fail with one line of evidence. A post with any
  fail does not go to the hub.
- Checks: `organic.py card-check` (card against brain and content map), `week-check` (week rules), `route` (format
  router inside the monthly budget).

Source: growth-engine/ORGANIC-OS.md section 7.1, growth-engine/GATES.md, growth-engine/production/STORY-FORMATS.md section 1, growth-engine/DAILY.md section 2

## Week rules

- 7 posts a week: 3 reels, 3 carousels, 1 image (images only for a strong question, a real review quote or an
  announcement).
- No format family or job two days in a row.
- At least 1 contrarian post and 1 B7 (human, trust) post a week.
- A conversion CTA at least every 5 posts.
- Job mix near the stage target. New account: reach 50%, trust 35%, convert 15% (growing 40/40/20, mature 35/40/25).
- At most 1 tier A piece a week; at least 1 story reel a week (`organic.json` week_rules).
- Plan monthly, detail 2 weeks of topics, keep about 20% of slots open for reactive posts.
- StraightScale's calendar is ORGANIC-OS 6.6 template C (in `content-map.json`). STORY-FORMATS 5.1 gives a story-reel
  version of the same week (Monday story reel, Tuesday One Step carousel, and so on).

Source: growth-engine/config/organic.json (week_rules, stage_mix), growth-engine/DAILY.md section 2, growth-engine/ORGANIC-OS.md sections 6.2 and 6.6, clients/straightscale/content-map.json, growth-engine/production/STORY-FORMATS.md section 5.1

## Beliefs and jobs

| Belief | Buyer must hold | Usual job |
|---|---|---|
| B1 | This problem is real, and it is costing me | reach |
| B2 | It isn't my fault; the real cause is X | reach, trust |
| B3 | This can actually be solved | trust, reach |
| B4 | This method is how it gets solved | trust |
| B5 | It's better than the alternatives I know | trust, convert |
| B6 | It works for a business like mine (proof bank only) | convert |
| B7 | I trust and like these people | trust, reach |
| B8 | The next step is easy, safe and worth doing now | convert |

Job metrics: reach = sends per reach (plus follows per 1k reach, skip rate, watch time); trust = saves per reach;
convert = qualified DMs. Metric order: money and conversations first, then follows, then views.

Source: growth-engine/config/organic.json (beliefs, jobs), growth-engine/ORGANIC-OS.md sections 6.1, 6.2, 9.1

## Organic CTA rules

- One ask per post, fitting the card's job: follow, save, send, comment (an answer to a question), keyword, dm, book.
- Keyword CTAs only for a keyword live in the client's brain, with a real resource and a live hub funnel. For
  StraightScale today that is only ANALIZA (funnel `analiza`). PATCHWORK and HARTA may not be used until their flows
  exist.
- "Book" only on convert posts, said as the keyword or DM path ("comment ANALIZA; the booking button comes in the
  DM").
- Never a link, price, discount, guarantee or urgency. Never "we answer within 1 hour".
- Hard offer post (a convert post about the one free offer): about 3% of output; at most 1 a month for a new account.
- StraightScale interim limits: no B8 "what happens in the analysis" post until decision D3; no B6 post without
  permitted proof or The Build series; no behind-the-scenes formats without real footage. See
  [[StraightScale decisions]].

Source: growth-engine/DAILY.md section 2.4, growth-engine/config/organic.json (cta_types, stage_mix note), growth-engine/GATES.md (conversion row), growth-engine/production/STORY-FORMATS.md section 5.2

## Formats

Credits are Higgsfield credits per piece from `organic.json` (with about 25% retakes). STANDARDS 10 prices win where
they differ. Families decide which pipeline steps run ([[Production layer]]).

| Format | Family | Tier | Credits |
|---|---|---|---|
| image_question, image_review_quote (needs proof) | still | C | 1 to 15 |
| carousel_framework, _self_check, _mistakes, _teardown, _comparison, _opinion | still | C | 16 to 33 |
| carousel_bts (real photos) | real | C | 0 to 29 |
| reel_motion (always voiced, motion-reel) | motion | C | 0 to 30 |
| reel_quote_broll (the daily quote reel recipe) | keyframe_reel | C | 25 to 40 |
| reel_bts_real, reel_talking_head_real (owner films) | real | C | 0 to 10 |
| reel_strategist_prop, reel_ugc_pov | ai_video | B | 80 to 200 |
| reel_animation_short | ai_video | B | 70 to 100 |
| reel_story_narrated | ai_video | B | 210 to 445 |
| reel_podcast | ai_video | B | 220 to 320 |
| reel_animation | ai_video | A | 150 to 220 |
| reel_drama_pov | ai_video | A | 180 to 495 |
| reel_song | song | A | 140 to 355 |

Tier A only with `angle_proven: true` or the month's one wildcard. Test new angles cheap (tier C or B) first.

Source: growth-engine/config/organic.json (formats), growth-engine/ORGANIC-OS.md section 7.7

## Story templates

Eight narrative shapes a card can name in `story_template` (full beats in [[Production layer]] and STORY-FORMATS.md):
pov_day (a day in the buyer's life), two_days (same morning, two owners), hidden_villain (the problem is a
character), object_speaks (an object tells its story), overheard (witness line), confession_pov (owner confession;
needs real footage), song_day (song of the buyer's day), podcast_disagreement (two hosts disagree). Animated formats
also name one of four locked looks: claymation, crochet, family_film_3d, storybook_2d.

Source: growth-engine/config/organic.json (story_templates, animation_styles), growth-engine/production/STORY-FORMATS.md section 3

## Agents

All in `.claude/agents/`. Each reads ORGANIC-OS.md, the client's brain.json, content-map.json and learnings first;
none publishes, approves or messages customers.

| Agent | Does | Gate it sets |
|---|---|---|
| organic-director | Approves brain and content map, reviews every batch, Monday memo, changes rules only after 3+ posts confirm a lesson; can veto anywhere | originality, truth, language |
| brain-builder | Fills brain.json and brain.md, owner ramble, demand map, belief ladder; writes "unknown" instead of guessing | blocks on empty required fields |
| research-scout | 3-month outlier mining with the 4 checks, adjacent niches, own-account audit, weekly refresh | none |
| content-strategist | Monthly content map and 2-week slate; writes the Post Cards; picks formats with `route` | map |
| idea-agent | Level-4 narrow idea, Trinity of Value, shock score, $5 test, key visual | idea |
| hook-agent | 10 hooks per post, ships only A or A+ triple hook stack plus 2 trial variants | hook |
| script-agent | Reel scripts through Script Lab with the organic adapter; every reel has a voice | script |
| carousel-agent | Carousels and single images through carousel-machine | visual, sound_off |
| video-producer | Routes reels by format; tier A pieces make 6 derived assets; logs credits | sound_off, visual, budget |
| distribution-agent | Captions, hashtags, trial reel plan, story frames, the hub draft (never as scheduled) | none |
| conversion-agent | Lead magnets, keyword flows, DM qualification; no keyword until its resource and funnel are live | conversion |
| analyst | Scorecard at 72 h and 7 d, outlier and template flags, diagnosis, proposed lessons | none |
| visual-planner, prompt-reviewer, visual-reviewer, take-reviewer | Shot Specs and the fresh reviews: see [[Production layer]] | production gates |

Source: .claude/agents/*.md, growth-engine/ORGANIC-OS.md section 10

## Gates before Matan's approval

Card gates (owner in brackets): map (Strategist), idea (Idea Agent), hook (Hook Agent), script (Script Agent),
sound_off (Producer), visual (Producer plus fresh reviewers; every ledger gate PASS), originality (Director), truth
(Director), conversion (Conversion Agent), language (Director: non-English flagged for a native read), budget
(Producer), human (Matan approves on the hub's Content page).

Director batch review per post: is every gate in `pipeline.py status` passed; will the right buyer stop; which
belief moves one step; would an owner send it to a partner; is it the best version on Instagram; is every claim in
the brain; does the CTA follow from the payoff. Then for the batch: `week-check` passes, a contrarian and a B7 post
exist, the mix is near target.

Source: growth-engine/GATES.md

## Budgets

- Each client has a **monthly Higgsfield credit cap** in `clients/<slug>/brain.json` (`monthly_credit_cap`).
  StraightScale: 1,300.
- Keep a 25% retake buffer. Before every batch check `organic.py ledger <slug>` and the live Higgsfield balance
  (credits are shared across sessions). Log every piece with `organic.py ledger-add`. The production gate G-BUDGET
  enforces it ([[Production layer]]).
- If the budget can't cover a card's format, re-route to tier C and say so.
- Kill rule: a premium format under the account median on its job metric 3 times in a row pauses for 60 days.
- Package defaults per month (ORGANIC-OS 7.7, estimates): Gold 8 videos about 700 to 800 credits; Diamond 16 videos
  about 1,700 to 2,000; StraightScale own account about 1,200 to 1,400. 1 credit is about $0.05 on auto-refill and
  about $0.033 inside the Ultra plan (as written 15 Oct).
- ElevenLabs credits are outside the cap (STORY-FORMATS 5.6).
- StraightScale brand kit weekly line: carousels up to 30 Higgsfield credits a week. A carousel now costs about 13
  at its floor, so 3 a week is 39: an open owner question in the 16 Oct approval queue. Current answer unknown.

Source: clients/straightscale/brain.json (monthly_credit_cap), growth-engine/DAILY.md section 3 (Budget), growth-engine/ORGANIC-OS.md section 7.7, growth-engine/production/STORY-FORMATS.md section 5.6, clients/straightscale/brand-kit.md, growth-engine/production/queue/2026-10-16.md

## Tools

`python3 growth-engine/tools/organic.py ...` (exit code 1 on a blocking fail):
- `brain-check <slug> [--write]`: brain schema, blocking fields, gaps report.
- `card-check <slug> <card|dir>`, `week-check <slug> <dir|cards>`, `route <slug> <card> [--prev-family F]`.
- `ledger <slug> [--month YYYY-MM]`, `ledger-add <slug> --post ID --format F --credits N ...`.
- `outliers <dataset.json> [--days 90]`, `score <slug> [--write]`.

`python3 growth-engine/tools/hub.py ...`: `ping`, `clients`, `client <slug>`, `items`, `upload`, `push <item.json>`,
`funnel <slug> <funnel.json>`, `results <slug>`. Needs the studio token from the hub's Settings, kept as a cloud
environment secret; never print or paste it.

`python3 growth-engine/tools/brain_note.py <slug> [--title <Client name>] [--check]`: rewrites the "Profile
(generated)" section of the client's note in this vault (`brain/Clients/<Title>/<Title>.md`) from
`clients/<slug>/brain.json`, only between its markers; keys that look like secrets are left out. `--check` writes
nothing and exits 1 when the note is out of date. Tests: `python3 -m unittest growth-engine/tools/test_brain_note.py`.

Source: growth-engine/tools/organic.py --help, growth-engine/tools/hub.py (docstring), growth-engine/tools/brain_note.py (docstring), .claude/skills/growth-engine/SKILL.md (Access check)

## Safety rules

Nothing is posted until a person approves it (and the business has Auto-publish on). No invented facts, numbers,
reviews, clients or results. Non-English copy is flagged for a native read. Secrets live in the hub Settings or the
cloud environment's secrets. Full list: [[Standing rules]].

Source: growth-engine/PLAN.md (Safety rules), growth-engine/ORGANIC-OS.md section 14

## Open or unknown

- Meta permissions for publishing and insights were "App Review in progress" or "to add" as of 14 Oct; current
  status not in the repo files I read. Insights for the Learn loop wait on decision D6.
- The StraightScale baseline is empty; the first 6 posts set it (STORY-FORMATS 5.7).
- Whether the daily scheduled task is still active cannot be confirmed from the repo.

Source: growth-engine/PLAN.md, growth-engine/production/STORY-FORMATS.md section 5.7, clients/straightscale/brain.json (decisions_open)

## Related

[[Production layer]] · [[Motion Studio]] · [[Social Agent hub]] · [[StraightScale]] · [[StraightScale content log]] ·
[[Client brain template]] · [[How Claude uses this brain]]
