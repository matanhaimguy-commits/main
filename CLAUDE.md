# Repo guide

- **Video work** (reels, launch videos, explainers, ads, motion graphics, B-roll, any client video): use the
  `motion-reel` skill. It is the A-to-Z workflow; it starts with `bash motion-studio/setup.sh` and reads
  `motion-studio/knowledge/README.md`. House rules: `motion-studio/CLAUDE.md`. Client projects live in
  `motion-studio/projects/<client>-<piece>/`.
- **Reference bank** of proven viral reels with breakdown cards and a per-client usage ledger (so films never
  repeat): `motion-studio/refbank/` (`refbank/tools/refbank.py pick|search|check|log`).
- **Building an automated reel machine** on top of this: read `motion-studio/HANDOFF.md` first.
- `references/` holds five complete reference repos (HyperFrames, onetake, gbro-collage-broll,
  claude-animation-base, lemo-opuscar), gitignored and downloaded by `bash references/fetch.sh`.
- **Instagram / Facebook automation** (comment-to-DM funnels, AI sales DMs, for us and clients): `social-agent/`.
  Read `social-agent/README.md` and `social-agent/docs/SETUP.md`. One YAML per business in
  `social-agent/businesses/`; run `npm run audit` there after every config change. Never commit tokens.
- Other folders: `Mark AI/` (product research), `openmontage-work/` and `straightscale-reel/` (earlier video
  experiments, see `motion-studio/knowledge/our-pipeline.md`).
