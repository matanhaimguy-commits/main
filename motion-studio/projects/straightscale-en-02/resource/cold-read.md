# Cold reads of the WORDS Sheet (28 Oct 2026)

Two fresh subagents played AV-01 (founder-led coach, consultant or agency owner, $20K to $50K a month, lumpy months,
tired of marketing advice) and read only `WORDS.md`. Neither ran live searches (read 1: Firecrawl reported out of
credits, so nothing was spent; read 2: told to use no paid tools). Both judged the syntax from knowledge.

## Read 1: what it found, what changed
| Finding | Change |
|---|---|
| `[NICHE]` mixed up the buyer and the reader: "how to get [NICHE] clients" found the reader's peers, not their buyers | blank split; every search is built on `[BUYER]` (who pays you) and their pain |
| 12 searches in 18 minutes is not realistic | one search per section marked "Start here" (6 for the first run), the other 6 next time; `check.mjs` enforces exactly one per section |
| Sorting rules contradicted each other between sections | one rule per column plus a tie-break (label beats pain, pain beats wish); section lines follow it |
| Maps search useless for online coaches; "[NICHE] [CITY] reviews" returns listicles | Maps marked local only; Search 2 is `"[COMPETITOR]" reviews -site:[COMPETITOR WEBSITE]` |
| Trustpilot domain format unclear; bare `OR` without brackets; YouTube already defaults to Top; Facebook example `clients` broke the pain-word rule; most groups private | domain-only note, brackets, Newest sort, pain-word examples, public groups only |
| "567" twice reads as a brag; "buyers stop for their own words" asserted | 567 once; the claim replaced by the fact that the reel's own hook was a buyer's review sentence |
| "We collect hundreds, not 15" belittles the reader | rewritten as "for a client we run the same searches across..." |

## Read 2: what it found, what changed
| Finding | Change |
|---|---|
| Still 30 minutes, not 20 | the promise is now "one sitting of 20 to 30 minutes" in the sheet and the DM |
| IDENTITY example ("race to the bottom... I knew it") is not a label | rule reworded to "how they describe themselves or their place in the market"; the quote is kept (it is real and positions them) |
| "Why they bought is DESIRE" broke the tie-break; "confessions = IDENTITY" overreached | "FEAR if it is a pain, DESIRE if it is an outcome"; confessions sorted by the tie-break |
| Coaches' buyers are not on Trustpilot | fallback: 2 and 3 star Amazon reviews of the top books on the buyer's problem |
| Facebook Search 11 alone gives no sentences | Search 11 now uses the Public groups filter and goes straight into Search 12 |
| `[COMPETITOR WEBSITE]` hidden; starter pains are owner-only | its own blank; non-owner buyers write 3 phrases they would say to a friend |
| Substack comments often empty, custom domains missed | fallback `"[PAIN]" [BUYER] newsletter` |

Not changed: read 2 suggested starter phrases for non-owner buyers ("promoted to manager", "imposter"). They are not
from our corpus, so the sheet asks the reader to write their own instead of printing invented phrases.
Both reads: the last section is a soft ask, not bait; the search syntax (operators, Trustpilot `?stars=`, Maps and
YouTube sorts) is correct.
