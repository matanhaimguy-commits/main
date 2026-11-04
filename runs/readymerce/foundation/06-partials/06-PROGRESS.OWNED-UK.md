# 06-PROGRESS.OWNED-UK.md

agent_id: VOC-OWNED-UK · STEP 06 HARVEST · SCOPE: OWNED-UK
status: DONE (floors met)

RESUME POINT: url_index=40 (all 40 rank-ordered, diarization-clean calls read; ranks 3 and 5 read and
explicitly zeroed with reason — see 06-HARVEST-LOG.OWNED-UK.md). Ranking CSV
(`datasets/owned-UK-ranking.csv`) has 42 candidate calls total after the source-quality filter; ranks 41–42
(lowest prospect word count, thin content) were not read this session and are the natural next slice if this
harvest is resumed or re-mined. The 80 BLOCKED-FORMAT files (no `[Speaker N]` tags, merged speech) and the
2 excluded files (1 US-number mis-file, 1 unresolved Mike Davison pair) remain unharvested and are named in
the log for orchestrator follow-up.

Records: 72 Q-O (floor 70 met, target 120 not reached) · 40 distinct calls (floor 40 met) · 13 C rows (cap 40).
All 9 scoped tag/CP floors met after the Step 4 tag-augmentation pass (see log).

Files written:
- 06-partials/06-VOC_MASTER.OWNED-UK.csv (renamed from .partial — final)
- 06-partials/06-HARVEST-LOG.OWNED-UK.md
- 06-partials/06-PROGRESS.OWNED-UK.md (this file)
- 06-partials/06-HANDOFF.OWNED-UK.json
- datasets/owned-UK-turns.jsonl
- datasets/owned-UK-ranking.csv

cost_usd: 0.00 (code execution only, no web/tool calls against budget)
