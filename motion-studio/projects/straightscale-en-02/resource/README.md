# EN 02 resource: the WORDS Sheet

The free resource behind EN 02's CTA ("Comment WORDS for the exact searches we use") and part two of the EN song
(EN 03, "where to find your buyers' words").

| File | What |
|---|---|
| `WORDS.md` | the source (edit this one) |
| `WORDS.pdf` | built from it; never edit by hand (`WORDS.html` is built too, not committed) |
| `build/` | `build.mjs` (main) wires `check.mjs` (brief checks), `markdown.mjs`, `page.mjs` (brand page), `print.mjs` (PDF) |
| `funnel/` | the hub funnel (comment and DM), its routing, and `create.sh` |
| `cold-read.md` | the AV-01 cold read and what changed |

Method: the pre-meeting skill's step 1b (vault `Skills/pre-meeting-business-audit/SKILL.md`): competitors' reviews,
the broad market on Reddit, pain words not product words, coded into fear, desire and identity, verbatim with source
and date. Every quote in the sheet is from the EN 02 corpus as cited in `../PROJECT.md` or EN 01 / EN 03 docs.

```
cd motion-studio/projects/straightscale-en-02/resource
node --test build/*.test.mjs     # 9 tests, including "the real WORDS.md passes"
node build/build.mjs             # fails on any brief check, else writes WORDS.html and WORDS.pdf
```
