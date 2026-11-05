# English runs (@straightscale_)

Every English piece's production run lives here: `pipeline.py init straightscale-en <post_id> --format ...` makes
`runs/<post_id>/` (ledger, calls, prompts, Shot Specs). G-BUDGET counts this folder's `ledger.csv` against
`brain.json` `package.monthly_usd_cap` ($100 a month, Matan, plan 28 Oct).

The hub has one business, `straightscale`; `brain.json` `hub.business` names it, so `hub.py` and the studio commands
(`studio-push straightscale-en <post_id>`) post there without `--business`.

`clients/straightscale/runs/SS-EN-SONG-01` was made before this folder existed and stays where it is.
