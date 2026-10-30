# Client starter folder

Copy this folder to `clients/<slug>/` when a brand is accepted (`cp -r clients/_template clients/<slug>`), then work
through `growth-engine/ONBOARDING.md`. Do not put real client data in `_template`.

| File or folder | What it holds | Filled in |
|---|---|---|
| `brain.json` | The Client Brain. Every value starts as `unknown: ...`; the draft gives each fact a source in `field_sources`. Facts about the brand change only here. | O1 draft (`draft.py`), Brand card (`hub.py brand-pull`), O3; checked by `organic.py brain-check <slug>` and `draft.py check <slug>` |
| `content-map.json` | The month's Content Map: theme, mix, pillars, series. | O4 (Plan) |
| `intake/` | `slim.json` (quick intake) or `answers.json` and `files.json` (old shape), written by `hub.py intake-pull <slug>`. | O1 (Intake) |
| `foundation/` | The client's uploaded documents, downloaded by `intake-pull`. **Gitignored: private, never committed.** Not part of the starter folder; created on the first pull. | O1 (Intake) |
| `research/` | Foundation steps 01 to 03: voice of the customer, competitors and ads, outliers, page facts, demand map, Hook Library. | O2 (Research) |
| `cards/` | Post Cards, one folder per week (`cards/2026-11-W1/`). | O4 (Plan) |

On the template, `brain-check` fails on purpose. It must fail only on the unknowns (six blocking fields) and never on
the schema. That is tested in `growth-engine/tools/clients/test_template.py`.

Also add the brand to `growth-engine/tools/clients/registry.json` with status `onboarding`, then run
`hub.py client-sync <slug> --dry-run`.
