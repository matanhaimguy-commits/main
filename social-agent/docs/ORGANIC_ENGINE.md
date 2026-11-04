# Organic Engine V2.4 -> Social Agent (landing pages)

This integrates with the **existing** Instagram/Facebook Social Agent. The content machine writes the scripts, CTAs and six promised tools; Social Agent handles the comment, private reply, button tap, AI conversation, lead and tracking. No duplicate sender is created.

## The viewer experience

1. The viewer comments a keyword on a Reel: מודעות / מילים / הצעה / שפינדורה / רווח / כבוד.
2. Social Agent sends its ordinary private reply with a **שלח לי** tap button.
3. After the tap, its ordinary link-message opens a public Emperium page with:
   - a short explanation of the benefit,
   - three very simple steps,
   - the actual prompt, guide or calculator,
   - an **העתק** button to copy it,
   - a link to open ChatGPT.
4. The viewer can reply in the original DM; the existing AI sales agent continues the conversation.

No registration is required to open the resource. Use of the page does not depend on Social Agent sending six long messages. The existing link delivery path is unchanged.

## Public pages on the existing Social Agent host

Once this Social Agent build is deployed, these routes serve the actual approved resources from imports/emperium-v24.json:

- /resources/emperium/V24-01 - five awareness levels
- /resources/emperium/V24-02 - customer-language research
- /resources/emperium/V24-03 - three new offers without discounts
- /resources/emperium/V24-04 - eight creative angles and a short guide
- /resources/emperium/V24-05 - campaign profit calculator and prompt
- /resources/emperium/V24-06 - seven boundary-setting replies and an adapted prompt

The host is the **existing** Social Agent domain. This document intentionally does not invent a public URL. Both Dockerfiles now bundle the approved import data for runtime use.

## Preview, no live messages

From social-agent/:

    npm ci
    npm run typecheck
    npm test
    npm run organic:import -- --file imports/emperium-v24.json --business emperium

Expected: 6 pending flows, 0 imported funnels, no Meta calls and no config writes.

## After publishing a Reel

Find its real Instagram media ID:

    npm run cli -- meta:posts emperium instagram

Import exactly that video after checking that the deployed resource page opens in a browser:

    npm run organic:import -- --file imports/emperium-v24.json --business emperium --post V24-01=REAL_NUMERIC_POST_ID --base-url https://YOUR_ACTUAL_SOCIAL_AGENT_DOMAIN --apply

Repeat --post for several published videos.

The importer writes only **PAUSED** funnels pinned to real post IDs and keeps all existing business settings. It does not send messages or enable live delivery.

Check before enabling:

    npm run audit
    npm run cli -- preview emperium oe-v24-01
    npm run cli -- match emperium instagram REAL_NUMERIC_POST_ID "מודעות"

Then test a real comment from a separate test account. Only after a successful complete DM and link test, turn the specific funnel to active. Social Agent's existing business live flag, allowed testers and LIVE_SENDING switch still control real sends.

## Change management

Organic Engine owns the creative source at clients/emperium/outputs/social_agent_handoff_v24.json in the organic-engine repository. The Social Agent imports snapshot lives at social-agent/imports/emperium-v24.json in this repository.

When new content is approved, refresh the snapshot, test the landing pages and import the new video/post pairs. If a flow ID is already present but the post or resource link changed, the importer refuses to overwrite it silently.

These six landing pages are built into the repository, not confirmed deployed. No Reels have been published, and none of the comment-to-DM funnels are active from this integration.
