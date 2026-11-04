# 07-SOPH — MARKET SOPHISTICATION (SOPH half of STEP 07) · Readymerce · US
agent_id: 07-SOPH · wave W2 · MODE: SOPH · started 2026-09-24T21:20Z · box 40 min / 150 calls · budget standard (GetHookd ≤2.0 cr, ≤6 networks, Meta 1 category + ≤3 population keywords)
LOCK CARD: inputs = 02-partials (8 NW handoffs + KEYWORDS handoff, 8 swipe partials, network cards) + 01-HANDOFF.json (PB-##, CP-##). Merged 02-swipe.csv NOT read (being written by 03 in W2). Sections use FULL numbering (0, 5, 7, 8, 14-EK, 18) so 07-FULL pastes them; every count below is computed in code over the two CSVs.
TOOL STATE (TOOL CARD ADDENDUM 2026-09-24T20:35Z): GetHookd WORKING · Meta Ad Library WORKING · Apify / Firecrawl-scrape / Browserbase / WebFetch BLOCKED-ON-TOOL (not needed) · Exa not used (brief) · search volume UNAVAILABLE → `search_volume: UNSCANNED`.

> Awareness is a person; sophistication is a crowd. This file reads only the crowd. Nothing here assigns a stage to a population.

## 0 · COVERAGE CARD (SOPH)

| field | value |
|---|---|
| mode | SOPH |
| PB-## n | 7 in 01 (PB-01..PB-07). Read for the 01 lanes PB-01, PB-06, PB-05 **and** PB-02, PB-07 — the lanes the long-runners actually sell; PB-03/PB-04 printed for completeness |
| CP-## n | 7 (01 §6) — population keywords on Meta: CP-02/CP-07, CP-06, CP-01 |
| N_total / N_tagged per PB | `LATE-BOUND: 06-HANDOFF.json → 06-VOC_MASTER.csv` (awareness is FULL-mode) |
| IM-## records in 02 partials | M = 29 (NW-SEED-01/02: 0 ads; NW-NEW-SEED-02 and NW-SEED-03 title-only via Meta) · stage-tagged `awareness_entry` N = 25 |
| ads read for the 20-ad table | 20 counted distinct bodies (DCO / identical-body / translation variants collapsed) + 2 EXCLUDED groups (<14 d) · bodies reused from 02: 15 · newly opened by 07-SOPH: 5 |
| networks in the read | 5 (NW-NEW-SEED-01, -03, -04, -05, NW-SEED-03); NW-NEW-SEED-02 excluded (all ads ≤2 d); NW-SEED-01/02 0 ads |
| ABOVE-FLOOR NW (02 `scale`, traffic ≥50k/mo) | **1** — NW-NEW-SEED-05 (78,722 monthly_visits [D], `network_type: EDUCATION`). All others `UNSIZED`; NW-NEW-SEED-03 (32 active) and NW-NEW-SEED-04 (85 active) pass only the money-read proxy (≥30 / ≥50 active ads), printed as a sensitivity, never counted as independent |
| tools connected / used | GetHookd (`get_user_profile`, `get_top_ads`, `search_ads`, `get_ad`) · Meta `ads_library_search` · code (python3 csv/json) |
| budget level | standard (ASSUMED per INPUTS CARD) |

**Network cards read (02 handoffs):**

| NW-## | name | network_type | scale | active_ads | longest_days_active | competitor_quality | rows in the 20 |
|---|---|---|---|---|---|---|---|
| NW-NEW-SEED-01 | Ecom Websites (ecomwebsites.com) | BRAND — DORMANT since 2026-06-21 | UNSIZED | 0 (922 historical) | 271 | INCUMBENT but DORMANT | 2 |
| NW-NEW-SEED-02 | Ecom Family net (3 pages) | BRAND-cluster | UNSIZED | 160 | 0.1 | YOUNG-SCALER (ad-ev) | 0 |
| NW-NEW-SEED-03 | Done for you brands | BRAND | UNSIZED | 32 (Meta 35) | 87 | ESTABLISHED-caveat | 3 |
| NW-NEW-SEED-04 | Ecom Accelerator | BRAND (managed / profit-share) | UNSIZED | 85 | 540 | INCUMBENT + REAL-BRAND-adj | 6 |
| NW-NEW-SEED-05 | Ecom Degree University + Will Rivera | EDUCATION | ABOVE-FLOOR (78,722 visits [D]) | 203 | 179 (this read) | ESTABLISHED | 8 |
| NW-SEED-01 | Ecom Done For You | BRAND | UNSIZED | 0 | — | UNKNOWN | 0 |
| NW-SEED-02 | Ecommerce Paradise | BRAND | UNSIZED | COUNT-UNKNOWN | — | INSUFFICIENT DATA | 0 |
| NW-SEED-03 | EcomXpertz | BRAND | UNSIZED | 1 | 36 | UNCLASSIFIED | 1 |

`get_top_ads`: **NOT RUN — needs operator yes: start_brand_spy** (all 5 indexed brand_ids returned `brand_not_spied`: 297031, 134049, 6294245, 118898, 1437830). The `search_ads` days_active-desc pull (no query) carried the read. `transcribe_ad`: NOT RUN — the lever is tagged on headline + first two lines of the written copy, which every GetHookd row carries; video-internal reveal timing is UNSCANNED except where 02 already transcribed (ED IM-01 reveal ~4% of runtime).

## 5 · INCUMBENT ENTRY-STAGE SHARE `incumbent_entry_share[PB-##]` [S]

Source: 02 swipe partials, `awareness_entry` of every IM-## (M = 29); entry stage = the earliest stage the field names (`Unaware->Problem` → AW-1; `Problem/Solution boundary` → AW-2); boundary rows flagged: 8 of 25. UNKNOWN/NULL rows (Meta title-only) stay in M and out of N. Proxy 2 only — `entry_gap_read`: `LATE-BOUND: 07-FULL (needs proxy 1 from 06-VOC_MASTER.csv)`.

**ALL IM rows** — leading entry stage: AW-1/AW-2/AW-3 (8 of 25) stage-tagged ads (of M = 29 IM-## in scope)

| NW-## / POOLED | AW-1 | AW-2 | AW-3 | AW-4 | AW-5 | N_tagged | M_opened |
|---|---|---|---|---|---|---|---|
| NW-NEW-SEED-01 | 0 | 2 | 0 | 1 | 0 | 3 | 3 |
| NW-NEW-SEED-02 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| NW-NEW-SEED-03 | 1 | 1 | 3 | 0 | 0 | 5 | 5 |
| NW-NEW-SEED-04 | 0 | 1 | 2 | 0 | 0 | 3 | 3 |
| NW-NEW-SEED-05 | 7 | 4 | 3 | 0 | 0 | 14 | 14 |
| NW-SEED-03 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| POOLED | 8 | 8 | 8 | 1 | 0 | 25 | 29 |

**PB-01** — leading entry stage: AW-3 (4 of 9) stage-tagged ads (of M = 10 IM-## in scope)

| NW-## / POOLED | AW-1 | AW-2 | AW-3 | AW-4 | AW-5 | N_tagged | M_opened |
|---|---|---|---|---|---|---|---|
| NW-NEW-SEED-01 | 0 | 2 | 0 | 1 | 0 | 3 | 3 |
| NW-NEW-SEED-03 | 1 | 1 | 3 | 0 | 0 | 5 | 5 |
| NW-NEW-SEED-04 | 0 | 0 | 1 | 0 | 0 | 1 | 1 |
| NW-SEED-03 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| POOLED | 1 | 3 | 4 | 1 | 0 | 9 | 10 |

**PB-06** — leading entry stage: NONE (0 stage-tagged) stage-tagged ads (of M = 0 IM-## in scope)

| NW-## / POOLED | AW-1 | AW-2 | AW-3 | AW-4 | AW-5 | N_tagged | M_opened |
|---|---|---|---|---|---|---|---|
| POOLED | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**PB-05** — leading entry stage: AW-3 (7 of 11) stage-tagged ads (of M = 11 IM-## in scope)

| NW-## / POOLED | AW-1 | AW-2 | AW-3 | AW-4 | AW-5 | N_tagged | M_opened |
|---|---|---|---|---|---|---|---|
| NW-NEW-SEED-01 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| NW-NEW-SEED-03 | 0 | 1 | 3 | 0 | 0 | 4 | 4 |
| NW-NEW-SEED-04 | 0 | 0 | 1 | 0 | 0 | 1 | 1 |
| NW-NEW-SEED-05 | 1 | 1 | 3 | 0 | 0 | 5 | 5 |
| POOLED | 1 | 3 | 7 | 0 | 0 | 11 | 11 |

**PB-02** — leading entry stage: AW-1/AW-2 (7 of 19) stage-tagged ads (of M = 22 IM-## in scope)

| NW-## / POOLED | AW-1 | AW-2 | AW-3 | AW-4 | AW-5 | N_tagged | M_opened |
|---|---|---|---|---|---|---|---|
| NW-NEW-SEED-01 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| NW-NEW-SEED-02 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| NW-NEW-SEED-03 | 1 | 1 | 0 | 0 | 0 | 2 | 2 |
| NW-NEW-SEED-04 | 0 | 1 | 2 | 0 | 0 | 3 | 3 |
| NW-NEW-SEED-05 | 6 | 4 | 3 | 0 | 0 | 13 | 13 |
| POOLED | 7 | 7 | 5 | 0 | 0 | 19 | 22 |

**PB-07** — leading entry stage: AW-2 (3 of 7) stage-tagged ads (of M = 10 IM-## in scope)

| NW-## / POOLED | AW-1 | AW-2 | AW-3 | AW-4 | AW-5 | N_tagged | M_opened |
|---|---|---|---|---|---|---|---|
| NW-NEW-SEED-02 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| NW-NEW-SEED-04 | 0 | 1 | 2 | 0 | 0 | 3 | 3 |
| NW-NEW-SEED-05 | 2 | 2 | 0 | 0 | 0 | 4 | 4 |
| POOLED | 2 | 3 | 2 | 0 | 0 | 7 | 10 |

**PB-03** — leading entry stage: AW-3 (2 of 3) stage-tagged ads (of M = 3 IM-## in scope)

| NW-## / POOLED | AW-1 | AW-2 | AW-3 | AW-4 | AW-5 | N_tagged | M_opened |
|---|---|---|---|---|---|---|---|
| NW-NEW-SEED-01 | 0 | 0 | 0 | 1 | 0 | 1 | 1 |
| NW-NEW-SEED-03 | 0 | 0 | 2 | 0 | 0 | 2 | 2 |
| POOLED | 0 | 0 | 2 | 1 | 0 | 3 | 3 |

**PB-04** — leading entry stage: NONE (0 stage-tagged) stage-tagged ads (of M = 0 IM-## in scope)

| NW-## / POOLED | AW-1 | AW-2 | AW-3 | AW-4 | AW-5 | N_tagged | M_opened |
|---|---|---|---|---|---|---|---|
| POOLED | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

**Counter #2:** entry-tagged N = 25 of M = 29 · proxy 2 (incumbents) pooled: AW-1 8 · AW-2 8 · AW-3 8 · AW-4 1 · AW-5 0 — a three-way split, no leading stage · proxy 1 = LATE-BOUND (06) · shape = LATE-BOUND (07-FULL). [D] Reading: 7 of the 8 AW-1 openers belong to the EDUCATION network (cold lifestyle / REPORT / pattern-interrupt openers); the DFY-store brands open later — AW-2 3, AW-3 3, AW-4 1, AW-1 1 of 8 tagged (setup overwhelm, courses failed, free-offer distrust); Ecom Accelerator opens at AW-2/AW-3 with a capital qualifier.

## 7 · THE SOPHISTICATION READ `SOPH-PB##` [S]

**Lever codebook as applied [A] (printed so 07-FULL / 10 can audit every tag):** the lever is read on the dominant element of headline (Meta link title) + the first two lines of the written copy. In this category the *category promise itself* ("we/my team build your store/business") is the CLAIM, not a mechanism — a mechanism must name a cause of the problem or a how that works differently (a platform, a loophole, a monetisation model, a false belief). `CLAIM` = outcome/offer, no how, no quantifier · `ENLARGED-CLAIM` = the same with a price, number, superlative, authority rank or time bound · `MECHANISM` = names a cause or a how (any named mechanism in headline + 2 lines wins over a claim) · `EFS` = names the how AND enlarges it against the old way ("double the return vs Amazon", "still wide open vs saturated", "without quitting") · `IDENTITY` = who the reader is / the enemy, no promise in the lead. Stage map CLAIM→S1, ENLARGED-CLAIM→S2, MECHANISM→S3, EFS→S4, IDENTITY→S5. `product_reveal_position` = % of body words before the first mention of what the advertiser sells (store build, partnership, training/webinar); WITHHELD = never named in the body (scored 100); computed in code on the written copy, not the video.

**Sampling:** GetHookd `search_ads {brand_id, sort_column:"days_active", sort_direction:"desc", limit:10, compact:true}` with no query, status active for the 4 live brand_ids and status inactive for all 5 (the dormant ecomwebsites.com has no active rows; its 234–271 d long-runners are controls, status inactive) → merged on ad_id with the 02 IM rows → DCO variants, identical bodies and one Spanish translation collapsed → sorted by days_active → cap ≤8 per network → top 20. Tiers: A ≥45 d = 13 · B 30–44 d = 2 · FILL 14–29 d = 5 (all five FILL rows are EDUCATION-network text cards; a ≥30 d-only sensitivity is printed).

### The 20 longest-running ads (CSV: `07-partials/07-SOPH-20ADS.csv`, every row + the excluded rows kept)

| # | IM-## | NW-## | days_active | status | used_count | performance_score | performance_title | lever | evidence_line (≤15w verbatim) | product_reveal_position | ltv_rich |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IM-02@NW-NEW-SEED-04 (ad 41256421 (sibling 41256434)) | NW-NEW-SEED-04 | 540 | inactive | 1 (+DCO 140 cards/39 media; 41256434 used 2) | NULL | NULL (inactive) | **EFS** | “Our stores are seeing almost double the return then on Amazon” | WITHHELD — offer never named in body (100%) | N (UNSIZED) |
| 2 | IM-03@NW-NEW-SEED-04 (ad 41256428 (sibling 41256429)) | NW-NEW-SEED-04 | 519 | inactive | 1 (+6 collapsed; 41256429 used 2, 40 media) | NULL | NULL (inactive) | **MECHANISM** | “Top Economists Are Referring To THIS As “Amazon’s New Rival”” | 63% of body words | N (UNSIZED) |
| 3 | NEW-07S (not in 02) (ad 41256422) | NW-NEW-SEED-04 | 441 | inactive | 1 | NULL | NULL (inactive) | **ENLARGED-CLAIM** | “My team will build you an e-Commerce business in as little as 14 days.” | 5% of body words | N (UNSIZED) |
| 4 | NEW-07S (not in 02) (ad 58381757) | NW-NEW-SEED-04 | 294 | inactive | 1 | NULL | NULL (inactive) | **CLAIM** | “find a way to make money while you sleep” | WITHHELD — offer never named in body (100%) | N (UNSIZED) |
| 5 | IM-01@NW-NEW-SEED-01 (ad 70486040 (IM-01 = 70823628)) | NW-NEW-SEED-01 | 271 | inactive — NW DORMANT | 1 (+>=25 DCO variants @232-271d) | NULL | NULL (inactive) | **ENLARGED-CLAIM** | “$20 Done for you eCommerce Store” | 37% of body words | N (UNSIZED) |
| 6 | IM-02..07,13,14@NW-NEW-SEED-05 (ad 85639337 (active twin 89404596 @175d)) | NW-NEW-SEED-05 | 179 | inactive (twins active @175/140/68d) | 1 (>=13 ad ids share this body) | NULL (twins 74/100) | NULL (twins Growing/Winning) | **EFS** | “While most people are still chasing saturated Amazon or Shopify side hustles” | 66% of body words | N |
| 7 | NEW-07S (not in 02) (ad 85639324) | NW-NEW-SEED-05 | 179 | inactive | 1 | NULL | NULL (inactive) | **EFS** | “a Walmart income model that quietly outpaces their traditional salaries, without quitting their careers” | 76% of body words | N |
| 8 | NEW-07S (not in 02) (ad 98804125) | NW-NEW-SEED-05 | 137 | active | 1 | 81 | Optimized | **MECHANISM** | “How To Sell Name Brand Products On Walmart & Make $5K-$10K/Month” | 4% of body words | N |
| 9 | IM-01@NW-NEW-SEED-04 (ad 103675232) | NW-NEW-SEED-04 | 119 | active | 1 (+5 same-body @103-119d; +2 price-test @21-22d) | 1 (best twin 100) | Testing (best twin Winning) | **ENLARGED-CLAIM** | “My team will build you an e-Commerce business in as little as 30 days” | 7% of body words | N (UNSIZED) |
| 10 | NEW-07S (not in 02) (ad 103675148) | NW-NEW-SEED-04 | 119 | active | 1 | 100 | Winning | **CLAIM** | “Want My Team To Build You An e-Commerce Business” | 0% of body words | N (UNSIZED) |
| 11 | IM-03@NW-NEW-SEED-03 (ad 74657770 (active twins 150503331/151824680)) | NW-NEW-SEED-03 | 87 | inactive (same-body twins active @32-35d) | 2 (+7 collapsed; es translation 59411595 @78d) | NULL (twins 100) | NULL (twins Winning) | **ENLARGED-CLAIM** | “STOP buying courses! I’ll design you a beautiful eCommerce store from scratch for just $20!” | 3% of body words | N (UNSIZED) |
| 12 | IM-05@NW-NEW-SEED-03 (ad 59618906) | NW-NEW-SEED-03 | 77 | inactive | 1 | NULL | NULL (inactive) | **MECHANISM** | “People are stealing your money. And it’s legal.” | 39% of body words | N (UNSIZED) |
| 13 | IM-02@NW-NEW-SEED-01 (ad 97210901) | NW-NEW-SEED-01 | 47 | inactive — NW DORMANT | 1 (+2 identical-body siblings) | NULL | NULL (inactive) | **ENLARGED-CLAIM** | “We were named the #1 Commerce Coach in North America by Shopify.” | 6% of body words | N (UNSIZED) |
| 14 | IM-01@NW-SEED-03 (ad 1376173990650081 (Meta)) | NW-SEED-03 | 36 | active | NULL — searched | NULL — searched | NULL — searched (Meta) | **CLAIM** | “Launch Your Amazon Store with Confidence” | UNKNOWN — body NOT OPENED (Meta title only) | N (UNSIZED) |
| 15 | IM-01@NW-NEW-SEED-03 (ad 150503395 (IM-01 = 169243242)) | NW-NEW-SEED-03 | 35 | active | 1 (+7 same-body @28-35d) | 1 (best twin 86) | Testing (best twin Optimized) | **ENLARGED-CLAIM** | “77,254+ people from around the world have already claimed their online store.” | 5% of body words | N (UNSIZED) |
| 16 | IM-08@NW-NEW-SEED-05 (ad 169343657) | NW-NEW-SEED-05 | 24 | active | 1 | 41 | Scaling | **MECHANISM** | “The biggest lie in business? “You need your own product.”” | WITHHELD — offer never named in body (100%) | N |
| 17 | IM-09@NW-NEW-SEED-05 (ad 169343649) | NW-NEW-SEED-05 | 24 | active | 1 | 41 | Scaling | **ENLARGED-CLAIM** | “No better business to start in 2026” | 78% of body words | N |
| 18 | IM-10@NW-NEW-SEED-05 (ad 169343631) | NW-NEW-SEED-05 | 24 | active | 1 | 41 | Scaling | **MECHANISM** | “how to start making money selling products on Walmarts online marketplace” | 31% of body words | N |
| 19 | IM-11@NW-NEW-SEED-05 (ad 169343626) | NW-NEW-SEED-05 | 24 | active | 1 | 41 | Scaling | **CLAIM** | “Grandmas can still get rich 🤑” | WITHHELD — offer never named in body (100%) | N |
| 20 | IM-12@NW-NEW-SEED-05 (ad 169343625) | NW-NEW-SEED-05 | 24 | active | 1 | 41 | Scaling | **IDENTITY** | “Don’t get a job in 2026” | WITHHELD — offer never named in body (100%) | N |

**EXCLUDED — bet, not control** (under 14 days; outside every count below, lever tagged only so 10/12 can widen):

- IM-03@NW-NEW-SEED-01 · NW-NEW-SEED-01 · 13 d · inactive · lever would read IDENTITY · “You’ve thought about starting an online store before” — EXCLUDED — bet, not control
- IM-01..03@NW-NEW-SEED-02 · NW-NEW-SEED-02 · 0.1 d · active · lever would read IDENTITY · “I Didn’t Have a Cape. Just a Laptop and a Family to Fight For!” — EXCLUDED — bet, not control

**Counter #3:** lever_counts {'CLAIM': 4, 'ENLARGED-CLAIM': 7, 'MECHANISM': 5, 'EFS': 3, 'IDENTITY': 1} · networks_n 5 (max share of one NW 40.0% — NW-NEW-SEED-05) · LTV-RICH rows 0 of 20 (ltv_rich needs monthly_visits ≥500,000 = 10× the 02 floor; the only sized NW has 78,722) · qualifying n = 20 (≥45 d: 13, ≥30 d: 15) · credits spent 0.56 GetHookd (283.63 → 283.07).

### Reads

#### SOPH — POOLED (all 20, EDUCATION kept, flagged)
- lever_counts: {'CLAIM': 4, 'ENLARGED-CLAIM': 7, 'MECHANISM': 5, 'EFS': 3, 'IDENTITY': 1} (n = 20; networks 5: NW-NEW-SEED-01, NW-NEW-SEED-03, NW-NEW-SEED-04, NW-NEW-SEED-05, NW-SEED-03; max one-NW share 40.0%)
- modal_lever: **ENLARGED-CLAIM** (35.0%) · confirmation: **MIXED** — S2 ENLARGED-CLAIM(7) ↔ S3 MECHANISM(5); higher stage governs
- stage by lever count: S3 · overrides: S4 override: 2 distinct stated_cause on ABOVE-FLOOR NW (C10, C9)
- **stage: S4** · one_stage_ahead_lever: **NEW INFORMATION / IDENTIFICATION / NEW AUDIENCE** (by lever count alone: EFS (enlarge or refresh the mechanism))
- product_reveal_median: 39% of body words (WITHHELD scored 100: 5 rows; UNKNOWN excluded: 1) · revealed-only median: 19.0% · S5 tell (offer kept out of the first 30% of the copy): YES — carried by WITHHELD investor/education rows
- label: **EARLY SIGNAL** · Independence caveat: only 1 traffic-sized ABOVE-FLOOR network (EDUCATION); the read cannot be VALIDATED under rule 5 whatever the lever share.

#### SOPH — SENSITIVITY — DFY-only (NW-NEW-SEED-05 EDUCATION excluded; for 07-FULL if it narrows)
- lever_counts: {'CLAIM': 3, 'ENLARGED-CLAIM': 6, 'MECHANISM': 2, 'EFS': 1, 'IDENTITY': 0} (n = 12; networks 4: NW-NEW-SEED-01, NW-NEW-SEED-03, NW-NEW-SEED-04, NW-SEED-03; max one-NW share 50.0%)
- modal_lever: **ENLARGED-CLAIM** (50.0%) · confirmation: **PLURALITY**
- stage by lever count: S2 · overrides: none triggered · money-read proxy (UNSIZED NW with ≥30 active ads counted as above-floor) would add the S4 override: 6 distinct causes
- **stage: S2** · one_stage_ahead_lever: **MECHANISM (name the how / the cause)**
- product_reveal_median: 7% of body words (WITHHELD scored 100: 2 rows; UNKNOWN excluded: 1) · revealed-only median: 6% · S5 tell (offer kept out of the first 30% of the copy): NO
- label: **SUPPORTED** · 0 traffic-sized ABOVE-FLOOR networks remain, so no strict override can fire; the label rests on 4 UNSIZED networks.

#### SOPH — SENSITIVITY — ≥30 d rows only (FILL tier dropped)
- lever_counts: {'CLAIM': 3, 'ENLARGED-CLAIM': 6, 'MECHANISM': 3, 'EFS': 3, 'IDENTITY': 0} (n = 15; networks 5: NW-NEW-SEED-01, NW-NEW-SEED-03, NW-NEW-SEED-04, NW-NEW-SEED-05, NW-SEED-03; max one-NW share 40.0%)
- modal_lever: **ENLARGED-CLAIM** (40.0%) · confirmation: **PLURALITY**
- stage by lever count: S2 · overrides: S4 override: 2 distinct stated_cause on ABOVE-FLOOR NW (C10, C9)
- **stage: S4** · one_stage_ahead_lever: **NEW INFORMATION / IDENTIFICATION / NEW AUDIENCE** (by lever count alone: MECHANISM (name the how / the cause))
- product_reveal_median: 22.0% of body words (WITHHELD scored 100: 2 rows; UNKNOWN excluded: 1) · revealed-only median: 6.5% · S5 tell (offer kept out of the first 30% of the copy): NO
- label: **SUPPORTED**

#### SOPH — PB-01 (can’t build the store — 01 lead lane)
- lever_counts: {'CLAIM': 2, 'ENLARGED-CLAIM': 5, 'MECHANISM': 1, 'EFS': 0, 'IDENTITY': 0} (n = 8; networks 4: NW-NEW-SEED-01, NW-NEW-SEED-03, NW-NEW-SEED-04, NW-SEED-03; max one-NW share 37.5%)
- modal_lever: **ENLARGED-CLAIM** (62.5%) · confirmation: **CONFIRMED**
- stage by lever count: S2 · overrides: none triggered · money-read proxy (UNSIZED NW with ≥30 active ads counted as above-floor) would add the S4 override: 4 distinct causes
- **stage: S2** · one_stage_ahead_lever: **MECHANISM (name the how / the cause)**
- product_reveal_median: 6% of body words (WITHHELD scored 100: 0 rows; UNKNOWN excluded: 1) · revealed-only median: 6% · S5 tell (offer kept out of the first 30% of the copy): NO
- label: **HYPOTHESIS** — `SOPH: PROVISIONAL (n=8)`

#### SOPH — PB-06 (store built, no sales — 01 runner-up lane)
- n = 0 — `NULL — searched: 0 of 20 long-runners carry this PB in pb_ids` → `SOPH: PROVISIONAL (n=0)`; stage UNSCANNED for this lane; the pooled read applies only as a PRIOR. 

#### SOPH — PB-05 (don’t know what to sell)
- lever_counts: {'CLAIM': 1, 'ENLARGED-CLAIM': 4, 'MECHANISM': 2, 'EFS': 0, 'IDENTITY': 1} (n = 8; networks 4: NW-NEW-SEED-01, NW-NEW-SEED-03, NW-NEW-SEED-04, NW-NEW-SEED-05; max one-NW share 37.5%)
- modal_lever: **ENLARGED-CLAIM** (50.0%) · confirmation: **PLURALITY**
- stage by lever count: S2 · overrides: S4 override: 2 distinct stated_cause on ABOVE-FLOOR NW (C10, C9)
- **stage: S4** · one_stage_ahead_lever: **NEW INFORMATION / IDENTIFICATION / NEW AUDIENCE** (by lever count alone: MECHANISM (name the how / the cause))
- product_reveal_median: 6.0% of body words (WITHHELD scored 100: 2 rows; UNKNOWN excluded: 0) · revealed-only median: 4.5% · S5 tell (offer kept out of the first 30% of the copy): NO
- label: **HYPOTHESIS** — `SOPH: PROVISIONAL (n=8)`

#### SOPH — PB-02 (job dependence / need a second income — the lane the long-runners sell most)
- lever_counts: {'CLAIM': 3, 'ENLARGED-CLAIM': 4, 'MECHANISM': 4, 'EFS': 3, 'IDENTITY': 1} (n = 15; networks 3: NW-NEW-SEED-03, NW-NEW-SEED-04, NW-NEW-SEED-05; max one-NW share 46.7%)
- modal_lever: **MECHANISM** (26.7%) · confirmation: **MIXED** — S3 MECHANISM(4) ↔ S2 ENLARGED-CLAIM(4); higher stage governs
- stage by lever count: S3 · overrides: none triggered · money-read proxy (UNSIZED NW with ≥30 active ads counted as above-floor) would add the S4 override: 5 distinct causes
- **stage: S3** · one_stage_ahead_lever: **EFS (enlarge or refresh the mechanism)**
- product_reveal_median: 63% of body words (WITHHELD scored 100: 4 rows; UNKNOWN excluded: 0) · revealed-only median: 31% · S5 tell (offer kept out of the first 30% of the copy): YES
- label: **EARLY SIGNAL**

#### SOPH — PB-07 (idle savings / an asset — sold by the capital-qualifier ads)
- lever_counts: {'CLAIM': 3, 'ENLARGED-CLAIM': 2, 'MECHANISM': 2, 'EFS': 1, 'IDENTITY': 0} (n = 8; networks 2: NW-NEW-SEED-04, NW-NEW-SEED-05; max one-NW share 75.0%)
- modal_lever: **CLAIM** (37.5%) · confirmation: **MIXED** — S1 CLAIM(3) ↔ S3 MECHANISM(2); higher stage governs
- stage by lever count: S3 · overrides: none triggered · money-read proxy (UNSIZED NW with ≥30 active ads counted as above-floor) would add the S4 override: 3 distinct causes · S1 re-check ("S5 in disguise"): ad 58381757=not identity (borrowed-authority desire lead); ad 103675148=not identity; ad 169343626=identity-addressed
- **stage: S3** · one_stage_ahead_lever: **EFS (enlarge or refresh the mechanism)**
- product_reveal_median: 47.0% of body words (WITHHELD scored 100: 3 rows; UNKNOWN excluded: 0) · revealed-only median: 7% · S5 tell (offer kept out of the first 30% of the copy): YES — carried by WITHHELD investor/education rows
- label: **HYPOTHESIS** — `SOPH: PROVISIONAL (n=8)`

#### SOPH — PB-03 (burned before / scam fear)
- lever_counts: {'CLAIM': 0, 'ENLARGED-CLAIM': 2, 'MECHANISM': 0, 'EFS': 0, 'IDENTITY': 0} (n = 2; networks 2: NW-NEW-SEED-01, NW-NEW-SEED-03; max one-NW share 50.0%)
- modal_lever: **ENLARGED-CLAIM** (100.0%) · confirmation: **CONFIRMED**
- stage by lever count: S2 · overrides: none triggered
- **stage: S2** · one_stage_ahead_lever: **MECHANISM (name the how / the cause)**
- product_reveal_median: 4.5% of body words (WITHHELD scored 100: 0 rows; UNKNOWN excluded: 0) · revealed-only median: 4.5% · S5 tell (offer kept out of the first 30% of the copy): NO
- label: **HYPOTHESIS** — `SOPH: PROVISIONAL (n=2)`

#### SOPH — PB-04 (no time to run it)
- n = 0 — `NULL — searched: 0 of 20 long-runners carry this PB in pb_ids` → `SOPH: PROVISIONAL (n=0)`; stage UNSCANNED for this lane; the pooled read applies only as a PRIOR. 

**[D] What the read says.** Two crowds sit in these 20 controls. The DFY-store crowd Readymerce competes in (Ecom Websites, Done for you brands, EcomXpertz, and Ecom Accelerator's build-it-for-you headlines) still leads with an enlarged claim — a price ($20 / free), a count (77,254+ / 40,000 / 200,000), a rank (#1 Commerce Coach) or a time bound (24 hours, 14 / 30 days): 6 of 12 DFY-only rows (50.0%) → S2 by count, and the PB-01 subset is 62.5% ENLARGED-CLAIM. Their mechanisms ("Shopify pays us a commission", profit share, a new platform) already exist but sit below line 2 — the S2→S3 hand-over. The make-money / investor crowd (Ecom Degree's Walmart "loophole" reports, Ecom Accelerator's "Amazon's New Rival" platform ads) leads with mechanisms and enlarged mechanisms; there the stated-cause override lifts the pooled read to S4. A cold Readymerce ad competes against S2 claims inside a feed whose readers have already seen S3–S4 platform mechanisms. One stage ahead for the DFY lane (PB-01/PB-05) = a named mechanism the S2 crowd has not led with (the mechanism must pass 07-FULL's PT-## capability check); for the pooled make-money market (PB-02) = new information, identification or a new audience. PB-06 (store built, no sales) is sold by none of the 20 long-runners.

## 8 · CORROBORATING SIGNALS [S] (beside the read, never instead of it)

Meta `ads_library_search` · `countries:["US"]` · `ad_active_status:"ACTIVE"` · `limit:50` · 2026-09-24 · one batch of 4. Distinct page_id computed in code on the 50 rows returned; DFY-relevance and "income-opportunity adjacent" flags are hand-coded from page_name + ad_creative_link_title `[D]`. The connector matches semantically, so `estimated_total_count` is corpus noise, never a crowding figure (same finding as 02-KEYWORDS §11).

| signal | value | term / date / source | agrees_with_read (Y/N/UNSCANNED) |
|---|---|---|---|
| advertisers_on_category_keyword | distinct page_id 34 of 50 rows · DFY-store pages 0 · income-opportunity-adjacent pages 0 · estimated_total_count 62,954 (loose) | “done for you shopify store” · 2026-09-24 · Meta [R-TOOL] | N — 0 DFY-store advertisers on the category phrase in the rows read: no crowd evidence at the keyword layer |
| advertisers_on_population_keyword (CP-02/CP-07) | distinct page_id 31 of 50 rows · DFY-store pages 1 · income-opportunity-adjacent pages 6 · estimated_total_count 1,735 (loose) | “passive income for parents” · 2026-09-24 · Meta [R-TOOL] | N — only Done for you brands (952198114852442) surfaces; the population is being sold to by adjacent income/investment offers, not by DFY stores |
| advertisers_on_population_keyword (CP-06) | distinct page_id 24 of 50 rows · DFY-store pages 0 · income-opportunity-adjacent pages 6 · estimated_total_count 1,120 (loose) | “retirement online business” · 2026-09-24 · Meta [R-TOOL] | N — no DFY-store advertiser; adjacent coaching / free-training funnels only |
| advertisers_on_population_keyword (CP-01) | distinct page_id 16 of 50 rows · DFY-store pages 0 · income-opportunity-adjacent pages 0 · estimated_total_count 13,707 (loose) | “quit your 9 to 5 online store” · 2026-09-24 · Meta [R-TOOL] | N — noise only (sheets, novels, dealerships) |
| distinct_stated_causes_n (above-floor NW) | strict (02 `scale` ABOVE-FLOOR = NW-NEW-SEED-05): **2** (C10 belief you need your own product; C9 saturated incumbent platforms vs early-window platform) · money-read proxy (+NW-NEW-SEED-03, -04): 7 · all networks: 9 | 02 swipe `stated_cause`, canonicalised in code (C1–C10; map printed below this table) | Y — ≥2 distinct causes = mechanism competition (drives the S4 override) |
| skepticism_records_n · repeated_claims_disbelieved[] | `LATE-BOUND: 06-VOC-REPORT §7` | [F] | UNSCANNED (FULL) |

**Corroborators agreeing: 1 / 3** (stated causes Y; category keyword N; population keywords N). Confirmation is not raised (it can only move PLURALITY → CONFIRMED, and the pooled count is MIXED). [D] The two N's say the same thing from outside the ad library: the literal DFY phrase and the population phrases do not surface a DFY-store crowd on Meta today — the population layer (parents, retirement, 9-to-5 quitters) is contested by adjacent income offers (investment income, direct selling, free trainings), not by store builders. That is a population-level opening (a population can sit at S2–3 inside an S4–5 category), for 07-FULL §9 to test with the corpus.

Canonical stated causes (from 02 `stated_cause`): NW-NEW-SEED-01 IM-01 → C1 · NW-NEW-SEED-01 IM-02 → C3 · NW-NEW-SEED-01 IM-03 → C4 · NW-NEW-SEED-03 IM-01 → C1 · NW-NEW-SEED-03 IM-02 → C5 · NW-NEW-SEED-03 IM-03 → C5 · NW-NEW-SEED-03 IM-04 → C5 · NW-NEW-SEED-03 IM-05 → C6 · NW-NEW-SEED-04 IM-01 → C7 · NW-NEW-SEED-04 IM-02 → C8 · NW-NEW-SEED-04 IM-03 → C9 · NW-NEW-SEED-05 IM-01 → C9 · NW-NEW-SEED-05 IM-02 → C9 · NW-NEW-SEED-05 IM-08 → C10 · C1 setup/tech complexity + product choice · C3 distrust of free/cheap offers · C4 procrastination / self-doubt · C5 courses teach but deliver no asset · C6 hidden middleman loophole · C7 lack of operating expertise/data · C8 traditional-ecom operational burden · C9 saturated incumbent platforms vs early-window platform · C10 belief you need your own product. Cross-network recurrence: C1 on 2 NW (-01, -03), C9 on 2 NW (-04, -05).

## 14 · EXISTING KNOWLEDGE & BELIEFS — ADVERTISER-ASSUMES rows `EK-##` [S] (minted from IM-## `assumed_knowledge[]`)

07-FULL merges these with 03 `existing_beliefs[]`, dedupes, renumbers and re-classes; until a Q-## confirms a row it stays ADVERTISER-ASSUMES and is never exported as CUSTOMER-BELIEVES (rule 6.9). `ek_stamps[]`: `LATE-BOUND: 06-VOC-REPORT §17`.

| EK-## | existing_belief | evidence (IM-## · assumed_knowledge verbatim) | networks | used_count (sum) | class | copy_implication ("a new ad may begin at…") | ek_stamp |
|---|---|---|---|---|---|---|---|
| EK-01 | “Shopify”, “dropshipping” and “an online store” are known words — ads name them without explaining them | IM-01@NW-NEW-SEED-01: “you know what dropshipping/an online store generally is” / IM-01@NW-NEW-SEED-03: “Shopify named without explanation” / IM-02@NW-NEW-SEED-03: “dropshipping websites / 2018 used as shorthand, undefined” / IM-03@NW-NEW-SEED-03: “dropshipping websites / 2018 used as shorthand, undefined” / IM-04@NW-NEW-SEED-03: “dropshipping / 2018 used as shorthand, undefined” | 2 (NW-NEW-SEED-01, NW-NEW-SEED-03) | 8 | ADVERTISER-ASSUMES (IM-## only) | a new ad may use “store” as a known word; never lead with “dropshipping” as the promise (see EK-02); ADS-ASSUME-ONLY until 06 ek_stamps confirm | LATE-BOUND: 06 §17 |
| EK-02 | 2018-style dropshipping sites are cheap and dated — the reader already distrusts them | IM-02@NW-NEW-SEED-03: “dropshipping websites / 2018 used as shorthand, undefined” / IM-03@NW-NEW-SEED-03: “dropshipping websites / 2018 used as shorthand, undefined” / IM-04@NW-NEW-SEED-03: “dropshipping / 2018 used as shorthand, undefined” · body: “No, these aren’t some cheap dropshipping websites that should’ve been left back in 2018.” | 1 (NW-NEW-SEED-03) | 4 | ADVERTISER-ASSUMES (IM-## only) | a new ad may begin by separating a branded, owned store from a “cheap dropshipping site”; ads assume it, corpus unconfirmed | LATE-BOUND: 06 §17 |
| EK-03 | A free or $20 store must hide a catch | IM-02@NW-NEW-SEED-01: “you already know what free-with-a-catch offers usually feel like” · IM-01@NW-NEW-SEED-03 (its assumed_knowledge field is unrelated; evidence is the body) · bodies: “I know what you're thinking. "What's the catch?"” (EW 97210901); “I know. At that price it sounds fake.” (DFYB 150503395) | 2 (NW-NEW-SEED-01, NW-NEW-SEED-03) | 3 | ADVERTISER-ASSUMES (IM-## only) | a new ad may begin by naming the catch before the reader does (what it costs, who owns it, what is refunded); ads assume the suspicion | LATE-BOUND: 06 §17 |
| EK-04 | Amazon is the reference point: early Amazon sellers got rich and Amazon/Shopify are now crowded | IM-02@NW-NEW-SEED-04: “'traditional ecommerce' headaches assumed familiar; implicit Amazon-seller frame of refere” / IM-03@NW-NEW-SEED-04: “'Amazon Marketplace sellers back in the year 2000' historical reference assumed familiar” / IM-01@NW-NEW-SEED-05: “Walmart seller program; wholesale price; AI product tools” · body: “And Walmart in 2026 looks like Amazon in 2015.” (REPORT, >=13 ad ids) | 2 (NW-NEW-SEED-04, NW-NEW-SEED-05) | 5 | ADVERTISER-ASSUMES (IM-## only) | usable only for PB-02/PB-07 capital-holders and side-hustle seekers; do not begin there for a DFY-store (PB-01) buyer — not shown to hold it | LATE-BOUND: 06 §17 |
| EK-05 | Marketplace-seller mechanics (seller account, wholesale price, profit share, platform economics) need no explanation | IM-01@NW-NEW-SEED-04: “'the platform that's been around 30 years' (unnamed, assumes viewer infers Amazon/eBay); '” / IM-01@NW-NEW-SEED-05: “Walmart seller program; wholesale price; AI product tools” / IM-12@NW-NEW-SEED-05: “'seller account' and 'ScanProfit app' named with no setup-cost/difficulty explanation” | 2 (NW-NEW-SEED-04, NW-NEW-SEED-05) | 3 | ADVERTISER-ASSUMES (IM-## only) | do not begin there: an education/investor assumption; a DFY-store ad must not assume seller-account knowledge | LATE-BOUND: 06 §17 |
| EK-06 | Starting a business means you must invent your own product | IM-08@NW-NEW-SEED-05: “reader already associates business-starting with needing your own product” | 1 (NW-NEW-SEED-05) | 1 | ADVERTISER-ASSUMES (IM-## only) | a new ad may begin by removing the “I need my own product” belief (PB-05) — single network (EDUCATION), 24-day row | LATE-BOUND: 06 §17 |
| EK-07 | “The people making money online” exist and the reader has watched them | IM-03@NW-NEW-SEED-01: “you already know 'the people making money online' as a comparison group” | 1 (NW-NEW-SEED-01) | 1 | ADVERTISER-ASSUMES (IM-## only) | a comparison opener is assumed by one 13-day bet only — do not begin there | LATE-BOUND: 06 §17 |
| EK-08 | A “legal loophole” / done-for-you setup is a recognisable idea | IM-05@NW-NEW-SEED-03: “legal loophole / done-for-you setup used before being defined” | 1 (NW-NEW-SEED-03) | 1 | ADVERTISER-ASSUMES (IM-## only) | do not begin there: one network’s 77-day ad; compliance-sensitive framing | LATE-BOUND: 06 §17 |

## 18 · COVERAGE STATEMENT (SOPH clauses)

CONFIDENCE — sophistication: EARLY SIGNAL on n=20 ads across 5 networks (LTV-RICH 0; ABOVE-FLOOR by traffic 1, EDUCATION) — pooled S4 (MIXED, modal ENLARGED-CLAIM 35.0%; S4 via stated-cause override), DFY-only S2 (PLURALITY ENLARGED-CLAIM 50.0%, n=12, SUPPORTED) · per PB: PB-01 S2 HYPOTHESIS n=8, PB-06 n=0 UNSCANNED, PB-05 S4 HYPOTHESIS n=8, PB-02 S3 EARLY SIGNAL n=15, PB-07 S3 HYPOTHESIS n=8 · corroborators agreeing 1/3 · search volume UNSCANNED · floors met/missed: SOPH 20 rows MET (20 counted: 13 ≥45 d, 2 at 30–44 d, 5 FILL 14–29 d; ≥3 networks MET — 5; ≥3 independent ABOVE-FLOOR networks MISSED — 1) · sources opened: bodies 20 (reused from 02 15, newly opened 5; 10 search_ads + 7 get_ad calls), Meta queries 4, credits spent 0.56 GetHookd / $0 Meta / $0 Exa / $0 Apify · HARVEST-## orders issued: none (SOPH mode) · no market % was read from record counts, no stage from keyword volume alone, no population stage assigned · WEAKEST LINK: independence — one traffic-sized ABOVE-FLOOR network, and it is EDUCATION; `start_brand_spy` (operator yes) → `get_top_ads` on brand_ids 297031/134049/6294245/118898/1437830, plus GetHookd traffic sizing of doneforyoubrands.co and ecomaccelerator.io, would close it · WHAT WE COULD NOT VERIFY: video-internal reveal timing (transcribe_ad not run), the EcomXpertz body (Meta title only), the Ecom Family cluster bodies (≤2 d, excluded), whether any long-runner outside these networks sells PB-06 (0 of 20 here)
