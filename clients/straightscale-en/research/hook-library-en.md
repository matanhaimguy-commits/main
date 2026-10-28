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
- **No transcripts (Instagram rows).** No Instagram row has a transcript, so no spoken first sentence could be read. Every hook below is the
  caption's first line (text only). The spoken hook of every `HF` and `HL` entry still needs a transcript.
- **No frames.** The cover images could not be downloaded (Instagram CDN refused by the session proxy), so the text
  on screen and the visual format are unknown. Each entry gives only what the data has: length in seconds and the
  post type.
- YouTube Shorts (added 28 Oct 2026): TranscriptAPI listings of @AlexHormozi and @DanMartell, 4 pages each, 192
  shorts each (`raw/yt-shorts_*`). 44 and 17 shorts at 3x+ their channel's median, 53 and 41 at 0.5x or less. 9
  on-topic breakouts (HF-10 to HF-18) and 5 on-topic losers (HL-07 to HL-11) now have a verbatim spoken first line
  from a transcript. @JeremyHaynes: not found by handle or name, skipped.
- YouTube Shorts, second batch (28 Oct 2026): one listing page (48 Shorts) each for @thefutur, @AlexBerman,
  @PatrickDang, @codiesanchezct, @LeilaHormozi, @NoahKagan, @JeremyMiner and @DanLok (`raw/yt-shorts_<handle>_p1.json`,
  trimmed to id, title and views; `..._outliers.csv`). @JeremyMiner and @DanLok had no Short at 3x+; @ImanGadzhi
  listed no Shorts; @JordanPlatten's best was 2.4x (not saved). 15 transcripts with timing in
  `raw/yt-shorts_transcripts.jsonl`; 12 on-topic breakouts are HF-19 to HF-30. Each is also a reference card in
  `motion-studio/refbank/cards/yt-*.md` (the card id is given per entry).
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

## Organic breakouts from YouTube Shorts (28 Oct 2026)
Source: TranscriptAPI `list_channel_videos` (tab "shorts", 4 pages per channel) saved as
`raw/yt-shorts_<handle>_p1..p4.json`, scored with `organic.py yt-import` and `organic.py outliers --days 0`
(`raw/yt-shorts_<handle>_outliers.csv`); spoken lines from `raw/yt-shorts_transcripts.jsonl` (TranscriptAPI
`get_youtube_transcript`). A Shorts listing carries no dates, so each median is over the 192 shorts fetched (about the
latest 192, all ages mixed), not over a date window. View counts are YouTube's rounded figures ("249K views").
On topic was judged by title only. @JeremyHaynes could not be listed (handle and name both "not found").
Spoken lines in a hot seat are the guest's, not the creator's: the creator answers from the second line.

- `HF-10` · Hot seat: the owner names a sales problem · AlexHormozi (YouTube Shorts) · 249K views (median 23K over 192 shorts) · 10.83x · **10x+** · https://www.youtube.com/shorts/P1Y82k_ZjXI
  - spoken (first sentence, verbatim from the transcript): "We do AI SEO." (then: "We went from zero to a million in roughly one year. What's stopping us right now is sales are crap.")
  - formula: "We do [service]. We went from [start] to [revenue] in [time]. What's stopping us right now is [sales / leads] are [blunt word]." (mad-lib)
  - checks: views only (a listing carries no likes or comments)
- `HF-11` · Hot seat: the owner who does not know his ad numbers · AlexHormozi (YouTube Shorts) · 216K views (median 23K over 192 shorts) · 9.39x · https://www.youtube.com/shorts/StctBbhyWFE
  - spoken (first sentence, verbatim from the transcript): "We sell drywall and plaster repair." (then: "What's revenue?" / "About 1.5 to 1.8. I think that my constraint right now is solid leads.")
  - formula: "We sell [service]." / "What's revenue?" / "[number]. I think my constraint right now is [solid leads]." (mad-lib)
  - checks: views only (a listing carries no likes or comments)
- `HF-12` · The beginner's excuse, answered bluntly · AlexHormozi (YouTube Shorts) · 198K views (median 23K over 192 shorts) · 8.61x · https://www.youtube.com/shorts/XYNw0FlE_xw
  - spoken (first sentence, verbatim from the transcript): "I see beginning entrepreneurs say they're like, "Well, that's not scalable.""
  - formula: "I see [buyers at their stage] say, "[the excuse they repeat]." And I'm like, "[two-word blunt truth]."" (mad-lib)
  - checks: views only (a listing carries no likes or comments)
- `HF-13` · Named pricing method, then the questions · AlexHormozi (YouTube Shorts) · 193K views (median 23K over 192 shorts) · 8.39x · https://www.youtube.com/shorts/r-9RpAv1P9A
  - spoken (first sentence, verbatim from the transcript): "There's called the Van Wesson door pricing analysis." (the auto-captions' spelling)
  - formula: "There's [a named method]. I do this most times when I [launch a new offer]. There's [four] questions you ask." (mad-lib)
  - checks: views only (a listing carries no likes or comments). The same clip with nearly the same transcript
    is `HL-10` at 0.27x under another title: the spoken hook did not make the difference here.
- `HF-14` · Hot seat: the owner names the constraint · AlexHormozi (YouTube Shorts) · 138K views (median 23K over 192 shorts) · 6.0x · https://www.youtube.com/shorts/dzAfAylrd48
  - spoken (first sentence, verbatim from the transcript): "I run a DTC uh skincare brand e-commerce." (then: "We do actually 10 million. We want to get to 100. The key constraint right now is margins, right?")
  - formula: "I run a [business]. We do [revenue]. We want to get to [goal]. The key constraint right now is [problem]." (mad-lib)
  - checks: views only (a listing carries no likes or comments)
- `HF-15` · "Is that like any good?" question from the audience · DanMartell (YouTube Shorts) · 120K views (median 24K over 192 shorts) · 5.0x · https://www.youtube.com/shorts/ycw9PAdAcbM
  - spoken (first sentence, verbatim from the transcript): "Do you like make websites for local business owners that don't have one?"
  - formula: "Do you like [do the service] for [the clients] that don't have one? Is that like any good?" (mad-lib)
  - checks: views only (a listing carries no likes or comments). Opens with a question, unlike principle 4.
- `HF-16` · One question, one-word answer · AlexHormozi (YouTube Shorts) · 86K views (median 23K over 192 shorts) · 3.74x · https://www.youtube.com/shorts/hB42tludbw0
  - spoken (first sentence, verbatim from the transcript): "Where is the moat in content?" (answer: "Reality is the moat.")
  - formula: "Where is the [edge] in [content / referrals / ads]?" / "[One word] is the [edge]." (mad-lib)
  - checks: views only (a listing carries no likes or comments). Opens with a question, unlike principle 4.
- `HF-17` · Hot seat: what the expert sells and to whom · AlexHormozi (YouTube Shorts) · 85K views (median 23K over 192 shorts) · 3.7x · https://www.youtube.com/shorts/qLS7wVGOBvw
  - spoken (first sentence, verbatim from the transcript): "I sell communication skills to senior leaders." (then: "Last 10 months, 300K.")
  - formula: "I sell [what the expert teaches] to [who buys]. Last [months], [revenue]." (mad-lib)
  - checks: views only (a listing carries no likes or comments)
- `HF-18` · Hot seat: revenue first, then where clients came from · AlexHormozi (YouTube Shorts) · 78K views (median 23K over 192 shorts) · 3.39x · https://www.youtube.com/shorts/n9ut262nmcQ
  - spoken (first sentence, verbatim from the transcript): "We are at 5.4 million." (then: "A 100% of our clients used to come from organic Tik Tok and Instagram.")
  - formula: "We are at [revenue]. [All] of our clients used to come from [one channel]." (mad-lib)
  - checks: views only (a listing carries no likes or comments)

What the 9 share (counts, not a grade): 5 of 9 are hot seats where a business owner speaks first and names the
business, a number or the constraint (HF-10, HF-11, HF-14, HF-17, HF-18); in 2 more a question opens and the creator
answers on the next line (HF-15, HF-16; the transcript has no speaker names). 0 of the 5 losers below open with a
hot seat. Only HF-10 is 10x+.

Off topic at 3x+ (by title, no transcript fetched, no id): AlexHormozi 36 more of his 44 at 3x+, led by "Am I In
The Wrong Business?" 808K (35.13x), "They Actually Followed Hormozi's Insane Advice" 503K (21.87x), "Which One Of Us
Is Right?" 467K (20.3x); DanMartell 16 more of his 17, led by "Whats the best AI tool right now?" 258K (10.75x), "Have
you tried Higgsfield Genjutsu?" 174K (7.25x).

## Organic breakouts from YouTube Shorts, second batch (28 Oct 2026)
Source and limits as the first batch above, with two differences: each median is over one listing page (the
channel's latest 48 Shorts), not 192, and on topic was judged from the transcript, not the title. Spoken lines are
verbatim from TranscriptAPI auto-captions. No frames could be fetched (i.ytimg.com refused by the proxy), so on-screen
text and visual are unknown unless the words imply them. Ranked by breakout.

- `HF-19` · Identity question with one prop · AlexBerman (YouTube Shorts) · 567K views (median 6.3K over 48 shorts) · 90.0x · **10x+** · https://www.youtube.com/shorts/w05ZBo57gvA
  - spoken (first sentence, verbatim): "Are you a businessman or are you an entrepreneur?" (then: "Here's an easy way to find out.")
  - formula: "Are you a [label A] or are you a [label B]? Here's an easy way to find out." then one object, two paths (mad-lib)
  - card: `yt-alexberman-orange` · checks: views only (a listing carries no likes, comments or dates)
- `HF-20` · "If I had to... here's exactly what I'd do" · PatrickDang (YouTube Shorts) · 31K views (median 1.75K over 48 shorts) · 17.71x · **10x+** · https://www.youtube.com/shorts/CBQsuB4m06c
  - spoken (first sentence, verbatim): "If I needed to make $3,000 with Claude AI in the next 30 days, here's exactly what I would do even if I had a full-time job."
  - formula: "If I needed to [goal] in the next [days], here's exactly what I would do, even if [constraint]." (mad-lib; the number must be the viewer's goal, never our result)
  - card: `yt-patrickdang-thirty-days` · checks: views only
- `HF-21` · Rule first, then a role-played sales call · thefutur (YouTube Shorts) · 154K views (median 9.75K over 48 shorts) · 15.79x · **10x+** · https://www.youtube.com/shorts/d-Wkas8aKko
  - spoken (first sentence, verbatim): "Just talk about money first." (then: "Talk about money because money is the disqualifier.")
  - formula: "Just [do the thing sellers avoid] first. [Do it] because [it] is the disqualifier." then a mock call (mad-lib)
  - card: `yt-thefutur-money-first` · checks: views only
- `HF-22` · Three picks, asked by someone else · thefutur (YouTube Shorts) · 150K views (median 9.75K over 48 shorts) · 15.38x · **10x+** · https://www.youtube.com/shorts/A-LQwz40G7Y
  - spoken (first sentence, verbatim, the second voice): "What are three marketing books every creative should read?"
  - formula: "What are [three] [things] every [buyer] should [use]?" asked by another person, answered item by item (mad-lib)
  - card: `yt-thefutur-three-books` · checks: views only. Opens with a question (principle 4), asked by someone else.
- `HF-23` · Blunt claim, then a mentor's words · LeilaHormozi (YouTube Shorts) · 27K views (median 2.3K over 48 shorts) · 11.74x · **10x+** · https://www.youtube.com/shorts/MW1yUGVdcEs
  - spoken (first sentence, verbatim): "The only thing you've got is your character."
  - formula: "The only thing you've got is your [quality]." then "[Mentor] told me: you don't have more [A], [B] or [C]..." (mad-lib)
  - card: `yt-leila-character` · checks: views only
- `HF-24` · "I can tell from one sentence": five levels · codiesanchezct (YouTube Shorts) · 214K views (median 18.5K over 48 shorts) · 11.57x · **10x+** · https://www.youtube.com/shorts/3NDIHrvyVCM
  - spoken (first sentence, verbatim): "I can now tell if an employee's going to make it from one sentence, and it's what they say when something breaks."
  - formula: "I can now tell if [a person] is going to [succeed] from one sentence, and it's what they say when [moment]. There are five levels." (mad-lib)
  - card: `yt-codie-five-levels` · checks: views only
- `HF-25` · Mid-story start with an age · NoahKagan (YouTube Shorts) · 8.4M views (median 644.5K over 48 shorts) · 13.03x · **10x+** · https://www.youtube.com/shorts/wJZYoF2C0RA
  - spoken (first sentence, verbatim, the guest): "Age 18 I started my own business selling nuts door-to-door."
  - formula: "Age [age], I started [first business]." then two falls and the question that turned it (mad-lib)
  - card: `yt-noahkagan-tire-shop` · checks: views only. On topic through the turn ("what do you do for a living?" asked to people who already had the result), not the first line.
- `HF-26` · Stop doing the three cheap versions · PatrickDang (YouTube Shorts) · 12K views (median 1.75K over 48 shorts) · 6.86x · https://www.youtube.com/shorts/-T34eARzeWU
  - spoken (first sentence, verbatim): "If you're trying to make money with Claude and AI, stop trying to do these AI coloring books, Etsy templates, or cheap PDFs." (auto-captions: "cloud")
  - formula: "If you're trying to [goal], stop trying to do [tactic 1], [tactic 2], or [tactic 3]." (mad-lib; aim at the tactic, never at the viewer)
  - card: `yt-patrickdang-s-tier` · checks: views only
- `HF-27` · Behind the scenes with a big number · NoahKagan (YouTube Shorts) · 3.3M views (median 644.5K over 48 shorts) · 5.12x · https://www.youtube.com/shorts/gOowzG23YX8
  - spoken (first sentence, verbatim): "I met a guy in the street, he had a clip about why rich people have too much money that has 17 million views."
  - formula: "I [found] a [thing] that [already worked], so we [built on it]." (mad-lib; the number must be real and ours)
  - card: `yt-noahkagan-millions-views` · checks: views only
- `HF-28` · Question, one-line answer, one number · LeilaHormozi (YouTube Shorts) · 9.7K views (median 2.3K over 48 shorts) · 4.22x · https://www.youtube.com/shorts/cHV0luUDVl4
  - spoken (first sentence, verbatim): "How do you evaluate trust?"
  - formula: "How do you [judge the thing buyers worry about]?" / "It usually comes from [one-line answer]." (mad-lib)
  - card: `yt-leila-trust` · checks: views only. Opens with a question (principle 4).
- `HF-29` · The paradox, then two labels · codiesanchezct (YouTube Shorts) · 65K views (median 18.5K over 48 shorts) · 3.51x · https://www.youtube.com/shorts/E3_naI8UUcs
  - spoken (first sentence, verbatim): "The most profitable businesses I've ever owned sell something nobody wants to buy."
  - formula: "The most [successful] [businesses] I've ever [run] [do the opposite of what you'd expect]. Let me explain." (mad-lib)
  - card: `yt-codie-oxygen-dessert` · checks: views only. Names life coaching as a "dessert" example: do not copy that line to coaches.
- `HF-30` · "My client just..." case in one breath · PatrickDang (YouTube Shorts) · 5.8K views (median 1.75K over 48 shorts) · 3.31x · https://www.youtube.com/shorts/5AaOQrN8_aA
  - spoken (first sentence, verbatim): "So, my client Tom just landed an $8,000 per month client selling AI services." (then: "And the funny part is he didn't even know anything about AI 2 months ago.")
  - formula: "So, my client [name] just [result]. And the funny part is [the excuse he didn't have]." (mad-lib; needs a real client result with an evidence file, brain E5)
  - card: `yt-patrickdang-client-tom` · checks: views only

What the 12 share (counts, not a grade): 6 of 12 put a contrast or a verdict in the first sentence (HF-19, HF-21,
HF-23, HF-24, HF-26, HF-29); 3 of 12 open with a question (HF-19, HF-22, HF-28), 2 of them asked by a second
voice or answered within 4 s; 4 of 12 are told as a story or a process with a person in it (HF-20, HF-25, HF-27,
HF-30). 7 of 12 are 10x+.

Off topic at 3x+ (transcript fetched, no id): codiesanchezct "Women make more money doing this ONE thing" 104K
(5.62x; card `yt-codie-one-thing`); AlexBerman "Companies That Own Everything" 22K (3.49x; card
`yt-alexberman-own-everything`); NoahKagan "How this Passenger Affords First Class" 2.0M (3.1x; card
`yt-noahkagan-first-class`, the street-interview format). Off topic by title, no transcript: AlexBerman "Buying the
Apple Vision Pro" 1.3M (206x), "How to Trick ChatGPT in 15 Seconds" 33K (5.24x); NoahKagan 7 more at 3x+ (wealth and life
stories); LeilaHormozi 5 more at 3x+ (leadership lines).

### Losers from YouTube Shorts (0.5x or less, on topic), ranked from the lowest
- `HL-07` · Client story about an offer · AlexHormozi (YouTube Shorts) · 5.4K views (median 23K over 192 shorts) · 0.23x · https://www.youtube.com/shorts/Co9FC0G3SNM
  - spoken (first sentence, verbatim from the transcript): "So, I had a lady a couple months ago and so she did hairstyle stuff and so she's like, "Okay, I can teach hairdressers how to do this particular type of cut.""
  - formula: "So, I had a [client] a couple months ago and so she did [niche] and so she's like, "[what she sells]."" (mad-lib)
  - checks: views only (a listing carries no likes or comments)
- `HL-08` · Bare milestone as the first words · AlexHormozi (YouTube Shorts) · 5.5K views (median 23K over 192 shorts) · 0.24x · https://www.youtube.com/shorts/_-dt0VAqbFs
  - spoken (first sentence, verbatim from the transcript): "Zero to a million."
  - formula: "[Start] to [milestone]. Really, really simple." (mad-lib)
  - checks: views only (a listing carries no likes or comments)
- `HL-09` · If-then rule about better clients · AlexHormozi (YouTube Shorts) · 5.7K views (median 23K over 192 shorts) · 0.25x · https://www.youtube.com/shorts/iIpgcNGAwrA
  - spoken (first sentence, verbatim from the transcript): "If you increase the quality of your prospects, you will increase the quality of your product."
  - formula: "If you increase the [quality] of your [prospects], you will increase the [quality] of your [product]." (mad-lib)
  - checks: views only (a listing carries no likes or comments)
- `HL-10` · Named pricing method (same clip as HF-13) · AlexHormozi (YouTube Shorts) · 6.2K views (median 23K over 192 shorts) · 0.27x · https://www.youtube.com/shorts/Ij9RfYWzzBk
  - spoken (first sentence, verbatim from the transcript): "There's called the Van Wesson door pricing analysis."
  - formula: same as HF-13; the title was "Ask your customers these four questions before you set your price." against
    HF-13's "How I Price Every New Offer" (the listing has no dates, so which came first is unknown)
  - checks: views only (a listing carries no likes or comments)
- `HL-11` · "The worst thing you could say" question · DanMartell (YouTube Shorts) · 7.4K views (median 24K over 192 shorts) · 0.31x · https://www.youtube.com/shorts/Y0yte9zAy6k
  - spoken (first sentence, verbatim from the transcript): "Do you know the worst thing you could say on a sales call?"
  - formula: "Do you know the worst thing you could say on a [sales call]?" (mad-lib)
  - checks: views only (a listing carries no likes or comments)

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
HL-01 to HL-11 structures; hooks that open with a question (principle 4); the banned hook words from the
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
- YouTube Shorts (HF-10 to HF-18, HL-07 to HL-11): views only, as YouTube rounds them (no likes, comments or dates in
  a listing), so none of the 4 checks beyond views could run and the age of each short is unknown. Each median is
  over the 192 shorts fetched, not a date window. Two creators only, one of them (AlexHormozi) gives 12 of the 14
  entries. On topic was judged by title. The transcripts are auto-captions (e.g. "Van Wesson door" in HF-13), and a
  hot seat's first line is the guest's voice. HF-13 and HL-10 carry nearly the same transcript at 8.39x and 0.27x,
  so for these clips the title or timing, not the spoken words, made the gap. YouTube Shorts are not Instagram reels:
  the same hook may do differently on @straightscale_.
- Second batch (HF-19 to HF-30): the same limits, plus a median over only 48 Shorts per channel (one page), so a few
  Shorts move it. NoahKagan's median is 644.5K: his 3x bar is near 2M. Six of the twelve come from two channels
  (PatrickDang, codiesanchezct). PatrickDang's titles and hooks lean on AI money claims; take the structure only.

## Live results
(empty: logged by the analyst at 72 h and 7 d after each post)
