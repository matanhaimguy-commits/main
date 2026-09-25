# Readymerce — research + ads run · master index

Everything from this run lives in this folder, on branch `claude/sweet-keller-g8zeli`. Two zips hold the reader-facing files for download: `readymerce-research.zip` (the 13-step foundation) and `ads/batch-01/campaign.zip` (the ad batch).

## Start here (read in this order)
| # | file | what it is |
|---|---|---|
| 1 | `foundation/00-RUN-CARD.md` | inputs, tool card, wave plan, and the **COMPLETION CHECK** at the bottom (every agent's coverage line, open items, spend, weakest link) |
| 2 | `foundation/09-AVATARS.md` | the avatars: launch order AV-07, AV-01, AV-04, AV-02, AV-03; the two operator hypotheses (fathers; 50+ with money) tested → UNPROVEN, in reserve |
| 3 | `foundation/12-OFFER-TESTPLAN-PLAYBOOK.md` | the offer ($500 Build → "The Second-Shot Launch"), economics, buy-now triggers, 18 test cells, rulebook, creative playbook, writer contracts |
| 4 | `foundation/handoff.json` | the single machine-readable contract (v2, 65 keys) the page, ad and scale prompts read |
| 5 | `ads/batch-01/gallery.html` | all 15 rendered ads with their copy (open next to `ads/batch-01/images/`; full-res links inside) |
| 6 | `ads/batch-01/test-plan.md` | how to run batch-01: 1 ABO campaign, 3 ad sets at $33.33/day, 9 live ads, reads, cuts, wave-2 queue |
| 7 | `ads/batch-01/campaign-spec.json` | the Meta build spec, **not built**: fill ad account, page, pixel/event first |

## foundation/ — the 13-step research (one file per step + its ≤2 KB handoff)
| step | deliverable | handoff | in one line |
|---|---|---|---|
| 00 | `00-RUN-CARD.md`, `00-STATUS.md` | | run card + completion check; append-only ledger of every wave, audit and checkpoint |
| 01 | `01-PRODUCT-TRUTH.md` | `01-HANDOFF.json` | what readymerce.com actually says and sells (PT-## facts, complaints, limits, TRUTH CARD) |
| 02 | `02-COMPETITOR-INTEL.md`, `02-swipe.csv` | `02-HANDOFF.json` | the 5 competitor networks that really run ads (Ecom Degree University, Ecom Family, Ecom Accelerator, Done for you brands, EcomXpertz) + 32 swipe rows |
| 03 | `03-VALIDATED-MESSAGING.md` | `03-HANDOFF.json` | proven claims, story structures and existing-knowledge rows from the market's ads |
| 04 | `04-COMMUNITY-MAP.md` | `04-HANDOFF.json` | where the three problem populations talk (forums, YouTube, groups); Reddit lane blocked |
| 05 | `05-URL-CORPUS.md` | `05-HANDOFF.json` | every source URL harvested, by problem and lane |
| 06 | `06-VOC-REPORT.md`, `06-VOC_MASTER.csv` (362 rows), `06-VOC-LEDGERS.csv`, `06-HARVEST-LOG.md`, `06-SOURCE-MANIFEST.md` | `06-HANDOFF.json` | the voice-of-customer corpus: market voices + the 280 sales calls (objections by call outcome in §6, owned cut in §13) |
| 07 | `07-AWARENESS-SOPHISTICATION.md`, `07-SOPH-20ADS.csv` | `07-HANDOFF.json` | awareness rung per problem, market sophistication stage, the lane one step ahead |
| 08 | `08-DESIRES-LF8.md`, `08-DESIRES.csv` | `08-HANDOFF.json` | mass desires ranked (MD-01 "an income that isn't hostage to a job", MD-04 "build something of my own") |
| 09 | `09-AVATARS.md` | `09-HANDOFF.json` | the avatar portfolio with evidence per avatar and the launch / reserve / expansion split |
| 10 | `10-MECHANISMS.md` | `10-HANDOFF.json` | LOCK-A "The One-Shot Launch" (staged-release loop) and LOCK-B "The Handover Cliff" (we stay after launch day) |
| 11 | `11-BELIEFS.md` (merged from 5 per-avatar partials) | `11-HANDOFF.json` | belief ladders, objections, proof map, claims ranked, the do-not-say list (DNS-01..19), honest box |
| 12 | `12-OFFER-TESTPLAN-PLAYBOOK.md`, `handoff.json` | `12-HANDOFF.json` | offer + economics + test plan + playbook + writer contracts; handoff.json v2 |
| 13 | `13-BRAND.md`, `assets/readymerce-visual-identity/README.md` | `13-HANDOFF.json` | positioning, enemy, narrator, voice, palette, fact sheet; Higgsfield element + render IDs |

Supporting folders: `*-partials/` (the per-agent files each merged step was built from), `datasets/` (counts, clusters, minted rows, the top-ads pull from the brand spy), `progress/` (agents' progress logs).

## ads/batch-01/ — the first creative batch for the $500 Build
| file | what it is |
|---|---|
| `gallery.html` | the 15 ads with copy, render size, QA status, full-res links |
| `campaign.zip` | everything below in one download |
| `ad-index.csv` | one row per ad: concept, vehicle, launch/benched, hook, subhead, body, proof, CTA, image, QA |
| `batch.json` | the full ledger (audited by the skill's `audit_batch.py --final`: ok, 0 errors) |
| `captions.txt`, `headlines.txt` | the evergreen caption pool (5) and Meta headlines (5) for the designed and native statics |
| `stories.txt` | the 5 long-form story ads with their 5 hook options each (primary text for the V3 ads) |
| `test-plan.md`, `campaign-spec.json` | how to run it and the paused-campaign build spec (operator blanks marked) |
| `qa-notes.md`, `source-notes.md` | per-image QA with credits; every quote/fact ID behind every line |
| `ads/C1.md … C5.md` | one file per concept: concept card, V1 designed static, V2 native static, V3 story (working + clean copy), video script, source notes |
| `images/` | 800 px proof copies of all 15 renders (+ two `-orig` versions before post-fix); full-size files are in the Higgsfield workspace |
| `prompts/` | the 15 paste-ready image prompts |
| `videos/` | C1 UGC video: `C1-V.json` (shot jobs, transcripts, stitched MP4 URLs), end-card proof, 9 frames |
| `contact-sheets/` | contact sheet + closest-pairs audit |
| `work/` | the research-to-concept tables: pre-flight, benefit ladder, language harvest (110 phrases), desire stack, belief ledger, white space, voice cards, concept slate, hook candidates, sizing, pairing map |
| `briefs/` | the agent briefs used to produce the batch (common, writer, captions, image, transport, video) |
| `scripts/` | `merge_batch.py`, `finalize_batch.py` (rebuild the ledger, gallery, notes, spec rows, zip) |
| `00-ADS-STATUS.md` | the batch ledger (every phase, spend, decisions) |

Concepts: C1 AV-07 Owner Wants It Automated (launch, ★) · C2 AV-01 Store That Died (launch) · C3 AV-04 Paycheck-Tethered (launch) · C4 AV-02 Paid-and-Got-Nothing (benched) · C5 AV-03 Stuck Starter (benched).

## prompts/ — the methodology used
`STEP-01.md … STEP-13.md` (the 13 step prompts, verbatim), `OPERATING-RULES-AND-LABELS.md`, `AGENT-BRIEF-COMMON.md` (+ tool card addendum), `BRIEF-VOC-OWNED.md`, `BRIEF-11-COMMON.md`, `audit.py` (wave-end audit).

## inputs/
`transcripts/` — the 280 sales-call transcripts (US format A ≈155, UK/IE/DE format B ≈125). Privacy: the corpus refers to prospects only by hashed IDs (O-####); no phone numbers or surnames were carried into any deliverable.

## Open items for the operator (from the completion check and the batch ledger)
1. Name the Meta ad account for Readymerce's own marketing, the page ID, the pixel and the booked-call event.
2. Validate the booked-call proxy economics ($19.03 target, $10.36 guard, 4.76% close) or replace them.
3. Decide the destination: the live page or a short congruence lander carrying "one shot / we stay after launch day".
4. Legal read of the refund line as conditioned; the proposed 60-day guarantee stays out until adopted.
5. Optional spend: render the C2 and C3 videos (≈470 Higgsfield credits); paste 5–10 Reddit threads or restore Apify to run the open harvest orders (HARVEST-01..23).
