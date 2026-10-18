---
type: template
updated: 2026-10-18
tags: [template, client, onboarding]
---

# Client brain template

A fill-in client note with the same sections as [[StraightScale]]. Each section is empty and has one line saying what
goes in it. Rules that hold for every client: [[Standing rules]]. Back to [[00 Index]].

**How to use it**

1. Make the folder `Clients/<Client name>/` in this vault and copy this note into it as `<Client name>.md`. If you
   insert it with Obsidian's Templates plugin, `{{title}}` below becomes the note's title; otherwise replace it by
   hand. Links to the client's own notes are written in code here, for example
   `[[{{title}} decisions]]`, so this template has no broken links; remove the backticks when you fill the note.
2. Set the frontmatter to `type: client`, `updated:` today's date, `tags: [client, <slug>]`, and delete this
   "How to use it" block.
3. Make two more notes beside it: `<Client name> decisions` (open questions for the owner, from `decisions_open`) and
   `<Client name> content log` (every post, its status and QA history). Shape them like [[StraightScale decisions]]
   and [[StraightScale content log]].
4. Fill each section from the client's files only. Write "unknown: <what is missing>" where a fact is not known. Never
   paste a token, key, password or personal phone number here; say where it lives instead (hub Settings, Lovable
   Cloud Secrets, cloud environment secrets).

**What the automated runs read.** The daily run and the weekly cycle read `clients/<slug>/brain.json` (checked
against `growth-engine/schemas/brain.schema.json` by `python3 growth-engine/tools/organic.py brain-check <slug>`), plus
`brand-kit.md` and `content-map.json`. They do not read this note. This note is the plain-words summary for people and
for a fresh session; when it and brain.json disagree, brain.json wins and this note gets fixed.

Source: growth-engine/schemas/brain.schema.json, growth-engine/DAILY.md (section 2), .claude/agents/brain-builder.md,
growth-engine/ORGANIC-OS.md (section 4)

---

# {{title}}

One paragraph: who the client is, their hub business id (the slug), what stage the account is in, and links to
`[[{{title}} decisions]]`, `[[{{title}} content log]]`, [[Standing rules]] and [[00 Index]]. Say where brain.json is and
when the next 90-day refresh is due (`refresh_due`).

Source:

## Where the files live

A table of what sits under `clients/<slug>/`: `brain.json`, `brain.md`, `brain-gaps.md`, `brand-kit.md`,
`style-bible.md`, `brand/` (real logo files), `content-map.json` and `.md`, `cards/`, `content/<key>/`, `reviews/`,
`research/` (with `demand-map.csv`), `competitors.md`, `plans/`, `ledger.csv`, `runs/`, `results-log.md`,
`analytics/`. Only list what exists.

Source:

## What they sell

What the business sells, price notes (never quoted in posts), margin and capacity if known, and the sales process.
brain.json field: `business_model`.

Source:

## The rule of three ones

The one offer content points to, the one path a viewer takes (keyword, DM, booking) and the one metric that counts.
brain.json field: `offer`; brand kit section "The rule of three ones".

Source:

## Avatar AV-01 and buyer words

Each avatar (1 to 3): role, situation, what keeps them up, their exact words, what they tried, false beliefs,
desires, fears, identity; then the demand map summary (20 to 40 buyer phrases tagged direct / bridge / off_map).
brain.json fields: `avatars`, `demand_map_file`, `awareness`.

Source:

## Mechanism and beliefs

The problem name (UMP), the solution name (UMS) and its steps, the big idea, the contrast line; the 8 beliefs B1 to B8
with each one's state (held, not_held, unknown); the contrarian vault (positions with their source).
brain.json fields: `mechanism`, `belief_ladder`, `contrarian_vault`.

Source:

## Voice and language

Three adjectives, real samples, banned words, the language and register (for example "ti" or "ju").
brain.json fields: `voice`, `market.language`.

Source:

## Facts we may use in content

Only facts from the proof bank, each with its permission (yes, no, pending, internal_only). If the proof bank is
empty, say so plainly: no numbers, results, names or reviews until the owner adds them with permission.
brain.json field: `proof_bank`.

Source:

## Never

What the client cannot say or will not show (claims, prices, guarantees, words), on top of the [[Standing rules]].
brain.json fields: `constraints.cannot_say`, `constraints.will_not_show`, `voice.banned`.

Source:

## Visual identity

Colours, fonts, the real logo files (a model never draws a logo), face choice (real person, AI character, faceless,
mixed), AI label rule, whether real footage exists, the set and the recurring object, the style bible.
brain.json field: `visual`.

Source:

## Accounts and cadence

Platforms and handles, who approves and the turnaround, posts per week and the format mix, posting times, account
stage, whether a daily run or scheduled task covers this client, whether auto-publish is on in the hub.
brain.json fields: `package`, `constraints.approver`, `constraints.turnaround_hours`, `market` (country, city,
timezone, events).

Source:

## Budget

The monthly Higgsfield credit cap, the weekly studio budget from the brand kit, and what has been spent so far
(from `ledger.csv`). brain.json field: `package.monthly_credit_cap`.

Source:

## Keyword funnels

A table of each keyword, what it gives, whether it is live, and its hub funnel id. Only live keywords may appear in a
post. brain.json field: `lead_magnets`.

Source:

## Content strategy now

The current theme, pillars, series in the lab, and the latest research findings, with the content map's approval
status. Files: `content-map.json`, `content-map.md`, `research/`.

Source:

## Still unknown

Every gap from `brain-gaps.md` and every field marked "unknown". Open owner decisions go to `[[{{title}} decisions]]`.
brain.json field: `decisions_open`.

Source:

## Keeping this note true

When brain.json, brand-kit.md or a decision changes, update this note and `[[{{title}} decisions]]` in the same
session, and say what changed in that day's log note (for example [[Log 2026-10-18]]). After every brain.json
change run `python3 growth-engine/tools/brain_note.py <slug> --title <Client name>`; it rewrites only the text between
the markers below.

Source: growth-engine/tools/brain_note.py (docstring)

## Profile (generated)

<!-- generated:start -->
<!-- generated:end -->

## Notes from the owner

The owner writes here. Claude reads this section and never edits, moves or deletes it.

---

## Onboarding checklist (Brain Builder)

Run by the brain-builder agent when a client is onboarded, and again at each 90-day refresh.

- [ ] Gather the inputs: questionnaire, meeting notes, brand docs, sales calls, DMs and comments in the hub inbox.
- [ ] Get the owner ramble: a 15 to 20 minute voice note; transcribe it and pull themes, positions, stories and real
      phrases.
- [ ] Read `growth-engine/ORGANIC-OS.md`, then the client's `brain.json`, `content-map.json` and
      `analytics/learnings.md` if they exist.
- [ ] Fill `clients/<slug>/brain.json` against `growth-engine/schemas/brain.schema.json` and keep `brain.md` in sync.
- [ ] Build `research/demand-map.csv`: 20 to 40 buyer phrases tagged direct / bridge / off_map, each with its source.
- [ ] Never guess a field: write "unknown: <what is missing>" and add it to `decisions_open` when the owner must
      decide.
- [ ] Run `python3 growth-engine/tools/organic.py brain-check <slug> --write` (it writes `brain-gaps.md`) and stop on
      blocking errors.
- [ ] Facts only from the brain and its proof bank; no em dashes, no hype words.
- [ ] Never publish, approve or message customers: a person approves in the hub.
- [ ] End with a 3-line summary of what was done and what blocks; then fill this note, the decisions note and the
      day's log.

The full first-month timeline (research, content map, conversion setup, first batch) is in ORGANIC-OS section 11;
the client kit steps (hub profile, brand kit, style bible, competitors) are "Step 0" of the growth-engine skill.

Source: .claude/agents/brain-builder.md, growth-engine/ORGANIC-OS.md (sections 4 and 11),
.claude/skills/growth-engine/SKILL.md ("Step 0 · Client kit"), growth-engine/tools/organic.py (brain-check)
