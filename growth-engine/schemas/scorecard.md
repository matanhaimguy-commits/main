# Post scorecard (`clients/<slug>/analytics/posts.csv`)

One row per published post, filled at 72 hours and again at 7 days (the 7-day values overwrite). Section 9 of
ORGANIC-OS.md. Empty cell = not measured (never 0 unless it really was 0).

| Column | From | Notes |
|---|---|---|
| post_id | Post Card | e.g. SS-2026-10-W3-01 |
| hub_id | hub `content_items.id` | |
| published | hub | YYYY-MM-DD |
| family | Post Card | reel / carousel / image |
| format | Post Card | id from `config/organic.json` |
| job, belief, pillar, series | Post Card | |
| cta_keyword | Post Card | |
| reach, nonfollower_reach, views | Insights | |
| skip_rate | Insights | reels, 0 to 1 |
| avg_watch_s | Insights | reels |
| likes, comments, saves, sends | Insights | sends = shares |
| profile_visits, follows | Insights | follows gained from the post |
| keyword_comments, dms, qualified_dms, booked | hub (funnel + leads) | |
| revenue | CRM | EUR |
| credits, minutes | `ledger.csv` | production cost |
| measured_at | | YYYY-MM-DD, 72h or 7d |

Derived by `organic.py score`: sends_per_reach, saves_per_reach, follows_per_1k_reach, the job metric vs the account
median for that job, candidate (2x) and template (3x + checks, or any booked) flags, and a diagnosis line (9.4).
