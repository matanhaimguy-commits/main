# EN 02 distribution package

Distribution Agent, ORGANIC-OS 8.2 to 8.4, 28 Oct 2026. Account @straightscale_ (English, global). Delivery: `deliver/v1/`
(9:16, 1080x1920, 42.15 s). Card: `clients/straightscale-en/cards/2026-11-W1/SSEN-2026-10-W5-02.yaml`.
Hub draft: `hub/item.json` (caption in `hub/caption.txt`). Status: **not pushed yet** (see Blocked).

## Hub check (28 Oct, read only)
- `hub.py ping`: OK, 1 business.
- `straightscale`: **live**, timezone Europe/Tirane, Instagram @straightscale_. Profile is the Albanian offer (audience
  "owners of service businesses in Albania", free 45-minute analysis in Tirana, link titles in Albanian); the voice line
  answers in the customer's language (Albanian, English or Hebrew).
- Funnels: `analiza` (comment, all posts, active) and `analiza-dm` (DM keyword, active), keywords analiza, analizë,
  analize, analysis. **No WORDS funnel.** A WORDS comment today gets no funnel reply; a DM gets the Albanian-offer bot.

## Caption (8.2)
First line restates the hook with search words (hooks, buyers, exact words). The CTA repeats the keyword WORDS. Global
account, so no location tag. 756 characters.

```
Your buyers already wrote your hooks. Here are 3 places to find their exact words.

"2 years of posting content, running ads, and praying someone books a call."
We didn't write that. A business owner did, in a review.

Where to find your buyers' sentences:
1. Your competitors' worst reviews: what people paid for and never got.
2. Reddit threads in your niche: the problem, before they know you exist.
3. Newsletters where owners write about their worst month.

Copy the sentence. Don't polish it. Once it's polished, it sounds like an ad.

Comment WORDS for the exact searches we use. You get the WORDS Sheet in your DMs: 12 copy-paste searches for reviews, Reddit, newsletters and more.

#voiceofcustomer #copywritingtips #agencyowner #coachingbusiness
```

Facts: the quote is VOC Q-E-0009 (Trustpilot, 20 Aug 2025), verbatim, no name; the three places and the polish line are
the script's own lines; "12 copy-paste searches" is the brain's WORDS `resource` line. No numbers beyond those.

## Hashtags (8.2: 3 to 5, specific)
`#voiceofcustomer #copywritingtips #agencyowner #coachingbusiness`: the method, the job the viewer is doing, and the
avatar's two roles (AV-01: agency owner, coach). No #reels, #explore or broad tags.

## Cover
`deliver/v1/poster.png` (1080x1920, from the film). Goes up as the hub item's `cover_url`.

## AI label (STANDARDS 7)
The narrator is an AI voice (Kokoro af_heart), so **Instagram's own AI label is on** when the post goes out. No burned-in
tag. The hub notes start with "AI label: on".

## Trial reel plan (8.3)
One change at a time, judged at 72 hours against the main post (first EN reel, so it sets the baseline).
1. **Main post** to followers: v1 as delivered.
2. **Trial 1, first frame only**: same cut, the first frame's text super changed to hook 2 from PROJECT.md, "The best
   copywriter for your business is a one-star review." (A-). Needs a v1b render of the opening card only; not made yet.
   Judge on skip rate and average watch time, not comments (a trial reaches non-followers, and Instagram won't
   recommend posts that ask non-followers to comment a word).
3. If the main post beats the account baseline 2x, re-post it as a trial 14 to 30 days later with a new spoken hook
   (hook 3, "Your best hook is already written. By your buyer."), which needs a new voice line and render.

## Stories (8.4, point, expand, proof, CTA), day of posting
Only after the `words-dm` funnel is live, because the last frame asks for a DM.
1. Point: "Your best hook is already written. Not by you."
2. Expand: the quote slip from the film, "2 years of posting content, running ads, and praying someone books a call."
3. Proof: "We collected 567 of these before we posted a single video." (PROJECT.md: 06-VOC_MASTER.csv, 567 quotes)
4. CTA: "DM me WORDS for the 12 searches." plus the new reel sticker.

## Checks run
`organic.py brain-check straightscale-en`: OK, 10 gaps (among them `lead_magnets[WORDS]` not live).
`organic.py card-check straightscale-en ...` cannot run: `clients/straightscale-en/content-map.json` does not exist.
The same check function with an empty map gives:
- FAIL map: pillar "Research" and series "how the pieces fit" are not on the map (no map yet).
- FAIL conversion: keyword WORDS has no live flow and resource yet (`live: false` in the brain).
- warn reach: Instagram won't recommend posts that ask non-followers to comment a word; on a reach post prefer send, save
  or follow. Kept: the WORDS resource is the point of the post (owner's brief, SIMPLE.md step 7).
- warn: B4 usually serves trust and fits solution aware; 42 s sits between the O30 and O60 tiers.

## Blocked
- **Uploads**: `hub.py upload` fails with STORAGE_UNREACHABLE: the network policy denies the hub's storage host
  `c--239a3368-f157-4af9-9f3c-129789693927-prod.lovable.cloud`. The hub API itself is reachable. With no media URLs, the draft is
  not pushed (a reel draft with no video can't be approved or posted). Once the host is allowed:
  `python3 growth-engine/tools/hub.py push motion-studio/projects/straightscale-en-02/hub/item.json` uploads the video
  and cover and creates the draft in one step (status draft, no scheduled time); then
  `hub.py upload straightscale motion-studio/projects/straightscale-en-02/resource/WORDS.pdf` for the PDF URL.
- **Before approval**: English profile and the WORDS funnel live and tested from a tester account (the notes say so).
