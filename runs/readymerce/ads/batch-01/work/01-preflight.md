# 01 · A1b Commercial Pre-flight · Readymerce ads batch-01 · P1 SLATE

Reported, not blocking (A1b). Every number below is copied from `foundation/handoff.json` (offer_architecture, margin_sanity, budget_rules, kpi_table, campaign_structure) or 01 §TRUTH CARD; nothing re-derived from memory.

## Flag summary

| # | check | verdict | one line |
|---|---|---|---|
| 1 | Offer vs cold-traffic cost | **FLAG (RED)** | $500 single with contribution $213.50 sits $4.00 BELOW the $217.50 breakeven CPA and $186.06 below the $399.56 target; at $100/day the purchase-level test capacity is 0 concepts; the batch can only be read on the booked-call proxy ($19.03, T1 guard $10.36, OPERATOR-VALIDATES). |
| 2 | Price match | **PASS with rules** | Only "$500 one-time" (PT-01, F-12) is live. T2 $2,000 / T3 $3,000 / bump $149 / OTOs / Keep-Running $550/mo / 60-day guarantee / "7–10 days" are INFERRED or OPERATOR-VALIDATES and stay out of every ad. |
| 3 | Page congruency | **FLAG (AMBER)** | /what-you-get carries "in your name", "staged (not single-drop) product release", "budgets you approve", "early performance review", "post-launch corrections"; the live page does NOT carry "one shot" or "we stay after launch day", and the home hero is the dark "operator console" register (13 §6 page_register) = a register break after a candid native ad. Recommend a short congruence lander (below). |
| 4 | Tracking | **FLAG (UNKNOWN)** | Pixel / Conversions API on readymerce.com cannot be verified from this runtime (no fetch); the booked-call conversion event and the offline PAID/DEPOSIT upload the proxy depends on are unconfirmed; no Meta ad account is named for Readymerce's own marketing (00-ADS-STATUS.md). |

## 1 · Offer vs cold-traffic cost

| figure | value | source |
|---|---|---|
| single (only live price) | **$500** one-time, "The Store Build & Research Package" | PT-01, F-12 (GIVEN) |
| landed COGS | ≈ $243 (2.06× multiple) | ADS-BRIEF-COMMON A1 #1; 12 §3 INFERRED labour basis |
| T1 contribution | $213.50 | handoff.json margin_sanity.T1_contribution |
| breakeven CPA | $217.50 | offer_architecture.breakeven_cpa |
| target CPA (locked) | $399.56 | offer_architecture.target_cpa_locked |
| T1 vs breakeven | **−$4.00** | margin_sanity.T1_vs_breakeven |
| projected AOV (with INFERRED ladder) | $864.80 (ratio 1.73) | offer_architecture.projected_aov |
| purchase-level capacity at $100/day | testable concepts **0**, max ad sets **0** | 12 §1a, coverage_statement |
| booked-call proxy | **$19.03** per booked call (close 4.76% = 4 PAID/DEPOSIT of 84 calls, SAMPLE(84)); T1-only guard **$10.36**; kill after $20.72 proxy spend | kpi_table, budget_rules (OPERATOR-VALIDATES) |
| proxy capacity | testable concepts 18, max ad sets 5 | 12 §1a (OPERATOR-VALIDATES) |

**Read.** The single price is at breakeven, not above it: T1 alone survives only at a booked call ≤ $10.17–$10.36 (margin_sanity note). A1b.1 would normally say "lead with the bundle", but T2/T3 are not on the live page (PT-02: "no single number is published"), so the ads cannot lead with them (price-match rule, #2). **Recommendation to the operator (not to the writers):** (a) confirm the booked-call proxy and optimise the campaign on the booked call (campaign_structure objective OUTCOME_LEADS); (b) the upsell path (T2 "The Second-Shot Launch") lives on the fit call and the post-purchase path, not in ad copy; (c) if the operator publishes T2 on the page, a wave-2 cell can lead with it. Creative cannot fix this line; the batch is built on the $500 entry only.

## 2 · Price match (A1b.2): binding for P2/P3

| allowed in ads | never in ads (source) |
|---|---|
| "$500" / "the $500 Build" / "Start with the $500 Build" (PT-01; entry name Q-O-0029 "I'll start with the 500") | T2 $2,000, T3 $3,000, "Save $1,500", per-round prices (INFERRED, 12 §5) |
| "ad spend, product costs and store fees are extra / yours" (PT-05) | bump "+2 products $149", OTO1 $1,500, OTO2 $600, Keep-Running $550/mo (INFERRED) |
| "the ad budget is one you approve" (F-05) | "60 days ... every penny back" (OPERATOR-VALIDATES + legal; replaces PT-15 only when adopted) |
| the refund ONLY as conditioned: 7 days from payment, the $500 fee only, ends when you accept delivery, buy any add-on, or ask for further work; platform fees, ad spend, domain, apps and supplier costs never refunded (PT-15, F-10), or leave it out | "7-day money-back guarantee" / "100% money-back" unqualified (DNS-06) |
| "a written list of what the $500 covers and what it doesn't" (PT-04/PT-05; MK-22 keeper) | "GIFT-01 Every Cost in Writing" as a named gift (TO-BUILD, not on the page) |
| no build duration (PT-06 NULL; PT-04 gives none) | "7–10 days", "within days", "ready in 7 days" (OPERATOR-VALIDATES; DNS-19) |
| n/a | "3 vetted products" or any product count (PT-19 UNKNOWN) · "account manager", "client portal", "credits" (DNS-07, PT-19) |
| n/a | any urgency, countdown, stock, "limited stores per month" (12 object 7: NONE, evergreen) |

## 3 · Page congruency (A1b.3, A15)

Destination: **PDP https://readymerce.com** (not fetchable here; words from 01 §TRUTH CARD T3/T5 and 13 §14).

| batch mechanism-match word (handoff writer_handoff[AV].message_match_words) | on the live page? | where |
|---|---|---|
| "in your name" | YES | /what-you-get F-11 "The store account is in your name and stays in your name" |
| "in stages" | YES (as "a staged (not single-drop) product release") | /what-you-get PT-04 |
| "a budget you approve" | YES (as "Controlled ad testing with budgets you approve") | /what-you-get F-05 |
| "one shot" (LOCK-A problem) | **NO** | not on any of 9 pages read |
| "left on launch day" / "we stay after launch day" (LOCK-B) | **NO** (closest: "post-launch corrections", "ongoing listing optimisation and new product rollout ... agreed on the fit call") | /what-you-get PT-04, PT-08 |
| page register | **BREAK**: dark "operator console" hero after a candid phone-real ad (13 §6) | home page (Exa read) |
| trust surface | /results "Straight From Our Stores. Unfiltered." renders no cards (PT-07); testimonials disclose actors (01 T3); ScamAdviser 0/100, ScamDoc 25% "Poor" (PT-16, F-14/F-15) | AV-02 will Google it (Q-O-0102) |

**Recommendation.** The 12 `prelander_trigger` (advertorial from the winning story at $500–1,000/day + ROAS ≥2.5 over 48 h) is NOT reached at $100/day, so no advertorial now. What A15 asks for now is a **short congruence lander** (one screen + the proof list), one variant per lock, in the REG-1 register:
- fold: "Your store should get more than one shot. We build it in your name. Then we stay after it goes live." (13 §10 fold line, grade −0.5, 0 banned words)
- LOCK-A variant (C2 AV-01, C3 AV-04): "one shot" → "products go live in stages, each with a small test on a budget you approve, an early review, what doesn't sell replaced" (PT-04, F-05)
- LOCK-B variant (C1 AV-07, C4 AV-02, C5 AV-03): "left on launch day" → "after it goes live: an early performance review, corrections, new products rolled in; you approve the budgets and see the reports" (PT-04, PT-08)
- then the /what-you-get list verbatim, "What is NOT included" (PT-05), "We make no income guarantees" (F-13), the refund as conditioned (PT-15), the owner field "in your name" (F-11)
- scene-level rule (13 §14): an ad opening on the idle admin lands on a fold that says "sitting there"; never a scene on the page the ad did not show.
Until the lander exists, every ad ends on the page's own words ("in your name", "in stages", "budgets you approve") and never promises a sentence the page does not carry.

## 4 · Tracking (A1b.4)

UNKNOWN → FLAG. Operator must confirm before spend: (1) Meta pixel + CAPI firing on readymerce.com and on the booking/confirmation page; (2) a "booked call" custom conversion (the campaign optimises on it, OUTCOME_LEADS); (3) offline upload of PAID/DEPOSIT outcomes for the ROAS read in kill_scale_rules; (4) the ad account to use (none named for Readymerce's own marketing, 00-ADS-STATUS.md 00:50Z). No creative decision waits on this; the launch does.

`PRE-FLIGHT: flags 3 (offer RED, page AMBER, tracking UNKNOWN) · price match PASS-with-rules · blocking 0 · spend $0`
