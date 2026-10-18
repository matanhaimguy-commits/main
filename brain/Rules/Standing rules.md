---
type: rules
updated: 2026-10-18
tags: [rules, security, approvals, git, budget, brand]
---

# Standing rules

The rules every Claude session follows in this repo, whatever the task: cloud sessions, the daily scheduled run and
the owner's local Claude. Read them before any work that touches the hub, a client, a generation or git. They are a
summary; the source files under each section are the rule. If this note and a source file disagree, the source file
wins: follow it and fix this note. How to use the brain: [[How Claude uses this brain]]. Back to [[00 Index]].

## 1. Secrets and security

- Never ask for, accept or repeat a token, key or password in chat. If someone pastes one, do not use it or store it;
  say where it belongs instead.
- Secrets live in three places only: the hub's Settings page (stored encrypted), Lovable Cloud Secrets (a secret with
  the same name overrides the Settings value), and the cloud environment's secrets (for example the studio token
  `HUB_TOKEN`, which comes from the hub Settings, Studio token). Point to these places; never copy a value.
- Never commit tokens or keys, in any repo, and never write them into this brain.
- Never print or store tokens. Never print the `app_state` rows `settings` or `tick_target`.
- Never change a business's settings in the hub as part of a content run.

Source: CLAUDE.md, lovable-app/AGENTS.md, lovable-app/README.md ("How it runs"), growth-engine/DAILY.md (section 0),
.claude/skills/growth-engine/SKILL.md ("Access check"), the scheduled task "StraightScale daily content" (its prompt)

## 2. Approvals and publishing

- Nothing is posted without the owner's approval. The owner (Matan) approves on the hub's Content page; the hub's
  publisher then posts approved items at their time.
- Claude never approves and never publishes, and never messages customers.
- Drafts go into the hub as status `draft` only. Never insert or set an item as `scheduled` or `published`.
- Failed items are reported with the reason, never re-approved by Claude.
- Human checkpoints that only the owner closes (STANDARDS 9): G-HUMAN-FINAL on every post (Albanian text marked for a
  native read), G-HUMAN-VOICE once per voice, G-HUMAN-SONG on every song master, G-HUMAN-LOOK once per series,
  G-HUMAN-HOOKBOARD on every hook board, G-HUMAN-ESCALATE after 3 failed attempts or 3 script FIX loops.
  G-HUMAN-SPINE is the one that can be delegated (recorded as `--by "claude (delegated)"` with the reason).
  Claude records an owner checkpoint (`pipeline.py approve ... --by Matan`) only after the owner has given it.
- When a checkpoint is missing, queue it (`pipeline.py ask ...`), say so in the report and let that piece wait.

Source: CLAUDE.md, growth-engine/DAILY.md (intro, sections 1, 3, 4), growth-engine/production/STANDARDS.md (section 9,
"Human checkpoints"), .claude/agents/brain-builder.md, .claude/skills/growth-engine/SKILL.md ("Modes")

## 3. AI disclosure and AI people

- Instagram's own AI label goes on every post with a photoreal AI person, an AI voice speaking as a person (every
  voiced reel) or realistic AI footage, and on slides or images with a photoreal AI person or scene. Stylized
  animation gets it too until the owner decides otherwise (decision D1). The hub draft's notes start with
  "AI label: on" when it applies.
- Until D1 is decided: AI people only from behind, hands only, at a distance, as stylized animation, or as a clearly
  staged scene. An AI person is never presented as a real client or customer and never carries a result.
- An anecdote in the brand's voice is only a clearly framed POV dramatization ("POV: ..."), never stated as fact.

Source: growth-engine/production/STANDARDS.md (section 7), growth-engine/DAILY.md (sections 3 and 4)

## 4. Real DMs are off by default

- The hub's real sending to customers is off by default; everything is a dry run, recorded on the Activity page.
  Sending is real only when it is switched on in Settings and the business is set to Live with no blocking problems.
- Do not change that default in code, and do not switch a business to Live. Whether any business is live today is
  not recorded here: check the hub, do not guess.

Source: lovable-app/AGENTS.md, lovable-app/README.md ("How it runs")

## 5. Git

- Studio work: repo `matanhaimguy-commits/main`, branch `claude/ig-fb-chatbot-automation-zk8w44`. Commit and push
  there.
- The Lovable-connected repo (`matanhaimguy-commits/agent-start-spark`; a copy of the code sits in `lovable-app/`):
  every push to its `main` syncs to Lovable and rebuilds the app. Never force push, rebase, amend or squash commits
  that are already pushed; it rewrites history on Lovable's side and the project history can be lost. Keep the branch
  working: run `npx tsc --noEmit -p .`, `bun run test` and `bun run build` before pushing.
- Hub schema changes go in a new file under `supabase/migrations/` and are applied to the database by hand.
- Never commit tokens (section 1).

Source: growth-engine/DAILY.md (intro), lovable-app/AGENTS.md, lovable-app/README.md (intro, "Changing the database"),
CLAUDE.md

## 6. Facts only

- Client facts come only from the client's brain (`clients/<slug>/brain.json`, `brain.md`) and brand kit
  (`brand-kit.md`), whose source of truth is the hub profile. Never invent numbers, results, client names, reviews,
  testimonials or prices.
- Never guess a brain field: write "unknown: <what is missing>" and add it to `decisions_open` when the owner must
  decide.
- An empty proof bank means no numbers, results, names or reviews in content until the owner adds them with
  permission.
- Keyword calls to action only for keywords live in the brain. No links, prices, discounts, guarantees or urgency in
  posts. Screens in pictures show states, not counts, and no real platform names or logos.
- Writing: plain words, no em dashes, no hype words. Client-specific "never say" lists live in each client note (for
  example [[StraightScale]]).

Source: growth-engine/DAILY.md (sections 2 and 3), .claude/agents/brain-builder.md,
clients/straightscale/brand-kit.md ("Proof bank", "Never"), .claude/skills/growth-engine/SKILL.md ("Step 0")

## 7. Logos and brand material

- Logos only from the client's real files (for StraightScale: `clients/straightscale/brand/` and
  `motion-studio/projects/straightscale-03/assets/brand/`). A model never draws a logo.
- Image prompts leave the logo corner calm and empty; after the review the real logo goes on with
  `python3 growth-engine/tools/brand_overlay.py <in> <out> --client <slug>`.
- Video: real brand material only (official logo file, captured colours and fonts, real product UI); no redrawn logos.

Source: clients/straightscale/brand-kit.md ("Visual identity"), growth-engine/DAILY.md (section 3), motion-studio/CLAUDE.md

## 8. Every generation passes the gate

- Every Higgsfield and ElevenLabs generation goes through the PreToolUse hook `.claude/hooks/generation_gate.py`
  (wired in `.claude/settings.json`). It blocks any call whose prompt, Shot Spec, references and budget have not
  passed their gates. Never work around it.
- A session rooted above the repo runs `bash growth-engine/production/install-gate.sh` first, then proves the gate:
  `generate_image` with the prompt `GATE-SELFTEST` must come back blocked. If it generates instead, stop and say so.
- Generate with exactly the registered prompt and references. Reviewers are fresh agents each time and get only the
  review packet.
- Details: [[Production layer]].

Source: CLAUDE.md, growth-engine/DAILY.md (sections 0 and 3), .claude/settings.json

## 9. Budgets

- The daily run stays within 60 Higgsfield and 1,000 ElevenLabs credits per run.
- Each client has a monthly Higgsfield cap in `brain.json` (StraightScale: 1,300 credits a month). Check it with
  `organic.py ledger <slug>` and the live Higgsfield balance before every batch, keep a 25% retake buffer, and log
  every piece with `organic.py ledger-add`.
- `pipeline.py budget` (gate G-BUDGET) runs before a run's first generation and again within 24 hours of each later
  batch; a video is re-priced in full at step 9. Re-check the balance right before every submit: credits are shared
  with every other session.
- The weekly studio budget per client is in its `brand-kit.md` (StraightScale: Apify research about $0.50, carousels
  up to 30 Higgsfield credits, voiceover only on flagship reels, no paid music).
- If the budget cannot cover a card's format, re-route to a cheaper tier and say so. Stop rather than spend past a
  budget.

Source: the scheduled task "StraightScale daily content" (its prompt; the 60 and 1,000 limits are written there, not
in a repo file), growth-engine/DAILY.md (section 3), growth-engine/production/STANDARDS.md (section 10),
clients/straightscale/brand-kit.md ("Budget per week"), clients/straightscale/brain.md,
.claude/skills/growth-engine/SKILL.md ("Modes")

## Related

[[Social Agent hub]] · [[Growth Engine]] · [[Production layer]] · [[Motion Studio]] · [[Client brain template]]
