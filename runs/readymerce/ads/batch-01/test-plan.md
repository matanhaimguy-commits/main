# TEST PLAN — Readymerce batch-01 (orchestrator, on skill A19/A20/B17/C10 + handoff.json budget_rules/kpi_table)

## 0 · What we test
ONE product/offer: the $500 Build entry (T1) to readymerce.com. If it does not work, we iterate marketing angles (wave 2/3 queue below), not the product. Every number marked OPERATOR-VALIDATES comes from the booked-call proxy (4 closes in 84 seller-contacted calls, 4.76%) because at $100/day a purchase-level test cannot fund one ad set (target CPA $399.56 > daily budget).

## 1 · Structure (skill A19: under ~$150/day → ABO, even split; CBO only after 3+ concepts are proven)
| level | name | setting |
|---|---|---|
| campaign | RM-ABO-01-LAUNCH3 | objective: leads (booked call) — OPERATOR-VALIDATES which pixel event fires; if the pixel fires on payment, objective sales/Purchase instead. Broad targeting inside US, 18+; exclude customers and booked-call list. Automatic placements. Start 00:00 account time. |
| ad set 1 | C1-AV7-owner-automate | $33.33/day · ads C1-V1 (designed), C1-V2 (native), C1-V3 (story) |
| ad set 2 | C2-AV1-store-died | $33.33/day · ads C2-V1, C2-V2, C2-V3 |
| ad set 3 | C3-AV4-paycheck-side | $33.33/day · ads C3-V1, C3-V2, C3-V3 |
| benched | C4 (AV-02), C5 (AV-03) × 3 vehicles + 3 video scripts | built, not live; enter as swap-ins or when budget rises (A4 cap: 9 live cold ads at $50–150/day) |
Ad set floor $10/day (handoff budget_rules.adset_floor). Meta button: Shop Now (skill A13). Destination: https://readymerce.com until the short congruence lander exists (pre-flight PAGE AMBER); then the lander, one variant per mechanism (LOCK-A for C2/C3, LOCK-B for C1).

## 2 · Reading windows and decisions
| when | rule | source |
|---|---|---|
| first read | at ≈2× target cost per booked call spent per ad set (≈$38, i.e. end of day 1–2): pause an ad set with 0 form starts / 0 booked calls AND link CTR < ~0.8% | A19 (ATC → booked-call start) |
| 72 h | read 1 (handoff read_1): compare ad sets on cost per booked call; no edits before this | handoff budget_rules |
| day 7 | full read (read_2): cost per booked call, link CTR, CPC, landing → form start → booked call → paid | A19 / handoff |
| min spend before a CPA kill | $20.72 per ad set on the proxy (purchase-level would be $435, unreachable) | handoff budget_rules |
| judge in this order | 1 cost per booked call (proxy for cost per purchase) · 2 link CTR + CPC · 3 landing view → form start → booked call · 4 spend per ad inside the winner (which vehicle Meta prefers) | A19 |

## 3 · KPIs and gates
| metric | gate | source |
|---|---|---|
| link CTR | > ~1.5% (story ads often lower CTR, higher intent; read with cost per booked call) | A19 |
| form-start rate (of landing views) | > ~10% (A19 ATC gate adapted) | A19 |
| booked-call rate (of landing views) | > ~3% (A19 CVR gate adapted; OPERATOR-VALIDATES against the real funnel) | A19 |
| cost per booked call | target $19.03; T1-only guard $10.36 (while only the $500 tier sells) | handoff kpi_table (OPERATOR-VALIDATES) |
| form-start cost | ≤ $4.76 | handoff kpi_table |
| CPM | < $80; ad set off if ≥ $100 after $20 | B17 |
| link CPC | < $3 | B17 |
| frequency (cold) | > 2 = fatigue → new hooks / vehicles | A19 |
Reading rule (A19): low CTR = hook or angle · good CTR + weak form start = belief shift, benefits or page · good form start + weak booked call/paid = call flow or offer.

## 4 · Hard cuts (B17 adapted to the proxy; end of day, 48-hour blocks, no edits mid-learning)
- $20 spent with no form start → ad set off.
- $40 (≈2× target cost per call) with no booked call → ad set off.
- $100 spent with cost per booked call above 2× target ($38) → off.
- CPM ≥ $100 after $20 → off.
- Inside a surviving ad set, kill an ad only at $40 with no booked call.

## 5 · 48-hour buckets (B17)
1. Bad ad metrics, no intent → one more day, then cut, next angle.
2. Good ad metrics, no intent → check for click-bait images, then fix the offer presentation on the page (the four gifts from 12 §5, the conditioned refund stated plainly) and answer the top pre-buy questions above the fold; do not cut price.
3. Bad ad metrics, good intent → creative cost; run the Variation SOP on the best ad set: (a) new hook set → (b) new story/body same angle + image → (c) new story + new image, each 24–48 h as a new ad set `C#-V#-<shape>`; still nothing → the reserve angle → then cut the avatar.

## 6 · Wave 2 and the angle queue (A20 + the 18 handoff cells)
Net-new pacing ≈ 1 new ad per $1,000/month → ≈3 net-new ads per month at $3,000/month. Wave 2 mix: 50–60% replicate the winner (runner-up hooks from work/09, new vehicles/surfaces), 20–30% adjacent iterations, 20–30% net-new concepts. Angle queue in order: reserve angles AN-02 (C1), AN-06 (C2), AN-09 (C3); then the benched concepts C4 (AN-13, reserve AN-15) and C5 (AN-16, reserve AN-17); then the remaining handoff cells (AN-03, AN-04, AN-07, AN-08, AN-11, AN-12, AN-14, AN-18) and the three NEW angles in work/04. Videos (C1 VF1, C2 VF4, C3 VF10) enter as swap-ins for the weakest vehicle after the day-3 read, or as their own ad sets when the budget rises; iterate videos hooks → body → format (C10).

## 7 · Hygiene
Cold frequency > 2 = fatigue. New ads go into a new ad set, never into a winning one. Scale by raising budget (winner = 2–3 consecutive days at or under target cost per call; then +20–30%/day). Moderate comments daily: hide hostile, answer real questions as the brand, pin the best organic positive comment. Weekly loop: score every ad, update the building-blocks log (avatars, angles, hooks, bodies, mechanisms, closes, images) HYPOTHESIS/VALIDATED with numbers, feed winners before fatigue, export the next batch.

## 8 · Tracking columns (sheet)
date · ad set · ad · spend · impressions · CPM · link clicks · link CTR · link CPC · landing views · form starts · cost per form start · booked calls · cost per booked call · calls held · paid ($500) · deposits · CPA (paid) · revenue · ROAS · frequency · notes/decision.

## 9 · Before spend (operator)
1. Name the ad account (the three under business "Readymerce" look like client stores). 2. Confirm pixel/CAPI and the booked-call event; upload PAID/DEPOSIT as offline conversions weekly. 3. Validate the proxy numbers ($19.03 / $10.36 / 4.76%). 4. Decide the destination (live page vs the short congruence lander). 5. Legal read of the refund line as conditioned (7-day, voided by add-ons); the 60-day guarantee stays out until adopted.
