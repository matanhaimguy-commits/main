# Hook Library: StraightScale English page (@straightscale_), B2B growth for founder-led experts

Organic Hook Library per `growth-engine/adapters/hook-lab-organic.md` ("The organic Hook Library"): built only from
real posts measured against each creator's own median views, plus competitor ads ranked by days running. Rebuilt
28 Oct 2026 from the raw Apify datasets (`raw/`, listed in `raw/README.md`). Replaces the 27 Oct version, whose
evidence (774 posts with transcripts) could not be found again. Refresh by 27 Dec 2026 (60 days).

How to cite: a hook names one `HF-nn` (organic post, 3x or more) as its proven format and one or more buyer phrase
ids from `buyer-phrases-en.md`. `HL-nn` are losers: never copy them. `HA-nn` are ads (proof by run time, not by
views); the hook check (`organic_os/hook_sources.py`) reads only `HF` and `HL` ids today.

## Coverage
- Organic: `raw/instagram-posts_hAUOxNiKOpKuAA0GS.jsonl`, apify/instagram-scraper, 25 Oct 2026, 145 posts from 8
  accounts: jeremy, iamcameronengland, siggyvonvoss, russruffino, thechrisbarry, clientascension, raviabuvala,
  itskaibax. Only 2 of the 13 creators named in the 25-26 Oct brief (jeremy, iamcameronengland) are in it. The
  774-post scrape with transcripts is not in the Apify run list for 22 to 26 Oct.
- Scored with `python3 growth-engine/tools/organic.py outliers <file> --days 0` (the 4 checks of ORGANIC-OS 5.1:
  views 3x the median, comments above the account's rate, likes in proportion, engagement 2% or more). 85 videos
  have views; 12 are at 3x or more, 10 at 0.5x or less, 63 in between.
- **No transcripts.** No row has a transcript, so no spoken first sentence could be read. Every hook below is the
  caption's first line (text only). The spoken hook of every `HF` and `HL` entry still needs a transcript.
- **No frames.** The cover images could not be downloaded (Instagram CDN refused by the session proxy), so the text
  on screen and the visual format are unknown. Each entry gives only what the data has: length in seconds and the
  post type.
- Ads: 11 Meta Ad Library datasets (curious_coder/facebook-ads-library-scraper, 25 Oct 2026), 550 ads from 11
  pages, 126 distinct ad texts after merging copies (empty and template texts left out).

## Organic outliers on the buyer's topics (3x or more), ranked by breakout, grouped by formula family
Topics: clients, leads, referrals, content, posting, offer, pricing, ads, pages, sales calls, lumpy months. Three
outliers at 3x+ are off topic or have no caption and get no id (listed after the families).
**10x+** marks a structure that may be copied as is; 3x to 10x is a proven format to adapt.

### Family 1: an analogy from outside the niche
- `HF-01` · Luxury-brand analogy · russruffino · 18,006 views (median 170) · 105.6x · **10x+** · 22 Oct 2026
  - text (caption line 1; spoken line not in data): "There’s a reason luxury brands like Cartier don’t just disappear the second you buy"
  - formula: "There's a reason [famous premium brand] don't just [do the thing buyers fear] the second you [buy]"
  - on screen: not in data · visual: 7 s reel · checks: comments 0 (account rate 0.04 per 1K), likes not in
    proportion, engagement 0.2%: the views may be paid or looped, not chosen

### Family 2: the inside look
- `HF-02` · Inside look at being a client · siggyvonvoss · 213,028 views (median 7,236) · 29.4x · **10x+** · 15 Jan 2026
  - text (caption line 1): "What it looks like to be a 1-1 client inside ScaleInfo"
  - formula: "What it looks like to be a [type of client] inside [the business]"
  - on screen: not in data · visual: reel, length not in data · checks: comments 0.10 per 1K (account 0.24), likes
    not in proportion, engagement 0.3%: views may be paid (the same account runs ScaleInfo ads)

### Family 3: two roles side by side
- `HF-03` · Role versus role · siggyvonvoss · 208,076 views (median 7,236) · 28.8x · **10x+** · 17 Apr 2026
  - text (caption line 1, the whole caption): "setter vs closer"
  - formula: "[role A] vs [role B]" (two jobs in the buyer's own sales process)
  - on screen: not in data · visual: 58 s reel · checks: comments 0.25 per 1K (above the account's 0.24), likes in
    proportion, engagement 0.9% (under 2%): the best-checked on-topic winner (3 of 4 checks)

### Family 4: the myth, then the correction (numbered)
- `HF-04` · Numbered myth list, vanity vs paying clients · russruffino · 1,928 views (median 170) · 11.3x · **10x+** · 24 Oct 2026
  - text (caption line 1): "1. “You need more followers.” No. You need more paying clients."
  - formula: "1. “You need more [vanity number].” No. You need more [the thing that pays]."
  - on screen: not in data · visual: 7 s reel · checks: 0 comments, likes in proportion, engagement 0.5%
- `HF-05` · Numbered myth list, selling vs wanting · russruffino · 1,864 views (median 170) · 10.9x · **10x+** · 23 Oct 2026
  - text (caption line 1): "1. You shouldn’t sell to your prospects. You should make them WANT to buy."
  - formula: "1. You shouldn't [what everyone does] your [buyers]. You should [the opposite they want]."
  - on screen: not in data · visual: 7 s reel · checks: 0 comments, likes in proportion, engagement 0.6%

### Family 5: call out the buyer, then name their month
- `HF-06` · Buyer call-out with the lumpy month · siggyvonvoss · 48,676 views (median 7,236) · 6.7x · 15 Jun 2025
  - text (caption line 1): "follow @siggyfoss if you’re a coach who wants $50-100k/months"; line 2: "but every month feels like starting from zero again bc you’re stuck relying on referrals, posting once a day, or even sending cold dms"
  - formula: "[follow / watch] if you're a [buyer] who wants [outcome] / but every month feels like starting from zero again bc you're stuck relying on [referrals], [posting], or [cold DMs]"
  - on screen: not in data · visual: 10 s reel · checks: comments 0.16 per 1K (under 0.24), likes in proportion,
    engagement 0.5%. Line 2 is the closest match in the set to the buyer phrases on referrals and lumpy months
    (`Q-R-0058`, `Q-RN-0001`).

### Family 6: the result as the label
- `HF-07` · Result number as the whole hook · siggyvonvoss · 48,292 views (median 7,236) · 6.7x · 28 Sep 2026
  - text (caption line 1, the whole caption): "12x roas on profile funnel"
  - formula: "[result number] on [the method]"
  - on screen: not in data · visual: 83 s reel · checks: comments 0.25 per 1K (above 0.24), likes in proportion,
    engagement 0.6%

### Family 7: the introduction
- `HF-08` · "If we haven't met" intro · iamcameronengland · 123,830 views (median 27,055) · 4.6x · 21 Aug 2026
  - text (caption line 1): "Hey if we haven’t met, my name is Cameron."; line 2 starts: "I run License & Scale and help agency owners break past their revenue ceiling"
  - formula: "Hey if we haven't met, my name is [name]. I run [company] and help [buyer] [outcome] without [cost they fear]."
  - on screen: not in data · visual: 42 s reel · checks: comments 0.58 per 1K (account 3.14), likes in proportion,
    engagement 2.8%

### Family 8: what the expert sees in clients
- `HF-09` · "Most [buyers] I work with don't" · thechrisbarry · 509 views (median 113) · 4.5x · 22 Oct 2026
  - text (caption line 1): "Most coaches I work with don't actually get into the inbox."
  - formula: "Most [buyers] I work with don't actually [basic thing they assume works]."
  - on screen: not in data · visual: 37 s reel · checks: 0 comments, likes in proportion; tiny base (113 median)

### Outliers at 3x+ with no id (off topic or no text)
- russruffino, 2,262 views, 13.3x, 18 Oct 2026, mindset: "You don't have to believe it all at once."
- iamcameronengland, 153,543 views, 5.7x, 8 Sep 2026: no caption, topic unknown (needs a transcript)
- jeremy, 49,172 views, 5.6x, 22 Oct 2026: "Opening my $25M award!" (the only post in the set passing all 4 checks)

## Losers on the buyer's topics (0.5x or less), ranked from the lowest
- `HL-01` · Ads tip · thechrisbarry · 31 views (median 113) · 0.27x · 19 Oct 2026
  - text (caption line 1): "Running ads may be unprofitable in the beginning."
  - formula: "[Channel] may be [bad thing] in the beginning." · visual: 48 s reel · 0 likes, 0 comments
- `HL-02` · Question the buyer asks · thechrisbarry · 33 views (median 113) · 0.29x · 25 Oct 2026 (0 days old at the scrape)
  - text (caption line 1): "How do I niche down without scaring off clients?"
  - formula: "How do I [fix] without [fear]?" · visual: 47 s reel · 0 likes, 0 comments
- `HL-03` · Blunt rule · siggyvonvoss · 3,202 views (median 7,236) · 0.44x · 16 Oct 2026
  - text (caption line 1): "you don’t have a business unless you can buy customers"
  - formula: "you don't have a [business] unless you can [do the thing]" · visual: 31 s reel · comments 0.62 per 1K
    and engagement 2.6% (both above the account): seen by few, liked by those who saw it
- `HL-04` · Someone else's costly setup · siggyvonvoss · 3,275 views (median 7,236) · 0.45x · 25 Oct 2026 (0 days old)
  - text (caption line 1): "bro was paying 15k/mo base to his closers AND 15% COMMS"
  - formula: "bro was paying [cost] to his [role] AND [extra cost]" · visual: 68 s reel · engagement 2.2%
- `HL-05` · Sales-call how-to · thechrisbarry · 53 views (median 113) · 0.47x · 18 Oct 2026
  - text (caption line 1): "Get on a free call. Find what they're facing and give them 30 minutes of real value."
  - formula: "[Step 1]. [Step 2] and give them [free value]." · visual: 43 s reel · 0 likes, 0 comments
- `HL-06` · "The biggest mistake" · thechrisbarry · 56 views (median 113) · 0.50x · 23 Oct 2026
  - text (caption line 1): "The biggest mistake: your offer and your marketing are focused on the warm audience, not the cold."
  - formula: "The biggest mistake: your [thing] is [wrong way], not [right way]." · visual: 46 s reel · 0 likes, 0 comments

Off topic or no text at 0.5x or less (no id): jeremy 0.47x "When your motives die, your reasons have to change.";
siggyvonvoss 0.41x "life by design"; iamcameronengland 0.48x and 0.44x, no caption.

## Ads that kept running (proof by run time), ranked by days
Days = first seen start date to the scrape (25 Oct 2026) or to the end date. Copies = ads in the set with the same
text. Only pages that sell to coaches, consultants or agency owners get an id.
- `HA-01` · Will B. Consulting · 71 days, 27 copies, image, active · title: "The Client Acquisition System Built For Established Coaches And Consultants"
  - line 1: "Attention coaches and consultants:" then "If your business is already bringing in consistent monthly revenue, you don't need more hustle."
  - formula: "Attention [buyers]: If your business is already [what they have], you don't need more [what they think they need]."
- `HA-02` · Russ Ruffino - Clients on Demand · 68 days, 3 copies, video, active
  - line 1: "The Real Reason Coaches With Mediocre Funnels Scale to $100K/Month:"
  - formula: "The Real Reason [buyers] With [weak version of the fix] [get the outcome]:"
- `HA-03` · Russ Ruffino - Clients on Demand · 68 days, 3 copies, video, active
  - line 1: "How We're AI-Proofing Our Coaching Business in 2026:"
  - formula: "How We're [protecting against the new threat] Our [business type] in [year]:"
- `HA-04` · Russ Ruffino - Clients on Demand · 64 days, 5 copies, video, active · title: "Your Sales Calls Aren’t the Problem."
  - line 1: "A great offer isn’t enough if you’re still wondering where your next client is coming from." then "Posting more. / Launching again. / Changing your ads."
  - formula: "A great [thing they have] isn't enough if you're still wondering where your next [client] is coming from. [Fix 1]. [Fix 2]. [Fix 3]."
- `HA-05` · Will B. Consulting · 64 days, 1 copy, video, active
  - line 1: "YouTube deleted my channel and my business tripled, jumping to $1.1M cash-collected with $1.3M in revenue for April"
  - formula: "[Channel] deleted my [asset] and my business [grew], jumping to [number]"
- `HA-06` · Will B. Consulting · 49 days, 1 copy, video, active
  - line 1: "Ross Wade spent 2,500 on ads in his first month and turned it into 52,000 in revenue."
  - formula: "[Client name] spent [amount] on [channel] in his first month and turned it into [result]."
- `HA-07` · Will B. Consulting · 45 days, 33 copies, image, active · title as `HA-01`
  - line 1: "For coaches and consultants who want consistent growth:" then "Referrals are great until they slow down. / Organic content works until the algorithm shifts. / Word of mouth builds momentum until it suddenly doesn't."
  - formula: "For [buyers] who want [consistent outcome]: [Channel A] are great until they [stop]. [Channel B] works until [it stops]."
- `HA-08` · Kai Bax - ScaleClients.io · 42 days, 3 copies, video, active
  - line 1: "AI Automation Agencies / AI Agencies: These simple AI Meta Ads generate my sales team 300 - 500 qualified, pre-sold sales calls every month for my high-ticket offer on complete autopilot…"
  - formula: "[Buyer type]: These simple [tool] generate my [team] [number] [result] every month"
- `HA-09` · Kai Bax - ScaleClients.io · 40 days, 17 copies, image, active · title: "Pay In Full After This AI Gets You Clients"
  - line 1: "GHL SaaS Agencies: This simple AI Ad Infrastructure generates my agency 300–500 pre-sold sales calls and 75+ new high-ticket clients every month."
  - formula: as `HA-08`, with the payment terms in the title
- `HA-10` · Scaling With Systems · 38 days (8 Mar to 15 Apr 2026), 2 copies, video, stopped
  - line 1: "$100k/Mo Founders: If most of your deals require 2–3 calls to close, your system is leaking time and capacity."
  - formula: "[Revenue level] Founders: If most of your [deals] require [number] [calls] to close, your [system] is leaking [time]."
- `HA-11` · License & Scale - Cameron England · 36 days, 46 copies, video, active · title: "Work With Me One-on-One"
  - line 1: "I’ve opened a limited number of spots to work with me one-on-one."
  - formula: "I've opened a limited number of spots to [work with me] [format]."

Ran 30+ days but sell to a different buyer (no id): Christian Bonnier 145 days (people leaving a 9-to-5); Daniel
Fazio 114 days, 10 texts (new AI agencies); FP Sales 56 days, 60 copies (salespeople); Will B. Consulting 92, 64, 54
and 39 days (selling a company, life, "The journey is never linear").

Ads that stopped fast (losers by run time, no id): Scaling With Systems, 9 texts that ran 2 to 7 days in Feb and Mar
2026, for example "Your close rate isn’t a sales problem.", "Most founders think they have a lead problem.", "Why
are you paying for calls you can’t close?". 8 of the 9 ended between 8 and 11 Mar 2026, so they may have been
cut as a batch, not one by one.

## Custom principles (each with its count; ids above)
1. **Views alone are not proof here.** Of the 12 posts at 3x+, 9 fail the comments check and 10 fail engagement
   2%; 1 passes all four checks, and it is off topic (jeremy). On topic, the best-checked winner is HF-03 (3 of
   4). Cite an `HF` for its structure, not as proof that buyers came.
2. **Short beat long at the same creator.** russruffino: 4 of his 5 clips under 10 s reached 10x+ (HF-01,
   HF-04, HF-05, and an off-topic one); the fifth is 2.1x. All 7 of his clips over 45 s sat at 0.56x to 1.29x.
   All 5 short ones have 0 or 1 comments, so this is a format to test, not a proven buyer-getter.
3. **A number in the first line:** 6 of 12 winners (50%), 2 of 10 losers (20%), 17 of 63 in between (27%).
4. **No winner opens with a question:** 0 of 12 winners, 1 of 10 losers (HL-02), 7 of 63 in between.
5. **Length and "you" do not separate them.** First-line median words: winners 9, losers 10.5, middle 17. "you" in
   the first line: 5 of 12, 3 of 10, 32 of 63.
6. **Losers are partly just young.** 8 of 10 losers were 7 days old or less at the scrape, against 6 of 12 winners.
   HL-02 and HL-04 were 0 days old. 2 of the 6 on-topic losers (HL-03, HL-04) beat their account on
   comments and engagement.
7. **Tips with zero response at a tiny account.** 4 of the 6 on-topic losers are thechrisbarry tips (median 113
   views); all 4 had 0 likes and 0 comments.
8. **The ads that lasted name the buyer or the buyer's situation first:** 8 of the 11 `HA` ads (`HA-01` to `HA-04`,
   `HA-07` to `HA-10`); the other 3 open with a result or an offer (`HA-05`, `HA-06`, `HA-11`).
9. **The two ads with the most copies say the lumpy month in channel words:** `HA-07` (33 copies) "Referrals are
   great until they slow down." and `HA-01` (27 copies), same page and title. Buyers say the same thing: 7 referral
   lines in `buyer-phrases-en.md` (section 2), e.g. `Q-RN-0014` "...but that cannel also dried up".

## Do not use
HL-01 to HL-06 structures; hooks that open with a question (principle 4); the banned hook words from the
strategy (Patchwork, agency, done-for-you, funnel, qualified, guaranteed, growth partner, AI); real platform logos
or names on screen. The 27 Oct entries (Priestley "Cold email?" 12.5x, danmartell "Sales." 11.2x, sabrisuby,
takimoore, kallawaymarketing) are withdrawn: their rows were not recovered, so they cannot be cited.

## Limits
- 145 posts, 85 with views, 8 accounts; only 2 of the 13 creators the buyer follows. Small samples per account
  (9 to 20 videos), so one post moves a median.
- No transcripts and no frames: every hook is a caption line, and on-screen text and visual format are unknown.
- Views are not buyers. Several winners look paid or looped (principle 1).
- Ads: run time shows a page kept paying for an ad, not that it made money. Pages scraped as "active only" show no
  stopped ads, so ad losers come from one page.
- Dates are post dates; the scrape is 25 Oct 2026.

## Live results
(empty: logged by the analyst at 72 h and 7 d after each post)
