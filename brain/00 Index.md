---
type: index
updated: 2026-10-18
tags: [brain, index, start-here]
---

# 00 Index

This is the shared brain: an Obsidian vault in plain markdown in the `brain/` folder of the repo
`matanhaimguy-commits/main`. Every Claude session reads it at the start of work and adds to it at the end: cloud
sessions, the daily scheduled run and Matan's local Claude with Obsidian. The notes are short summaries that point to
the real files; when a note and a repo file disagree, the repo file wins and the note gets fixed.

Source: CLAUDE.md (repo guide), git remote of this repo

## How to use it

Read [[How Claude uses this brain]] first. In short:

1. Start here, then read [[Standing rules]].
2. For client work, read the client note with its decisions and content log. For other work, read the project note.
3. Read the newest note in `brain/Log/` (today: [[Log 2026-10-18]]).
4. At the end, append an entry to the day's Log note and update the client's content log and decisions.
5. Client facts change only in `clients/<slug>/brain.json`; the client note's generated profile is refreshed with
   `python3 growth-engine/tools/brain_note.py <slug>`.

Source: brain/How Claude uses this brain.md, growth-engine/tools/brain_note.py

## Projects

- [[Social Agent hub]]: the always-on Lovable app that answers Instagram and Facebook comments and DMs, and holds
  the content calendar that approved posts are published from.
- [[Growth Engine]]: the content system for clients: research, plan, Post Cards, the daily run that keeps the hub
  4 days ahead with drafts, the gates and the agents.
- [[Production layer]]: how every image, carousel and video is made and checked: the 16-step gated pipeline, the
  generation hook, the fresh reviewers and STANDARDS.md.
- [[Motion Studio]]: the code-rendered video studio and the `motion-reel` workflow, its engines and the reference
  bank of viral reels.
- [[Mark AI]]: an archived e-commerce product-research run from August 2026; not client work.

## Clients

Today there is one client: [[StraightScale]] (our own agency, Instagram @straightscale_, Albanian).

- [[StraightScale]]: the client brain in plain words (offer, buyer, voice, never-list, look, funnels), plus the
  profile generated from brain.json.
- [[StraightScale decisions]]: every question waiting for Matan, with its interim rule and status.
- [[StraightScale content log]]: every post, its hub status and QA history.

A new client starts from [[Client brain template]].

Source: clients/ (one folder: straightscale)

## Rules and logs

- [[Standing rules]]: secrets, approvals, AI label, real DMs off by default, git, facts only, logos, the generation
  gate, budgets.
- [[How Claude uses this brain]]: start and end steps, where facts live, how to connect Obsidian.
- [[Client brain template]]: the empty client note and the onboarding checklist.
- [[Log 2026-10-18]]: the first daily log (covers 14 to 16 Oct and the brain set-up). New days get a new
  `Log YYYY-MM-DD` note.

## Where things live

| What | Where |
|---|---|
| Repo and working branch | GitHub `matanhaimguy-commits/main`, branch `claude/ig-fb-chatbot-automation-zk8w44` (per `growth-engine/DAILY.md`) |
| Repo guide | `CLAUDE.md` |
| Hub app (running code) | GitHub `matanhaimguy-commits/agent-start-spark`; every push to its `main` deploys to Lovable |
| Hub app (Lovable project) | id `239a3368-f157-4af9-9f3c-129789693927`; published at `https://matan-social-agent.lovable.app` |
| Hub app (mirror in this repo) | `lovable-app/` (read `README.md` and `AGENTS.md`) |
| Original hub version | `social-agent/` (Node/Railway; not the running app) |
| Growth Engine spec, plan, daily run, gates | `growth-engine/ORGANIC-OS.md`, `PLAN.md`, `DAILY.md`, `GATES.md` |
| Growth Engine config, schemas, adapters | `growth-engine/config/organic.json`, `growth-engine/schemas/`, `growth-engine/adapters/` |
| Tools | `growth-engine/tools/` (`organic.py`, `pipeline.py`, `hub.py`, `vqa_crops.py`, `brand_overlay.py`, `fix_drawn_logo.py`, `brain_note.py`) |
| Production rules and numbers | `growth-engine/production/` (start with `README.md`; numbers only in `STANDARDS.md` and `standards.json`) |
| Owner approval queue | `growth-engine/production/queue/<date>.md` |
| Agents, skills, hook | `.claude/agents/`, `.claude/skills/`, `.claude/hooks/generation_gate.py` (wired in `.claude/settings.json`) |
| Client folders | `clients/<slug>/` (StraightScale: `clients/straightscale/`, with `brain.json` as the source of client facts) |
| Video studio | `motion-studio/` (`HANDOFF.md`, `CLAUDE.md`, `refbank/`, `projects/<client>-<piece>/`) |
| Reference repos | `references/` (gitignored; `bash references/fetch.sh`) |
| Earlier video experiments | `openmontage-work/`, `straightscale-reel/` |
| Product research | `Mark AI/` |
| Secrets | Never in the repo or this brain: the hub Settings page, Lovable Cloud Secrets and the cloud environment's secrets |

Source: CLAUDE.md, growth-engine/DAILY.md (intro and section 0), lovable-app/README.md,
lovable-app/docs/APP_REVIEW_RECORDING.md (published address), ls of the repo root

## Notes from the owner

Matan writes here. Claude reads this section and never edits, moves or deletes it.
