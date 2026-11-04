# 02-PROGRESS — NW-NEW-SEED-03 (Done for you brands / doneforyoubrands.co)

STATUS: COMPLETE (full N1–N8 crawl run; early-exit rule checked and did not apply — 32 active ads / 35 Meta-ACTIVE found at sizing, well above the 5-ad floor).

STEPS COMPLETED:
- N1 sizing: list_shops, get_domain_advertisers, aggregate_ads (all 0/empty — domain not shop-indexed, consistent pattern), Meta search_terms (too generic, 0 relevant), get_brand (resolved brand_id 297031 directly from two upstream partials) → active_ads 32 [R-TOOL], cross-confirmed Meta page_ids ACTIVE=35.
- N2 crawl: CRAWL COMPLETE after 5 searches — single Facebook page identity confirmed across all 38 sampled ad rows.
- N3 size: competitor_quality ESTABLISHED-with-caveat, scale UNSIZED (no shop record).
- N4 rankings: pulled via brand-scoped search_ads (active + inactive, sort days_active desc) — 21 active + 17 inactive rows sampled (both calls truncated by local tool-output cap before reaching full roster/meta.total; historical total NOT MAPPED).
- N5 open: 5 ads opened in full via free get_ad (one per distinct concept + the CO-02 dual-era instance); get_ad_technologies x2 (Heyflow detected on current funnel); Meta page_ids ALL+ACTIVE cross-check.
- N6 classify: 4 distinct concepts (CO-01..CO-04) coded as 5 IM records, all NON-STORY bucket, avatar detected 5/5.
- N7 per-network objects: 3 rankings (runtime/performance/replication) built; coverage columns; mechanism row; offer+funnel row; loser/winner pairs NONE FOUND — searched; keep-list 1 row (LK-01, Trustpilot BLOCKED-ON-TOOL); hook bank 5 rows. save_ad_to_swipe_file NOT called (no STRICT winners to file, per bucket findings — all NON-STORY).
- N8 write: coverage statement written, both partials renamed, handoff JSON written.

RESUME POINT: N/A — scope complete. If resumed for deeper coverage: page through the remaining ~11 uncoded active-variant ids and the unmapped historical (inactive) roster via `search_ads{brand_id:297031,status:"inactive",page:2,limit:30,ads_per_brand_limit:0}` to confirm no 5th distinct concept exists and to get a true historical total for a GetHookd-basis pct_active.

CREDITS: GetHookd 285.43 -> 284.09 (delta 1.34 of <=1.5 cap). Meta: 3 free calls. Exa: 1 run, $0.10 of <=$0.30 cap (combined landing-page + Trustpilot query).
