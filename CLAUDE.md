# Repo guide

- **Video work** (reels, launch videos, explainers, ads, motion graphics, B-roll, any client video): use the
  `motion-reel` skill. It is the A-to-Z workflow; it starts with `bash motion-studio/setup.sh` and reads
  `motion-studio/knowledge/README.md`. House rules: `motion-studio/CLAUDE.md`. Client projects live in
  `motion-studio/projects/<client>-<piece>/`.
- `references/` holds five complete reference repos (HyperFrames, onetake, gbro-collage-broll,
  claude-animation-base, lemo-opuscar), gitignored and downloaded by `bash references/fetch.sh`.
- **Content for clients** (weekly posts, competitor research, carousels and reels as a series, "what should X post"):
  use the `growth-engine` skill. Plan: `growth-engine/PLAN.md`. One folder per client: `clients/<slug>/`. Finished posts
  go to the hub (the app's Content page) as drafts with `growth-engine/tools/hub.py`; nothing is posted without approval.
- **Instagram / Facebook automation** (comment-to-DM funnels, AI sales DMs, for us and clients): the hosted app
  is `lovable-app/` (a Lovable project; read `lovable-app/README.md`). It is pushed to the Lovable project's own
  GitHub repo, which deploys it; businesses are edited in its dashboard. `social-agent/` is the original
  Node/Railway version the engine was ported from. Never commit tokens.
- Other folders: `Mark AI/` (product research), `openmontage-work/` and `straightscale-reel/` (earlier video
  experiments, see `motion-studio/knowledge/our-pipeline.md`).
