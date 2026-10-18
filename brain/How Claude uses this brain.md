---
type: guide
updated: 2026-10-18
tags: [brain, howto, obsidian, sessions, memory]
---

# How Claude uses this brain

This vault is the shared memory for every Claude session that works for us: cloud sessions, the daily scheduled run
and Matan's local Claude with Obsidian. It is plain markdown in the `brain/` folder of the repo
`matanhaimguy-commits/main`, so every session that clones the repo already has it. The notes summarise and link to
the real files; the files are the rule. Back to [[00 Index]].

## 1. At the start of every session

Read these, in this order, before any work:

1. [[00 Index]]: what exists and where.
2. [[Standing rules]]: secrets, approvals, AI label, git, budget.
3. The client note for the client in question, for example [[StraightScale]], with its [[StraightScale decisions]]
   and [[StraightScale content log]]. For work that is not about a client, read the project note instead
   ([[Social Agent hub]], [[Growth Engine]], [[Production layer]], [[Motion Studio]], [[Mark AI]]).
4. The newest Log note in `brain/Log/` (the file names sort by date; today that is [[Log 2026-10-18]]).

Then open the source files the notes point to ("Source:" lines) before acting on them. If a note and a source file
disagree, the source file wins: follow it and fix the note.

Source: this vault's layout; CLAUDE.md (repo guide)

## 2. At the end of every session

1. **Append** a short entry to the Log note for the day, `brain/Log/Log YYYY-MM-DD.md`. Create the file if it does
   not exist yet (same frontmatter and headings as [[Log 2026-10-18]]). Never rewrite or delete another session's
   entry. One entry has four lines:
   - **Did:** what was done, with the files or commits.
   - **Waits for the owner:** each decision or check only Matan can close, and where it is queued.
   - **Spend:** Higgsfield credits, ElevenLabs credits and minutes, or "none". The real figures go in
     `clients/<slug>/ledger.csv`; the log only repeats them.
   - **Decisions taken:** by whom (Matan, the Organic Director, Claude), or "none".
2. Update the client's content log note (for StraightScale, [[StraightScale content log]]) when a post was made,
   changed, reviewed, approved, rejected or posted.
3. Update the client's decisions note (for StraightScale, [[StraightScale decisions]]) when a question was asked,
   answered or dropped.
4. Commit and push `brain/` with the rest of the work (see section 6).

Source: growth-engine/DAILY.md (the run's summary), growth-engine/production/README.md ("Who decides what"),
clients/straightscale/ledger.csv

## 3. Where facts live (one place each)

- **Client facts** (offer, audience, what may and may not be said, keywords, credit cap, open decisions) change only
  in `clients/<slug>/brain.json`. That is the machine source the pipelines check (`organic.py brain-check`,
  `card-check`). Never edit a client fact in the client note by hand.
- The client note (for example [[StraightScale]]) is regenerated from brain.json with the `brain_note.py` tool (see
  [[Growth Engine]]). Run it after every brain.json change, then `organic.py brain-check <slug>`.
- **Notes from the owner:** Matan's free notes go under a heading `## Notes from the owner` in any note. Claude reads
  them, never edits, moves or deletes them, and a regenerated note keeps that section word for word. If an owner note
  holds a new client fact, Claude asks him and, once he confirms, puts it in brain.json.
- **Numbers** for production (models, durations, loudness, safe zones, pass rules, prices) live only in
  `growth-engine/production/STANDARDS.md` and `standards.json`. Notes cite the section, they do not copy the number
  as a rule.
- **Secrets** never enter the brain. They live in the hub's Settings page, Lovable Cloud Secrets and the cloud
  environment's secrets. See [[Standing rules]].

Source: clients/straightscale/brain.json, growth-engine/tools/organic.py, growth-engine/production/README.md,
growth-engine/DAILY.md (section 0)

## 4. Writing a note

- YAML frontmatter with `type`, `updated` (the date) and `tags`.
- Link with `[[Exact note title]]`. Titles are file names without `.md`; keep them unique in the vault.
- Short sections, plain words, no em dashes, no hype. A "Source: path" line under each section.
- Facts only from repo files. Unknown or undecided things are written as "unknown" or "not decided", never guessed.
- A new client starts by copying [[Client brain template]] to `brain/Clients/<Name>/`.

Source: this vault's conventions

## 5. Connecting the vault to Obsidian (for Matan)

**Option A: open it as its own vault.**
1. Clone the repo: `git clone https://github.com/matanhaimguy-commits/main`. The work is pushed to the branch named
   in `growth-engine/DAILY.md` (on 18 Oct: `claude/ig-fb-chatbot-automation-zk8w44`), so check out that branch until
   it is merged: `git checkout claude/ig-fb-chatbot-automation-zk8w44`.
2. In Obsidian: Open folder as vault, and pick the `brain/` folder inside the clone.
3. Install the community plugin **Obsidian Git**. Turn on pull on startup, auto pull every few minutes (for example
   5) and auto commit-and-sync (commit and push) every few minutes. If the plugin does not find the repo from the
   `brain/` folder, open the whole clone as the vault instead and work in its `brain/` folder.

**Option B: add it to the vault you already use.**
1. Put a clone of the repo inside the existing vault folder. To get only the brain and not the code:
   `git clone --filter=blob:none --sparse https://github.com/matanhaimguy-commits/main`, then inside it
   `git sparse-checkout set brain` and check out the branch above.
2. Install Obsidian Git in that vault, set its custom base path (Git repository path) to the clone's folder, and
   set auto pull and auto commit-and-sync to every few minutes, as in option A.
3. Tell your local Claude (the one with the Obsidian memory) to treat the cloned `brain/` folder as this brain and
   to follow sections 1 and 2 of this note. Keep your own private notes outside that folder; anything inside it is
   pushed to GitHub and read by every session.

Signing in to GitHub happens in the computer's git credentials (or GitHub Desktop), never in a note. If Obsidian Git
reports a merge conflict in a Log note, keep both entries.

Where Matan's current Obsidian memory lives is not recorded in the repo, so which option fits is his choice.

Source: growth-engine/DAILY.md (repo and branch), git remote of this repo

## 6. How a cloud session reads and writes it

- The brain is at `brain/` in the clone (in cloud sessions, `/home/user/main/brain/`). No Obsidian is needed: read the
  notes with Read, find a linked note with Glob `brain/**/<title>.md`, search with Grep.
- The daily scheduled run wakes the studio session described in `growth-engine/DAILY.md`; it follows the same start
  and end steps.
- Before writing: `git pull --rebase` on the working branch, so entries from Obsidian and other sessions come in
  first. After writing: commit `brain/` together with the work and push to the same branch. Never force-push.

Source: growth-engine/DAILY.md (intro and section 0), CLAUDE.md

## Notes from the owner
