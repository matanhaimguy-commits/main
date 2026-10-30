# Research refresh, 28 Oct 2026 (for 2026-W45 and W46)

**Status: the new scrape is blocked.** The gated Apify run (apify/instagram-scraper, 7 handles from `competitors.md`
without @hormozi, posts newer than 2026-07-28, resultsLimit 100, cap USD 3; the Apify gate allowed it) was refused by
Apify: "Too many outstanding invoices". Spend: USD 0. Owner action: settle the Apify invoices, then re-run the call in
`scrape-pending.json`.

**What was done instead.** The 14 Oct dataset (172 posts, last 20 per handle, spanning May to Oct 2026) was rebuilt as
`dataset.json` from `../2026-10-14/dataset_min.tsv` and scored with the 4 outlier checks:
`organic.py outliers dataset.json --days 200 --out outliers.csv` (136 unpinned posts). This is not the 3-month base
set the OS asks for: 20 posts per account is a thin sample, and adjacent-niche accounts are still not listed.

## Trusted outliers (all 4 checks)
| x median | Account | Post | Type |
|---|---|---|---|
| 8.18 | @sabrisuby | https://www.instagram.com/p/DeBOovWhrXI/ | reel |
| 6.38 | @sabrisuby | https://www.instagram.com/p/Dc9pq-nh-l6/ | reel |
| 3.62 | @addoaesthetics | https://www.instagram.com/p/DdURDRfivLI/ | reel |

Captions are not in the reduced dataset, so these three can't be broken down without the CDN or a re-scrape: they
count as format evidence only (short talking reels win for the non-Albanian accounts).

## Hidden likes, for a check by hand
None in this dataset: no post has likesCount -1. Rerun after the new scrape.

## Likes-only breakouts (carousels and images; fallback signal, not trusted)
| x median (likes) | Account | Post |
|---|---|---|
| 30.31 | @eri.businesscoach | https://www.instagram.com/p/DeXWyI2CE-y/ (numbered owner self-check, 14 Oct pick) |
| 15.78 | @ermalmamaqiofficial | https://www.instagram.com/p/Dd64Fk8CDKj/ |
| 8.75 | @addoaesthetics | https://www.instagram.com/p/DdZlJVmlpiv/ |
| 7.81 | @eri.businesscoach | https://www.instagram.com/p/DeeyfcYDS23/ (owner-fear question image, 14 Oct pick) |
| 4.30 | @ermalmamaqiofficial | https://www.instagram.com/p/DeM2S-gHAlp/ |

## What it changes for the plan
Nothing new against 14 Oct: owner-focused numbered self-checks and single uncomfortable questions still lead locally;
reels that win are short and spoken. The plan keeps the 14 Oct pattern (`../2026-10-14/pattern.txt`) and the vault, and
leans on the contrarian vault and the demand map for the 20 to 30% original share.
