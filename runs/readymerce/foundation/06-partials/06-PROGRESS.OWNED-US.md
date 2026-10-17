# 06 PROGRESS — SCOPE OWNED-US

agent_id: VOC-OWNED-US · started_utc: 2026-09-24T20:30:43Z

RESUME POINT: url_index=46 (of 155 scoped calls, ranked by prospect word count desc in datasets/owned-US-ranking.csv). Ranks 1-46 attempted (44 yielded records, rank3=internal training call skipped, rank22=garbled transcript skipped). Ranks 47-155 (109 calls) not yet read — floors were met at rank 46 inside the time box.

STATUS: DONE (all scoped floors met; box ended before exhausting the corpus, which is expected — RE-MINE can extend later).

Floors (final):
- records: 109/70 (target 120) — MET (short of stretch target 120, not required)
- distinct calls: 44/40 — MET
- objection: 27 records / 24 calls (floor >=20) — MET
- belief: 21 records / 17 calls (floor >=10) — MET
- skepticism: 20 records / 16 calls (floor >=10) — MET
- desire+deeper_hope: 23 records (18+5) (floor >=12) — MET
- spend: 26 records / 21 calls (floor >=10) — MET
- trigger+made_them_act: 13 records (5+8) (floor >=8) — MET
- failed_solution: 18 records / 18 calls (floor >=6) — MET
- scene: 15 records / 13 calls (floor >=8) — MET
- C rows: 16/40 (cap, not floor) — within cap

Outputs written:
- 06-partials/06-VOC_MASTER.OWNED-US.csv (109 Q-O records + 16 C rows, 48 columns, csv.QUOTE_ALL)
- 06-partials/06-HARVEST-LOG.OWNED-US.md (lock card, per-call counter, CHECKPOINTs every 10 calls, C-row table, ledgers, manifest, coverage statement)
- 06-partials/06-PROGRESS.OWNED-US.md (this file)
- 06-partials/06-HANDOFF.OWNED-US.json
- datasets/owned-US-turns.jsonl (14,736 parsed speaker turns, both roles, all 155 files)
- datasets/owned-US-ranking.csv (155 calls ranked by prospect word count)

Weakest link: CP-07 (spouse can't work because of kids) has only 1 record from 1 call in this rank range — under-sampled. A RE-MINE pass over ranks 47-155, or a targeted keyword pass for "my wife/husband can't work" across the full corpus, would close it.

If resuming: read datasets/owned-US-ranking.csv from rank 47 onward, skip any thread_id already present in 06-VOC_MASTER.OWNED-US.csv, continue writing Q-O-#### starting at Q-O-0110.
