# Reference bank

Proven, scroll-stopping reels broken down into reusable grammar, plus a memory of what each client's films
already used, so every new film starts from a strong reference and never looks like the last one.

- **Why:** a reel made from a blank page drifts to the same safe look. Reel 03, the best one so far, started from
  a measured viral reference and rebuilt its grammar in the client's brand. The bank makes that the default and
  removes the hunt for references on every job.
- **What a card is:** one viral reel, broken down so it can be rebuilt without seeing it again. Each card has:
  - stats;
  - the hook in the first 2 s;
  - a timed beat map;
  - the signature device;
  - pacing numbers measured from frames;
  - palette and type;
  - why it works;
  - steal / leave;
  - how to build it in our engines;
  - three business translations.
- **What a card is not:** a licence. Third-party reels are for study only. We take structure, timing, devices and
  sound logic, and never their pixels, words, characters, music or marks.

**What's in it** (28 Oct 2026):
- **107 cards in total.**
  - 81 viral social reels: 75 from TikTok and 6 from Instagram. The median is 8.1M plays and 38 have 10M+.
  - 15 YouTube Shorts (`yt-`, added 28 Oct): talking explainers, conversation scenes and story reels that sell
    services or ideas through talk, each a breakout of 3x or more over its own channel's median. Built from
    transcripts only (no frames), so their cards carry no pacing numbers.
  - 11 onetake craft films (study only).
- **20 categories**, listed in `TAGS.md`.
- **Usefulness:** 60 cards score relevance 4-5 for client marketing, and 48 of those are buildable at difficulty 3
  or less in our stack.
- **Picking a reference:** `devices.md` sorts the bank by signature device and by business message.
- **Overview:** `python3 tools/refbank.py stats`.

**Pacing (measured):** viral reels change something big every 0.5-1.5 s (median by category), mostly inside
continuous shots rather than through cuts. Medians by category are in `../HANDOFF.md` §7.3.

## Files
| Path | What |
|---|---|
| `cards/<id>.md` | One card per reference (YAML front matter + body). Ids: `tt-` TikTok, `ig-` Instagram, `yt-` YouTube Shorts, `onetake-` craft films from `references/onetake` (study only, PolyForm NC) |
| `index.json` | Built from the cards by `tools/refbank.py build`; searchable without opening cards |
| `TAGS.md` | Controlled vocabulary: category, hook, devices, energy, palette, sound, engine, fit |
| `TEMPLATE.md` | The card format |
| `devices.md` | Catalogue of signature devices across the bank: what each is, examples, how to build it here, business uses |
| `ledger.json` | Per-client usage memory (references, category, devices, hook, palette, camera, engine, music per film) |
| `metrics/<id>.json` | Pacing, palette and energy curve measured from the sampled frames |
| `tools/refbank.py` | `build`, `search`, `pick`, `check`, `log`, `history`, `stats` |
| `tools/frames_metrics.py` | Metrics + contact sheet from a folder of sampled frames |
| `tools/CARD_BRIEF.md` | The instructions used to write cards (reuse for refreshes) |
| `tools/test_refbank.py` | Checks every card builds into the index with known tags, and that every `yt-` card states its channel median and a 3x+ multiple: `python3 -m unittest discover -s motion-studio/refbank/tools -p 'test_*.py'` |
| `frames/` | Sampled frames per reference. Local only, gitignored (third-party media) |

## Use it in a job (motion-reel stages 3, 4 and 13)
```bash
R=motion-studio/refbank/tools/refbank.py
python3 $R pick --client <client> --fit <agency|saas|local-service|ecommerce|...> --n 6   # fresh refs for this client
python3 $R search --category explainer-2d --max-difficulty 3                              # browse
python3 $R check --client <client> --category <cat> --devices <signature>,<other>          # before committing to a concept
python3 $R log --client <client> --project <client>-<piece> --refs <id1>,<id2> --category <cat> \
  --devices <signature>,<others> --hook <hook> --palette <light|dark|...> --camera "<camera language>" --engine canvas
```
Rules that `pick` and `check` enforce for a client's next film:
- no reference it already used;
- not the previous film's category;
- no signature device from its last 3 films;
- at most one device shared with the last film.

Also change palette and camera language from film to film.

## Add references
Follow `tools/CARD_BRIEF.md` and the capture recipe in `../HANDOFF.md` §7.4. In short:
1. Run the TikTok and Instagram hashtag scrapers through the Apify connector and rank by plays and by
   plays / followers.
2. Get scene descriptions and transcripts with `clockworks/tiktok-scraper` and `aiVideoDescription`.
3. Get frames with `seemuapps/video-frame-extractor`.
4. Run `frames_metrics.py`, write the card, run `refbank.py build`, and commit.

Each reference costs about $0.10-0.25. Instagram, TikTok and Apify's own API host are blocked in our containers,
so everything goes through the Apify MCP connector. Read datasets as `format=xlsx`, which is saved to disk instead
of being pasted into the conversation.

## Sourcing log
- **2026-10-14:** first bank.
  - TikTok hashtags: motiondesign, motiongraphics, aftereffects, kinetictypography, 3danimation, 2danimation,
    satisfyinganimation, explainervideo, blender3d, motiondesigner, typographyanimation, productanimation,
    saasmarketing, mograph, logoanimation, uianimation, datavisualization, explained, typography, productvideo,
    cgi, fooh, brandidentity, appanimation, infographic, motiongraphicsdesign. That gave 1,640 unique videos,
    319 of them with 1M+ plays.
  - Instagram reels for 16 hashtags gave 699 unique videos. Instagram's hashtag feed is mostly recent posts, so
    only 15 had 1M+ plays.
  - 81 were picked for business-relevant grammar across six areas: CGI and brand ads, product, logo and UI
    motion, kinetic type, explainers, satisfying simulations, and story or wow hooks.
  - Added: 11 onetake craft films and the divyansh.fx_ reel behind StraightScale reel 03.
  - Apify spend was about $24. That covers sourcing about 2,500 candidates, scene descriptions, transcripts, and
    frames for 81 reels with a few re-runs.
  - **Not captured, for the next refresh:**
    - the_archive_27, `https://www.instagram.com/p/Ddvyte1sNI9/`, 1.0M plays. A math race: 2ⁿ against the
      product of primes, with the lead changing hands. Instagram returned HTTP 500 on every frame download.
  - **Re-captured with a higher download cap** (40 MB instead of 6 MB): spectrazeeua5, thebioswitch and
    vaporama_vision. The 6 MB cap silently skipped long videos.
- **2026-10-28:** 15 YouTube Shorts (`yt-` cards), for English StraightScale films. Apify was blocked (unpaid
  invoices), so everything came through the TranscriptAPI connector, 27 credits at most.
  - Listings: one Shorts page (48 Shorts) each for thefutur, AlexBerman, JeremyMiner, DanLok, codiesanchezct,
    PatrickDang, LeilaHormozi, NoahKagan and JordanPlatten; ImanGadzhi returned no Shorts. Saved as
    `clients/straightscale-en/research/raw/yt-shorts_<handle>_p1.json` (trimmed to id, title and views); JordanPlatten
    was not saved (no Short above 2.4x).
  - Proof: `organic.py yt-import` then `organic.py outliers --days 0` (`..._outliers.csv`). Each card lists the
    channel median and the multiple. A listing has no likes, comments or dates, so only the views check ran, and
    the median is over those 48 Shorts, not a date window. JeremyMiner and DanLok had no Short at 3x+.
  - Transcripts: `get_youtube_transcript` for the 15 picks, saved with their timing in
    `raw/yt-shorts_transcripts.jsonl` (field `timed`).
  - **Not captured:** frames and thumbnails. i.ytimg.com is refused by the session proxy and YouTube blocks the
    Higgsfield sandbox, so no card has pacing numbers, palette or a verified first frame. Next step: sample frames
    from these 15 (the `frames_metrics.py` route) when a downloader works, and fill `pacing` and `palette_hex`.
  - New slugs in `TAGS.md`: categories talking-explainer, conversation-scene, story-reel (none of the 17 fitted a
    reel whose words carry the film); hooks stop-doing, if-i-had-to; devices roleplay-dialogue, street-interview,
    qa-cold-open, quadrant-matrix, rise-fall-turn, prop-analogy, step-plan, mentor-quote; fit coaching. The
    devices are described in `devices.md` ("Talk").
