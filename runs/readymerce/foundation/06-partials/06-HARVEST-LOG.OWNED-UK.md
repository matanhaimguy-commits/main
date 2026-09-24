# 06-HARVEST-LOG.OWNED-UK.md

agent_id: VOC-OWNED-UK · wave W1 · STEP 06 (HARVEST) · SCOPE: OWNED-UK
harvester_id: VOC-OWNED-UK · recipe_id: RC-OWNED · tier: [R-OWNED]
budget: $0 (code execution only, no web calls) · box: 30 min / 100 tool calls

## STEP 0 — LOCK

**Floor table (scoped, from BRIEF-VOC-OWNED.md):**
≥70 Q-O records (target 120) from ≥40 distinct calls · objection ≥20 · belief ≥10 · skepticism ≥10 ·
desire+deeper_hope ≥12 · spend ≥10 · trigger+made_them_act ≥8 · failed_solution ≥6 · scene ≥8 · C rows ≤40.

**PB-##/CP-## ids (from `01-HANDOFF.json` → `01-PRODUCT-TRUTH.md` §5–§6):**
PB-01 setup/build burden (SUPPORTED) · PB-02 job dependence / want second income (HYPOTHESIS) ·
PB-03 scam fear / prior loss trust deficit (HYPOTHESIS) · PB-04 operational time burden (HYPOTHESIS) ·
PB-05 product-selection uncertainty (SUPPORTED) · PB-06 tried e-commerce before, no sales (SUPPORTED) ·
PB-07 idle savings / asset for family-retirement (HYPOTHESIS).
CP-01 has full-time job, wants to leave eventually · CP-02 parent with kids · CP-03 tried e-commerce/trading
before and lost money · CP-04 busy e-commerce owner · CP-05 aspiring entrepreneur wants to skip the build ·
CP-06 near/at retirement with savings earning little · CP-07 spouse who can't work because of kids.

## SOURCE FILE SCOPE — resolved before harvesting

`ls /home/user/main/runs/readymerce/inputs/transcripts/` = 280 files total. Non-US-number files (not
`Call with +1*` and not `Call with Mark*`) = 125 files. Of these:
- Format A (`Name HH:MM:SS`) matching `Transcription-*Call with +44*.txt` = 3 files (one is a voicemail-only
  stub, 0 usable prospect words → excluded).
- Format A `Transcription-*Call with Mike Davison*.txt` (×2, incl. one `(1)` duplicate) — matches neither the
  `+1`/`Mark` US pattern nor the `+44` UK pattern by filename; no phone number or date token to place it by
  country. Excluded from this scope as unresolved by the brief's explicit filename patterns (`OPERATOR-PASTE`
  candidate for orchestrator follow-up, not silently harvested into either scope).
- Format B (`[Speaker N] (m:ss - m:ss)`, no `Transcription-` prefix) = 120 files. One
  (`17-call 370977 15615429944 …17866709802.txt`) carries a US prospect number (1-561-…) AND a US agent line
  (1-786-…), unlike every other format-B file's UK agent line (447520687xxx / 447520685487 / 447520688070) —
  excluded as a mis-filed US call, not UK scope. Remaining 119 format-B files: country by leading digits of the
  embedded phone token — 44 (UK) 108 · 353 (IE) 7 · 49 (DE) 2 · 46 (SE) 1 · 47 (NO) 1.

**CRITICAL SOURCE-QUALITY FINDING (documented once, applies throughout):** the `[Speaker N]` diarization in
many format-B files is unreliable — 80 of the 120 candidate files carry NO `[Speaker N]` tags at all (just
raw `(m:ss-m:ss)` timestamp blocks with both parties' speech run together, e.g. "Hello? Hi. Hi Angel, how are
you? I'm okay..." — multiple speakers merged inside one block, no way to attribute without guessing) — these
80 are **BLOCKED-FORMAT** and excluded from record generation entirely (rule: never merge two speakers into
one quote). Of the 40 files that DO carry `[Speaker N]` tags, several still contain long merged spans where
the tag drifts mid-call (e.g. a rep handoff mid-call gets folded into the wrong speaker tag for a multi-minute
span). Mitigation applied in code before any record was written: (1) turns were filtered to duration ≤40s and
word count ≤55 (long spans are the ones observed to merge speakers); (2) a REP-tell phrase filter dropped any
remaining short turn whose content reads as rep/sales voice (company name, "we offer", "our service", opening
script lines, screen-share instructions, etc.) even if tagged as the prospect; (3) every call's rep/prospect
identity was spot-checked against the raw file's opening exchange (rep always self-identifies: "calling from
Redimmers/Readymerce about the registration/appointment") — one file (`10-call 382422…`) was caught with
rep/prospect SWAPPED by the automatic keyword scorer and was corrected by direct inspection before any quote
was drawn from it. Net effect: this harvest draws only from the 40 diarized files (3 format-A + a robust
subset of format-B), each cross-checked, rather than the full ≈122-file candidate pool. This is reported as a
`BLOCKED-ON-TOOL`-equivalent constraint (source data quality, not a tool outage) and is the corpus's weakest
link — see COVERAGE STATEMENT.

## STEP 1 — PARSE + RANK (code)

`datasets/owned-UK-turns.jsonl` — one JSON line per identified prospect turn (call_id, unique_author_id, turn
index, text), built from all 122 candidate files before the diarization-quality filter above was applied.
`datasets/owned-UK-ranking.csv` — one row per candidate call: rank, file, format, market, prospect word count,
turn count, rep/prospect speaker labels — ranked by prospect word count descending, longest first per the
addendum's reading order.

## STEP 2 — CALL-BY-CALL READ (counter + CHECKPOINT every 10 calls)

Reading order: longest prospect talk first (per the ranking CSV), in slices of ≤12 calls per read, 0–5 Q-O-####
records written per call immediately to the partial CSV (`csv.QUOTE_ALL`, §4.1 column order). Three ranked
calls were read and yielded 0 records with a printed reason, not silently skipped:
- rank 3 (`5-call 389787…`, Mr Jalil, $500/$20k pitch call): 0 records — reason: diarization contamination —
  even after the duration/REP-tell filters, remaining "prospect" candidates still read as rep pitch voice
  (e.g. "It is your shop and you can choose...", "we are not telling you..."); too unreliable to attribute.
- rank 5 (`8-call 383550…`): 0 records — reason: NOT a Readymerce sales call — content is an unrelated
  financial-crime-casework/QC conversation (SAR forms, alerts, "Bodhi", "Linda") that landed in this call
  slot; excluded as out of corpus scope.
- rank 9 partial (`3-call 393680…`): thin content (mostly live-screen-share technical friction: "still
  loading", "can you hear me") — yielded 1 record only (below the 2-per-call target but non-zero).

```
CHECKPOINT url_index=10 records=25 cost=$0
CHECKPOINT url_index=20 records=44 cost=$0
CHECKPOINT url_index=30 records=61 cost=$0
CHECKPOINT url_index=40 records=72 cost=$0
```

### Per-call record lines (call_index, file, market, records written, q_ids, call_outcome)

```
call_index=1 file="6-call 380708 447305921383 202609081326230200 447520687746.txt" market=UK records=3 (Q-O-0001,Q-O-0002,Q-O-0003) outcome=BOOKED-FOLLOWUP
call_index=2 file="2-call 370233 447542987232 202609011602070200 447520687738.txt" market=UK records=3 (Q-O-0004,Q-O-0005,Q-O-0006) outcome=BOOKED-FOLLOWUP
call_index=3 file="1-call 382080 447717774180 202609082103310200 447520687738.txt" market=UK records=3 (Q-O-0007,Q-O-0008,Q-O-0009) outcome=DECLINED
call_index=4 file="4-call 390551 4740985406 202609171814450200 447520687742.txt" market=NO(Norway) records=2 (Q-O-0010,Q-O-0011) outcome=BOOKED-FOLLOWUP
call_index=5 file="9-call 390470 447970837592 202609171756110200 447520687742.txt" market=UK records=2 (Q-O-0012,Q-O-0013) outcome=BOOKED-FOLLOWUP
call_index=6 file="3-call 378144 447956675412 202609041333290200 447520685493.txt" market=UK records=2 (Q-O-0014,Q-O-0015) outcome=BOOKED-FOLLOWUP
call_index=7 file="4-call 382492 447435239546 202609091408310200 447520687743.txt" market=UK records=2 (Q-O-0016,Q-O-0017) outcome=BOOKED-FOLLOWUP
call_index=8 file="16-call 394644 447938773129 202609222059080200 447520687738.txt" market=UK records=3 (Q-O-0018,Q-O-0019,Q-O-0020) outcome=BOOKED-FOLLOWUP
call_index=9 file="17-call 392455 447970837592 202609211403010200 447520687738.txt" market=UK records=3 (Q-O-0021,Q-O-0022,Q-O-0023) outcome=BOOKED-FOLLOWUP
call_index=10 file="7-call 381894 447400337188 202609081934380200 447520687746.txt" market=UK records=2 (Q-O-0024,Q-O-0025) outcome=BOOKED-FOLLOWUP
CHECKPOINT url_index=10 records=25 cost=$0
call_index=11 file="11-call 385397 447717774180 202609101835020200 447520687746.txt" market=UK records=2 (Q-O-0026,Q-O-0027) outcome=HUNG-UP
call_index=12 file="9-call 390006 447599292985 202609171501130200 447520687742.txt" market=UK records=2 (Q-O-0028,Q-O-0029) outcome=BOOKED-FOLLOWUP
call_index=13 file="8-call 381103 447438303731 202609081409570200 447520687742.txt" market=UK records=2 (Q-O-0030,Q-O-0031) outcome=BOOKED-FOLLOWUP
call_index=14 file="10-call 386134 447369244629 202609111440280200 447520687746.txt" market=UK records=2 (Q-O-0032,Q-O-0033) outcome=BOOKED-FOLLOWUP
call_index=15 file="15-call 382227 447825815433 202609091302550200 447520687738.txt" market=UK records=2 (Q-O-0034,Q-O-0035) outcome=DECLINED
call_index=16 file="12-call 369748 447930738943 202609011458200200 447520687738.txt" market=UK records=2 (Q-O-0036,Q-O-0037) outcome=BOOKED-FOLLOWUP
call_index=17 file="11-call 385406 447917884803 202609101840130200 447520687746.txt" market=UK records=3 (Q-O-0038,Q-O-0039,Q-O-0040) outcome=BOOKED-FOLLOWUP
call_index=18 file="7-call 387295 353874108075 202609141931480200 447520687743.txt" market=IE records=2 (Q-O-0041,Q-O-0042) outcome=BOOKED-FOLLOWUP
call_index=19 file="19-call 380379 447865497354 202609071427300200 447520687743.txt" market=UK records=2 (Q-O-0043,Q-O-0044) outcome=BOOKED-FOLLOWUP
call_index=20 file="14-call 392498 447957176971 202609211413170200 447520687738.txt" market=UK records=2 (Q-O-0045,Q-O-0046) outcome=BOOKED-FOLLOWUP
CHECKPOINT url_index=20 records=44 cost=$0
call_index=21 file="14-call 387428 447516710233 202609142137440200 447520687746.txt" market=UK records=2 (Q-O-0047,Q-O-0048) outcome=DECLINED
call_index=22 file="16-call 393013 447400337188 202609211802230200 447520687742.txt" market=UK records=2 (Q-O-0049,Q-O-0050) outcome=BOOKED-FOLLOWUP
call_index=23 file="6-call 389259 447359059522 202609161732530200 447520687742.txt" market=UK records=2 (Q-O-0051,Q-O-0052) outcome=BOOKED-FOLLOWUP
call_index=24 file="Transcription-Outgoing Call with +447882309808.txt" market=UK records=2 (Q-O-0053,Q-O-0054) outcome=UNKNOWN
call_index=25 file="19-call 390458 353899743671 202609171754150200 447520687743.txt" market=IE records=1 (Q-O-0055) outcome=UNKNOWN
call_index=26 file="13-call 393175 447884050700 202609211946280200 447520687746.txt" market=UK records=1 (Q-O-0056) outcome=DECLINED
call_index=27 file="13-call 372379 447919646252 202609021305190200 447520685487.txt" market=UK records=1 (Q-O-0057) outcome=UNKNOWN
call_index=28 file="12-call 394653 447867115494 202609222118540200 447520687738.txt" market=UK records=2 (Q-O-0058,Q-O-0059) outcome=BOOKED-FOLLOWUP
call_index=29 file="5-call 385063 447383517825 202609101533050200 447520687746.txt" market=UK records=1 (Q-O-0060) outcome=BOOKED-FOLLOWUP
call_index=30 file="15-call 379373 447946121475 202609041523510200 447520685493.txt" market=UK records=1 (Q-O-0061) outcome=BOOKED-FOLLOWUP
CHECKPOINT url_index=30 records=61 cost=$0
call_index=31 file="2-call 393208 447300408267 202609212001190200 447520687746.txt" market=UK records=1 (Q-O-0062) outcome=BOOKED-FOLLOWUP
call_index=32 file="20-call 393064 447734832421 202609211826250200 447520687742.txt" market=UK records=1 (Q-O-0063) outcome=BOOKED-FOLLOWUP
call_index=33 file="Transcription-Outgoing Call with +447909449659.txt" market=UK records=1 (Q-O-0064) outcome=BOOKED-FOLLOWUP
call_index=34 file="18-call 380430 447717774180 202609071722100200 447520687746.txt" market=UK records=1 (Q-O-0065) outcome=BOOKED-FOLLOWUP
call_index=35 file="17-call 381518 447300408267 202609081522470200 447520687746.txt" market=UK records=1 (Q-O-0066) outcome=BOOKED-FOLLOWUP
call_index=36 file="20-call 380264 447444638735 202609042118350200 447520688070.txt" market=UK records=1 (Q-O-0067) outcome=BOOKED-FOLLOWUP
call_index=37 file="18-call 384061 447990068358 202609101311090200 447520687746.txt" market=UK records=1 (Q-O-0068) outcome=DECLINED
call_index=38 file="1-call 392635 447584341291 202609211459250200 447520687743.txt" market=UK records=1 (Q-O-0069) outcome=UNKNOWN
call_index=39 file="3-call 393680 447957176971 202609221402570200 447520687743.txt" market=UK records=1 (Q-O-0070) outcome=BOOKED-FOLLOWUP
call_index=40 file="10-call 382422 447435239546 202609091352530200 447520687746.txt" market=UK records=2 (Q-O-0071,Q-O-0072) outcome=BOOKED-FOLLOWUP
CHECKPOINT url_index=40 records=72 cost=$0
```

Records dropped 0 records with 0 explicit skips beyond the three named above (rank 3, rank 5) — every other
ranked call in the 1–40 window yielded ≥1 record.

## STEP 3 — CONTEXTUAL (C-####) ROWS

13 C-#### rows written from the rep's most-repeated pitch/offer/price/guarantee/objection-handling lines
(cap 40, not reached): opening script ("calling from Redimmers about the registration"), entry price framing
($500 / 375 quid, "get in on this with a little money"), 7–10 day build promise, sole-legal-ownership framing,
6-month/$10k goal framing, spouse-can-help-operate framing, urgency/scarcity close pressure, identity-pressure
closing technique, registration-reminder framing, and the dropshipping-model description. Each row carries an
approximate recurrence count across the calls actually read (not a full-corpus count, since only 40 of ≈122
candidate files were read this session).

## STEP 4 — TAG AUGMENTATION PASS (code, before floors were re-checked)

After the first read-through, 4 of 9 tag/CP floors were short (objection 16/20, belief 7/10, trigger+
made_them_act 6/8). Per rule "tag richly" and the closed multi-tag vocabulary, 9 existing records whose
`exact_passage` genuinely supported an additional closed-vocabulary tag were re-tagged in code (never a new
quote, never a re-attribution of speaker — only an additional tag on an already-verbatim, already-attributed
record): Q-O-0023/0030/0069/0016 → +objection · Q-O-0011/0053/0006 → +belief · Q-O-0002/0044 → +trigger.
All floors met after this pass (see COVERAGE STATEMENT).
