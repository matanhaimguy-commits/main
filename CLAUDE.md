# Repo guide

- **Shared memory (read first)**: the owner's Obsidian vault, repo `matanhaimguy-commits/brain`, cloned at
  `/home/user/brain` (if missing: `add_repo` owner `matanhaimguy-commits` repo `brain`, then clone it there; it syncs
  with Obsidian Git). Agency work lives in its `Agency OS/` folder: start with `Agency OS/00 Agency OS.md`, then the
  client's note; at the end, add an entry to `Agency OS/Log/`, update the client's content log and decisions, commit
  and push the vault (`main`, never force). Client facts change only in `clients/<slug>/brain.json` here (regenerate
  the note with `growth-engine/tools/brain_note.py <slug>`). The rest of the vault (`HOME.md`) is the READYMERCE
  brand-building system. Never put a token or key in a note.
- **Video work** (reels, launch videos, explainers, ads, motion graphics, B-roll, any client video): use the
  `motion-reel` skill. It is the A-to-Z workflow; it starts with `bash motion-studio/setup.sh` and reads
  `motion-studio/knowledge/README.md`. House rules: `motion-studio/CLAUDE.md`. Client projects live in
  `motion-studio/projects/<client>-<piece>/`.
- **Reference bank** of proven viral reels with breakdown cards and a per-client usage ledger (so films never
  repeat): `motion-studio/refbank/` (`refbank/tools/refbank.py pick|search|check|log`).
- **Building an automated reel machine** on top of this: read `motion-studio/HANDOFF.md` first.
- `references/` holds five complete reference repos (HyperFrames, onetake, gbro-collage-broll,
  claude-animation-base, lemo-opuscar), gitignored and downloaded by `bash references/fetch.sh`.
- **Content for clients** (weekly posts, competitor research, carousels and reels as a series, "what should X post"):
  use the `growth-engine` skill. Strategy spec (what to make, for whom, why): `growth-engine/ORGANIC-OS.md`, with its
  agents in `.claude/agents/` and checks in `growth-engine/tools/organic.py`. Plan: `growth-engine/PLAN.md`. One folder per client: `clients/<slug>/`. Finished posts
  go to the hub (the app's Content page) as drafts with `growth-engine/tools/hub.py`; nothing is posted without approval.
- **Production layer** (how every image, carousel and video for those posts is made and checked):
  `growth-engine/production/`; read its `README.md` first. Every Higgsfield and ElevenLabs generation is gated by the
  hook `.claude/hooks/generation_gate.py` (runs and gates: `growth-engine/tools/pipeline.py`); every number comes from
  `STANDARDS.md`; story reels follow `STORY-FORMATS.md`.
  Atlas Cloud runs only through the gated `atlas` command (`growth-engine/tools/atlas/README.md`; install: `bash growth-engine/tools/atlas/setup.sh`).
- **Instagram / Facebook automation** (comment-to-DM funnels, AI sales DMs, for us and clients): the hosted app
  is `lovable-app/` (a Lovable project; read `lovable-app/README.md`). It is pushed to the Lovable project's own
  GitHub repo, which deploys it; businesses are edited in its dashboard. `social-agent/` is the original
  Node/Railway version the engine was ported from. Never commit tokens.
- **StraightScale website** (straightscale.com): its own repo `matanhaimguy-commits/straight-scale` (if missing:
  `add_repo` it with push access and clone it to `/home/user/straight-scale`), synced with the Lovable project
  "StraightScale Homepage". Read its `AGENTS.md` first; commits to `main` sync into Lovable, so never force-push,
  rebase or amend there. The plan is `Agency OS/Projects/Website plan 2026-10.md` in the vault. Never publish without
  the owner.
- Other folders: `Mark AI/` (product research), `openmontage-work/` and `straightscale-reel/` (earlier video
  experiments, see `motion-studio/knowledge/our-pipeline.md`).
- **Code structure (owner rule, 27 Oct 2026)**: never one large, long file. One small main file (a page, an entry point,
  a CLI dispatcher) that only wires things together, and each function or component in its own file, so every part is
  easy to control, edit and manage: one responsibility per file, short files, clear names, tests per module. When a
  file you touch has grown long, split it as part of the change.
