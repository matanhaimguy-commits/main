# 12 · OFFER + TEST PLAN + PLAYBOOK + HANDOFF — Readymerce · US (ASSUMED) · MODE: ASSEMBLE (W6)
agent 12-ASSEMBLE · generated 2026-09-24T23:14Z · File 1 of 2 (File 2 = `handoff.json` v2) · **$0 external spend this step — MODE: ASSEMBLE never re-researches** (no GetHookd, Meta, Exa, Apify, Firecrawl, Browserbase, WebFetch call made; `NOT RUN — needs operator yes` for any) · run ledgers as handed over: GetHookd ≈282.89 cr · Apify $0 · Exa ≈$5.30 cumulative · Higgsfield 1,977.5 cr (unchanged by this step).
Sections 1–5 are the MODE: OFFER output (`12-partials/12-OFFER.md`, ACCEPTABLE) carried verbatim, with an **ASSEMBLE resolution block** under each that binds its `LATE-BOUND: 11.*` references to the merged `11-BELIEFS.md`. `12-partials/*`, `13-BRAND.md` and `13-HANDOFF.json` were read, never edited.

## 1 · LOCK CARD + ASSUMPTIONS

### 1a · ASSEMBLE lock (this run)
| field | value | source / tag |
|---|---|---|
| PRODUCT / PDP / market | Readymerce · https://readymerce.com · US · USD | GIVEN / GIVEN / ASSUMED (00-RUN-CARD) |
| budget level · daily test budget | standard · **$100/day** ($3,000/mo) | ASSUMED (blank → $100/day, §2 INPUTS) |
| account age · creative capacity · format preference · offer assets | new · 5 stories + 5 images/week · native story · TO-BUILD | ASSUMED |
| 11 inputs | 5 scoped partials merged → `11-BELIEFS.md` + `11-HANDOFF.json` (this step, §6) | resolves 12-OFFER `LATE-BOUND: 11.OBJ-##, 11.P-##, 11.GO-AV#` |
| 13 inputs | `13-HANDOFF.json` + `13-BRAND.md` present → brand keys taken from 13; **handoff_version 2** | 13 name_status PROVISIONAL (USPTO NOT FETCHED — OPERATOR-VALIDATES) |
| operator ICP hypotheses | (a) fathers → AV-05 Evening-Only Parent · (b) 50+ with money → AV-06 Fixed-Income Retiree + CL-09 capital holder | HYPOTHESIS — 09 verdict **UNPROVEN / RESERVE** (AV-05 0 of 9 converted, 0 fathers in market voices; AV-06 0 of 9 converted, 9 of 9 booked follow-ups = the tire-kicker signature); never promoted into the test plan |
| capacity (purchase level) | testable_concepts **0**, max_adsets **0** (target CPA $399.56 > $100/day) | 12-OFFER §3, code |
| capacity (booked-call proxy) | close rate 4.76% (4 PAID/DEPOSIT of 84 calls, [R-OWNED] SAMPLE(84)) → target cost per booked call **$19.03** → testable_concepts_proxy **18**, max_adsets_proxy **5**; T1-only guard: booked call ≤ **$10.36** | 12-OFFER §3 proxy lock — **OPERATOR-VALIDATES** on every number derived from it below |

**testing_sequence (09) — class · LF8 · THE ONE BELIEF (11 merged):**
| # | AV | adset | class | LF8 | THE ONE BELIEF (11) | lock | lane_applied (11 GO) |
|---|---|---|---|---|---|---|---|
| 1 | AV-07 The Owner Who Wants It Automated ★ | AV7-owner-automate | UNTAPPED | #5 | B-03.AV-07 | LOCK-B MK-06 | S1–2 reset → claim + Name-it, PROOF-led (LOCK-B) |
| 2 | AV-01 The Store That Died | AV1-store-died | UNTAPPED | #3 | B-102.AV-01 | LOCK-A MK-01 | NEW INFORMATION → mechanism DESCRIBED (LOCK-A) |
| 3 | AV-04 The Paycheck-Tethered Builder | AV4-paycheck-side | STEALABLE | #5 | B-42.AV-04 | LOCK-A MK-01 | S4 → mechanism made surer + New Information (LOCK-A) |
| 4 | AV-02 Paid-and-Got-Nothing | AV2-paid-got-nothing | STEALABLE (EARLY SIGNAL) | #3 | B-02.AV-02 | LOCK-B MK-06 + F-11 | S4 (ASSUMED) → LOCK-B made surer + NI-04 ownership |
| 5 | AV-03 The Stuck Starter | AV3-stuck-starter | OWNED | #5 | B-03.AV-03 | LOCK-B MK-06 | S2 OWNED pond → Name-it mechanism first, claim second (LOCK-B) |

`INPUTS: files 9/9 (01+DEEP, 02, 03, 06, 07, 08, 09, 10, 11 merged) + 13 present, NW 8 (above-floor 1), OF 4, PP 7, FS 20 (11 merged), avatars 5 launch / 8 total, testable_concepts 0 (proxy 18 OPERATOR-VALIDATES), max_adsets 0 (proxy 5 OPERATOR-VALIDATES)`

### 1b · OFFER-mode lock card (carried verbatim from 12-partials/12-OFFER.md §1)

**Identity:** Readymerce (readymerce.com) — done-for-you Shopify/Etsy store build + optional ongoing management (SERVICE; no physical SKU) · market US `ASSUMED` · currency USD · category DFY e-commerce store service `INFERRED` (01 confirms) · truth-card band PROXY-SKU (01-DEEP) · lock state PROVISIONAL-ON-[A] (01).

**Operator inputs (blank → printed with source):**
| input | value | source / tag |
|---|---|---|
| HERO PRICE | **$500 one-time — "The Store Build & Research Package"** | GIVEN — site: PT-01 / F-12 (readymerce.com/pricing, /terms-of-service) `[R-PAGE via Exa]` |
| upper tiers | "Boss Boost" / "Full Service Launch" ≈ **$2,000**; "higher packages exist" (rep: "even 500,000 packages but ... very very rare") | `INFERRED [R-OWNED]` — 01 SEED §2 price row, T-01/T-02/T-05/T-06 = 4 of 10 SEED-read calls; C-row recurrence in 06-VOC_MASTER.csv: a ladder above $500 pitched in **C-0011 (2 of 155 calls)** + **C-0016 (2 of 155 calls)**; the $500 entry itself in C-0001 (61 of 155), C-0019 (~10+ UK calls read), C-0023 (~10+). The site publishes NO second tier (PT-02: "no single number is published") → every price above $500 below is `INFERRED — OPERATOR-VALIDATES`. |
| LANDED COGS | UNKNOWN (01: `unit_cost UNKNOWN — searched`; `landed_cogs N/A — service`) → **`INFERRED` category-typical labour-hours × rate + tooling**, computed in §3 with the assumption printed | `INFERRED` (basis: category-typical; offshore build labour — the only location hint is R-01 reviewer claim "workers from the Philippines", uncorroborated PT-17) |
| MONTHLY AD BUDGET / DAILY TEST BUDGET | $3,000/mo / **$100/day** | `ASSUMED` |
| ACCOUNT AGE · CREATIVE CAPACITY · FORMAT · OFFER ASSETS | new · 5 stories + 5 images/week · native story · TO-BUILD | `ASSUMED` |
| shipping | $0 — digital service delivery (no parcel) | given (01 physical_form: service) |
| consumption_model | one-time build + optional monthly management (PT-04, PT-08, F-07: "level of ongoing management ... agreed on the fit call") | given (EXACT PRODUCT MATERIAL) → ladder shape **C (kit / system)** |
| refund instrument (current) | 7-day money-back on the $500 fee; voids on delivery acceptance, ANY add-on/upgrade purchase, or a request for further work; third-party costs never refundable | PT-15 / F-10 (refund-policy + terms-of-service, word-for-word matching) |
| income claims | NONE allowed — "We make no income guarantees" (F-13, 5 of 9 site pages); PT-09 | given — rep lines "Our goal is for every shop to make at least $10,000 in 6 months." (C-0020, ~4 calls) and "91 percent ... success rate" (01 T-04) CONTRADICT PT-09 and are **kept out of every object below** |

**testing_sequence (09 avatar_portfolio) — class · LF8 button · THE ONE BELIEF (09 §7 `one_belief_that_must_break`):**
| # | AV | name | class | LF8 primary | THE ONE BELIEF |
|---|---|---|---|---|---|
| 1 ★ | AV-07 | Owner Who Wants It Automated | UNTAPPED | #5 Comfortable living (the business runs without me) | "a store only works if the owner runs it himself — or pays an agency a fortune" (Q-O-0103; Q-O-0006) |
| 2 | AV-01 | The Store That Died | UNTAPPED | #3 Freedom from fear (of losing again) | "the store died because e-commerce doesn't work for someone like me (or I picked the wrong product)" (Q-O-0108; Q-F-9004) |
| 3 | AV-04 | Paycheck-Tethered Builder | STEALABLE | #5 Comfortable living (income not hostage to the job) | "the only safe way to start is to keep the job and not bet the salary" (Q-O-0133; Q-O-0052) |
| 4 | AV-02 | Paid-and-Got-Nothing | STEALABLE | #3 Freedom from fear (of being robbed again) | "every done-for-you offer is a scam that takes the money and leaves" (Q-O-0073; Q-O-0130) |
| 5 | AV-03 | Stuck Starter | OWNED | #5 Comfortable living (the hard part done for me) | "the hard part is the build — once it's live, the job is done" (Q-F-0012; Q-F-0040) |
Reserve AV-06, AV-05, CL-09 · expansion AV-08 (09).

**MD-## top 5 (08 handoff):** MD-01 ★ "income not hostage to a job" (VALIDATED, top DS-01 "I'm actually thinking to, you know, replace my job" Q-O-0053) · MD-04 "build something of my own" (VALIDATED, DS-28 "So many years I've been thinking about it, but I never had time." Q-O-0160) · MD-02 "ease off / someone else runs it" (VALIDATED, DS-13 "build a a income that I can sit back and relax" Q-O-0015) · MD-03 provide for family (EARLY SIGNAL) · MD-05 big money (EARLY SIGNAL).

**M-1 / M-2 / big_promise / lane (10 locked):** LOCK-A MK-01 "The One-Shot Launch" (PB-06 + PB-05) — M-1: a first store is launched as a single bet and written off when the guess misses · M-2: staged release + capped, owner-approved ad tests + early review, replace what doesn't sell (PT-04, F-05, F-07) · big_idea "First stores die from getting one shot, not from e-commerce." · wedge **"Your store should get more than one shot."** · big_promise: built in your name within days, launched in stages, every product gets a small test on a budget you approve, an early review shows what's selling and what gets replaced (no income, no time-to-sale) · LOCK-B MK-06 "The Handover Cliff" (PB-01) — wedge **"We stay after launch day."**; claim line "We build it. We run it. You own it." ([R-TOOL] Meta ad title, 4 of 31 ads; C-0004 50 of 155 calls). **lane:** PB-05 S4 → mechanism + new information · PB-06 all three (LATE-BOUND stage) · PB-01 S2 → claim + Name-it.

**11 inputs:** `11-partials/` holds only `.partial` headers for AV-01/03/04 and no `11-HANDOFF.AV-##.json` at 22:36Z → `LATE-BOUND: 11.OBJ-##`, `LATE-BOUND: 11.P-##`, `LATE-BOUND: 11.GO-AV#` — objections from 06 OBJ-##, proof from 03 PR-## + PT-## (method step 4 fallback).

**Kept out of every offer object (claims router):** "Our goal is for every shop to make at least $10,000 in 6 months." (C-0020) · "91 percent of our clients have a success rate within the first two to three weeks" (01 T-04) · "If you don't go to the website within this minute, I'm gonna have to hang up and close this opportunity for you forever." (C-0024 — manufactured urgency) · "fully automate" as a promise (MC-02; 10 LOCK-B correction) · any testimonial from readymerce.com/how-it-works (actor-portrayal disclosure, 01 T3 CONTRADICTS block).

**Provisional economics (target CPA = AOV ÷ 2 at the anchor guess $500 → $250):** testable_concepts = floor(7 × 100 ÷ (2 × 250)) = **1** · max_adsets = floor(100 ÷ 250) = **0** → re-locked in §3.

`INPUTS: files 8/9 (01+DEEP, 02, 03, 06, 07 handoff, 08, 09, 10; 11 LATE-BOUND), NW 8 (above-floor 1), OF 4, PP 7, FS 6, avatars 5 launch / 8 total, testable_concepts 1, max_adsets 0 (provisional)`


## 2 · OFFER BENCHMARK


| ob_id | nw | floor | single_price | ladder_shape | tiers[] | gifts[] | guarantee | subscription Y/N + % | free_shipping_rule | funnel_destination | apps_detected[] | im_ids[] | days_active_longest |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| OB-01 | NW-01 Ecom Degree University (EDUCATION) | ABOVE-FLOOR | FREE webinar → $27 front-end | education ladder (free → coaching), not A/B/C | Free webinar → $27 → $47–97 → $99/mo → $1,995–1,997 → $2,997–3,000 → $4,300 | none in ads; $197 30-day coach access add-on (PDP) | CONTRADICTORY (claimed 'four figures or refund' vs BBB refund complaints) | Y ($99/mo community) | N/A (service) | MSL→squeeze/webinar→(offline sales)→paid (13 of 14 IMs webinar/squeeze, 1 comment-DM) | NOT RUN — get_shop skipped per brief | IM-01..IM-14 | 70 |
| OB-02 | NW-02 Ecom Family net [D candidate brand] | UNSIZED | FREE AI store builder [D] | free lead magnet → course → coaching [D] | FREE / $1,495 / $7,500 [D] | '30 Winning Products' [D] | internally conflicting (30-day vs 72-hour) [D] | Y (Shopify $1/mo pass-through) [D] | N/A | UNKNOWN (3 IMs) | NOT RUN | IM-15..IM-17 | 0.1 |
| OB-03 | NW-03 Ecom Accelerator | UNSIZED | $15K–$30K / $25K–$35K liquid capital | single capital-threshold tier + 70/30 profit share | 1 tier + profit share | none | 16-month 'No Profit No Payment' (share forfeited, work free; not cash) | N (profit share) | N/A | MSL→application-gated VSL (5 IMs) | NOT RUN | IM-18..IM-22 | 540 |
| OB-04 | NW-04 Done for you brands | UNSIZED | $20 (20 products) | A-like quantity step ($20 → $97 for 50 products) + disclosed recurring fees | $20 / $97 + Shopify $1/mo×3 then $39/mo + Zendrop $79/mo; 'Fast Shipping Suppliers' $49 | none | 30-day 100% refund 'no questions asked'; CO-15 'refunded and keep the setup anyway' | Y (platform + supplier fees, disclosed) | N/A | direct PDP 3, quiz 2 | NOT RUN | IM-23..IM-27 | 87 |
| OB-05 | NW-05 EcomXpertz | UNSIZED | $3,000/yr | 3-rung annual profit-share retainer | $3k (70/30) / $5k (80/20) / $7k (100/0) TikTok; $4k / $6k / $8k Amazon FBA | none | full refund only if project not started (20 days) | Y (annual) | N/A | UNKNOWN (1 IM) | NOT RUN | IM-28 | 36 |
| OB-06 | NW-06 Ecom Websites (DORMANT) | UNSIZED | $0 / $20 advertised | bait-then-upsell (ad price ≠ funnel price) | $1/mo×3 + 'one-time processing fee of up to $500' | 30 products 'completely free' | none in ads; funnel 'all sales final' | Y (Shopify trial → paid plan) | N/A | MSL→quiz→Shopify-trial upsell (4 IMs) | NOT RUN | IM-29..IM-32 | 271 |
| OB-07 | NW-07 Ecom Done For You | UNSIZED (0 ads) | $2,000 (Walmart automation) | UNKNOWN | $2,000; others UNKNOWN | none | '100% ROI guarantee within 6 months' (conditional; credit substitution) | N | N/A | PDP only (0 ads) | NOT RUN | — | NONE FOUND — 0 ads |
| OB-08 | NW-08 Ecommerce Paradise | UNSIZED (0 ads) | $9,997 | C-like: 3 one-time build tiers + monthly turnkey + add-ons | $9,997 / $14,997 / $19,997 (promo $9,998.50) + $2,997/mo | none | milestone: 'suppliers approved, products live ... within 90 days — or we continue working for free ... There are no refunds' | Y ($2,997/mo turnkey) | N/A | PDP only (0 ads); top-tier 50% off 'Only 5 Spots' | NOT RUN | — | NONE FOUND — 0 ads |

**Band floor:** above-floor networks with an offer context = 1 of 8 (NW-01 only; 02 §3) < 3 → **`BAND: NULL`**. Rows OB-02..OB-08 are UNSIZED — printed as a reference range, never counted as a band (02 rule: UNSIZED never counts toward crowding).

**GetHookd `aggregate_ads` for the one above-floor domain (join.ecomdegree.com — 02 had price ladder but no ad-level offer classification):** `cls_offer_type` → 0 analyzed ads (groups []) · `cls_has_money_back_guarantee` → 0 analyzed ads · `cls_price_point` → 0 analyzed ads · `page_type` → landing_page 226 [R-TOOL, as_of 2026-09-24T22:32Z]. Read: the index has not classified NW-01's offers → offer_type / MBG / price_point = `NOT MAPPED — searched: aggregate_ads ×3 (0 analyzed)`; destination confirmed as landing page on 226 indexed ads.
**Charged calls:** GetHookd aggregate_ads ×4 @0.01 = **0.04 cr** (balance 282.98 → 282.94, reconciled with get_user_profile before/after, free) · get_shop NOT RUN (skipped per brief) · Exa 0 · Apify 0 · **$ cost 0.00 (credits only)**.

**Reference convergence across all 8 networks (NOT a band — UNSIZED included; an element is copied only when ≥2 independent networks converge):**

| element | networks (count / 8) | ids | copy? |
|---|---|---|---|
| entry price ≤ $27 (free/$20 bait) | 4 / 8 | NW-01, NW-02, NW-04, NW-06 | YES (≥2) |
| a rung ≥ $1,995 | 6 / 8 | NW-01, NW-02, NW-03, NW-05, NW-07, NW-08 | YES (≥2) |
| recurring fee / subscription / retainer | 6 / 8 | NW-01, NW-02, NW-04, NW-05, NW-06, NW-08 | YES (≥2) |
| a cash refund window (any length) | 2 / 8 | NW-04, NW-05 | YES (≥2) |
| 'we keep working for free' continuation guarantee | 2 / 8 | NW-03, NW-08 | YES (≥2) |
| quiz / application gate before price | 3 / 8 | NW-03, NW-04, NW-06 | YES (≥2) |
| gift / free units in the offer | 2 / 8 | NW-02, NW-06 | YES (≥2) |

Price map (03 §12 + code): ad-visible prices are bimodal — $0–$27 entries (NW-01, NW-02[D], NW-04, NW-06) vs ≥$1,995 rungs (NW-01, NW-02[D], NW-03, NW-05, NW-07, NW-08); **no network sells at Readymerce's $500 one-time point** (03 §12 'Price hole'). Same-function DFY build+manage band (NW-05 $3k–$8k/yr, NW-07 $2,000, NW-08 $9,997–$19,997 + $2,997/mo) = **$2,000–$19,997** reference range.
**Hero price:** not re-set — $500 GIVEN (site). `OB: 8 rows (1 above-floor), band NULL (reference $0–$19,997; DFY build+manage $2,000–$19,997), charged calls 4, cost 0.04 cr / $0.00`


## 3 · ECONOMICS LABELS


**landed_cogs (T1) — `INFERRED` category-typical, labour-hours × rate + tooling:** hours {"fit call (C6)": 1.0, "niche/product research, 3 products (C3)": 3.0, "store build + config (C1)": 5.0, "branding logo/banner/structure (C2)": 2.0, "listings x3 (C1)": 2.0, "supplier + shipping profiles (C4)": 2.0, "staged release + capped ad-test setup (C5)": 2.0, "early review + corrections (PT-04)": 2.0} = **19 h** × **$12/h** (offshore build-team rate, INFERRED; band $8–$20/h) + tooling $15/store (research tool + design assets, INFERRED) = **$243.00** (band $167.00–$395.00). Shopify/Etsy plan, apps, domain, ad spend and product costs are paid by the buyer (PT-05) → $0 to Readymerce. Sales-close labour (phone reps) is NOT in COGS — see sensitivity S-3.
**one test-and-review cycle ('shot')** = {"research 3 new products": 2.0, "list them": 1.5, "capped ad test setup + monitoring": 2.0, "review + report": 1.0} = 6.5 h × $12 = **$78.00** · cadence ASSUMED 2 cycles/month under management · account-manager time (C9) 1 h/week × $12 = $12/week.

COGS multiple check: $500 ÷ $243.00 = **2.06×** vs the 5–6× rule for a blank price (5–6× = $1,215–$1,458) → the GIVEN $500 sits BELOW the rule; the price is not re-set (site GIVEN) — printed as the pressure the ladder must carry.

| tier | price | basis | cycles | cogs formula | cogs | gift cogs | contribution = price − cogs − gifts − price×2.9% − price×5% − $0 ship |
|---|---|---|---|---|---|---|---|
| T1 Build | $500 | GIVEN (site PT-01/F-12) | 1 | T1 $243 + 0×$78 + 0 wk×$12 + 0 h×$12 | $243.00 | $4.00 | $213.50 |
| T2 Build + Manage (90 days) | $2,000 | INFERRED [R-OWNED] ($2,000 "Full Service Launch", 01 SEED T-06) — OPERATOR-VALIDATES | 7 | T1 $243 + 6×$78 + 13 wk×$12 + 0 h×$12 | $867.00 | $23.80 | $951.20 |
| T3 Build + Manage + Scale (180 days) | $3,000 | INFERRED — top-tier strength floor (≤0.55 × singles-math $6,500 = $3,575 → $3,000); OPERATOR-VALIDATES | 13 | T1 $243 + 12×$78 + 26 wk×$12 + 10.5 h×$12 | $1,617.00 | $23.80 | $1,122.20 |
| bump (+2 products in wave 1) | $149 | INFERRED | — | 2×(1.0+0.75) h×$12 | $42.00 | — | $95.23 |
| OTO1 (upgrade T1→T2) | $1,500 | INFERRED | +6 | T2 − T1 cogs + GIFT-03/04 | $643.80 | — | $737.70 |
| OTO2 (second storefront) | $600 | INFERRED | — | 7 h×$12 | $84.00 | — | $468.60 |
| subscription overlay (Keep-Running plan, per month) | $550/mo | INFERRED | 2/mo | 2×$78 + 4.33 wk×$12 | $208.00 | — | $298.55 |

**breakeven_cpa_single** = price − landed COGS − 2.9% fees − 5% refund reserve − shipping = 500 − 243.00 − 14.50 − 25.00 − 0 = **$217.50**
**gross_margin (T1)** = (500 − 243.00) ÷ 500 = **51.4%** vs 70% → **BELOW** (band 21.0%–66.6% across the rate band)

**Tier-weighted order economics** (attach ASSUMED: bump 20% of orders · OTO1 10% of T1 buyers · OTO2 5% of orders; shipping $0; gift COGS inside tier COGS):

| scenario | AOV (tiers only) | projected AOV (+bump/OTO) | cogs_per_order | cm_per_order = AOV − COGS − AOV×0.029 − 0 − AOV×0.05 | target_cpa = min(AOV÷2, cm) |
|---|---|---|---|---|---|
| EVIDENCE mix 90/8/2 (ASSUMED from [R-OWNED]: 4 of 84 calls paid/deposit, all at the $500 entry; upgrades seen only post-purchase, C-0016 2/155) — **LOCKED** | $670.00 | $864.80 | $396.92 | $399.56 | min($432.40, $399.56) = **$399.56** |
| DEFAULT mix 20/55/25 (formula default) — upside scenario, not locked | $1,950.00 | $2,039.80 | $975.02 | $903.64 | min($1,019.90, $903.64) = **$903.64** |

**target_cpa_locked = $399.56** (evidence mix). T1-only buyer breakeven: $217.50.

| metric | formula | value | band | label | fix order (if BELOW) |
|---|---|---|---|---|---|
| CM/order | AOV − COGS − AOV×2.9% − ship − AOV×5% | $399.56 | ≥$35 PASS · 25–34 BORDER | PASS |  |
| required_cvr @ CPC $0.80 | CPC ÷ target_cpa_locked | 0.200% | ≤3% PASS · 3–5 BORDER | PASS |  |
| required_cvr @ CPC $1.25 | CPC ÷ target_cpa_locked | 0.313% | ≤3% PASS · 3–5 BORDER | PASS |  |
| required_cvr @ CPC $1.75 | CPC ÷ target_cpa_locked | 0.438% | ≤3% PASS · 3–5 BORDER | PASS |  |
| required_cvr @ CPC $0.80 (T1-only buyer) | CPC ÷ breakeven_cpa_single | 0.368% | ≤3% PASS · 3–5 BORDER | PASS |  |
| required_cvr @ CPC $1.25 (T1-only buyer) | CPC ÷ breakeven_cpa_single | 0.575% | ≤3% PASS · 3–5 BORDER | PASS |  |
| required_cvr @ CPC $1.75 (T1-only buyer) | CPC ÷ breakeven_cpa_single | 0.805% | ≤3% PASS · 3–5 BORDER | PASS |  |
| aov_ratio (AOV:FE) | projected AOV ÷ $500 | 1.73 (ACCEPTABLE) | ≥2.0 PASS · 1.6–1.99 BORDER | BORDER | (BORDER → recommendation) raise OTO1 → add bump → deepen top tier → re-anchor single |
| LTV60 : AOV | LTV60 = AOV + AOV×0.15 + AOV×0.15×2×0.8 (defaults: reorder 15%, sub attach 15%) | $1,202.07 → 1.39 | ≥2.0 PASS · 1.3–1.9 BORDER | BORDER |  |
| LTV60 : AOV (service form, printed beside) | AOV + sub attach 15% × 2 mo × $550 × 0.8 | $996.80 → 1.15 | ≥2.0 PASS · 1.3–1.9 BORDER | BELOW | offer the Keep-Running plan at T1 (not preselected) → graduate T1 buyers via OTO1 |
| Net margin | (cm − target_cpa − $500 ops ÷ orders) ÷ AOV; orders/mo = $3,000 ÷ target_cpa | -7.7% (7.5 orders/mo) | ≥30% PASS · 15–30 BORDER | BELOW | optimise to a booked call and hold CPA under the Net-30 line below → raise OTO1 attach → raise T1 toward 5× COGS |
| Runway | cash ÷ monthly burn | UNKNOWN (cash not given) | ≥90d PASS · 60–90 BORDER | UNKNOWN | operator gives cash on hand |
| gross_margin T1 (vs 70%) | (price − COGS) ÷ price | 51.4% | ≥70% | BELOW | labour efficiency or T1 price; T2/T3 carry the margin |

**Six bands:** {'CM': 'PASS', 'CVR@1.25': 'PASS', 'AOV:FE': 'BORDER', 'LTV:AOV': 'BORDER', 'Net': 'BELOW', 'Runway': 'UNKNOWN'}
Net-band note: at target_cpa = cm an order nets $0 by construction, so Net prints BELOW whenever cm < AOV÷2. Net ≥30% needs an actual CPA ≤ **$120.10** (cm − 0.30×AOV − $500 ÷ ($3,000 ÷ CPA), solved in code) = ≤ **$5.72 per booked call** at the 4.76% close rate. Paid testing decides; nothing here is a forecast.

**profit_per_session[tier] = CVR × AOV × margin** (margin = contribution ÷ price, before ad cost; CVR 2.0% blended default · reader lane 4% · skimmer 1% — a landing-page purchase CVR for a $500+ phone-closed service is UNKNOWN; these are the formula defaults, not a forecast):

| tier | AOV | margin | CVR 1% | CVR 2% | CVR 4% |
|---|---|---|---|---|---|
| T1 Build | $500 | 42.7% | $2.13 | $4.27 | $8.54 |
| T2 Build + Manage (90 days) | $2,000 | 47.6% | $9.51 | $19.02 | $38.05 |
| T3 Build + Manage + Scale (180 days) | $3,000 | 37.4% | $11.22 | $22.44 | $44.89 |
| blended (evidence mix) | $864.80 | 46.2% | $4.00 | $7.99 | $15.98 |

**Re-locked capacity:** testable_concepts = floor(7 × 100 ÷ (2 × 399.56)) = **0** · max_adsets = floor(100 ÷ 399.56) = **0** → a purchase-optimised test cannot fund one adset at $100/day (capacity BELOW).
**Proxy lock (for ASSEMBLE; OPERATOR-VALIDATES):** the sale closes on the phone, so the ad optimises a booked call. close_rate = (PAID 2 + DEPOSIT 2) ÷ 84 calls = 4.76% [R-OWNED] SAMPLE(84) (06 §6 outcome denominators; seller-contacted prospects) → target_cost_per_booked_call = 399.56 × 0.0476 = **$19.03** → testable_concepts_proxy = floor(700 ÷ (2 × 19.03)) = **18** · max_adsets_proxy = min(5, floor(100 ÷ 19.03)) = **5**. T1-only guard: a booked call must cost ≤ **$10.36** (= 217.50 × 0.0476) while the front end sells only the $500 package.

**Sensitivities (printed, not locked):** S-1 labour $8/h → T1 COGS $167.00, breakeven $293.50; $20/h → $395.00, breakeven $65.50 · S-2 default mix 20/55/25 → projected AOV $2,039.80, cm $903.64, target CPA $903.64, AOV ratio 4.08 · S-3 rep commission 10% of AOV (ASSUMED, outside the formula) → cm_per_order − $86.48.

`ECON: breakeven $217.50, CM/order $399.56, target CPA $399.56, AOV ratio 1.73 [ACCEPTABLE], bands PASS 2 / BORDER 2 / BELOW 1 (+ Runway UNKNOWN)`


**ASSEMBLE note:** economics unchanged (no new price input). Every proxy-derived number (booked-call CPA $19.03, T1 guard $10.36, 18 concepts, 5 adsets, all kill thresholds in §10) is `OPERATOR-VALIDATES` — the close rate is SAMPLE(84) seller-contacted calls, association only.

## 4 · VALUE-EQUATION SCORECARD


Value = (Dream Outcome × Perceived Likelihood) ÷ (Time Delay × Effort & Sacrifice)

| component | lever | id | note |
|---|---|---|---|
| dream_outcome | a store of my own, in my name — the idea finally real (MD-04) | DS-28 · Q-O-0160 | "So many years I've been thinking about it, but I never had time." — status word: "my brand" (AV-07 what_they_call_it) |
| dream_outcome | income that isn't hostage to the job (MD-01 ★) | DS-01 · Q-O-0053 | "I'm actually thinking to, you know, replace my job" — the offer names the store and the tests, NEVER an income figure (PT-09, F-13) |
| dream_outcome | someone else runs it (MD-02) · deeper hope | DS-13 · Q-O-0015 · DS-03 Q-O-0105 | "build a a income that I can sit back and relax"; deeper hope: "...work anywhere in the world and don't have to worry about anything" |
| likelihood | M-2: staged release + capped, owner-approved tests + early review — more than one shot | PT-04 · F-05 · F-07 · 10 LOCK-A | the mechanism itself raises perceived likelihood without an income claim; biggest leap = products/stage UNKNOWN (PT-19) → the ladder states cycles per tier |
| likelihood | ownership you can log into (demonstrable) | F-11 · C11 | "The store account is in your name and stays in your name"; "Payouts go to your bank account — Readymerce never holds your revenue" |
| likelihood | first review report (demonstrable) | PT-04 · F-05 | "Ad monitoring and adjustments, plus regular reporting" — shown to the buyer, not described |
| likelihood | guarantee redesigned against OBJ-01/OBJ-03 (§5 object 6) | PR-02 (2 NW) · PT-15 | counted from launch, keep-what-we-built — OPERATOR-VALIDATES |
| likelihood | business-model transparency → every cost in writing (GIFT-01) | PR-07 (3 NW, longest-running proof element) · OBJ-04 | 03 proof_stack qual>PR-07>PR-01>PR-02; P-## = LATE-BOUND: 11.P-## |
| likelihood — DEFICIT | no verified client proof: results page renders empty; testimonials carry an actor disclosure; ScamAdviser 0/100, ScamDoc 25% | PT-07 · PT-16 · F-14 · F-15 | PR-01 volume proof = NULL for Readymerce → proof asset TO-BUILD (consented client reports) — the weakest lever |
| time_delay | store built in 7–10 days (shipping analogue ≤10 days ✓) | [R-OWNED] 01 T-09 · C-0022 (~12+ calls) · site 'within a matter of days' [R-SNIPPET] | deliverable timeframe, not an outcome timeframe |
| time_delay | first sign = the first cycle's early review | PT-04 (day number UNKNOWN) | operator sets the day (INFERRED proposal: ≤21 days from launch) — OPERATOR-VALIDATES |
| time_delay | guarantee clock starts at launch, not payment | Q-O-0030 · PT-15 | "if it's gonna take fourteen days how can i take back your money in seven" — the current window can close before the store exists |
| effort | nothing to learn — done for you | AD-03 (VALIDATED) · Q-O-0056 · PT-04 | "I don't wanna be trained to do it" |
| effort | the buyer's whole routine = one fit call + approve test budgets | F-06 · F-05 | one-step routine |
| effort | every cost on one page before paying (GIFT-01) | OBJ-04 · Q-O-0135 · SK-06 | "After paying $500, I should be paying £1 every month. You didn't tell me that earlier." |
| effort | split payment / BNPL | OBJ-01 · Q-O-0098 · C-0006 (15/155) | not in the current offer (UNKNOWN) → tested as OV-01, not assumed |
| effort | plain-words guide to what happens and when (GIFT-02) | OBJ-07 · NI-01 · NI-02 | replaces the rep's "$10,000 in 6 months" (C-0020) with the honest process |

Bottom-of-equation test (§6 rule 2): time-delay levers 3 (≥1) · effort levers 5 (≥1), each with IDs → **PASS**. Likelihood is the soft side: 1 printed DEFICIT row (no verified proof) — the guarantee and the demonstrables carry it until real client reports exist.

`VE: levers top 8 / bottom 8, test PASS`


**ASSEMBLE resolution of `LATE-BOUND: 11.P-##`:** likelihood levers now bind to the merged proof map — BIG PROOF P-01.AV-07 (PT-04 written post-launch + staged-test scope, EXISTS) · P-104.AV-01 (Product Lair 5–10 products, EXISTS) · P-03.AV-02 (F-11 ownership, EXISTS) · demonstrations P-08/P-09.AV-07, P-103.AV-01, P-07.AV-04, P-01/P-14.AV-02, P-01.AV-03 (SHOOTABLE-NOW [A]) · outcome proof NULL (PT-03/06/07/18). Time lever: build 7–10 days ([R-OWNED] T-09, OPERATOR-VALIDATES before print). Effort levers: GIFT-01 cost sheet, GIFT-02 guide, "you approve, you read" (B-04.AV-07). Test: **PASS** (≥1 time + ≥1 effort lever with IDs).

## 5 · THE OFFER

### OFFER-1 · ladder (shape C — kit / system; consumption_model = one-time build + optional monthly management)

**Unit = one test-and-review cycle ("a shot")** — research → list → capped test on a budget the owner approves → review → replace (M-2, PT-04). **Singles-math anchor = units × $500**, the site's own price for one build + first tested round (PT-01) — the only single price read; a round is not sold alone today, so the anchor reads "what N shots cost bought the way you bought the first one" (AV-01 bought three separate stores: "I've lost about $1,000 in total across three stores" Q-Y-0023). No "was" price is invented. **Display caveat (OPERATOR-VALIDATES):** if the operator judges a round ≠ a $500 package, the box shows per-round $ only and the strength floor is re-read.

| tier | contents (C-## INFERRED unless noted) | units | total | price_per_unit | singles-math | pct_vs_single (per unit) | saving_$ | saving_% | per_day_chip | badge | reason_line | contribution | margin_vs_breakeven (contrib − $217.50) | margin_vs_target_CPA (contrib − $399.56) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 Build — "The Store Build & Research Package" | C1 store built on Shopify or Etsy in your name · C2 brand name direction, logo, banner, structure · C3 niche/product research + 3 vetted products listed (count INFERRED: SEED + C-0003 25/155; PT-19 unconfirmed) · C4 supplier + shipping profiles · C6 fit call · C5 staged release + 1st capped test on a budget you approve (ad spend yours, PT-05) · early review + corrections (PT-04) · C11 ownership · GIFT-01 + GIFT-02 | 1 | $500 | $500.00 | $500 | +0.0% | $0 | 0.0% | one-time | Start here | Your store built in your name in 7–10 days, 3 researched products, the first test and an early review. | $213.50 | -4.00 | -186.06 |
| T2 Build + Manage — "The Second-Shot Launch" (90 days) | everything in T1 + 6 more test-and-review cycles over 90 days (2/month: new products researched, listed, tested on a capped budget you approve, reviewed, replaced — C7/CS-10) + account manager (C9) + reports (F-05) + GIFT-03 cycle make-good + GIFT-04 old-store audit | 7 | $2,000 | $285.71 | $3,500 | -42.9% | $1,500 | 42.9% | $22.22/day over 90 days | Recommended | More than one shot: 7 tested rounds and a team that stays after launch day. | $951.20 | +733.70 | +551.64 |
| T3 Build + Manage + Scale — "The Full Run" (180 days) | everything in T2 + 6 more cycles (13 total over 180 days) + scaling what passes review (retargeting + one campaign built around the products that sell — C5 SEED T-06) + priority build slot (C9 SEED)  | 13 | $3,000 | $230.77 | $6,500 | -53.8% | $3,500 | 53.8% | $16.67/day over 180 days | Lowest price per round | 13 tested rounds over six months, and the products that sell get scaled. | $1,122.20 | +904.70 | +722.64 |

**subscription_overlay — "Keep-Running plan" (the management plan):** $550/month, 2 cycles/month → $275.00/cycle · `preselected: false` — **NOT PRESELECTED** (§3.4: PT has no repurchase language; PT-08 cadence is 'agreed on the fit call'; 0 repurchase quotes on file) · `one_time_visible: true` · `cancel_frictionless: true` (cancel any month by one email — OPERATOR-VALIDATES) · `gift_stacked: true` (GIFT-01/02 kept) · `%`: +10% vs T2's implied management rate ($1,500 ÷ 3 = $500/mo) — the month-to-month flexibility premium, priced so it never undercuts a committed tier (checked below).
- cannibalisation check T1 + 3 months of plan vs T2: $2,150 for 7 cycles vs $2,000 → tier cheaper by $150 → PASS
- cannibalisation check T1 + 6 months of plan vs T3: $3,800 for 13 cycles vs $3,000 → tier cheaper by $800 → PASS

**validity_check (4 computed columns):**

| check | result | values |
|---|---|---|
| bigger tier strictly lower per-unit | PASS | $500.00 > $285.71 > $230.77 |
| more product (units) | PASS | 1 < 7 < 13 |
| subscription per-unit ≤ single | PASS | $275.00 ≤ $500 |
| no two tiers at one per-unit | PASS | [500.0, 285.71, 230.77, 275.0] |

**strength_floor:** mid (T2) 42.9% below singles-math (≥30%) → PASS · top (T3) 53.8% (≥45% or free units) → PASS · headline is units (rounds) + guarantee, never flat money-off <25% → PASS ⇒ **PASS**
**display_rule (bigger of $ or %):** T2 shows **"Save $1,500"** (1,500 > 42.9) · T3 shows **"Save $3,500"** · T1 shows no saving (it is the single). Per-round price printed under each tier ("$285.71 a round").
**decoy:** no dummy tier is added (a fake tier fails the honesty half of the screenshot test). T1 does the decoy work on price-per-round: $500 a round vs T2 $285.71 — the target tier T2 wins on per-round price, on rounds (7 vs 1) and on the post-launch team (LOCK-B "We stay after launch day."). T3 is the anchor that makes T2's step look small (+$1,000 for +6 rounds + scaling).
**margin per tier:** T1 contribution $213.50 ≥ $0 but BELOW the locked blended CPA by $186.06 → **T1 survives only at CPA ≤ $213.50 (≈ $10.17 per booked call at 4.76% close)**; T2 +$551.64 and T3 +$722.64 over the locked CPA. Margin survives every tier at breakeven? T1 −$4.00 after gift COGS (GIFT-01/02) vs $217.50 → **NO (T1 is at breakeven, not above it)**.

`LADDER: shape C, tiers 3 (+ overlay), validity PASS 4/4, floor PASS, sub not preselected, repair none (one design correction before print: cadence set to 2 cycles/month everywhere so the overlay cannot undercut T2/T3)`

### GIFT LADDER (GIFT-##) — objections from 06 OBJ-## (`LATE-BOUND: 11.OBJ-##`: no 11 partial handoff on disk)

| gift_id | gift | tier | kind | obj_id_killed | outcome_sped | cogs | threshold | asset_status | spec (sections with evidence IDs) |
|---|---|---|---|---|---|---|---|---|---|
| GIFT-01 | "Every Cost in Writing" sheet — one page before you pay | all tiers (baseline) | digital_guide | OBJ-04 ($500 is only the start — VALIDATED, 10 obs / 9 authors) + OBJ-02 (show what the $500 pays for — Q-O-0002) | — | $3.00 | baseline — sits below the 1.2–1.3× threshold on purpose: it kills a T1 objection before payment | TO-BUILD | the $500 fee and what it includes (PT-04) · what it never includes (PT-05: product costs, platform fees — category reference NW-04 discloses "$1/month for the first 3 months! After that, it's $39/month", ad spend, apps, domain) · the test budget YOU approve per round (F-05) · the refund terms in plain words (object 6) · every upgrade price (ladder) — answers "After paying $500, I should be paying £1 every month. You didn't tell me that earlier." (Q-O-0135, HUNG-UP) |
| GIFT-02 | Guide: "A Store of Your Own, With More Than One Shot — how your products are released in stages, tested on a budget you approve, and reviewed" | all tiers (baseline) | digital_guide | OBJ-07 (how fast / how much — VALIDATED, 12 obs): sets the honest process in place of income talk | reading the first review without panic (the first sign, PT-04) | $1.00 | baseline | TO-BUILD (≈8 h one-time, amortised $1/order) | title = outcome ("a store of your own") + M-2 in plain words · §1 Why first stores die from one shot — 10 big_idea; NI-01 ("Most successful dropshippers test 5 to 10 products before finding one that scales profitably." Product Lair 2024); FS-01 (25 authors) · §2 Your first 7–10 days — PT-04; [R-OWNED] T-09; C-0022 · §3 How one round works and what you approve — PT-04; F-05 · §4 Reading your first review: why ~600 clicks and zero sales is a product signal — NI-02 (Littledata 1.4%; Oberlo 1.58%); Q-F-0019 · §5 What is yours: store, payouts, assets — F-11 · §6 What we do not promise, and why — F-13; PT-09 · components C1–C11 `INFERRED` (01) |
| GIFT-03 | Round make-good — any scheduled round we miss is added free at the end | T2, T3 | extended_guarantee | OBJ-03 (scam — VALIDATED, 12 obs) + OBJ-08 (DFY vendors don't deliver — VALIDATED, 10 obs; "your store is half-ass done" Q-F-0002) | — | $7.80 | T2 $2,000 ≥ 1.2–1.3 × current AOV $500 ($600–$650) ✓ | TO-BUILD (terms) | copied element: work-for-free continuation — 2 independent networks converge (NW-03 "work for free until you do"; NW-08 "we continue working for free") ✓; cost = 10% miss rate ASSUMED × $78 |
| GIFT-04 | Old-store second opinion — a written read of the store you already have (or had) before we build | T2, T3 (T1 in OV-02) | digital_guide | OBJ-02 (proof before paying — see our read of your own store first; "I need a proof of concept that actually works." Q-O-0132) | round 1 starts from what already failed (AV-01 "the product did not sell, so I had to close the store" Q-O-0108; AV-07 "I must have three or four Shopify stores just sitting there" Q-O-0103) | $12.00 | T2 ✓ | TO-BUILD (template, 1 h/store) | sections: products tried · traffic vs sales (NI-02) · what the one-shot launch looked like (MK-01) · what round 1 changes |

Gift test (§6 rule 6): tied 4/4 · UNTIED — padding: 0.

### GUARANTEE (object 6)

**Current instrument — conditions as on file (verbatim where the run holds the words):**
- rep line (C-0002, 17 of 155 calls): "you do have a seven day money back guarantee"
- site fragment, verbatim (01-TRUTH-CARD T7, from readymerce.com/refund-policy): the guarantee is voided by "any additional service, add-on, upsell, or upgrade"
- 01 PT-15 / F-10 (01's wording, two site pages word-for-word matching — full site text NOT on file): 7 days from the payment date · covers the $500 build fee only · void immediately, even inside 7 days, when the buyer (a) approves/accepts delivery, (b) buys ANY additional service, add-on, upsell or upgrade, (c) requests or commits to further work · never refundable: platform fees, ad spend, domain costs, apps, supplier costs.
- `OPERATOR-PASTE: readymerce.com/refund-policy + the refund clause of readymerce.com/terms-of-service` (the verbatim paragraph; 12 runs no new research).

**Why it fails the job:** (1) the window can close before the store exists — build 7–10 days vs a 7-day clock from payment: "if it's gonna take fourteen days how can i take back your money in seven" (Q-O-0030); (2) it voids on acceptance, so it never covers the part buyers fear ("your store is half-ass done" Q-F-0002; "They stole $20,000 and have lied to me repeatedly" Q-E-0006); (3) **it voids on any add-on — so every bump/OTO below would cancel the buyer's refund** (conflict printed; see object 10).

**Top T1 objection class (06 §6, lost-call co-occurrence):** OBJ-01 money 6/13 · OBJ-02 proof 3/13 · OBJ-03 scam 2/13 → class = **money lost after paying** (no money now + fear of paying and getting nothing). A guarantee cannot create money (OV-01 tests that); it closes the fear half.

| field | value |
|---|---|
| type | **performance on deliverables** (a stated, checkable result — the store and the tests — NEVER income: PT-09, F-13) |
| days | **60 from payment** (template default 60; covers a ≤10-day build + first capped test + first review with room to spare) |
| wording | **"60 days to see your store live in your name, your first products tested and your first review in your hands — or every penny of the $500 back. You keep what we built."** (`[N] days to [outcome] or every penny back`; "you keep" rests on F-11 ownership, not copied) |
| scope | the $500 build fee on every tier; T2/T3 add GIFT-03 (missed rounds added free). Accepting delivery or buying the bump/upgrades does NOT void it (replaces PT-15's void triggers). Third-party costs stay non-refundable (PT-15) and are listed on GIFT-01. |
| copied elements (≥2 NW) | cash refund window (NW-04 30-day, NW-05 20-day) ✓ · work-for-free continuation (NW-03, NW-08) ✓ |
| no_return_under | N/A — service (no parcel to return); the analogue: the buyer never has to hand anything back to be refunded (F-11) |
| placement[] | under the pay button · the booking/order confirmation page · the fit-call close (reps read the wording verbatim, replacing C-0002's bare line) · the story P.S. · retargeting to booked-not-paid prospects (BOOKED-FOLLOWUP 56 of 84 calls) |
| status | `OPERATOR-VALIDATES` + legal review — it changes the site's published policy (PT-15). Refund reserve stays 5% (ASSUMED) in §3. |

### RATIONALE + URGENCY (object 7)

- **rationale_for_generosity:** "First stores die from one shot, not from e-commerce — so the rounds after launch are priced into the package instead of sold as extras." (10 big_idea; M-2) `[AUTHORED, CHECK THIS]`
- **scarcity_source:** the site's "limited number of stores launched each month" (01 §2 specs, `[R-SNIPPET]`) is a literal capacity limit ONLY if the operator publishes the real monthly number → until then **`NONE — evergreen`**.
- **urgency_device:** **`NONE — evergreen`** (no announced price rise, no gift deadline). Banned: "If you don't go to the website within this minute, I'm gonna have to hang up and close this opportunity for you forever." (C-0024) — a manufactured constraint.

### NAMED OFFER (object 8)

| part | words | source |
|---|---|---|
| [Container] | **The Second-Shot Launch** (T2 — the target tier) | 10 wedge "Your store should get more than one shot." (M-2 staged release + capped tests + early review) |
| [Result] | **your own store, built in your name — never just sitting there** | "I must have three or four Shopify stores just sitting there" (Q-O-0103, AV-07) · "The store account is in your name and stays in your name" (F-11) · "We build it. We run it. You own it." ([R-TOOL] Meta ad title; C-0004 50/155) |
| [Timeframe] | **built in 7–10 days, then 90 days of tested rounds** | build: [R-OWNED] 01 T-09 "7 up to 10 days" + C-0022 (~12+ calls) + site "within a matter of days" [R-SNIPPET]; 90 days = the container's own length (a deliverable). The site states NO income timeframe (PT-09) → none is named. |
| entry name (T1) | **Start with the $500 Build** | "I'll start with the 500, and then I'll hopefully graduate to the next level" (Q-O-0029) |

**NAMED OFFER:** *"The Second-Shot Launch — your own store, built in your name in 7–10 days, then 90 days of tested rounds so it's never just sitting there."* (entry: *"Start with the $500 Build"*). Build-time figure `OPERATOR-VALIDATES` (owned calls, not the site).

### OFFER-IN-THE-AD (object 9)

**offer_beat (38 words, ≤40 ✓):** "Start with the $500 Build: your store in your name in 7–10 days, first products tested on a budget you approve, every cost in writing first. Not live and tested in 60 days? Every penny back. No countdown." — tier: T1 entry ($500 Build) · gift: GIFT-01 (every cost in writing) · guarantee: object 6 · urgency source: `NONE — evergreen` ("No countdown"). Story P.S. variant for T2: "Or take the Second-Shot Launch: 7 tested rounds over 90 days, missed rounds added free." `[AUTHORED, CHECK THIS]`

### BUMP / OTO1 / OTO2 (object 10) — the seven lenses

| lens | candidate | role | evidence |
|---|---|---|---|
| usage journey — before | old-store second opinion | used as GIFT-04 (T2+), not sold | AV-01 / AV-07 dead or idle stores |
| usage journey — during | +2 products in your first wave | **BUMP** | FS-01 ("I picked the baby store. It just didn't work" Q-O-0082 — one guess) · PB-05 current_spend_hypothesis (product-research tools / guru 'winning product' lists) |
| usage journey — after | Keep-Running plan $550/mo | subscription overlay (§5), NOT PRESELECTED | PT-08 |
| adjacent pain | US-warehouse supplier shortlist ($99, INFERRED) | reserve (not in stack) | FS-06 ("got sick of misdeliveries and errors in pricing" Q-F-0034); NW-04 sells "Fast Shipping Suppliers" $49 (listing_read, COMPETITOR-CLAIMED) |
| completion (full M-2 protocol) | the remaining rounds after the build | **OTO1** | FS-02 ("they said they would build a store, but i am building the store???" Q-F-0004) · current_spend_hypothesis "$500 entry / $2,000 full launch" ([R-OWNED] T-06) |
| consumable attach | ad-test budget top-ups / portal credits | NOT USED — ad spend is the buyer's (PT-05); C8 portal credits UNKNOWN (PT-19) | — |
| premium upgrade | T3 Full Run / priority slot | in the ladder (T3) | C9 SEED |
| multi-pack / household / gift | second storefront on the other platform | **OTO2** | platform question: C-0005 (20/155); "I've not been able to figure out like, what's gonna be the best platform" (Q-O-0049) |
| cross-tribe identity | list the owner's existing brand products (AV-07) | reserve (AV-07 OV candidate) | AV-07 need_stack "tied to her existing products"; Q-O-0043 |

| role | lens | what | why_for_this_avatar | price | ratio check | cogs | contribution | listing_read / INFERRED |
|---|---|---|---|---|---|---|---|---|
| BUMP | usage journey (during) + completion | +2 products researched and listed in your first wave (5 instead of 3 get a first test) | AV-01 / AV-03: the first store died on one guess — more first-wave shots at the moment of highest hope | $149 | 0.30 of hero $500 (band 0.2–0.4) ✓ | $42.00 | $95.23 | listing_read — NW-04 product-count upsell "the $97 option, your custom store will come with 50 products" [R-PAGE via Exa, COMPETITOR-CLAIMED]; price INFERRED — OPERATOR-VALIDATES |
| OTO1 | completion (full M-2 protocol) | Second-Shot Management upgrade: T1 → T2 (6 more rounds over 90 days + account manager + GIFT-03/04) | AV-02: "they said they would build a store, but i am building the store???" (Q-F-0004) → LOCK-B "We stay after launch day."; AV-07: "I'll start with the 500, and then I'll hopefully graduate to the next level" (Q-O-0029) | $1,500 | 3.00 × AOV $500 (band 1.0–3.0) ✓ | $643.80 | $737.70 | listing_read — Readymerce's own rep ladder (C-0011 2/155, C-0016 'graduated' 2/155 [R-OWNED]) + NW-08 '$2,997/mo' turnkey [COMPETITOR-CLAIMED]; price INFERRED — OPERATOR-VALIDATES |
| OTO2 | multi-pack (second storefront) | the products that pass review also listed on the other platform (Etsy ↔ Shopify), same brand | AV-03 / AV-07 platform doubt (Q-O-0049): a second shelf for a tested product, not a new guess | $600 | 0.40 of OTO1 $1,500 (band 0.3–0.6) ✓ | $84.00 | $468.60 | listing_read — marketplaces sold per channel by NW-05 ($3k–$8k/yr each) and NW-07 ($2,000 Walmart) [COMPETITOR-CLAIMED]; price INFERRED — OPERATOR-VALIDATES |

**Conflict (resolve before any complement ships):** under the current policy (PT-15) buying the bump, OTO1 or OTO2 VOIDS the buyer's refund — the stack depends on the object-6 redesign; if the operator keeps PT-15, complements are offered only after the refund window closes and the bump leaves checkout.

### OFFER TEST VARIANTS (OV-##) (object 11) — runs_after: a winner adset exists · judged_on: profit_per_session = CVR × AOV × margin

| ov_id | variant | evidence | AOV | margin | runs_after | judged_on | CVR it must beat (control T1 at 2.0%: pps = 2.0% × $500 × 42.7% = $4.27) | note |
|---|---|---|---|---|---|---|---|---|
| OV-01 | Split entry: $250 at the fit call + $250 when the store is live (lower-risk entry vs the $500 anchor; BNPL analogue) | OBJ-01 (6/13 lost calls) · "I don't know that I would have the full 500 right away" (Q-O-0098) · "It's not easy to get $500, especially with other bills" (Q-O-0083) · C-0006 credit check 15/155 · a $250 deposit already occurs (01 R-01) | $500 | 38.6% | winner adset exists | profit_per_session | **2.21%** (= 2.0% × 213.50 ÷ 193.20; 1.11× control CVR) | default on the 2nd half ASSUMED 8% × $250 + $0.30 extra fee |
| OV-02 | "Second Shot" (ladder depth, AV-01 / AV-07 adsets): $900 = build + 2 extra rounds (3 total) + GIFT-04 moved down; $300 a round (between T1 $500 and T2 $285.71 ✓); singles-math $1,500 → 40% saving ✓ | AV-01 "the product did not sell, so I had to close the store" (Q-O-0108) · AV-07 stores "just sitting there" (Q-O-0103) · "I would not pay $2,500 to anybody unless I could see some results" (Q-O-0006) | $900 | 46.0% | winner adset exists | profit_per_session | **1.03%** (= 2.0% × 213.50 ÷ 413.90; 0.52× control CVR) | cogs 243 + 2×78 + 12 + 4 = $415 |

### SCREENSHOT TEST (object 12)

| criterion | in the box | pass |
|---|---|---|
| a visible contrast ≥30% in the box | T2 "Save $1,500" (42.9%) · T3 "Save $3,500" (53.8%) | PASS |
| free units / gift visible | 7 rounds vs 1 · GIFT-03 round make-good · GIFT-04 old-store audit | PASS |
| a guarantee a stranger would repeat | object-6 wording (60 days, keep what we built) | PASS |
| nothing on screen the reader cannot check | singles-math basis printed under the box ("each round priced as a $500 package") — borderline; no client proof on screen (PT-07) | PASS |

**Would a deal-hunter screenshot this buy box? PASS** — as designed (7 rounds for $2,000 vs $500 a round, plus a 60-day keep-what-we-built guarantee). Under the CURRENT instrument (7 days from payment, void on acceptance/add-on) the same box → **FAIL** (the guarantee is what a burned buyer screenshots). PASS is conditional on object 6 being adopted (`OPERATOR-VALIDATES`).

### STRENGTH LABEL (§6 rule 1)

| check | result |
|---|---|
| screenshot test | PASS (as designed) |
| strength floor | PASS (mid 42.9% ≥30 · top 53.8% ≥45) |
| validity | PASS 4/4 |
| margin survives every tier | FAIL — T1 contribution $213.50 is −$4.00 vs breakeven $217.50 after gift COGS, and −$186.06 vs the locked CPA $399.56 |
| real urgency or honest NONE — evergreen | PASS (NONE — evergreen) |

**Offer strength: ACCEPTABLE** (1 miss). Bonuses-before-discounts (§6 rule 3): headline = rounds + guarantee → PASS. Fix for the miss (recommendation, not applied — price GIVEN): raise T1 toward 5× COGS or cut T1 labour; or hold T1 CPA ≤ $213.50 (≈ $10.17 per booked call).

`OFFER: gifts 4 (tied 4), guarantee [performance (deliverables)/60 days], urgency NONE — evergreen, complements 3 read / 3 inferred (pattern read in the category; every price INFERRED — OPERATOR-VALIDATES), OV 2, screenshot PASS (conditional), label ACCEPTABLE`

---

**ASSEMBLE resolution of `LATE-BOUND: 11.OBJ-##` (gift ties re-read against the merged objection crosswalk, 11 §8):** GIFT-01 "Every Cost in Writing" → OBJ-04.AV-07/.AV-01/.AV-04/.AV-02, OBJ-05.AV-03, OBJ-12.AV-07, OBJ-01.AV-03 (the hidden-cost + "show me what the $500 pays for" T1 rows in all 5 avatars) · GIFT-02 guide → OBJ-07.AV-07/.AV-01/.AV-04/.AV-02, OBJ-04.AV-03 (how fast / how much — answered by process, never a figure) · GIFT-03 round make-good → OBJ-15.AV-02, OBJ-02.AV-03, OBJ-08.AV-02 (will they leave after launch) · GIFT-04 old-store audit → OBJ-02.AV-07/.AV-01/.AV-04/.AV-02 (proof before paying) and FS-01.AV-07 (idle stores). **Guarantee** (performance on deliverables, 60 days, keep what we built) closes the fear half of the money/scam T1 class (OBJ-01/03 rows; BD-1 survivors, 11 §2) — `OPERATOR-VALIDATES` + legal review; it REPLACES PT-15 and resolves DNS-06 (the unconditioned "7-day money-back" line). `LATE-BOUND: 11.GO-AV#` → lanes now bound per avatar in §1a. **Offer strength stays ACCEPTABLE** (1 miss: T1 margin vs breakeven).

## 6 · MERGE REPORT

`MERGE: partials 5, BD-1 candidates 5 → 1, CLM deduped 41 → 17, DNS deduped 55 → 19, ledger cells 251/290 (holes 39), 13 present`
- **BD-1 = BD-1.AV-04 candidate** — "A store launched in small, capped tests you approve — run by a team, not by your evenings, and kept in your name — is the key to an income that isn't hostage to your job." Dissolves 7 of 32 T1 rows across the five avatars (computed from the partials' own domino verdicts, 11 §2); domino PARTIAL.
- **bd_alternates[]:** BD-1.AV-07 (6/32) · BD-1.AV-02 (4/32) · BD-1.AV-03 (4/32) · BD-1.AV-01 (3/32) — verbatim in 11 §2.
- **Renumbering map:** `.AV-1/.AV-3/.AV-4` → `.AV-01/.AV-03/.AV-04`; AV-01 `B-101…107, P-101…113, OBJ-101…106, FS-101/102` and AV-04 `B-41…47, OBJ-41…44` suffixed; unsuffixed row IDs inside a block read as that block's avatar; global IDs (Q, C, PT, F, MC, MD, DS, IB, H, EM, AE, IM, NW, LK, MK, AF, NI) never renumbered — full text 11 §1.
- **Totals (code):** beliefs 33 (V 28 / S 4 / E 1) · OBJ 59 (T1 32, unresolved 2) · FS 20 (M-1 9) · proof EXISTS 46 / SHOOTABLE-NOW 9 / PLANNED 19 · P0 ≥2-type stacks 16 of 17 · openings 5 of 5 · every LEAK/GAP line carried.

## 7 · BUY-NOW TRIGGERS (TR-AV#)

### TR-AV-07 · The Owner Who Wants It Automated ★
| field | value |
|---|---|
| struggling_moment (time, place, trigger, Q-##) | early evening, small-business back room / desk: the marketing that "was the one bringing in the money" slows while "three or four Shopify and other stores" sit untouched (Q-O-0124, Q-O-0103; EM-09) |
| activation_events[] (AE-## / EM-##, Q-##) | EM-09 store/marketing slowed (Q-O-0124) · AE-05 built, never launched (Q-O-0153, Q-F-0018) · AE-06 a years-long delay recognised (Q-O-0160, Q-O-0152) |
| four_forces.push | "it's slowed down so much" (Q-O-0124) |
| four_forces.pull | "If I can turn this side hustle into a main job where I work anywhere in the world and don't have to worry about anything, that's ideal." (Q-O-0105) |
| four_forces.anxiety | "I pay $500 and then I'm gonna have to pay more money down the road for services?" (Q-O-0028) |
| four_forces.habit | "I'm a computer consultant and I have very little time." (Q-O-0154) · stores idle "in years" (Q-O-0103) |
| cost_of_inaction | UNQUANTIFIED — no loss-amount wallet quote from AV-07 persons; context only: agency quotes "$5,000, $20,000, $15,000" (Q-O-0104) = the alternative's price, not a loss |
| two_futures | LACK: IB-19 (Q-O-0103) · FULFILLMENT: H-09 (IB-26) |
| hot_state_scene | EM-09 + MICRO-DREAM SCENE Q-O-0103 (the idle admin) |
| loss_frame | [AUTHORED, CHECK THIS] "Every month the stores sit, the build you already paid for earns nothing." (from Q-O-0103 "in years") |
| made_them_act (battery WHAT-MADE-THEM-ACT) | "I'll start with the 500, and then I'll hopefully graduate to the next level" (Q-O-0029) · "I just wanna go through with it" (Q-O-0054) |

### TR-AV-01 · The Store That Died
| field | value |
|---|---|
| struggling_moment (time, place, trigger, Q-##) | Sunday night, kitchen table, dashboard open: ~600 sessions, 0 orders (Q-F-0019; EM-06) → the post-mortem count (Q-Y-0014; EM-07) |
| activation_events[] (AE-## / EM-##, Q-##) | EM-08 deciding whether to try again (Q-Y-0015, Q-B-0004) · AE-08 closed the store for lack of time (Q-O-0090) |
| four_forces.push | "I am growing tired of looking at all the traffic and no sales" (Q-F-0022) |
| four_forces.pull | "I'm looking for a steady income" (Q-O-0109) |
| four_forces.anxiety | "i had to give up or else i would literally lose all my money" (Q-Y-0049) |
| four_forces.habit | "that's why i'm going to continue working on the store to make it profitable" (Q-Y-0015; OBJ-106.AV-01) |
| cost_of_inaction | $41,754 summed from Q-Y-0013 $500 + Q-Y-0014 $254 + Q-Y-0023 $1,000 + Q-Y-0017 $40,000 — past losses quoted by AV-01/CP-03 voices (EM-07), SAMPLE(4) — the price of the one-shot pattern, never a forecast; median $750 (one $40,000 outlier, Q-Y-0017) |
| two_futures | LACK: NULL — searched: 08 §14 CP-03 rows (IB-12 "leave out"); nearest IB-08 (Q-O-0037) · FULFILLMENT: H-12 (IB-29) · IB-30 verbatim (Q-Y-0053) |
| hot_state_scene | EM-06 (Q-F-0019) |
| loss_frame | [AUTHORED, CHECK THIS] "Close it for good and the one-shot store stays the last word on whether this works for you." (FS-01; B-102.AV-01) |
| made_them_act (battery WHAT-MADE-THEM-ACT) | "I was afraid to ever try again, but eventually I did" (Q-B-0004) · "i failed the challenge … that's why i'm going to continue" (Q-Y-0015) |

### TR-AV-04 · The Paycheck-Tethered Builder
| field | value |
|---|---|
| struggling_moment (time, place, trigger, Q-##) | after the shift, kitchen table: the store gets the leftover hours (Q-F-0015; EM-01) · on break asking for the contract (Q-O-0116) |
| activation_events[] (AE-## / EM-##, Q-##) | AE-03 fatigue after 20 years (Q-O-0111) · AE-08 closed the store for lack of time (Q-O-0090) |
| four_forces.push | "come on, man. I wish I was doing something else." (Q-O-0096) |
| four_forces.pull | "a stable income flow" (Q-O-0046) · "To make 100% of my salary and above from it." (Q-O-0176) |
| four_forces.anxiety | "I earn good money now, so I don't want to quit and then start struggling." (Q-O-0133) |
| four_forces.habit | "anytime that I know that I'm ready ... I'll get back to you" (Q-O-0052) |
| cost_of_inaction | UNQUANTIFIED — no loss-amount wallet quote from AV-04 persons; time cost only: "a part time job ... fifteen to eighteen hours a week" (Q-O-0050) |
| two_futures | LACK: IB-06 (Q-F-0015) · FULFILLMENT: H-05 (IB-14) |
| hot_state_scene | EM-01 (Q-F-0015) |
| loss_frame | [AUTHORED, CHECK THIS] "Waiting until you're 'ready' means the store gets no tests at all this month." (Q-O-0052) |
| made_them_act (battery WHAT-MADE-THEM-ACT) | "If I can make the money, I'm a do it" (Q-O-0072) · "After weeks of overthinking, I finally committed" (Q-Y-0053) |

### TR-AV-02 · Paid-and-Got-Nothing
| field | value |
|---|---|
| struggling_moment (time, place, trigger, Q-##) | at the home desk, the login screen: "contact an administrator which should be me" (Q-F-0001; EM-03) · mid-call, typing the company into Google reviews (Q-O-0102) |
| activation_events[] (AE-## / EM-##, Q-##) | AE-14 a scam / lost money (Q-O-0062, Q-O-0148) · AE-05 the builder's store shut down (Q-F-0018) |
| four_forces.push | "they said they would build a store, but i am building the store???" (Q-F-0004) |
| four_forces.pull | "I would just link into the store once it is finished" (Q-F-0005) |
| four_forces.anxiety | "I felt like it was a scam" (Q-O-0073) |
| four_forces.habit | "go do a Google review of your company and see" (Q-O-0102) · "Call me back in two weeks" (Q-O-0064) |
| cost_of_inaction | $5,500 summed from Q-O-0062 $4,500 + Q-O-0074 $1,000 — [R-OWNED] money already lost or stuck (Q-O-0074 "over a thousand" = lower bound); competitor context kept apart: Q-E-0006 $20,000, Q-E-0010 $69+$169 (SIMILAR PRODUCT CONTEXT, not summed) |
| two_futures | LACK: IB-22 (Q-F-0018) · FULFILLMENT: H-12 (IB-29) |
| hot_state_scene | EM-03 (Q-F-0001, Q-F-0004) |
| loss_frame | [AUTHORED, CHECK THIS] "Staying out means the last builder's half-done store stays the only version you've seen." (Q-F-0002) |
| made_them_act (battery WHAT-MADE-THEM-ACT) | "I'm getting it ready promise" (Q-O-0013 — the scam-burned caller who put down a DEPOSIT) · "I was afraid to ever try again, but eventually I did" (Q-B-0004) |

### TR-AV-03 · The Stuck Starter
| field | value |
|---|---|
| struggling_moment (time, place, trigger, Q-##) | evening, week ten, still on the theme settings (Q-F-0013; EM-02) · at the signup product step (Q-F-0041; EM-10) |
| activation_events[] (AE-## / EM-##, Q-##) | AE-07 end of an overthinking spell (Q-Y-0053) · AE-05 built, never launched (Q-O-0153) |
| four_forces.push | "tons of links that are like a snowstorm of information, but nothing that actually helps me!" (Q-F-0006) |
| four_forces.pull | "build a a income that I can sit back and relax" (Q-O-0015) |
| four_forces.anxiety | "When the store was transferred to me, the store was shutdown almost immediately" (Q-F-0018) |
| four_forces.habit | "I would like to get in touch with y'all when I'm more prepared" (Q-O-0026; OBJ-07.AV-03) |
| cost_of_inaction | UNQUANTIFIED — time cost only: "10 weeks on simple tasks" (Q-F-0013); no money-loss quote from AV-03 persons |
| two_futures | LACK: IB-17 (Q-F-0013) · FULFILLMENT: H-10 (IB-27) |
| hot_state_scene | EM-02 (Q-F-0006, Q-F-0013) |
| loss_frame | [AUTHORED, CHECK THIS] "Another month in the settings is another month the store you started doesn't exist." (Q-O-0153) |
| made_them_act (battery WHAT-MADE-THEM-ACT) | "After weeks of overthinking, I finally committed" (Q-Y-0053) |

`TR: avatars 5/5, forces with Q 20/20, cost_of_inaction quantified 2/5`

## 8 · TEST CELLS (CELL-##)

**Count rule (code):** testable_concepts (proxy) = floor(7 × $100 ÷ (2 × $19.03)) = 18 → clamp [N_adsets × 3, N_adsets × 5] = [15, 25] → **18 cells** (AV-07 4 · AV-01 4 · AV-04 4 · AV-02 3 · AV-03 3). `tested_variable` = **avatar (WHO)** — adset = avatar (§3.14); the exception (one adset, ads = angles) is NOT applied: pooled stage S4 and a 5-avatar PORTFOLIO (09), not a stage 1–2 or NARROW portfolio. Every ranking here is **the research favorite, not the final winner.**

**held_constant[] (all cells):** concept/structure skeleton per angle (one story per ad; no mid-test edits) · offer (T1 "Start with the $500 Build" + offer_beat §5 object 9) · product (Readymerce $500 Store Build & Research Package, PT-01) · mechanism (the avatar's locked M-1/M-2, 10 §15) · image polish (REG-1 phone-real register, 13 §6) · copy quality (one writer contract §14, one writer)

### CELL-01 · AV-07 × PP-06 × MD-02 × AN-01 · AV7-A1-your-stores-didn-t-fail-nobo
| field | value |
|---|---|
| avatar_id | AV-07 The Owner Who Wants It Automated ★ (adset AV7-owner-automate) |
| problem_id | PP-06 — no time to run it |
| desire_id + lf8_root | MD-02 · LF8 #5 |
| angle | AN-01 · premise: Your stores didn't fail — nobody was assigned to them after the build; a built store isn't a running store. · strategic_frame: story/transformation (F1) · lane: S1–2 reset → claim + Name-it, PROOF-led (LOCK-B) · territory: FRESH · belief_to_break: B-02.AV-07 · structure: ST-04 · awareness_entry: AW-4 · avoid_list: "done-for-you"/"turnkey" (DNS-03) · "fully automated"/"hands-free" as our claim (DNS-04) · income/ROI/success-rate figures (DNS-01/02) · "we manage your store" (DNS-05) · "no sales"/"failed" (his stores SAT) · existing-store takeover (DNS-11) |
| hook_seeds[5] | 1. [unexpected concrete contrast] Same store. One sat for years. One got worked every week after it went live. (B-02.AV-07)<br>2. [scene in progress] Three or four stores, built, sitting in the admin for years. (Q-O-0103)<br>3. [blunt personal admission] "I had one before. I just ended it because I was dealing with a lot." (Q-O-0097)<br>4. [direct avatar callout] You run a business. Your store is "just sitting there ready to be loaded." (Q-O-0103)<br>5. [grounded belief correction] A built store isn't a running store. (B-02.AV-07) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): three or four stores "just sitting there" in the admin (Q-O-0103) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-01.AV-07 (EXISTS) · P-06.AV-07 (EXISTS) · P-09.AV-07 (SHOOTABLE-NOW [A]) |
| objection_ids[] | OBJ-12.AV-07 · OBJ-16.AV-07 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-O-0103 · Q-O-0097 · Q-O-0154 · Q-O-0169 (4) |
| market_validation | FRESH — 0 of 8 NW name the post-launch step (10 §12); CP-04 0 ads (07 §9) |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-02 · AV-07 × PP-06 × MD-01 × AN-02 · AV7-A2-it-was-never-do-it-myself-or
| field | value |
|---|---|
| avatar_id | AV-07 The Owner Who Wants It Automated ★ (adset AV7-owner-automate) |
| problem_id | PP-06 — no time to run it |
| desire_id + lf8_root | MD-01 · LF8 #1 |
| angle | AN-02 · premise: It was never "do it myself" or "$5,000–$20,000": a published $500 first step with a team that stays after go-live is the third option. · strategic_frame: bold proclamation (F3) · lane: S1–2 reset → claim + Name-it, PROOF-led (LOCK-B) · territory: CHALLENGER-3 · belief_to_break: B-03.AV-07 · structure: ST-03 · awareness_entry: AW-5 · avoid_list: "done-for-you"/"turnkey" (DNS-03) · "fully automated"/"hands-free" as our claim (DNS-04) · income/ROI/success-rate figures (DNS-01/02) · "we manage your store" (DNS-05) · "no sales"/"failed" (his stores SAT) · existing-store takeover (DNS-11) |
| hook_seeds[5] | 1. [grounded belief correction] It was never only "hire a developer" or "do it myself." (Q-F-9006)<br>2. [unexpected concrete contrast] $5,000, $20,000, $15,000 — or do it yourself. There's a third option. (Q-O-0104)<br>3. [direct avatar callout] Quoted $5k–$20k for a store? "I'm like, seriously? Come on." (Q-O-0104)<br>4. [blunt personal admission] "I would not pay $2,500 to anybody unless I could see some results." (Q-O-0006)<br>5. [scene in progress] "I'll start with the 500, and then I'll hopefully graduate to the next level." (Q-O-0029) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): moving money between her own accounts mid-call to fund the $500 (O-a654f844 marker) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-04.AV-07 (EXISTS) · P-05.AV-07 (EXISTS) · P-03.AV-07 (EXISTS) |
| objection_ids[] | OBJ-13.AV-07 · OBJ-04.AV-07 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-O-0104 · Q-O-0006 · Q-F-9006 · Q-O-0029 (4) |
| market_validation | CHALLENGER-3 vs VA-01 "we build it for you" (NW-03/04/06); BI-01 territory |
| format | STATIC |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-03 · AV-07 × PP-06 × MD-02 × AN-03 · AV7-A3-managed-not-automatic-a-team
| field | value |
|---|---|
| avatar_id | AV-07 The Owner Who Wants It Automated ★ (adset AV7-owner-automate) |
| problem_id | PP-06 — no time to run it |
| desire_id + lf8_root | MD-02 · LF8 #5 |
| angle | AN-03 · premise: Managed, not automatic: a team does the store's weekly work (review → fix → test) while you approve budgets and read reports. · strategic_frame: mechanism reveal (F2) · lane: S1–2 reset → claim + Name-it, PROOF-led (LOCK-B) · territory: FRESH (FRESHEN wording — never "we manage", DNS-05) · belief_to_break: B-04.AV-07 · structure: ST-02 · awareness_entry: AW-4 · avoid_list: "done-for-you"/"turnkey" (DNS-03) · "fully automated"/"hands-free" as our claim (DNS-04) · income/ROI/success-rate figures (DNS-01/02) · "we manage your store" (DNS-05) · "no sales"/"failed" (his stores SAT) · existing-store takeover (DNS-11) |
| hook_seeds[5] | 1. [blunt personal admission] "We don't have the budget to be able to do a lot of ads." (Q-O-0005)<br>2. [grounded belief correction] Not fully automated. Managed — you approve the budget, you read the report. (B-04.AV-07)<br>3. [scene in progress] The marketing "was the one bringing in the money, but it's slowed down so much." (Q-O-0124)<br>4. [direct avatar callout] "You guys can fully automate my online business"? Here's what that honestly looks like. (Q-O-0001)<br>5. [unexpected concrete contrast] Your week: running the business. The store's week: review, fix, test. Nobody had the second list. (B-01.AV-07) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): watching the marketing that "was the one bringing in the money" slow down (Q-O-0124) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-09.AV-07 (SHOOTABLE-NOW [A]) · P-01.AV-07 (EXISTS) · P-05.AV-07 (EXISTS) |
| objection_ids[] | OBJ-16.AV-07 · OBJ-15.AV-07 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-O-0001 · Q-O-0005 · Q-O-0124 · Q-O-0045 (4) |
| market_validation | FRESH — LOCK-B handle CLEAR (10 collision FRESHEN); MC-02 correct-in-copy |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-04 · AV-07 × PP-01 × MD-01 × AN-04 · AV7-A4-the-builder-s-job-ends-the-d
| field | value |
|---|---|
| avatar_id | AV-07 The Owner Who Wants It Automated ★ (adset AV7-owner-automate) |
| problem_id | PP-01 — can't get the store built/live myself |
| desire_id + lf8_root | MD-01 · LF8 #1 |
| angle | AN-04 · premise: The builder's job ends the day the store goes live — the platform's own guide says so; the weeks after are where it runs or sits. · strategic_frame: social proof/us-vs-them (F4) · lane: S1–2 reset → claim + Name-it, PROOF-led (LOCK-B) · territory: FRESH (EN-1 villain CLEAR, 13 §2) · belief_to_break: B-02.AV-07 · structure: ST-03 · awareness_entry: AW-4 · avoid_list: "done-for-you"/"turnkey" (DNS-03) · "fully automated"/"hands-free" as our claim (DNS-04) · income/ROI/success-rate figures (DNS-01/02) · "we manage your store" (DNS-05) · "no sales"/"failed" (his stores SAT) · existing-store takeover (DNS-11) |
| hook_seeds[5] | 1. [direct avatar callout] Paid a builder? Ask what happened the week after it went live. (Q-O-0169)<br>2. [scene in progress] "At what point do I take over the store? Is it something I have to run on my own?" (Q-O-0169)<br>3. [grounded belief correction] The platform's own guide has builders hand it over "when it's ready to go live." That's where their job ends. (P-06.AV-07)<br>4. [blunt personal admission] "I too have found this process to be not as they said it would be." (Q-F-0004)<br>5. [unexpected concrete contrast] Launch day is the starting line, not the finish line. (10 LOCK-B big_idea) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): three or four stores "just sitting there" in the admin (Q-O-0103) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-06.AV-07 (EXISTS) · P-07.AV-07 (EXISTS) · P-01.AV-07 (EXISTS) |
| objection_ids[] | OBJ-02.AV-07 · OBJ-18.AV-07 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-O-0169 · Q-F-0004 · Q-F-0018 · Q-O-0103 (4) |
| market_validation | FRESH — EN-1 build-and-leave VALIDATED 8 authors / 0 NW attack it (13 §2) |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-05 · AV-01 × PP-02 × MD-04 × AN-05 · AV1-A1-your-first-store-didn-t-prov
| field | value |
|---|---|
| avatar_id | AV-01 The Store That Died (adset AV1-store-died) |
| problem_id | PP-02 — built/ran a store, no sales, money gone |
| desire_id + lf8_root | MD-04 · LF8 #3 |
| angle | AN-05 · premise: Your first store didn't prove e-commerce can't work for you — it got one shot, and one guess misses more often than it hits. · strategic_frame: story/transformation (F1) · lane: NEW INFORMATION → mechanism DESCRIBED (LOCK-A) · territory: FRESH · belief_to_break: B-102.AV-01 · structure: ST-05 · awareness_entry: AW-2 · avoid_list: "done for you" in the hook (DNS-03) · "easy" (DNS-08) · "winning product" as a promise (DNS-09) · income figures (DNS-01/02) · product name before the solution requirement · calling his closed store a mistake |
| hook_seeds[5] | 1. [blunt personal admission] "Ive had 2 stores on Shopify both failed." (Q-F-9004)<br>2. [scene in progress] Sunday night. ~600 clicks. Still no sales. (Q-F-0019)<br>3. [grounded belief correction] Your first store didn't fail. It ran out of shots. (NI-01 hook sample)<br>4. [direct avatar callout] "There's plenty of us losing, including myself." (Q-Y-0027)<br>5. [unexpected concrete contrast] "You could have nine failed stores and that one winner will make you more money than all the others." (Q-Y-0026) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): Sunday night, dashboard open: ~600 sessions, 0 orders (Q-F-0019) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-104.AV-01 (EXISTS) · P-106.AV-01 (EXISTS) · P-101.AV-01 (EXISTS) |
| objection_ids[] | OBJ-101.AV-01 · OBJ-106.AV-01 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-O-0108 · Q-F-9004 · Q-Y-0027 · Q-Y-0026 · Q-F-0019 (5) |
| market_validation | FRESH — LOCK-A villain CLEAR 0/8 NW; PB-06 lane nobody sells (02) |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-06 · AV-01 × PP-02 × MD-01 × AN-06 · AV1-A2-hundreds-of-clicks-and-zero
| field | value |
|---|---|
| avatar_id | AV-01 The Store That Died (adset AV1-store-died) |
| problem_id | PP-02 — built/ran a store, no sales, money gone |
| desire_id + lf8_root | MD-01 · LF8 #3 |
| angle | AN-06 · premise: Hundreds of clicks and zero orders is a product signal, not a traffic signal — the next product needs a test, not more clicks. · strategic_frame: mechanism reveal (F2) · lane: NEW INFORMATION → mechanism DESCRIBED (LOCK-A) · territory: FRESH (NI-02) · belief_to_break: B-107.AV-01 · structure: ST-01 · awareness_entry: AW-3 · avoid_list: "done for you" in the hook (DNS-03) · "easy" (DNS-08) · "winning product" as a promise (DNS-09) · income figures (DNS-01/02) · product name before the solution requirement · calling his closed store a mistake |
| hook_seeds[5] | 1. [scene in progress] "i got zero sales which means i lost 254 dollars." (Q-Y-0014)<br>2. [unexpected concrete contrast] ~600 clicks at an average ~1.4% should bring about 8 orders. Zero means the product missed — not the traffic. (P-105.AV-01)<br>3. [blunt personal admission] "I am growing tired of looking at all the traffic and no sales." (Q-F-0022)<br>4. [grounded belief correction] More clicks for the same product was never going to change the answer. (B-105.AV-01)<br>5. [direct avatar callout] "I've tried selling jewelry I've tried selling baby pacifiers chess boards…" (Q-Y-0028) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): filming the post-mortem: "lost 254 dollars" (Q-Y-0014) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-105.AV-01 (EXISTS) · P-104.AV-01 (EXISTS) · P-101.AV-01 (EXISTS) |
| objection_ids[] | OBJ-102.AV-01 · OBJ-101.AV-01 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-Y-0014 · Q-F-0019 · Q-F-0022 · Q-Y-0028 (4) |
| market_validation | FRESH — NI-02 new information (10 §16a); 0 of 20 long-runners name it (03 §16) |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-07 · AV-01 × PP-04 × MD-01 × AN-07 · AV1-A3-you-re-right-to-guard-your-m
| field | value |
|---|---|
| avatar_id | AV-01 The Store That Died (adset AV1-store-died) |
| problem_id | PP-04 — burned by scams/vendors |
| desire_id + lf8_root | MD-01 · LF8 #3 |
| angle | AN-07 · premise: You're right to guard your money: every cost written before you pay, the store and payouts in your name, no test spends a dollar you didn't approve. · strategic_frame: fear+hope (F5) · lane: NEW INFORMATION → mechanism DESCRIBED (LOCK-A) · territory: CHALLENGER-3 · belief_to_break: B-104.AV-01 · structure: ST-01 · awareness_entry: AW-3 · avoid_list: "done for you" in the hook (DNS-03) · "easy" (DNS-08) · "winning product" as a promise (DNS-09) · income figures (DNS-01/02) · product name before the solution requirement · calling his closed store a mistake |
| hook_seeds[5] | 1. [grounded belief correction] It isn't easy money. It's small tests you approve and can stop. (B-103.AV-01)<br>2. [blunt personal admission] "I've been burned many times." (Q-Y-0030)<br>3. [direct avatar callout] "Is that one-off payment or I need to make a regular payment?" Here's every cost, first. (Q-O-0112)<br>4. [scene in progress] "i had to give up or else i would literally lose all my money." (Q-Y-0049)<br>5. [unexpected concrete contrast] One store, one guess — or several small capped tries in a store in your name. (B-107.AV-01) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): closing the store tab and cancelling the plan (Q-O-0108) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-108.AV-01 (EXISTS) · P-102.AV-01 (EXISTS) · P-107.AV-01 (EXISTS) · P-103.AV-01 (SHOOTABLE-NOW [A]) |
| objection_ids[] | OBJ-04.AV-01 · OBJ-03.AV-01 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-Y-0030 · Q-Y-0049 · Q-O-0112 · Q-Y-0032 (4) |
| market_validation | CHALLENGER-3 vs VA-03 business-model transparency (NW-03/04/06) |
| format | STATIC |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-08 · AV-01 × PP-03 × MD-04 × AN-08 · AV1-A4-the-ones-who-found-a-product
| field | value |
|---|---|
| avatar_id | AV-01 The Store That Died (adset AV1-store-died) |
| problem_id | PP-03 — don't know what to sell |
| desire_id + lf8_root | MD-04 · LF8 #6 |
| angle | AN-08 · premise: The ones who found a product that sells almost never found it first — they tested five to ten, each on a small budget. · strategic_frame: social proof/us-vs-them (F4) · lane: NEW INFORMATION → mechanism DESCRIBED (LOCK-A) · territory: FRESH (NI-01) · belief_to_break: B-107.AV-01 · structure: ST-01 · awareness_entry: AW-3 · avoid_list: "done for you" in the hook (DNS-03) · "easy" (DNS-08) · "winning product" as a promise (DNS-09) · income figures (DNS-01/02) · product name before the solution requirement · calling his closed store a mistake |
| hook_seeds[5] | 1. [unexpected concrete contrast] One product and a one-week deadline — or five to ten, each on a small budget. (P-104.AV-01)<br>2. [direct avatar callout] Still hunting the one product? "it takes years to find a winning product." (Q-Y-0064)<br>3. [grounded belief correction] The people with a product that sells almost never found it on the first try. (NI-01 hook sample)<br>4. [scene in progress] "i failed the challenge." (Q-Y-0015)<br>5. [blunt personal admission] "the product you're trying to sell people don't even want to buy." (Q-Y-0031) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): Sunday night, dashboard open: ~600 sessions, 0 orders (Q-F-0019) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-104.AV-01 (EXISTS) · P-106.AV-01 (EXISTS) · P-101.AV-01 (EXISTS) |
| objection_ids[] | OBJ-101.AV-01 · OBJ-07.AV-01 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-Y-0064 · Q-Y-0031 · Q-Y-0026 · Q-Y-0015 (4) |
| market_validation | FRESH — NI-01 (Product Lair 2024, practitioner guide); 0 of 20 long-runners name it |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-09 · AV-04 × PP-06 × MD-01 × AN-09 · AV4-A1-it-wasn-t-a-lack-of-ability
| field | value |
|---|---|
| avatar_id | AV-04 The Paycheck-Tethered Builder (adset AV4-paycheck-side) |
| problem_id | PP-06 — no time to run it |
| desire_id + lf8_root | MD-01 · LF8 #5 |
| angle | AN-09 · premise: It wasn't a lack of ability — the after-hours route asked you to run a second full job in leftover hours. · strategic_frame: social proof/us-vs-them (F4) · lane: S4 → mechanism made surer + New Information (LOCK-A) · territory: CHALLENGER-2 · belief_to_break: B-44.AV-04 · structure: ST-05 · awareness_entry: AW-3 · avoid_list: "quit/replace your job" as a promise (DNS-13) · "hands-free" (DNS-04) · re-explaining "we build it for you" (07 AW-4 must_not_be_told) · courses/training language (DNS-15) · a bigger number (SK-02) |
| hook_seeds[5] | 1. [scene in progress] "I work a full time job as well, so am only able to attend to my store after hours." (Q-F-0015)<br>2. [blunt personal admission] "i closed it because i didn't have time to try and work the business to see sales." (Q-O-0090)<br>3. [grounded belief correction] Stores don't fail from bad ideas. They fail from Tuesday nights. (AF-11 hook_seed)<br>4. [direct avatar callout] Five years in and still not sure "what's gonna be the best platform"? (Q-O-0049)<br>5. [unexpected concrete contrast] Your evenings vs a team's working day: which one should run the tests? (B-41.AV-04) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): after the shift, the store gets the leftover hours (Q-F-0015) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-01.AV-04 (EXISTS) · P-07.AV-04 (SHOOTABLE-NOW [A]) · P-09.AV-04 (PLANNED) |
| objection_ids[] | OBJ-06.AV-04 · OBJ-44.AV-04 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-F-0015 · Q-F-0016 · Q-O-0090 · Q-O-0049 · Q-F-0014 (5) |
| market_validation | CHALLENGER-2 vs VA-04 "it's not you — it's the barrier" (NW-04/06) — own wording only (DNS-18) |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-10 · AV-04 × PP-05 × MD-01 × AN-10 · AV4-A2-keep-the-salary-that-s-the-s
| field | value |
|---|---|
| avatar_id | AV-04 The Paycheck-Tethered Builder (adset AV4-paycheck-side) |
| problem_id | PP-05 — stuck in (or out of) a job |
| desire_id + lf8_root | MD-01 · LF8 #3 |
| angle | AN-10 · premise: Keep the salary — that's the safe part; the store can start now beside the job on small, capped tests you approve. · strategic_frame: bold proclamation (F3) · lane: S4 → mechanism made surer + New Information (LOCK-A) · territory: FRESH (no NW sells keep-the-job; NW-01/IM-14 sell quitting) · belief_to_break: B-42.AV-04 · structure: ST-04 · awareness_entry: AW-4 · avoid_list: "quit/replace your job" as a promise (DNS-13) · "hands-free" (DNS-04) · re-explaining "we build it for you" (07 AW-4 must_not_be_told) · courses/training language (DNS-15) · a bigger number (SK-02) |
| hook_seeds[5] | 1. [scene in progress] On break: "Can I review full contract before making payment?" (Q-O-0116)<br>2. [direct avatar callout] "I earn good money now, so I don't want to quit and then start struggling." Good. Don't. (Q-O-0133)<br>3. [grounded belief correction] Keep the salary. Start with small tests on budgets you approve. (CLM-03 (CLM-01.AV-04))<br>4. [blunt personal admission] "anytime that I know that I'm ready ... I'll get back to you." (Q-O-0052)<br>5. [unexpected concrete contrast] Quit-your-job ads vs a store that starts beside the job. (B-42.AV-04) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): on break at work: "Can I review full contract before making payment?" (Q-O-0116) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-01.AV-04 (EXISTS) · P-07.AV-04 (SHOOTABLE-NOW [A]) · P-04.AV-04 (EXISTS) |
| objection_ids[] | OBJ-11.AV-04 · OBJ-04.AV-04 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-O-0133 · Q-O-0052 · Q-O-0026 · Q-O-0057 (4) |
| market_validation | FRESH — counter-position to IM-14 "Don't get another job in 2026" (NW-01) |
| format | STATIC |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-11 · AV-04 × PP-02 × MD-01 × AN-11 · AV4-A3-a-first-store-that-got-one-g
| field | value |
|---|---|
| avatar_id | AV-04 The Paycheck-Tethered Builder (adset AV4-paycheck-side) |
| problem_id | PP-02 — built/ran a store, no sales, money gone |
| desire_id + lf8_root | MD-01 · LF8 #5 |
| angle | AN-11 · premise: A first store that got one guess only proved one guess missed; sellers who find a product usually tested several, each small. · strategic_frame: fear+hope (F5) · lane: S4 → mechanism made surer + New Information (LOCK-A) · territory: FRESH (NI-01) · belief_to_break: B-47.AV-04 · structure: ST-04 · awareness_entry: AW-4 · avoid_list: "quit/replace your job" as a promise (DNS-13) · "hands-free" (DNS-04) · re-explaining "we build it for you" (07 AW-4 must_not_be_told) · courses/training language (DNS-15) · a bigger number (SK-02) |
| hook_seeds[5] | 1. [direct avatar callout] "I picked the baby store. It just didn't work"? (Q-O-0082)<br>2. [grounded belief correction] A first store that got one guess only proved one guess missed. (B-47.AV-04)<br>3. [scene in progress] On the drive in: "I wish I was doing something else." (Q-O-0096)<br>4. [blunt personal admission] "my store didn't even make $20, so I had to come out." (Q-O-0101)<br>5. [unexpected concrete contrast] One product switched on at once — or five to ten, each tested small. (P-05.AV-04) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): "I wish I was doing something else" on the drive in (Q-O-0096) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-05.AV-04 (EXISTS) · P-15.AV-04 (EXISTS) · P-01.AV-04 (EXISTS) |
| objection_ids[] | OBJ-07.AV-04 · OBJ-02.AV-04 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-O-0082 · Q-Y-0046 · Q-O-0101 · Q-O-0096 (4) |
| market_validation | FRESH — NI-01 new information (10 §16a) |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-12 · AV-04 × PP-05 × MD-02 × AN-12 · AV4-A4-you-don-t-need-to-be-trained
| field | value |
|---|---|
| avatar_id | AV-04 The Paycheck-Tethered Builder (adset AV4-paycheck-side) |
| problem_id | PP-05 — stuck in (or out of) a job |
| desire_id + lf8_root | MD-02 · LF8 #5 |
| angle | AN-12 · premise: You don't need to be trained into a second job: the build, tests and fixes are done; you approve and read — and the whole cost is on one line. · strategic_frame: story/transformation (F1) · lane: S4 → mechanism made surer + New Information (LOCK-A) · territory: CHALLENGER-1 · belief_to_break: B-46.AV-04 · structure: ST-01 · awareness_entry: AW-4 · avoid_list: "quit/replace your job" as a promise (DNS-13) · "hands-free" (DNS-04) · re-explaining "we build it for you" (07 AW-4 must_not_be_told) · courses/training language (DNS-15) · a bigger number (SK-02) |
| hook_seeds[5] | 1. [direct avatar callout] "The one thing I don't have in my life is time." (Q-O-0143)<br>2. [blunt personal admission] "I don't wanna be trained to do it. I wanna just put the money forward." (Q-O-0056)<br>3. [scene in progress] "a part time job ... fifteen to eighteen hours a week." (Q-O-0050)<br>4. [grounded belief correction] Not a course. Nothing to learn before it runs. (CLM-16 (PT-14))<br>5. [unexpected concrete contrast] $500 one-time, fees and an ad budget you set — vs another course that trains you into a second job. (CLM-04 (CLM-06.AV-04)) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): after the shift, the store gets the leftover hours (Q-F-0015) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-01.AV-04 (EXISTS) · P-04.AV-04 (EXISTS) · P-07.AV-04 (SHOOTABLE-NOW [A]) |
| objection_ids[] | OBJ-44.AV-04 · OBJ-04.AV-04 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-O-0056 · Q-F-0005 · Q-O-0143 · Q-O-0050 (4) |
| market_validation | CHALLENGER-1 vs VA-05 "delivered, not taught" (NW-04 only) — never "STOP buying courses" (DNS-15) |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-13 · AV-02 × PP-04 × MD-01 × AN-13 · AV2-A1-the-burned-stores-went-wrong
| field | value |
|---|---|
| avatar_id | AV-02 Paid-and-Got-Nothing (adset AV2-paid-got-nothing) |
| problem_id | PP-04 — burned by scams/vendors |
| desire_id + lf8_root | MD-01 · LF8 #3 |
| angle | AN-13 · premise: The burned stores went wrong in two checkable places: the store sat in the builder's account, and the builder stopped on launch day. Check both before you pay. · strategic_frame: mechanism reveal (F2) · lane: S4 (ASSUMED) → LOCK-B made surer + NI-04 ownership · territory: FRESH (NI-04: 0 of 32 IM sell ownership as a check) · belief_to_break: B-02.AV-02 · structure: ST-05 · awareness_entry: AW-4 · avoid_list: "legit/trust us" (DNS-16) · "free/$20 store" (DNS-17) · pressure close (DNS-14) · income figures (DNS-01/02) · re-teaching what a builder is · leading with the brand |
| hook_seeds[5] | 1. [direct avatar callout] "they said they would build a store, but i am building the store???" (Q-F-0004)<br>2. [scene in progress] "now I can't access it, contact an administrator which should be me." (Q-F-0001)<br>3. [grounded belief correction] Before you ask if a store will sell, ask whose name is on it. (NI-04 hook sample)<br>4. [blunt personal admission] "I felt like it was a scam." (Q-O-0073)<br>5. [unexpected concrete contrast] The store they held in their account vs a store opened in your name from day one. (CLM-10 / CLM-02) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): the login that says "contact an administrator" (Q-F-0001) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-03.AV-02 (EXISTS) · P-05.AV-02 (EXISTS) · P-06.AV-02 (EXISTS) · P-01.AV-02 (SHOOTABLE-NOW [A]) |
| objection_ids[] | OBJ-03.AV-02 · OBJ-13.AV-02 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-F-0001 · Q-F-0004 · Q-O-0073 · Q-O-0062 (4) |
| market_validation | FRESH — NI-04 (10 §16a); EN-1 VALIDATED 8 authors (13 §2) |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-14 · AV-02 × PP-04 × MD-04 × AN-14 · AV2-A2-paying-someone-to-build-it-w
| field | value |
|---|---|
| avatar_id | AV-02 Paid-and-Got-Nothing (adset AV2-paid-got-nothing) |
| problem_id | PP-04 — burned by scams/vendors |
| desire_id + lf8_root | MD-04 · LF8 #3 |
| angle | AN-14 · premise: Paying someone to build it wasn't the mistake — the version you bought stopped at go-live; here is what's different on paper. · strategic_frame: social proof/us-vs-them (F4) · lane: S4 (ASSUMED) → LOCK-B made surer + NI-04 ownership · territory: CHALLENGER-3 · belief_to_break: B-04.AV-02 · structure: ST-04 · awareness_entry: AW-3 · avoid_list: "legit/trust us" (DNS-16) · "free/$20 store" (DNS-17) · pressure close (DNS-14) · income figures (DNS-01/02) · re-teaching what a builder is · leading with the brand |
| hook_seeds[5] | 1. [blunt personal admission] "I need a proof of concept that actually works." (Q-O-0132)<br>2. [direct avatar callout] Googling a store company mid-call? Check these two things instead. (Q-O-0102)<br>3. [grounded belief correction] Paying someone to build it wasn't the mistake. The version you bought stopped at go-live. (B-04.AV-02)<br>4. [scene in progress] "Can I review full contract before making payment?" (Q-O-0116)<br>5. [unexpected concrete contrast] "the pitch is almost always the same" — so here is what is different, in writing. (Q-Y-0004) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): typing the company name into Google reviews mid-call (Q-O-0102) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-14.AV-02 (SHOOTABLE-NOW [A]) · P-02.AV-02 (EXISTS) · P-03.AV-02 (EXISTS) |
| objection_ids[] | OBJ-02.AV-02 · OBJ-04.AV-02 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-O-0102 · Q-O-0116 · Q-O-0132 · Q-Y-0004 (4) |
| market_validation | CHALLENGER-3 vs VA-03 transparency (NW-03/04/06) |
| format | STATIC |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-15 · AV-02 × PP-05 × MD-01 × AN-15 · AV2-A3-if-the-money-isn-t-there-yet
| field | value |
|---|---|
| avatar_id | AV-02 Paid-and-Got-Nothing (adset AV2-paid-got-nothing) |
| problem_id | PP-05 — stuck in (or out of) a job |
| desire_id + lf8_root | MD-01 · LF8 #3 |
| angle | AN-15 · premise: If the money isn't there yet, waiting is right; when it is, the first step is a fixed $500 with every other cost named and a store you can check before and after paying. · strategic_frame: fear+hope (F5) · lane: S4 (ASSUMED) → LOCK-B made surer + NI-04 ownership · territory: FRESH · belief_to_break: B-07.AV-02 · structure: ST-03 · awareness_entry: AW-4 · avoid_list: "legit/trust us" (DNS-16) · "free/$20 store" (DNS-17) · pressure close (DNS-14) · income figures (DNS-01/02) · re-teaching what a builder is · leading with the brand |
| hook_seeds[5] | 1. [unexpected concrete contrast] If the money isn't there yet, waiting is the right call. When it is: $500, every other cost named first. (B-06.AV-02)<br>2. [blunt personal admission] "I gave somebody $4,500, and they took my money." (Q-O-0062)<br>3. [scene in progress] "over a thousand dollars sitting in my account … I can't pull my money out." (Q-O-0074)<br>4. [direct avatar callout] "I was afraid to ever try again, but eventually I did." (Q-B-0004)<br>5. [grounded belief correction] Not every one of them: the ones that burned people kept the store in their account and stopped at launch. (B-02.AV-02) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): checking the account where "over a thousand dollars" is stuck (Q-O-0074) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-03.AV-02 (EXISTS) · P-02.AV-02 (EXISTS) · P-04.AV-02 (EXISTS) |
| objection_ids[] | OBJ-01.AV-02 · OBJ-15.AV-02 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-O-0074 · Q-O-0063 · Q-O-0062 · Q-B-0004 (4) |
| market_validation | FRESH — no NW addresses the burned buyer's check (09 CAM) |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-16 · AV-03 × PP-01 × MD-04 × AN-16 · AV3-A1-the-setup-was-never-your-wal
| field | value |
|---|---|
| avatar_id | AV-03 The Stuck Starter (adset AV3-stuck-starter) |
| problem_id | PP-01 — can't get the store built/live myself |
| desire_id + lf8_root | MD-04 · LF8 #1 |
| angle | AN-16 · premise: The setup was never your wall — the builder's job ends the day the store goes live; a store needs someone after launch day. · strategic_frame: mechanism reveal (F2) · lane: S2 OWNED pond → Name-it mechanism first, claim second (LOCK-B) · territory: FRESH (handle CLEAR; the build claim is OWNED by 4 NW) · belief_to_break: B-03.AV-03 · structure: ST-04 · awareness_entry: AW-2 · avoid_list: "done-for-you"/"business in a box" (DNS-03) · "we build your entire store / skip the setup" (DNS-19) · "easy" (DNS-08) · "winning product" in an AW-2 hook (DNS-09) · "you're not less capable" (DNS-18) · "we manage your store" (DNS-05) |
| hook_seeds[5] | 1. [grounded belief correction] Launch day is the starting line, not the finish line. (10 LOCK-B big_idea)<br>2. [scene in progress] "I've spent 10 weeks on simple tasks that the system doesn't verify." (Q-F-0013)<br>3. [direct avatar callout] "tons of links that are like a snowstorm of information, but nothing that actually helps me!" (Q-F-0006)<br>4. [blunt personal admission] "I'm tech savvy and competent. I cannot find a simple step by step." (Q-F-0012)<br>5. [unexpected concrete contrast] "When the store was transferred to me, the store was shutdown almost immediately." (Q-F-0018) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): week ten, still changing the theme image (Q-F-0013) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-02.AV-03 (EXISTS) · P-04.AV-03 (EXISTS) · P-05.AV-03 (EXISTS) |
| objection_ids[] | OBJ-02.AV-03 · OBJ-01.AV-03 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-F-0013 · Q-F-0006 · Q-F-0018 · Q-F-0012 (4) |
| market_validation | FRESH — MECHANISM step one stage ahead of the S2 claim (07 §15 SR-01) |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-17 · AV-03 × PP-03 × MD-04 × AN-17 · AV3-A2-what-should-i-sell-is-answe
| field | value |
|---|---|
| avatar_id | AV-03 The Stuck Starter (adset AV3-stuck-starter) |
| problem_id | PP-03 — don't know what to sell |
| desire_id + lf8_root | MD-04 · LF8 #1 |
| angle | AN-17 · premise: "What should I sell?" is answered by small tests, not a perfect first pick — products chosen from data and released in stages. · strategic_frame: story/transformation (F1) · lane: S2 OWNED pond → Name-it mechanism first, claim second (LOCK-B) · territory: FRESH (NI-01) · belief_to_break: B-06.AV-03 · structure: ST-03 · awareness_entry: AW-3 · avoid_list: "done-for-you"/"business in a box" (DNS-03) · "we build your entire store / skip the setup" (DNS-19) · "easy" (DNS-08) · "winning product" in an AW-2 hook (DNS-09) · "you're not less capable" (DNS-18) · "we manage your store" (DNS-05) |
| hook_seeds[5] | 1. [scene in progress] "After weeks of overthinking, I finally committed." (Q-Y-0053)<br>2. [direct avatar callout] "Do I just choose what I want to sell"? (Q-F-0041)<br>3. [blunt personal admission] "I developed one, but I never launched it. That's the problem." (Q-O-0153)<br>4. [grounded belief correction] "What should I sell?" gets answered by small tests, not a perfect first guess. (B-06.AV-03)<br>5. [unexpected concrete contrast] One perfect pick vs products chosen from search data, released in stages. (CLM-08 (CLM-06.AV-03)) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): at the signup product step: "Do I just choose what I want to sell" (Q-F-0041) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-08.AV-03 (EXISTS) · P-02.AV-03 (EXISTS) · P-09.AV-03 (EXISTS) |
| objection_ids[] | OBJ-09.AV-03 · OBJ-08.AV-03 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-F-0041 · Q-F-0040 · Q-O-0153 · Q-Y-0053 (4) |
| market_validation | FRESH — NI-01; EM-10 crowded entry reframed (07 §14a) |
| format | NATIVE_STORY |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

### CELL-18 · AV-03 × PP-01 × MD-01 × AN-18 · AV3-A3-one-published-price-and-a-st
| field | value |
|---|---|
| avatar_id | AV-03 The Stuck Starter (adset AV3-stuck-starter) |
| problem_id | PP-01 — can't get the store built/live myself |
| desire_id + lf8_root | MD-01 · LF8 #1 |
| angle | AN-18 · premise: One published price and a store in your name — and the team is still on it after it opens. · strategic_frame: bold proclamation (F3) · lane: S2 OWNED pond → Name-it mechanism first, claim second (LOCK-B) · territory: CHALLENGER-3 · belief_to_break: B-04.AV-03 · structure: ST-01 · awareness_entry: AW-4 · avoid_list: "done-for-you"/"business in a box" (DNS-03) · "we build your entire store / skip the setup" (DNS-19) · "easy" (DNS-08) · "winning product" in an AW-2 hook (DNS-09) · "you're not less capable" (DNS-18) · "we manage your store" (DNS-05) |
| hook_seeds[5] | 1. [blunt personal admission] "I don't know where to start or what I should sell." (Q-F-0040)<br>2. [unexpected concrete contrast] One published price: $500 for the build and research. Everything else named before you pay. (CLM-04 (CLM-07.AV-03))<br>3. [direct avatar callout] "I thought this call was gonna just show me exactly what the $500 pays for." (Q-O-0002)<br>4. [grounded belief correction] We build it in your name. Then we stay after it opens. (13 POS-1 stranger_safe_line)<br>5. [scene in progress] "At what point do I take over the store? Is it something I have to run on my own?" (Q-O-0169) — classes 5/5 · SYNTHESIZED from corpus language; quoted lines verbatim |
| image_concept | Behaviour scene (no product): scrolling help links "like a snowstorm of information" (Q-F-0006) — REG-1 phone-real register (13 §6) |
| proof_ids[] | P-10.AV-03 (EXISTS) · P-03.AV-03 (EXISTS) · P-02.AV-03 (EXISTS) |
| objection_ids[] | OBJ-01.AV-03 · OBJ-05.AV-03 |
| offer_beat | §5 object 9 (T1 "Start with the $500 Build", GIFT-01, 60-day deliverables guarantee OPERATOR-VALIDATES, "No countdown") |
| tested_variable | avatar (WHO) — exactly one |
| held_constant[] | the six constants above |
| voc_roots[] | Q-O-0002 · Q-O-0015 · Q-O-0169 · Q-F-0006 (4) |
| market_validation | CHALLENGER-3 vs VA-01 (OWNED pond: IM-29 271 d) |
| format | STATIC |
| status | READY (rule 9: every field an ID, one tested variable, six constants, voc ≥4, proof ≥1 EXISTS/SHOOTABLE-NOW, B-## named) |

**Summary**
| cell_id | avatar | PP | MD (lf8) | AN | frame | awareness | territory | format | tested_variable | status |
|---|---|---|---|---|---|---|---|---|---|---|
| CELL-01 | AV-07 | PP-06 | MD-02 (#5) | AN-01 | F1 | AW-4 | FRESH | NATIVE_STORY | avatar | READY |
| CELL-02 | AV-07 | PP-06 | MD-01 (#1) | AN-02 | F3 | AW-5 | CHALLENGER-3 | STATIC | avatar | READY |
| CELL-03 | AV-07 | PP-06 | MD-02 (#5) | AN-03 | F2 | AW-4 | FRESH | NATIVE_STORY | avatar | READY |
| CELL-04 | AV-07 | PP-01 | MD-01 (#1) | AN-04 | F4 | AW-4 | FRESH | NATIVE_STORY | avatar | READY |
| CELL-05 | AV-01 | PP-02 | MD-04 (#3) | AN-05 | F1 | AW-2 | FRESH | NATIVE_STORY | avatar | READY |
| CELL-06 | AV-01 | PP-02 | MD-01 (#3) | AN-06 | F2 | AW-3 | FRESH | NATIVE_STORY | avatar | READY |
| CELL-07 | AV-01 | PP-04 | MD-01 (#3) | AN-07 | F5 | AW-3 | CHALLENGER-3 | STATIC | avatar | READY |
| CELL-08 | AV-01 | PP-03 | MD-04 (#6) | AN-08 | F4 | AW-3 | FRESH | NATIVE_STORY | avatar | READY |
| CELL-09 | AV-04 | PP-06 | MD-01 (#5) | AN-09 | F4 | AW-3 | CHALLENGER-2 | NATIVE_STORY | avatar | READY |
| CELL-10 | AV-04 | PP-05 | MD-01 (#3) | AN-10 | F3 | AW-4 | FRESH | STATIC | avatar | READY |
| CELL-11 | AV-04 | PP-02 | MD-01 (#5) | AN-11 | F5 | AW-4 | FRESH | NATIVE_STORY | avatar | READY |
| CELL-12 | AV-04 | PP-05 | MD-02 (#5) | AN-12 | F1 | AW-4 | CHALLENGER-1 | NATIVE_STORY | avatar | READY |
| CELL-13 | AV-02 | PP-04 | MD-01 (#3) | AN-13 | F2 | AW-4 | FRESH | NATIVE_STORY | avatar | READY |
| CELL-14 | AV-02 | PP-04 | MD-04 (#3) | AN-14 | F4 | AW-3 | CHALLENGER-3 | STATIC | avatar | READY |
| CELL-15 | AV-02 | PP-05 | MD-01 (#3) | AN-15 | F5 | AW-4 | FRESH | NATIVE_STORY | avatar | READY |
| CELL-16 | AV-03 | PP-01 | MD-04 (#1) | AN-16 | F2 | AW-2 | FRESH | NATIVE_STORY | avatar | READY |
| CELL-17 | AV-03 | PP-03 | MD-04 (#1) | AN-17 | F1 | AW-3 | FRESH | NATIVE_STORY | avatar | READY |
| CELL-18 | AV-03 | PP-01 | MD-01 (#1) | AN-18 | F3 | AW-4 | CHALLENGER-3 | STATIC | avatar | READY |

**Frame × awareness matrix per avatar (code)**
| avatar | F1 story/transformation | F2 mechanism reveal | F3 bold proclamation | F4 social proof/us-vs-them | F5 fear+hope | awareness levels |
|---|---|---|---|---|---|---|
| AV-07 | AN-01@AW-4 | AN-03@AW-4 | AN-02@AW-5 | AN-04@AW-4 | — | 2 |
| AV-01 | AN-05@AW-2 | AN-06@AW-3 | — | AN-08@AW-3 | AN-07@AW-3 | 2 |
| AV-04 | AN-12@AW-4 | — | AN-10@AW-4 | AN-09@AW-3 | AN-11@AW-4 | 2 |
| AV-02 | — | AN-13@AW-4 | — | AN-14@AW-3 | AN-15@AW-4 | 2 |
| AV-03 | AN-17@AW-3 | AN-16@AW-2 | AN-18@AW-4 | — | — | 3 |

**Similarity (code, 5 attributes: frame, pain, structure, image scene, lead hook class):** max pairwise shared = **1/5 = 20%** across all 153 pairs (within-adset max 20%) — structure + lead-class assignment solved in code so no pair reaches 2/5 (40%); collisions swapped 11 (frames/pains/structures re-aimed before print: AN-03, AN-05, AN-07, AN-08, AN-09, AN-10, AN-11, AN-12, AN-14, AN-15, AN-18); no two ads of one avatar share frame + pain or frame + mechanism; largest premise family = 5 of 18 = 28% (≤ 1/3 ✓); structurally distinct concepts (frame × structure × premise family) = 18 (above the 8–12 band — every cell distinct; not THIN).
`AN: 18 minted (+10 reserve), frames/avatar min 3, awareness levels/avatar min 2, collisions swapped 11, similarity max 20%` · `CELLS: 18 (READY 18 / FLAGGED 0), testable_concepts 18 (proxy), clamp [15–25]`

## 9 · CAMPAIGN STRUCTURE (CS-1)

```
CS-1  RM-CBO-01-LAUNCH5  (1 CBO · $100/day ASSUMED · US · broad · automatic placements · start 00:00 account time)
  optimisation event: booked fit call (Schedule) — PROXY for purchase (sale closes on the phone) — OPERATOR-VALIDATES; deposits/payments fed back as offline Purchase events
  ├─ adset AV7-owner-automate  (min $10/day; 4 ads)
  │    ├─ AV7-A1-your-stores-didn-t-fail-nobo  [CELL-01 · NATIVE_STORY · up to 5 hook text options]
  │    ├─ AV7-A2-it-was-never-do-it-myself-or  [CELL-02 · STATIC · up to 5 hook text options]
  │    ├─ AV7-A3-managed-not-automatic-a-team  [CELL-03 · NATIVE_STORY · up to 5 hook text options]
  │    ├─ AV7-A4-the-builder-s-job-ends-the-d  [CELL-04 · NATIVE_STORY · up to 5 hook text options]
  ├─ adset AV1-store-died  (min $10/day; 4 ads)
  │    ├─ AV1-A1-your-first-store-didn-t-prov  [CELL-05 · NATIVE_STORY · up to 5 hook text options]
  │    ├─ AV1-A2-hundreds-of-clicks-and-zero  [CELL-06 · NATIVE_STORY · up to 5 hook text options]
  │    ├─ AV1-A3-you-re-right-to-guard-your-m  [CELL-07 · STATIC · up to 5 hook text options]
  │    ├─ AV1-A4-the-ones-who-found-a-product  [CELL-08 · NATIVE_STORY · up to 5 hook text options]
  ├─ adset AV4-paycheck-side  (min $10/day; 4 ads)
  │    ├─ AV4-A1-it-wasn-t-a-lack-of-ability  [CELL-09 · NATIVE_STORY · up to 5 hook text options]
  │    ├─ AV4-A2-keep-the-salary-that-s-the-s  [CELL-10 · STATIC · up to 5 hook text options]
  │    ├─ AV4-A3-a-first-store-that-got-one-g  [CELL-11 · NATIVE_STORY · up to 5 hook text options]
  │    ├─ AV4-A4-you-don-t-need-to-be-trained  [CELL-12 · NATIVE_STORY · up to 5 hook text options]
  ├─ adset AV2-paid-got-nothing  (min $10/day; 3 ads)
  │    ├─ AV2-A1-the-burned-stores-went-wrong  [CELL-13 · NATIVE_STORY · up to 5 hook text options]
  │    ├─ AV2-A2-paying-someone-to-build-it-w  [CELL-14 · STATIC · up to 5 hook text options]
  │    ├─ AV2-A3-if-the-money-isn-t-there-yet  [CELL-15 · NATIVE_STORY · up to 5 hook text options]
  ├─ adset AV3-stuck-starter  (min $10/day; 3 ads)
  │    ├─ AV3-A1-the-setup-was-never-your-wal  [CELL-16 · NATIVE_STORY · up to 5 hook text options]
  │    ├─ AV3-A2-what-should-i-sell-is-answe  [CELL-17 · NATIVE_STORY · up to 5 hook text options]
  │    ├─ AV3-A3-one-published-price-and-a-st  [CELL-18 · STATIC · up to 5 hook text options]
```
```json
{
 "campaign": {
  "name": "RM-CBO-01-LAUNCH5",
  "objective": "OUTCOME_LEADS (booked call; proxy — OPERATOR-VALIDATES)",
  "budget_optimization": "CBO",
  "daily_budget_usd": 100,
  "start": "00:00 account time",
  "countries": [
   "US"
  ],
  "placements": "automatic"
 },
 "adsets": [
  {
   "name": "AV7-owner-automate",
   "targeting": "broad, US, 18+",
   "min_daily_spend_usd": 10,
   "ads": [
    {
     "name": "AV7-A1-your-stores-didn-t-fail-nobo",
     "cell": "CELL-01",
     "format": "NATIVE_STORY",
     "hook_options": 5
    },
    {
     "name": "AV7-A2-it-was-never-do-it-myself-or",
     "cell": "CELL-02",
     "format": "STATIC",
     "hook_options": 5
    },
    {
     "name": "AV7-A3-managed-not-automatic-a-team",
     "cell": "CELL-03",
     "format": "NATIVE_STORY",
     "hook_options": 5
    },
    {
     "name": "AV7-A4-the-builder-s-job-ends-the-d",
     "cell": "CELL-04",
     "format": "NATIVE_STORY",
     "hook_options": 5
    }
   ]
  },
  {
   "name": "AV1-store-died",
   "targeting": "broad, US, 18+",
   "min_daily_spend_usd": 10,
   "ads": [
    {
     "name": "AV1-A1-your-first-store-didn-t-prov",
     "cell": "CELL-05",
     "format": "NATIVE_STORY",
     "hook_options": 5
    },
    {
     "name": "AV1-A2-hundreds-of-clicks-and-zero",
     "cell": "CELL-06",
     "format": "NATIVE_STORY",
     "hook_options": 5
    },
    {
     "name": "AV1-A3-you-re-right-to-guard-your-m",
     "cell": "CELL-07",
     "format": "STATIC",
     "hook_options": 5
    },
    {
     "name": "AV1-A4-the-ones-who-found-a-product",
     "cell": "CELL-08",
     "format": "NATIVE_STORY",
     "hook_options": 5
    }
   ]
  },
  {
   "name": "AV4-paycheck-side",
   "targeting": "broad, US, 18+",
   "min_daily_spend_usd": 10,
   "ads": [
    {
     "name": "AV4-A1-it-wasn-t-a-lack-of-ability",
     "cell": "CELL-09",
     "format": "NATIVE_STORY",
     "hook_options": 5
    },
    {
     "name": "AV4-A2-keep-the-salary-that-s-the-s",
     "cell": "CELL-10",
     "format": "STATIC",
     "hook_options": 5
    },
    {
     "name": "AV4-A3-a-first-store-that-got-one-g",
     "cell": "CELL-11",
     "format": "NATIVE_STORY",
     "hook_options": 5
    },
    {
     "name": "AV4-A4-you-don-t-need-to-be-trained",
     "cell": "CELL-12",
     "format": "NATIVE_STORY",
     "hook_options": 5
    }
   ]
  },
  {
   "name": "AV2-paid-got-nothing",
   "targeting": "broad, US, 18+",
   "min_daily_spend_usd": 10,
   "ads": [
    {
     "name": "AV2-A1-the-burned-stores-went-wrong",
     "cell": "CELL-13",
     "format": "NATIVE_STORY",
     "hook_options": 5
    },
    {
     "name": "AV2-A2-paying-someone-to-build-it-w",
     "cell": "CELL-14",
     "format": "STATIC",
     "hook_options": 5
    },
    {
     "name": "AV2-A3-if-the-money-isn-t-there-yet",
     "cell": "CELL-15",
     "format": "NATIVE_STORY",
     "hook_options": 5
    }
   ]
  },
  {
   "name": "AV3-stuck-starter",
   "targeting": "broad, US, 18+",
   "min_daily_spend_usd": 10,
   "ads": [
    {
     "name": "AV3-A1-the-setup-was-never-your-wal",
     "cell": "CELL-16",
     "format": "NATIVE_STORY",
     "hook_options": 5
    },
    {
     "name": "AV3-A2-what-should-i-sell-is-answe",
     "cell": "CELL-17",
     "format": "NATIVE_STORY",
     "hook_options": 5
    },
    {
     "name": "AV3-A3-one-published-price-and-a-st",
     "cell": "CELL-18",
     "format": "STATIC",
     "hook_options": 5
    }
   ]
  }
 ],
 "statics_rule": "one 3-2-2 dynamic set per adset (3 images × 2 primary texts × 2 headlines), max 2 live",
 "build_via": "Meta Ads Manager UI or manage_campaign MCP — NOT executed by this step (no ad-account write authorised)"
}
```
- **N adsets** = min(avatars 5, max_adsets_proxy 5, 5) = **5**; ads 3–5 per adset ✓ (4/4/4/3/3). Budget trims (if the operator funds < $50/day): drop adsets from the END of testing_sequence (AV-03, then AV-02 …), never below one.
- **route_split:** 10 lane per avatar (§1a) + FORMAT PREFERENCE native story (ASSUMED) → natives 13 / statics 5 (72% / 28%); statics are the $50/day pre-check creatives (09 §10) and one per adset.
- **warmup_ladder** (new account ASSUMED): $5/day (day 1) → $15–25 (days 2–3) → $50–100 (days 4–5) → full $100/day; reads begin at full budget.
- **exception_applied: N** — reason: 5 launch avatars (PORTFOLIO) and pooled stage S4; one-adset/angle testing is reserved for stage 1–2 or NARROW portfolios.
`CS-1: adsets 5, ads 18, budget $100/day (min $100 at proxy; $310.71 at purchase level — BELOW), warmup Y, exception N`

## 10 · BUDGET, KPIs, KILL/KEEP/SCALE + DECISION CALENDAR

**Budget rules (code).** Two reads are printed because the sale closes on the phone: purchase level (breakeven $217.50) and the booked-call proxy (T1-only breakeven per booked call $10.36 = 217.50 × 4.76%; target $19.03) — **OPERATOR-VALIDATES** the proxy.
| rule | formula | purchase level | booked-call proxy |
|---|---|---|---|
| campaign_min | max($100/day, 2 × breakeven × N_adsets ÷ 7) | $310.71/day (BELOW the $100 budget → a purchase-optimised test is unfunded) | $100.00/day → $100/day PASS |
| adset_floor | $10 | $10 | $10 |
| read_1 | 72 h | day 3 | day 3 |
| read_2 | day 7 | day 7 | day 7 |
| min_spend_before_cpa_kill | 2 × breakeven per adset | $435.00 (not reachable in 7 d at $20/day) | $20.72 per adset |
| pre_check (new account) | $50/day statics × 3 days | $150 | $150 (09 §10 statics) |
| capacity | daily budget ÷ target CPA | 0.25 purchases/day | 5.25 booked calls/day |

**KPI table**
| metric | natives | statics | video | this product's reference |
|---|---|---|---|---|
| CTR-all | ≥20% | ≥4% | — | — |
| CTR (link) | ≥2.5% | ≥2% | — | 09 truth-test link CTR target 1.5% (floor for a cold avatar read) |
| CPC (link) | <$2 (US) | <$3 | — | US |
| CPM | ≤$80 | ≤$80 | — | high CPM on AV-03/AV-04 = boats (09 §10 cpm_read) |
| cost/ATC → cost per form start | ≤$10 (≤25% of target CPA) | — | — | ≤$4.76 per booking-form start (25% of $19.03, OPERATOR-VALIDATES) |
| buying ratio 10:5:3 (ATC : IC : purchase) | → form start : booked call : deposit | — | — | deposit/paid via offline events; close 4.76% SAMPLE(84) |
| hook rate | — | — | ≥30% (kill <15–25%) | 09 hook_rate_target 0.30 |
| hold | — | — | ≥45% to scale | — |
| booked-call CPA | — | — | — | target ≤$19.03; T1-only guard ≤$10.36 (OPERATOR-VALIDATES) |

**Layer 1 — adset, end of day 3 (multiples of breakeven; event map ATC → booking-form start, purchase → booked call at the proxy)**
| rule | at product breakeven $217.50 (purchase) | at $40 (worked row) | at proxy $10.36 (booked call) |
|---|---|---|---|
| ≥1× spent, zero ATC/form start → OFF | $217.50 | $40.00 | $10.36 |
| ≥2× spent, zero purchase/booked call → OFF | $435.00 | $80.00 | $20.72 |
| CPM ≥$100 after ≥0.5× spent → OFF | $108.75 | $20.00 | $5.18 |
| ≥1 purchase/booked call or ≥2 form starts at KPI → KEEP untouched | — | — | — |
**Day-1 early warning at $50 spend:** CPC > $2 (US) and zero booked calls → Bucket 1 read, prepare replacements; not a cut.
**Layer 2 — ad level in surviving adsets, day 7 from creation, by spend share (the CBO's vote):** BREAKTHROUGH (≥30% of campaign spend under $100K/mo AND the budget can rise) · SPEND WINNER · KPI WINNER (ad booked-call CPA ≤ the campaign's 7-day CPA; leave on) · LOSER (OFF). Never force spend.
**Scale:** ROAS ≥2.5 on 2 consecutive days (read on deposits + paid, offline events) or 2–3 profitable days → +$50 per 48 break-even/profitable hours to $300–500/day, then +20% per 72 h; a variation adset every other day. **Winner confirmed** at $1K spend at target CPA (page-iteration trigger). **Angle death** only after ≥3 executions across ≥2 batches (adset death ≠ angle death). **Product decision** only after 5–8 avatars and ≥2 one-at-a-time fixes at 3-day intervals. **Split tests** start once a winner adset exists; a page/prelander variant runs as a new adset in the same CBO or its own $50/day CBO, read at 2–3 days on buying intent. No ROAS or profit is read from a spy score or an ad's runtime.

**Decision calendar**
| day | decision |
|---|---|
| 0 | warm-up $5 → launch at 00:00; pre-check statics $50/day × 3 d (optional) |
| 1 | early warning at $50 spend (CPC >$2 & 0 booked calls → Bucket 1 read, prepare replacements) |
| 3 | Layer 1 per adset (rules above, proxy thresholds) |
| 4 | variations begin for Bucket-3 adsets (new hooks first) |
| 7 | Layer 2 per ad (spend share); OV-## still locked until a winner adset exists |
| 14 | exit-testing read: surviving adsets → scale rules; dead adsets → next avatar in reserve/expansion only on evidence |

`RULEBOOK: budget rules 7, KPI rows 9, Layer 1 rows 4 + worked rows at $217.50 / $40 / $10.36, Layer 2 labels 4, calendar days 6`

## 11 · BUCKETS + VARIATION SOP

- **Bucket 1** (bad ad metrics, no buying intent): one more day, then replace with the next hook seed of the same cell (hooks 2–5).
- **Bucket 2** (good ad metrics, no intent): check the image for click-bait (scene must be a Behaviour scene, REG-1), then the OFFER (competitor offer +10%: a gift, the guide, the guarantee — never price; GIFT-01..04, object 6), then the page's top-5 pre-buy questions = the T1 crosswalk rows (11 §8: money now, proof first, is it real, total cost, how fast).
- **Bucket 3** (bad ad metrics, intent): variation SOP in order — new hooks → new story same angle → new story + new image → next reserve angle (§12) → next avatar; then the failed-desire ladder: Same Desire → New Entry Point (EM-##) → New Concept → New Angle → New Execution.

## 12 · SECOND-WAVE QUEUE + TRACKING SHEET

| AV | AN-## | premise | frame | territory | executions_tried |
|---|---|---|---|---|---|
| AV-07 | AN-R01 | AF-07 "Your store's first report went unread." (MK-04 the unread first weeks) | mechanism reveal | FRESH | 0 |
| AV-07 | AN-R02 | Your existing brand's products, released in stages on a new store in your name (need_stack "tied to her existing products"; Q-O-0043) — never a takeover claim (DNS-11) | story/transformation | FRESH | 0 |
| AV-01 | AN-R03 | AF-05 "Nobody told you when to stop spending." (MK-03 the bottomless ad budget) | mechanism reveal | FRESH | 0 |
| AV-01 | AN-R04 | AF-04 "The product sold. The supplier didn't." (MK-05 product-first, supplier-second) | social proof/us-vs-them | FRESH | 0 |
| AV-04 | AN-R05 | AF-09 "Every new idea restarted the clock." (MK-26 the idea-hop loop) | mechanism reveal | FRESH | 0 |
| AV-04 | AN-R06 | the family-time motive as a SECONDARY trait inside AV-04 (MD-08 EARLY SIGNAL; operator hypothesis a stays HYPOTHESIS — never its own adset) | story/transformation | FRESH | 0 |
| AV-02 | AN-R07 | AF-03 "Whose name is on your store?" (MK-07 borrowed keys) as a static | bold proclamation | FRESH | 0 |
| AV-02 | AN-R08 | AF-13 "It wasn't a scam. It was a payout hold." (MK-13; NI-05 conditional — OPERATOR-VALIDATES verification step first) | mechanism reveal | FRESH | 0 |
| AV-03 | AN-R09 | AF-12 "10 weeks on 'simple' tasks." (MK-15 the snowstorm setup) | story/transformation | FRESH | 0 |
| AV-03 | AN-R10 | AF-06 "You didn't get stuck. You got the steps out of order." (MK-09 the out-of-order build) | mechanism reveal | FRESH | 0 |
- **expansion_avatars[]:** AV-08 Restart After the Floor Fell (09 expansion_queue 1 — fit 22 < gate; wallet/ethics flag nofund 5/8). **Reserve (UNPROVEN, not tested until their HARVEST closes):** AV-05 Evening-Only Parent (operator hypothesis a — HARVEST-18: a father's own words), AV-06 Fixed-Income Retiree (operator hypothesis b — HARVEST-19; only with a no-advance-payment structure), CL-09 capital holder (HARVEST-21).
- **awareness_rewrite:** the winning cell's story rewritten one awareness level up/down (e.g. AW-4 → AW-3 recognition-first) in its own CBO.
- **prelander_trigger:** $500–1,000/day + ROAS ≥2.5 over 48 h (deposits/paid) → an advertorial built from the winning story, read on buying intent (booked calls).
- **offer_variants:** OV-01 split entry $250 + $250 (CVR to beat 2.21%) · OV-02 $900 Second Shot (1.03%) — §5 object 11; run only after a winner adset exists.
**Tracking sheet header row (19 + 14):**
`AD | Budget | Ad Set Name | Amount Spent | Adds To Cart | Checkouts Initiated | Cost per add to cart | Results | Cost per Results | Purchase ROAS | Purchases Conversion value | CTR (link) | CPC (link) | CPM | Impressions | Frequency | Landing-page-view rate per link-click | Ad Schedule | Date Created | cell_id | avatar | problem | desire | lf8 | angle | UMP | structure | awareness | hypothesis | learning | next_hypothesis | source_type (Iteration | Imitation | Ideation) | result_label`
`WAVE-2: reserve angles 10, expansion avatars 1, OV 2; SHEET: columns 19 + 14`

## 13 · CREATIVE RESEARCH PLAYBOOK

### PART 1 — what the market is saying (06/08/11 objects only; denominators printed; labels per line)
1. **physical experiences:** "I've spent 10 weeks on simple tasks" (Q-F-0013) · "~600 clicks" still no sales (Q-F-0019) — EM-02 5 speakers/1 thread SUPPORTED; EM-06 5/5 VALIDATED · VERBATIM VOC
2. **emotions:** discouragement "it's extremely discouraging and it just makes you want to give up" (Q-Y-0031) · hopelessness "pure loss of money of time of energy of honestly hope" (Q-Y-0047) · resignation (Q-O-0103) · VERBATIM VOC
3. **identity / social consequences:** "I'm tech savvy and competent" (Q-F-0012) · "I definitely was not an expert" (Q-Y-0039) · owner-not-operator "I don't wanna be trained to do it" (Q-O-0056) · VERBATIM VOC
4. **behavioural consequences:** closed the store (Q-O-0108, Q-O-0090) · stores idle "in years" (Q-O-0103) · Googles the company mid-call (Q-O-0102) — FS-01 25 authors (06) · OBSERVED PATTERN
5. **fears:** losing money again (Q-Y-0049) · being scammed (Q-O-0073) · quitting the job (Q-O-0133) · hidden fees (Q-O-0028) · 06 hidden_fears Q-O-0084, Q-O-0125, Q-O-0007 · VERBATIM VOC
6. **tradeoffs:** keep the salary vs start (Q-O-0133) · ad money vs tests (Q-O-0005) · ANALYST INFERENCE
7. **failed solutions:** own store one product (FS-01, 25 authors) → paid a builder (FS-02, 17) → courses/challenges (FS-03) → suppliers/payouts (FS-06, 4) → setup stall (FS-05) — 11 merged FS 20 rows, M-1 explains 9 · OBSERVED PATTERN
8. **objections:** 59 avatar rows, 32 T1; T1 classes: money now, proof first, is it real, total cost, how fast (11 §8) · OBSERVED PATTERN
9. **beliefs:** THE ONE BELIEF ×5: B-03.AV-07 · B-102.AV-01 · B-42.AV-04 · B-02.AV-02 · B-03.AV-03 (11 §3) · ANALYST INFERENCE on VERBATIM VOC
10. **contradictions:** reps' "91 percent … success rate" and "10k a month" vs "We make no income guarantees" (PT-09) → DNS-01/02 · "done for you" 0 of 307 passages vs ads that lead with it → DNS-03 · competitor reviews split 5 positive / 5 negative (06 §16) · "all these … scams" caller who then DEPOSITED (Q-O-0012 → Q-O-0013) · OBSERVED PATTERN
11. **consumer states:** awareness: AV-01/AV-03 AW-2→3; AV-07 AW-4/5; AV-04/AV-02 AW-4 (07/09, SAMPLE(N)) · OBSERVED PATTERN
12. **explicit desires:** "I'm looking for a steady income" (Q-O-0109) · "a stable income flow" (Q-O-0046) · "turn this side hustle into a main job" (Q-O-0105) · "I would just link into the store once it is finished" (Q-F-0005) · VERBATIM VOC
13. **inferred deeper desires:** MD-01 an income that is my own (VALIDATED) · MD-04 build something of my own (VALIDATED) · MD-02 money that works while I ease off (VALIDATED, Tier 3) · ANALYST INFERENCE (08)

### PART 2 — per launch desire (08 final_mass_desires_for_testing: MD-01, MD-04)
**MD-01 An income that isn't hostage to a job (LF8 #1/#3/#5)** — who_feels_it_most: AV-07, AV-04 (and AV-01 via #3) · why_it_matters: the job decides whether they are OK; the store was meant to be the other door (DS-01 "I'm actually thinking to, you know, replace my job" Q-O-0053) · ANALYST INFERENCE
- strongest_verbatim: Q-O-0109 · Q-O-0046 · Q-O-0105 · Q-O-0176 · Q-O-0133 · Q-O-0053 (VERBATIM VOC — text in 06-VOC_MASTER.csv)
- real_openings: OPN-34 (Q-F-0015) · OPN-36 (Q-F-0017) · OPN-06 (Q-F-0006)
- angles (10 fields = Name, Thesis, Existing Belief, Reframe, Core Tension, Supporting VOC, Consumer State, Evidence Strength, Contradicting Evidence, Confidence → see the AN-## card fields in §8: name=id, thesis=premise, existing belief=belief_to_break current (11 §5), reframe=its target, core tension=four forces (§7), supporting VOC=voc_roots, consumer state=awareness_entry, evidence strength=market_validation + proof state, contradicting evidence=11 counterevidence column, confidence=research favorite, not final winner): AN-02, AN-04, AN-06, AN-07, AN-10, AN-11, AN-13, AN-15, AN-18
- entry_points: EM-01 · EM-09 · EM-12 · EM-05
- concepts: SYNTHESIZED CREATIVE IDEA — "the Tuesday-night ledger": his evening hours vs the team's working day, one column each (AN-09) · SYNTHESIZED CREATIVE IDEA — "three quotes on the table": DIY, $5k–$20k, $500 published (AN-02) · SYNTHESIZED CREATIVE IDEA — "keep the badge": a work lanyard on the kitchen table beside the approve-budget screen (AN-10)
- lived_scenes: IB-06 after-hours store (Q-F-0015) · IB-03 "I wish I was doing something else" (Q-O-0096) · IB-19 stores sitting (Q-O-0103) (VERBATIM VOC)
- failed_advice: "quit your job" pitches (IM-14) · "you need more traffic" (EK-07) (OBSERVED PATTERN)
- fears_objections: OBJ-11.AV-04 job risk · OBJ-04 cost rows · OBJ-07 how much rows
- end_state: explicit "a stable income flow" (Q-O-0046) · inferred: the store stops depending on his hours (IB-14 H-05)
**MD-04 Build something of my own — not the one who "almost did" (LF8 #3/#6/#8)** — who_feels_it_most: AV-01, AV-03, AV-02 · why_it_matters: the store they started still does not exist, or died on one try (DS-28 "So many years I've been thinking about it, but I never had time." Q-O-0160) · ANALYST INFERENCE
- strongest_verbatim: Q-O-0153 · Q-F-0013 · Q-F-0006 · Q-Y-0027 · Q-B-0004 · Q-O-0160 · Q-Y-0053 (VERBATIM VOC — text in 06-VOC_MASTER.csv)
- real_openings: OPN-13 (Q-F-0013) · OPN-37 (Q-F-0018) · OPN-42 (Q-Y-0053)
- angles (10 fields = Name, Thesis, Existing Belief, Reframe, Core Tension, Supporting VOC, Consumer State, Evidence Strength, Contradicting Evidence, Confidence → see the AN-## card fields in §8: name=id, thesis=premise, existing belief=belief_to_break current (11 §5), reframe=its target, core tension=four forces (§7), supporting VOC=voc_roots, consumer state=awareness_entry, evidence strength=market_validation + proof state, contradicting evidence=11 counterevidence column, confidence=research favorite, not final winner): AN-05, AN-08, AN-14, AN-16, AN-17
- entry_points: EM-02 · EM-06 · EM-08 · EM-10
- concepts: SYNTHESIZED CREATIVE IDEA — "week ten": a theme-settings screen with a sticky note counting weeks (AN-16) · SYNTHESIZED CREATIVE IDEA — "the second shot": the closed-store email beside a staged-release calendar (AN-05) · SYNTHESIZED CREATIVE IDEA — "whose name is on it": the owner field circled on a login screen (AN-13)
- lived_scenes: IB-17 ten weeks on simple tasks (Q-F-0013) · IB-20 never launched (Q-O-0153) · IB-22 transferred and shut down (Q-F-0018) (VERBATIM VOC)
- failed_advice: "just watch this YouTube tutorial" (09 AV-03 tired_of_hearing) · "find a winning product" (Q-Y-0064) (OBSERVED PATTERN)
- fears_objections: OBJ-02.AV-03 run it on my own · OBJ-101.AV-01 will it sell · OBJ-15.AV-02 will they leave
- end_state: explicit "I would just link into the store once it is finished" (Q-F-0005) · inferred: the thing they started exists and is worked on (IB-25 H-08, IB-29 H-12)

### PART 3 — ammunition library
**Top 50 verbatim phrases** (ranked in code by how often the 5 belief partials cite the Q-##; MARKET_VOC + OWNED_PROOF only; >20 words trimmed with "…"; VERBATIM VOC):
"I had someone build a shopify store for me because I wanted to get started quickly" (Q-F-0018, ×33) · "make it seem like easy money when it's really not" (Q-Y-0016, ×24) · "they said they would build a store, but i am building the store???" (Q-F-0004, ×24) · "I must have three or four Shopify stores just sitting there" (Q-O-0103, ×21) · "I pay $500 and then I'm gonna have to pay more money down the road" (Q-O-0028, ×21) · "I'm a computer consultant and I have very little time." (Q-O-0154, ×20) · "You guys can fully automate my online business" (Q-O-0001, ×19) · "now I can't access it, contact an administrator which should be me" (Q-F-0001, ×19) · "I was afraid to ever try again, but eventually I did" (Q-B-0004, ×18) · "I'm tech savvy and competent. I cannot find a simple step by step" (Q-F-0012, ×18) · "at an exorbitant cost, $5,000, $20,000, $15,000" (Q-O-0104, ×17) · "I work a full time job as well, so am only able to attend to my store after hours" (Q-F-0015, ×17) · "After weeks of overthinking, I finally committed" (Q-Y-0053, ×17) · "I earn good money now, so I don't want to quit and then start struggling." (Q-O-0133, ×17) · "I would just link into the store once it is finished" (Q-F-0005, ×17) · "tons of links that are like a snowstorm of information" (Q-F-0006, ×16) · "i failed the challenge" (Q-Y-0015, ×16) · "if it's gonna take fourteen days how can i take back your money in seven" (Q-O-0030, ×16) · "go do a Google review of your company and see" (Q-O-0102, ×16) · "At what point do I take over the store? Is it something I have to run on my own?" (Q-O-0169, ×15) · "I closed it because I didn't have time to work the business" (Q-O-0090, ×15) · "I would not pay $2,500 to anybody unless I could see some results" (Q-O-0006, ×14) · "seven days is two lesser time. Seven days too. It's not realistic" (Q-O-0047, ×14) · "I'll start with the 500, and then I'll hopefully graduate to the next level" (Q-O-0029, ×13) · "a lot of them fake the reviews" (Q-Y-0032, ×13) · "I thought this call was gonna just show me exactly what the $500 pays for" (Q-O-0002, ×12) · "this coach never even scheduled a call with me" (Q-Y-0019, ×12) · "it takes years to find a winning product" (Q-Y-0064, ×12) · "I had one before. I just ended it because I was dealing with a lot" (Q-O-0097, ×12) · "there's plenty of us losing, including myself" (Q-Y-0027, ×12) · "I want a stable income flow" (Q-O-0046, ×12) · "I don't wanna be trained to do it" (Q-O-0056, ×12) · "a clever Shopify affiliate funnel with a big upsell" (Q-Y-0009, ×11) · "promises of more templates, ads, products etc. after you have paid" (Q-B-0001, ×11) · "anytime that I know that I'm ready ... I'll get back to you" (Q-O-0052, ×11) · "my store didn't even make $20, so I had to come out" (Q-O-0101, ×11) · "10 weeks on simple tasks that the system doesn't verify" (Q-F-0013, ×11) · "on my second attempt and now thinking about trying a different platform" (Q-F-0010, ×11) · "I hired and expert and he did a good job but then it still wasn’t making sales" (Q-F-8303, ×11) · "Is it $500 it's starting from, and it goes up to $5,000 or what?" (Q-O-0155, ×10) · "it isn't all sunshine and rainbows" (Q-Y-0025, ×10) · "Can I review full contract before making payment?" (Q-O-0116, ×10) · "still no sales. i've got ~600 clicks" (Q-F-0019, ×10) · "I’m not sure if migrating to Shopify is something I can handle on my own. Should I hire a developer" (Q-F-9006, ×9) · "i've already lost 500 drop shipping" (Q-Y-0013, ×9) · "I got scammed by the marketing guy." (Q-O-0130, ×9) · "problem of finding winning products is an eyesore" (Q-F-0031, ×9) · "getting profitable traffic is where 90% of beginners fail" (Q-Y-0008, ×9) · "यह एक स्कैम ही है" (Q-Y-0052, ×9) · "I simply can't compete with the likes of H&B, Amazon etc." (Q-F-9008, ×9)

**Organic openings (36 — MARKET + OWNED; competitor-review openings excluded) in the ten style groups** (06 §15 style tags [D]):
- raw emotion (16): OPN-02, OPN-07, OPN-12, OPN-26, OPN-28, OPN-29, OPN-30, OPN-31, OPN-32, OPN-33, OPN-38, OPN-40, OPN-43, OPN-44, OPN-45, OPN-46
- timeline (4): OPN-13, OPN-35, OPN-41, OPN-42
- question (2): OPN-27, OPN-34
- confession (14): OPN-01, OPN-03, OPN-04, OPN-05, OPN-06, OPN-08, OPN-09, OPN-10, OPN-11, OPN-14, OPN-25, OPN-36, OPN-37, OPN-39
- physical evidence (0): NULL — searched: 06 §15 style tags (no opening tagged this style)
- contradiction (0): NULL — searched: 06 §15 style tags (no opening tagged this style)
- frustration (0): NULL — searched: 06 §15 style tags (no opening tagged this style)
- update (0): NULL — searched: 06 §15 style tags (no opening tagged this style)
- reassurance seeking (0): NULL — searched: 06 §15 style tags (no opening tagged this style)
- "I tried everything" (0): NULL — searched: 06 §15 style tags (no opening tagged this style)
- strongest lived scenes: 09 filmable_scenes ×15 (§8 image concepts) · contradictions: Part 1 item 10 · most-repeated failed advice: "find a winning product", "you need more traffic", "watch this tutorial" · solution objections/baggage: "done for you" = a word buyers never use (DNS-03); "hands-free" (DNS-04) · PM-01..PM-13 (06 §15) · things_tired_of_hearing: $5k–$20k quotes (AV-07) · easy-money content (AV-01) · courses that train you (AV-04) · free/cheap stores with upsells (AV-02) · tutorials and bots (AV-03).

### 13 QC checks
| # | check | result |
|---|---|---|
| 1 | no synthesized line presented as verbatim | PASS — concepts labelled SYNTHESIZED; hooks marked SYNTHESIZED with verbatim lines quoted |
| 2 | no single-poster overcount (authors, not comments) | PASS — denominators carried from 06/11 author counts |
| 3 | outcomes ≠ desires | PASS — MD-## are desires; outcomes (a store live, a review) are proof |
| 4 | problem states ≠ angles | PASS — PP-## and AN-## kept apart |
| 5 | "I tried everything" ≠ an angle | PASS — used as an opening style group only |
| 6 | every angle answers the six questions | FIXED — mapped via the 10-field crosswalk to 11 objects (belief, reframe, tension, who, what tried, identity fear) |
| 7 | contradicting evidence kept | PASS — 11 counterevidence + Part 1 item 10 |
| 8 | every conclusion traces to IDs | PASS |
| 9 | openings sound like the platform | PASS — forum/YouTube first sentences verbatim |
| 10 | synthesized concepts labelled | PASS |
| 11 | usable by a human | PASS |
| 12 | usable by an LLM | PASS — IDs + JSON in handoff.json |
| 13 | concise | FIXED — full belief text left in 11-BELIEFS.md; pointers here |

### Static + story prompt inputs
- **Statics:** `(x number)` = the avatar's own number (~600 clicks Q-F-0019; 10 weeks Q-F-0013; 3–4 stores Q-O-0103; $5k–$20k Q-O-0104; $4,500 Q-O-0062) · `(avatar)` = adset persona tag · `(awareness level)` = cell awareness_entry · named scenarios = 09 filmable_scenes · plain outcome verbs: built, opened in your name, tested, reviewed, replaced, approved — DNS words never as outcomes.
- **Stories:** 2–3 supported prior attempts per avatar = FS-## sequence (11 §9) · the five hook classes (§8 hook_seeds) · discovery frame **A independent research** (13 STORY-1 stamp) · 1,200–1,700 words · hero (Readymerce) placed ≥60% in, after the solution requirement (11 GO-AV#).
`PLAYBOOK: verbatim 50/50, openings 36/30–50, desires 2/≤5, angles 18, concepts 6, QC 13/13, words 2341`

## 14 · RESEARCH → AD CONTRACT (writer_handoff[AV])

### writer_handoff[AV-07] · The Owner Who Wants It Automated ★
| # | field | value |
|---|---|---|
| 1 | persona_tag | AV7-owner-automate — runs a business; 3–4 stores built and "just sitting there" (Q-O-0103) |
| 2 | awareness_level + tired_of_hearing | AW-4/5 · tired: $5k–$20k agency quotes (Q-O-0104); "fully automated/hands-free" as a claim (DNS-04) |
| 3 | activation_moment | TR-AV-07 struggling_moment (EM-09; Q-O-0124, Q-O-0103) |
| 4 | conversation_in_head[] | Q-O-0103 · Q-O-0001 · Q-O-0104 · Q-O-0006 · Q-O-0028 · Q-O-0027 · Q-O-0029 · Q-O-0154 |
| 5 | failed_solutions_sequence[] | FS-01.AV-07 → FS-06.AV-07 → FS-02.AV-07 |
| 6 | belief_to_break | B-03.AV-07 (THE ONE) · FB-AV-07 |
| 7 | ump_ums_plain | M-1: the builder's job ends the day the store goes live · M-2: a team keeps working it after — review first results, fix, test the next product on a budget you approve (10 LOCK-B) |
| 8 | enemy | EN-1 the build-and-leave store deal (13) + industry pricing ($5k–$20k, WM-AV-07) |
| 9 | gradualization_ladder | GO-AV-07 · lane_applied S1–2 reset claim + Name-it, proof-led · BS-AV-07 B-01 → B-02 → B-05 → B-06 → B-03 → B-04 → final |
| 10 | proof_ranked[] | P-08.AV-07 [A] · P-09.AV-07 [A] · P-01.AV-07 · P-04.AV-07 · P-05.AV-07 · P-06.AV-07 · P-03.AV-07 (close only) |
| 11 | objections_even_if[] + jtbd_forces | OBJ-02.AV-07 · OBJ-04.AV-07 · OBJ-12.AV-07 · OBJ-07.AV-07 (even_if lines 11 §8) · forces TR-AV-07 |
| 12 | day_after_picture | deeper hope Q-O-0105 + H-09 (IB-26) |
| 13 | offer_summary | T1 "Start with the $500 Build" → OTO1 T2 "The Second-Shot Launch" $2,000 (§5) |
| 14 | cost_of_inaction | UNQUANTIFIED (TR-AV-07) |
| 15 | behaviour_scenes[3] + tribe_aesthetic | 09 AV-07 scenes 1–3 (S07-1..3) · TRIBE-1 role_wanted: acknowledgment as the owner (13 §13) |
| 16 | lane + strategic_frame | LOCK-B lane (§1a) · frames F1/F3/F2/F4 (CELL-01..04) |
| 17 | message_match_words | problem "one shot; left on launch day" · mechanism "in stages; a budget you approve" · promise "in your name; we stay after launch day" (13) |
| 18 | primary_buying_reason | someone stays on the store after it goes live, at a published first step (B-03.AV-07; Q-O-0029) |
| 19 | practical_change | the idle store gets a weekly review → fix → test cycle he approves (PT-04, F-05) |
| 20 | everyday_transformation | IB-26 H-09 "One of the three or four stores that sat 'ready to be loaded' is loaded and switched on." |
| 21 | benefit_statement_for_copy | [AUTHORED, CHECK THIS] "Your store gets worked every week after it goes live — you approve the budget and read the report." (CLM-01, CLM-03) |
| 22 | copy_emphasis | proof-led; show the package (Q-O-0002); price first; managed, not automatic (B-04.AV-07) |
| 23 | customer_language[] | "just sitting there" · "the backend" · "the 500" · "automate" · "my brand" · "seriously? Come on." |
| 24 | narrator_material | peer owner (13 NAR-1, SUPPORTED): Q-O-0103, Q-O-0097 lived lines · insider store manager REAL only |
| 25 | alternative_connection | DIY vs $5k–$20k agency vs published $500 (B-03.AV-07; EK-09.AV-07) |
| 26 | open_questions[] | post-launch window per tier (PT-08) · existing-store takeover (OBJ-18.AV-07) · managed-fee range (PT-02) · local stage (HARVEST-20) |
`CONTRACT: AV-07 filled 26/26, authored 1, STRANGER PASS`
**STRANGER TEST — PASS** (six artefacts, each from fields with IDs, no customer fact invented): 3 hooks ← hook_seeds of CELL-01, CELL-02 · 1 recognition section ← conversation_in_head + behaviour_scenes · 1 mechanism explanation ← ump_ums_plain + B-03.AV-07 proof_ranked · 1 comparison ← alternative_connection + CLM-## · 1 proof placement ← proof_ranked (demonstration first, guarantee last) + EB-AV-07 · 1 offer close ← offer_summary + §5 offer_beat. Condition printed: the guarantee wording is OPERATOR-VALIDATES; demonstrations are SHOOTABLE-NOW [A].

### writer_handoff[AV-01] · The Store That Died
| # | field | value |
|---|---|---|
| 1 | persona_tag | AV1-store-died — first store(s) closed after one product / one batch (Q-O-0108, Q-F-9004) |
| 2 | awareness_level + tired_of_hearing | AW-2→3 · tired: easy-money guru content (Q-Y-0016); "winning product" promises |
| 3 | activation_moment | TR-AV-01 struggling_moment (EM-06/EM-07; Q-F-0019, Q-Y-0014) |
| 4 | conversation_in_head[] | Q-O-0108 · Q-F-9004 · Q-Y-0027 · Q-F-0022 · Q-Y-0016 · Q-Y-0030 · Q-O-0112 · Q-Y-0049 |
| 5 | failed_solutions_sequence[] | FS-01.AV-01 → FS-101.AV-01 → FS-102.AV-01 → FS-03.AV-01 |
| 6 | belief_to_break | B-102.AV-01 (THE ONE) · FB-AV-01 |
| 7 | ump_ums_plain | M-1: a first store is launched as a single bet and written off when the guess misses · M-2: products released in stages, each tested on a budget he approves, an early review replaces what doesn't sell (10 LOCK-A) |
| 8 | enemy | the one-shot launch (familiar solution, E-B 13) + easy-money store videos (industry) |
| 9 | gradualization_ladder | GO-AV-01 · New Information → mechanism described · BS-AV-01 B-106 → B-101 → B-105 → B-107 → B-102 → requirement → B-103 → B-104 → final |
| 10 | proof_ranked[] | P-103.AV-01 [A] · P-106.AV-01 · P-104.AV-01 · P-105.AV-01 · P-101.AV-01 · P-109.AV-01 · P-107.AV-01 (close only) |
| 11 | objections_even_if[] + jtbd_forces | OBJ-101.AV-01 · OBJ-102.AV-01 · OBJ-04.AV-01 · OBJ-01.AV-01 (LEAK) · forces TR-AV-01 |
| 12 | day_after_picture | deeper hope Q-Y-0027 + H-12 (IB-29) |
| 13 | offer_summary | T1 $500 Build (+ bump +2 first-wave products $149) → OV-02 $900 Second Shot after a winner (§5) |
| 14 | cost_of_inaction | $41,754 summed past losses, SAMPLE(4), median $750 (TR-AV-01) |
| 15 | behaviour_scenes[3] + tribe_aesthetic | 09 AV-01 scenes 1–3 (S01-1..3) · TRIBE-1 aesthetic_already_used: the post-mortem format (13 §13) |
| 16 | lane + strategic_frame | LOCK-A New Information (§1a) · frames F1/F2/F5/F4 (CELL-05..08) |
| 17 | message_match_words | problem "one shot" · mechanism "in stages; a budget you approve" · promise "in your name" (13) |
| 18 | primary_buying_reason | a second try made of several small capped tries (FB-AV-01; Q-O-0109) |
| 19 | practical_change | products go live in turns, each with a capped test he approves (PT-04, F-05) |
| 20 | everyday_transformation | IB-29 H-12 "The store is handed over and stays up; the access is theirs." |
| 21 | benefit_statement_for_copy | [AUTHORED, CHECK THIS] "Your store gets more than one shot — several products, each tested small on a budget you approve." (CLM-03, CLM-05) |
| 22 | copy_emphasis | agree first (not easy money); new information before mechanism; every cost before benefit |
| 23 | customer_language[] | "still no sales" · "didn't sell one product" · "I had to close the store" · "burned many times" · "throwing cash off a cliff" |
| 24 | narrator_material | peer who lost on a first store (Q-Y-0027, Q-Y-0026 veteran lines, creator attribution) — 13 peer narrator |
| 25 | alternative_connection | one store tweaked alone vs several capped tries (OBJ-106.AV-01; FS-101/102.AV-01) |
| 26 | open_questions[] | products per stage (PT-19) · test budget + stop rule · local stage (HARVEST-14) · owned converted 0 of 5 |
`CONTRACT: AV-01 filled 26/26, authored 1, STRANGER PASS`
**STRANGER TEST — PASS** (six artefacts, each from fields with IDs, no customer fact invented): 3 hooks ← hook_seeds of CELL-05, CELL-06 · 1 recognition section ← conversation_in_head + behaviour_scenes · 1 mechanism explanation ← ump_ums_plain + B-102.AV-01 proof_ranked · 1 comparison ← alternative_connection + CLM-## · 1 proof placement ← proof_ranked (demonstration first, guarantee last) + EB-AV-01 · 1 offer close ← offer_summary + §5 offer_beat. Condition printed: the guarantee wording is OPERATOR-VALIDATES; demonstrations are SHOOTABLE-NOW [A].

### writer_handoff[AV-04] · The Paycheck-Tethered Builder
| # | field | value |
|---|---|---|
| 1 | persona_tag | AV4-paycheck-side — full-time job; store gets the leftover hours (Q-F-0015) |
| 2 | awareness_level + tired_of_hearing | AW-4 · tired: courses that train you (Q-O-0056) |
| 3 | activation_moment | TR-AV-04 struggling_moment (EM-01; Q-F-0015, Q-O-0116) |
| 4 | conversation_in_head[] | Q-F-0015 · Q-O-0133 · Q-O-0052 · Q-O-0056 · Q-O-0046 · Q-O-0176 · Q-O-0116 · Q-O-0090 |
| 5 | failed_solutions_sequence[] | FS-05.AV-04 → FS-01.AV-04 → FS-41.AV-04 (11 §9 AV-04 block) |
| 6 | belief_to_break | B-42.AV-04 (THE ONE, live wire honoured) · FB-AV-04 |
| 7 | ump_ums_plain | M-1: the first store is launched as one bet — for a salaried person the bet feels like the salary · M-2: small capped tests he approves, run by a team, early review (10 LOCK-A) |
| 8 | enemy | the one-guess all-at-once launch + quit-your-job pitch + courses that train you (11 WM-AV-04) |
| 9 | gradualization_ladder | GO-AV-04 · S4 surer + New Information · causal chain B-41 → … → requirement → product (11 §7) |
| 10 | proof_ranked[] | P-07.AV-04 [A] · P-08.AV-04 [A] · P-01.AV-04 · P-05.AV-04 · P-04.AV-04 · P-02.AV-04 · P-03.AV-04 (close only) |
| 11 | objections_even_if[] + jtbd_forces | OBJ-11.AV-04 · OBJ-04.AV-04 · OBJ-41.AV-04 · OBJ-03.AV-04 (LEAK) · forces TR-AV-04 |
| 12 | day_after_picture | deeper hope Q-O-0176 + H-05 (IB-14) |
| 13 | offer_summary | T1 $500 Build, keep the job (§5) → OV-01 split entry after a winner |
| 14 | cost_of_inaction | UNQUANTIFIED (TR-AV-04) |
| 15 | behaviour_scenes[3] + tribe_aesthetic | 09 AV-04 scenes 1–3 (S04-1..3) · TRIBE-1 identity_permission "I'm not lazy. I just don't wanna be trained to do it." |
| 16 | lane + strategic_frame | LOCK-A S4 surer (§1a) · frames F4/F3/F5/F1 (CELL-09..12) |
| 17 | message_match_words | problem "one shot" · mechanism "a budget you approve" · promise "in your name" (13) |
| 18 | primary_buying_reason | start now without betting the salary (B-42.AV-04; Q-O-0133) |
| 19 | practical_change | the store's tests run in the team's day, not his evenings (B-41.AV-04) |
| 20 | everyday_transformation | IB-14 H-05 "The store stops being an after-hours-and-weekends job." |
| 21 | benefit_statement_for_copy | [AUTHORED, CHECK THIS] "Keep the salary. Your store starts on small tests you approve, run in our working day — not your evenings." (CLM-03) |
| 22 | copy_emphasis | keep-the-job honoured in every line; terms and refund conditions on paper (procedural sceptic) |
| 23 | customer_language[] | "side hustle" · "replace my job" · "a stable income flow" · "I don't wanna be trained" · "when I'm ready" |
| 24 | narrator_material | employed peer (PLANNED: consented account from PAID buyer O-5455cbcf — P-09.AV-04) · until then peer lines Q-F-0015/16/17 |
| 25 | alternative_connection | evenings + courses vs a team running capped tests (FS-05.AV-04; OBJ-44.AV-04) |
| 26 | open_questions[] | B-44.AV-04 people-like-me proof (LEAK) · products per stage (PT-19) · local stage S4 HYPOTHESIS (HARVEST-17) |
`CONTRACT: AV-04 filled 26/26, authored 1, STRANGER PASS`
**STRANGER TEST — PASS** (six artefacts, each from fields with IDs, no customer fact invented): 3 hooks ← hook_seeds of CELL-09, CELL-10 · 1 recognition section ← conversation_in_head + behaviour_scenes · 1 mechanism explanation ← ump_ums_plain + B-42.AV-04 proof_ranked · 1 comparison ← alternative_connection + CLM-## · 1 proof placement ← proof_ranked (demonstration first, guarantee last) + EB-AV-04 · 1 offer close ← offer_summary + §5 offer_beat. Condition printed: the guarantee wording is OPERATOR-VALIDATES; demonstrations are SHOOTABLE-NOW [A].

### writer_handoff[AV-02] · Paid-and-Got-Nothing
| # | field | value |
|---|---|---|
| 1 | persona_tag | AV2-paid-got-nothing — paid a builder/vendor, got a half-done or locked store (Q-F-0004, Q-O-0062) |
| 2 | awareness_level + tired_of_hearing | AW-4 · tired: free/cheap stores with big upsells (Q-Y-0009); fake social proof (Q-Y-0005) |
| 3 | activation_moment | TR-AV-02 struggling_moment (EM-03; Q-F-0001, Q-O-0102) |
| 4 | conversation_in_head[] | Q-F-0001 · Q-F-0004 · Q-O-0062 · Q-O-0073 · Q-O-0102 · Q-O-0132 · Q-O-0116 · Q-F-0005 |
| 5 | failed_solutions_sequence[] | FS-02.AV-02 → FS-X2.AV-02 → FS-03.AV-02 → FS-04.AV-02 (11 §9) |
| 6 | belief_to_break | B-02.AV-02 (THE ONE) · FB-AV-02 |
| 7 | ump_ums_plain | M-1: the build is sold as the finish line and the store sits in the builder's account until handover · M-2: store opened in your name from day one; a team keeps working after launch (10 LOCK-B + F-11) |
| 8 | enemy | EN-1 build-and-leave + the store held in the builder's account + pressure closes / fake proof (11 WM-AV-02) |
| 9 | gradualization_ladder | GO-AV-02 · S4 surer + NI-04 · contradiction route (11 §6–7) |
| 10 | proof_ranked[] | P-01.AV-02 [A] · P-14.AV-02 [A] · P-03.AV-02 · P-05.AV-02 · P-06.AV-02 · P-02.AV-02 · P-04.AV-02 (close only) |
| 11 | objections_even_if[] + jtbd_forces | OBJ-03.AV-02 · OBJ-13.AV-02 (LEAK) · OBJ-02.AV-02 · OBJ-15.AV-02 (LEAK) · forces TR-AV-02 |
| 12 | day_after_picture | deeper hope Q-F-0005 + H-12 (IB-29) |
| 13 | offer_summary | T1 $500 Build + GIFT-01 every cost in writing + 60-day deliverables guarantee (OPERATOR-VALIDATES) (§5) |
| 14 | cost_of_inaction | $5,500 already lost/stuck [R-OWNED] (TR-AV-02) |
| 15 | behaviour_scenes[3] + tribe_aesthetic | 09 AV-02 scenes 1–3 (S02-1..3) · TRIBE-1 inauthenticity risks: actors as owners, income screenshots |
| 16 | lane + strategic_frame | LOCK-B + NI-04 (§1a) · frames F2/F4/F5 (CELL-13..15) |
| 17 | message_match_words | problem "left on launch day" · mechanism "a budget you approve" · promise "in your name; we stay after launch day" (13) |
| 18 | primary_buying_reason | a store she can check — her name on it, a team still on it after launch (B-02.AV-02) |
| 19 | practical_change | she logs in and sees her own name in the owner field (CLM-02; P-01.AV-02 [A]) |
| 20 | everyday_transformation | IB-29 H-12 "The store is handed over and stays up; the access is theirs." |
| 21 | benefit_statement_for_copy | [AUTHORED, CHECK THIS] "Check two things before you pay anyone: whose name the store is in, and who is still working on it the week after it goes live." (GO-AV-02 solution_requirement) |
| 22 | copy_emphasis | confirm the suspicion first; checks she runs herself; no bare "trust us" (DNS-16) |
| 23 | customer_language[] | "scam" · "they took my money" · "half-ass done" · "contact an administrator" · "proof of concept" |
| 24 | narrator_material | peer who was burned and checked (Q-O-0013 DEPOSIT after "all these scams" — outcome row, not a testimonial) |
| 25 | alternative_connection | the builder-held store vs a store in your name (CLM-10, CLM-02) |
| 26 | open_questions[] | independent reviews = 0 (P-12.AV-02 PLANNED) · PT-16 trust scores · post-launch window (PT-08) · local stage (HARVEST-15) |
`CONTRACT: AV-02 filled 26/26, authored 1, STRANGER PASS`
**STRANGER TEST — PASS** (six artefacts, each from fields with IDs, no customer fact invented): 3 hooks ← hook_seeds of CELL-13, CELL-14 · 1 recognition section ← conversation_in_head + behaviour_scenes · 1 mechanism explanation ← ump_ums_plain + B-02.AV-02 proof_ranked · 1 comparison ← alternative_connection + CLM-## · 1 proof placement ← proof_ranked (demonstration first, guarantee last) + EB-AV-02 · 1 offer close ← offer_summary + §5 offer_beat. Condition printed: the guarantee wording is OPERATOR-VALIDATES; demonstrations are SHOOTABLE-NOW [A].

### writer_handoff[AV-03] · The Stuck Starter
| # | field | value |
|---|---|---|
| 1 | persona_tag | AV3-stuck-starter — weeks in the setup or stuck on the product pick (Q-F-0013, Q-F-0041) |
| 2 | awareness_level + tired_of_hearing | AW-2/3 (AW-4 on calls) · tired: "just watch this YouTube tutorial"; bots and support chats (Q-F-0011) |
| 3 | activation_moment | TR-AV-03 struggling_moment (EM-02/EM-10; Q-F-0013, Q-F-0041) |
| 4 | conversation_in_head[] | Q-F-0013 · Q-F-0006 · Q-F-0012 · Q-F-0040 · Q-F-0041 · Q-O-0153 · Q-O-0002 · Q-O-0015 |
| 5 | failed_solutions_sequence[] | FS-05.AV-03 → FS-01.AV-03 → FS-02.AV-03 → FS-06.AV-03 (11 §9) |
| 6 | belief_to_break | B-03.AV-03 (THE ONE) · FB-AV-03 |
| 7 | ump_ums_plain | M-1: the builder hands the store over on launch day and leaves · M-2: a team stays after it goes live — first results read, corrections, products rolled in (10 LOCK-B) |
| 8 | enemy | build-and-leave + the platform help system + the "it's easy" promise (11 WM-AV-03) |
| 9 | gradualization_ladder | GO-AV-03 · S2 Name-it mechanism first · yes-but-incomplete route (11 §6–7) |
| 10 | proof_ranked[] | P-01.AV-03 [A] · P-02.AV-03 · P-04.AV-03 · P-05.AV-03 · P-07.AV-03 · P-10.AV-03 · P-06.AV-03 (close only) |
| 11 | objections_even_if[] + jtbd_forces | OBJ-01.AV-03 · OBJ-02.AV-03 · OBJ-05.AV-03 · OBJ-06.AV-03 · forces TR-AV-03 |
| 12 | day_after_picture | deeper hope Q-O-0015 + H-10 (IB-27) |
| 13 | offer_summary | T1 $500 Build + GIFT-02 guide (§5) |
| 14 | cost_of_inaction | UNQUANTIFIED — time only (TR-AV-03) |
| 15 | behaviour_scenes[3] + tribe_aesthetic | 09 AV-03 scenes 1–3 (S03-1..3) · TRIBE-1 role_wanted: owner, not student |
| 16 | lane + strategic_frame | LOCK-B S2 Name-it (§1a) · frames F2/F1/F3 (CELL-16..18) |
| 17 | message_match_words | problem "left on launch day" · mechanism "in stages" · promise "we stay after launch day" (13) |
| 18 | primary_buying_reason | the store finally exists — and is not left alone after it goes live (B-03.AV-03) |
| 19 | practical_change | no more weeks in the settings; listings, payments, shipping configured (F-01, CLM-13) |
| 20 | everyday_transformation | IB-27 H-10 "An evening with no help-doc marathon — the listings are already up." |
| 21 | benefit_statement_for_copy | [AUTHORED, CHECK THIS] "We build it in your name. Then we stay after it opens." (13 POS-1 stranger_safe_line) |
| 22 | copy_emphasis | name the mechanism before the claim (OWNED pond); honour "tech savvy and competent" |
| 23 | customer_language[] | "a snowstorm of information" · "a simple step by step" · "what I should sell" · "No wonder people give up" · "10 weeks on simple tasks" |
| 24 | narrator_material | peer who stalled at setup (Q-F-0012, Q-F-0013 forum voices) — 13 peer narrator |
| 25 | alternative_connection | tutorials/DIY vs a builder who leaves vs a team that stays (FS-05/FS-02.AV-03) |
| 26 | open_questions[] | FS-05 elimination INCOMPLETE (pre-launch stall) · post-launch window (PT-08) · build-day range on the PDP · fish UNSIZED (HARVEST-16) |
`CONTRACT: AV-03 filled 26/26, authored 1, STRANGER PASS`
**STRANGER TEST — PASS** (six artefacts, each from fields with IDs, no customer fact invented): 3 hooks ← hook_seeds of CELL-16, CELL-17 · 1 recognition section ← conversation_in_head + behaviour_scenes · 1 mechanism explanation ← ump_ums_plain + B-03.AV-03 proof_ranked · 1 comparison ← alternative_connection + CLM-## · 1 proof placement ← proof_ranked (demonstration first, guarantee last) + EB-AV-03 · 1 offer close ← offer_summary + §5 offer_beat. Condition printed: the guarantee wording is OPERATOR-VALIDATES; demonstrations are SHOOTABLE-NOW [A].

## 15 · HANDOFF SUMMARY + PATCH NOTE

- `handoff.json` v2 — **65 required keys present** (every §7 key; empty arrays allowed: `claims_register: []`) + `schema_lint` + `patch_note`; `generated_at` 2026-09-24T23:14Z; brand keys from `13-HANDOFF.json` (brand_name Readymerce PROVISIONAL, positioning, narrator peer owner, identity palette/fonts/elements); 13 fact-sheet copy: 5 late-bound rows filled (12.offer, 12.route, 11.*) — `13-BRAND.md` untouched.
- **schema lint (code):** tiered 36 / untiered 13 / [A] 15 over the 64 content keys (`coverage_statement` itself not linted; per-key in `handoff.json.schema_lint`).
- *"PATCH NOTE — this handoff emits `claims_register: []` and `ready_for_P3: "OPERATOR-CLEARED"`. The page prompt and the ad prompt take a one-line input patch: accept `claims_register: []` when `claims_ranked[]` is present; treat `ready_for_P3: OPERATOR-CLEARED` as YES."*
`HANDOFF: keys 65/65, tiered 36 / untiered 13 / [A] 15, version 2, patch note Y`

## 16 · COUNTERS + WHAT WE COULD NOT VERIFY

**Counters:** `INPUTS: files 9/9 + 13` · `MERGE: partials 5, BD-1 5 → 1, CLM 41 → 17, DNS 55 → 19, ledger 251/290, 13 present` · `TR: 5/5, forces with Q 20/20, cost_of_inaction quantified 2/5` · `AN: 18 (+10 reserve), frames/avatar min 3, awareness/avatar min 2, collisions swapped 11, similarity max 20%` · `CELLS: 18 (READY 18 / FLAGGED 0), clamp [15–25]` · `CS-1: adsets 5, ads 18, $100/day, warmup Y, exception N` · `WAVE-2: reserve 10, expansion 1, OV 2; SHEET 19 + 14` · `PLAYBOOK: verbatim 50, openings 36, desires 2, angles 18, concepts 6, QC 13/13` · `CONTRACT: AV-07 26/26, authored 1, STRANGER PASS` · `CONTRACT: AV-01 26/26, authored 1, STRANGER PASS` · `CONTRACT: AV-04 26/26, authored 1, STRANGER PASS` · `CONTRACT: AV-02 26/26, authored 1, STRANGER PASS` · `CONTRACT: AV-03 26/26, authored 1, STRANGER PASS` · `HANDOFF: keys 65/65, version 2, patch note Y` · spend this step $0.

| item | token | cost to close |
|---|---|---|
| purchase-level capacity | testable_concepts 0 / max_adsets 0 → booked-call proxy (close 4.76% SAMPLE(84)) — OPERATOR-VALIDATES | operator confirms the proxy or funds ≥$310.71/day ($0 research) |
| T2/T3 prices, bump/OTO prices | INFERRED — OPERATOR-VALIDATES | operator price decision ($0) |
| guarantee redesign | OPERATOR-VALIDATES + legal (replaces PT-15) | operator + legal review |
| build 7–10 days | [R-OWNED] T-09 only, not on the PDP — OPERATOR-VALIDATES | publish the day range ($0) |
| post-launch window | UNKNOWN — PT-08 "agreed on the fit call" | one operator decision ($0) |
| products per stage, test budget, stop rule | UNKNOWN — PT-19, PT-05 | one operator message ($0) |
| Readymerce outcome proof | NULL — searched: PT-03, PT-06, PT-07, PT-18 | one consenting client report (weeks) |
| demonstrations | SHOOTABLE-NOW [A] (build access ASSUMED) | ≈1 operator hour screen recording ($0) |
| LEAK lines | OBJ-01.AV-01 (no payment plan → OV-01) · OBJ-02 results half (AV-07/01/02) · OBJ-07.AV-07 · OBJ-03.AV-04 / OBJ-13.AV-02 legitimacy · OBJ-15.AV-02 + OBJ-04.AV-02 · B-44.AV-04 people-like-me | see 11 §17 costs |
| cost_of_inaction | UNQUANTIFIED for AV-07, AV-04, AV-03 | owned-call wallet re-read (HARVEST-19/20) |
| local stages | UNSCANNED AV-07 (n=0), AV-01/AV-02 (n<5); AV-04 S4 HYPOTHESIS | HARVEST-14/15/17/20 pastes ($0–$0.30) |
| brand name | PROVISIONAL — USPTO NOT FETCHED (13) | operator registry search ($0) |
| reserve avatars AV-05/AV-06 | UNPROVEN — operator hypotheses stay HYPOTHESIS | HARVEST-18/19 (fathers' own words; wallet) |
| Reddit / Trustpilot lanes | BLOCKED-ON-TOOL (Apify limit; not retrievable) | OPERATOR-PASTE of the listed URLs (09 §11) |
| existing-store takeover | UNRESOLVED (OBJ-18.AV-07; DNS-11) | operator capability statement ($0) |
| FLAGGED cells | none (18/18 READY) | — |

## COVERAGE STATEMENT

Offer: ACCEPTABLE, benchmark networks 1, anchor COGS-multiple 2.06× (GIVEN $500; BAND: NULL), price given (T1) / INFERRED (T2, T3), tiers valid Y, subscription not preselected, urgency NONE. Economics: target CPA $399.56, breakeven $217.50, CM/order $399.56, AOV ratio 1.73 ACCEPTABLE, testable concepts 0 (booked-call proxy 18, OPERATOR-VALIDATES), max adsets 0 (proxy 5, OPERATOR-VALIDATES). Merge: 5 partials → 11-BELIEFS.md. Test plan: 5 adsets × 3–4 ads = 18 cells (READY 18 / FLAGGED 0), budget $100/day, decisions day 3/7. Playbook: 50 verbatim, 36 openings, 18 angles, QC 13/13. Contract: filled AV-07 26/26, AV-01 26/26, AV-04 26/26, AV-02 26/26, AV-03 26/26; STRANGER TEST PASS. Handoff: 65 keys, version 2, late-bound [none from 11/13; OPERATOR-VALIDATES: booked-call proxy, 60-day guarantee, T2/T3 + complement prices, build 7–10 days; 13.name_status PROVISIONAL], patch note present. Weakest link: zero Readymerce outcome proof plus a purchase-level test the $100/day budget cannot fund — the whole plan rides a booked-call proxy built on 4 closes in 84 seller-contacted calls; cost to close: operator confirms the proxy + publishes the post-launch window and per-stage product count ($0), one ≈1-hour demo shoot ($0), one consenting client's post-launch report (weeks after a first sale). No ROAS or profit is read from a spy score or an ad's runtime; paid testing decides.
