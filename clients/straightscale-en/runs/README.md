# English runs (@straightscale_)

Every English piece's production run lives here: `pipeline.py init straightscale-en <post_id> --format ...` makes
`runs/<post_id>/` (ledger, calls, prompts, Shot Specs). G-BUDGET counts this folder's `ledger.csv` against
`brain.json` `package.monthly_usd_cap` ($100 a month, Matan, plan 28 Oct).

The hub has one business, `straightscale`; `brain.json` `hub.business` names it, so `hub.py` and the studio commands
(`studio-push straightscale-en <post_id>`) post there without `--business`.

`SS-EN-SONG-01` (EN 03, the song) was made under `clients/straightscale/runs/` before this folder existed and moved here on
28 Oct (main session), so it budgets against the English cap; its card is `cards/2026-11-W1/SSEN-2026-11-W1-01.yaml`.
