"""page_facts: checkable facts about a prospect's web page, for the leak scorecard. Facts only, never scores.

  python3 growth-engine/tools/page_facts <url> [--render] [--json] [--out FILE]

One job per module: fetch (+ opener, charset, urls) gets the page; htmldoc parses it once; trackers
(+ signatures), forms, routes, basics, jsonld and js_built read it; site_files (+ robots, sitemap) reads
robots.txt and the sitemap; render (+ render.js) is --render; facts assembles; summary (+ say_*) writes the
markdown; cli wires; errors holds the exit messages.

--json prints one object:
  url, final_url, status, mode ("static"|"rendered"), checked_at (UTC ISO), truncated (bool)
  js_built:   {flagged, body_text_chars, mount_points[], bundle_scripts[]}   (always about the static HTML)
  trackers:   [{name, found, ids[], evidence, seen_in[]}] for Meta Pixel, Google Tag Manager, GA4, Google Ads,
              TikTok Pixel, Microsoft Clarity, Hotjar; seen_in from "html", "rendered", "requests"
  forms:      [{action, method, where, fields: [{name, type, required}], fields_to_fill, asks_email, asks_phone}]
  routes:     [{kind: booking|form|messaging|direct, service, url, where: header|footer|body,
                via: link|iframe|embed, text?}]
  basics:     {title, meta_description, h1[], canonical, lang, viewport, og{}}   (None when missing)
  jsonld:     {types[], blocks, invalid_blocks}
  robots_txt: {url, status, present, sitemaps[], blocks_all, note?}
  sitemap:    {url, status, present, kind: urlset|sitemapindex|None, url_count, children?, children_read?, note?}
  rendered:   {requests_seen, network_idle}   (only with --render)

Tests: python3 -m unittest discover -s growth-engine/tools/page_facts -p 'test_*.py'
"""
