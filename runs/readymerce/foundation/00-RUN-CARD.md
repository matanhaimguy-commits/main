# 00-RUN-CARD · readymerce · US · standard · claude-code

## INPUTS CARD
| field | value | state |
|---|---|---|
| PRODUCT NAME | Readymerce (readymerce.com) — a done-for-you online-store / e-commerce business setup service sold by phone to inbound "I want to open an online business" registrations | GIVEN (product-name check: PRESENT → run starts) |
| PDP LINK | https://readymerce.com | GIVEN (our own site; 01 fetches it; competitors found by free search) |
| TARGET MARKET | US | ASSUMED (blank → US). The 280 owned sales-call transcripts split ≈151 US-number calls / ≈123 UK-number calls / 6 other; UK is a second run in its own folder. Owned records from UK calls are still coded (OWNED_PROOF) with `call_market: UK` in `life_context` so downstream can split. |
| category | done-for-you e-commerce store / "business in a box" (dropshipping, Shopify/Amazon/Etsy store build) | INFERRED: transcripts + readymerce.com (01 confirms) |
| components / spec | unknown | INFERRED path (01): our PDP claims → competitor PDPs → category-typical → VOC |
| price | unknown (transcripts mention deposits ≈ $500 and plan tiers) | INFERRED: 01 / 12 |
| competitor list | none given | 01 free searches → NW-SEED-## |
| budget level | standard | ASSUMED (default) |
| brand-name lock | Readymerce (existing brand) | GIVEN — 13 treats it as option 1 + 2 alternates |
| owned data | 280 sales-call transcripts (Sept 2026), `runs/readymerce/inputs/transcripts/` | GIVEN — `[R-OWNED]`, corpus OWNED_PROOF, harvested by VOC-OWNED-* in W1 |
| operator ICP hypotheses | (a) fathers of kids who want to provide a better future / more time with kids and wife; (b) adults 50+ with money who want an online business | HYPOTHESIS — entered by 01 as candidate populations with label HYPOTHESIS (operator-supplied, not validated); the run finds the validated directions |
| operator problem statement | current leads are low quality ("tire kickers"); wants narrow, accurate ICPs of buyers ready to invest, not broad | OPERATOR CONTEXT (recorded, never read as VOC) |

## RUN KNOBS
RUN_MODE fresh · PERSISTENT_RUN_DIR `/home/user/main/runs` (git repo, branch `claude/sweet-keller-g8zeli`) · BACKUP_DIR = the git remote `origin/claude/sweet-keller-g8zeli` (every checkpoint = commit + push) · BRAND_SLUG `readymerce` · RUNTIME `claude-code` (cloud container, Agent tool with sonnet/opus routing, run_in_background) · MAX_PARALLEL_AGENTS 8 · CHECKPOINT_DELIVERY both (git push + key files attached at wave ends via SendUserFile).
Run folder: `/home/user/main/runs/readymerce/foundation/` · probe PASS 2026-09-24T19:42:16Z · step prompts: `/home/user/main/runs/readymerce/prompts/STEP-nn.md` (pasted whole into every brief by path; each agent reads its prompt file in full first).

## BUDGET LEVEL + CAPS (standard)
02 ≈5–7 cr (≤3 seed networks + keywords) · 07 ≤2 cr · 09/10 ≤3 cr · 01 ≈$1.00 · 04 ≤$0.60 · 05/06 cap $8 (÷ N_PB per harvester) · 09 ≤$1. Credit guard: `start_brand_spy` NOT RUN — needs operator yes (asked once below); never unfiltered `list_shops` or `search_ads {}`.
Balances before W0: GetHookd 291.22 credits · Higgsfield 1,998.34 credits (ultra) · Apify: BRONZE tier, balance not exposed by the MCP (spend reconciled from per-run costs).

## TOOL CARD (inspected 2026-09-24T19:44Z)
| capability | status | provider / substitute | steps |
|---|---|---|---|
| Ad-intelligence source | AVAILABLE (GetHookd MCP `mcp__Gethooked__*`, 291.22 cr) + AVAILABLE (Meta Ad Library via `mcp__Facebook_Ads__ads_library_search`, free, live: 4,519 ads on a test term) | Apify `igolaizola/facebook-ad-library-scraper` as the third rung | 01·02·03·07·09·10·12·13 |
| Scraper (reviews, subreddits, threads, groups, comments, pages) | AVAILABLE (Apify MCP `mcp__Apify__call-actor` / `get-dataset-items` / `apify--rag-web-browser`, BRONZE) | browser (`mcp__browserbase__*`) / WebFetch / Firecrawl → OPERATOR-PASTE | 01·04·05·06·09·10·11 |
| Transcript source | AVAILABLE (GetHookd `transcribe_ad`; TranscriptAPI MCP `mcp__TranscriptAPI__get_youtube_transcript`; Apify `johnvc/YoutubeTranscripts`) | — | 02·05·06·07·13 |
| Web search + fetch | AVAILABLE (WebSearch, WebFetch, `mcp__Firecrawl__firecrawl_search/scrape`, browserbase, `mcp__Readymerce_Exa__agent_run`) | — | every step |
| Code execution | AVAILABLE (Bash, python3 3.11, node 22) | — | every step |
| Search-volume corroboration | UNAVAILABLE (no Ahrefs / SimilarWeb MCP) → `search_volume: UNSCANNED` | none | 07 |
| Audience-size read (Meta EAS) | UNAVAILABLE (drafting ad sets in the operator's ad account is an outward action not authorised for this run) → `fish: UNSIZED — method: EAS` | none | 09 |
| Image generation + consistency | AVAILABLE (Higgsfield MCP `mcp__Higgs__*`, 1,998 cr) | — | 13 |
| Delegated agents | AVAILABLE (Claude Code `Agent` tool, up to 8 in one message, `run_in_background`, model routed sonnet/opus) | — | every wave |
| TikTok Ads MCP | UNAVAILABLE (needs OAuth; not used) | — | — |

## FILE REGISTRY — see DELIVERABLES in the orchestrator prompt; files land under `foundation/` with the registry names; scoped partials under `nn-partials/`.

## WAVE PLAN
W0 SEED: `01` (MODE: SEED, opus, 10 min / 40 calls).
W1 FAN-OUT (≤8 at once; queue order: seed NW with most active ads → PB with most populations → 02-KEYWORDS → 01-DEEP → VOC-OWNED-*): `02-NW-<seed>` ×≤3 · `02-KEYWORDS` · `VOC-PB-##` ×≤5 (04→05→06 scoped) · `01-DEEP` · **orchestrator adaptation:** `VOC-OWNED-US` + `VOC-OWNED-UK` — STEP 06 HARVEST with `SCOPE: OWNED-US | OWNED-UK` over the 280 sales-call transcripts (lane `owned_paste`, corpus OWNED_PROOF, ids Q-O-####, pb_ids tagged from 01's PB map; 04's Step 9 "owned sources" COM row); they write `06-partials/06-VOC_MASTER.OWNED-US.csv` / `.OWNED-UK.csv` + logs + handoffs and merge in 06-MERGE. Rationale: the operator supplied the transcripts for objection / belief / angle analysis; the step prompts route owned data through 06 (OWNED_PROOF) and 11 (`[R-OWNED]` operator notes).
W2: `03` (MODE: MERGE then synthesis) ∥ `06-MERGE` ∥ `07-SOPH`.
W3: `07` (MODE: FULL) ∥ `08` ∥ `10`.
W4: `09`.
W5: `11-AV-##` ×≤5 ∥ `13` ∥ `12-OFFER`.
W6: `12` (MODE: ASSEMBLE).
Time boxes: 01 seed 10/40 · harvester 30/100 · network agent 25/80 · synthesis 40/150 · merge/assemble 20/60. Model routing: extraction (VOC-PB, VOC-OWNED, 02-NW, 02-KEYWORDS, 01-DEEP) → sonnet; everything else → opus.

## BRIEFS
Every brief = `prompts/AGENT-BRIEF-COMMON.md` (inputs card, tool card, MCP tool names, budget, rules pointer, label vocabulary pointer) + the step prompt file path (read whole) + the SCOPE/MODE line + inputs[] + outputs[] + max_minutes/max_tool_calls + model.

## PORTABILITY NOTE
Claude Code (cloud): one message launches a wave (Agent calls, run_in_background: true); this session polls the run folder, audits at wave end with `prompts/audit.py`, checkpoints (git commit + push), launches the next wave. Model choice honoured (sonnet / opus).

## OPERATOR QUESTIONS (asked once; the run does not wait)
1. `start_brand_spy` (8 cr per brand) on the top competitor network — yes/no? Without a yes it prints `NOT RUN — needs operator yes: start_brand_spy`.
