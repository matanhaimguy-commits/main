# page_facts

Checkable facts about a prospect's page for the leak scorecard: trackers (by exact signature, with ids), forms, booking and contact routes, page basics, JSON-LD types, robots.txt and the sitemap. Facts only: no scores or grades.

- Run: `python3 growth-engine/tools/page_facts https://acme.com` (markdown); add `--json` for the object documented in `__init__.py`, `--out FILE` to save it.
- `--render` also loads the page in headless Chromium (`render.js`, Node + Playwright) and checks its network requests, so it catches a pixel loaded through GTM.
- When the static HTML is a JavaScript shell (Lovable, Vite, Wix), the summary opens with an "Incomplete" warning: run again with `--render`.
- A proxy refusal or DNS failure exits with `UNREACHABLE: <host> ...`: allow the host in the cloud environment's network settings.
- Python standard library only; honest User-Agent, 20 s timeout, 3 MB cap, TLS always verified, only the page's own site is fetched.
- Tests (no network): `python3 -m unittest discover -s growth-engine/tools/page_facts -p 'test_*.py'`
- Layout: one job per module (see `__init__.py`); `cli.py` only wires them together.
