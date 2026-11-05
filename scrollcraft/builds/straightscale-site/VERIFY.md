# Verification: straightscale.com homepage rebuild (21 Oct 2026)

Branch `claude/homepage-rebuild` of `matanhaimguy-commits/straight-scale`. Everything below was checked on the local dev
server (Playwright, Chromium) unless it says "sandbox". This container cannot load the Higgsfield CDN, so every check of
the hero images and result screenshots was rendered in the Higgsfield sandbox with the same markup and CSS.

## Independent review (4 lenses, 26 agents)
Code, experience, brand/copy and scroll-craft reviewers found 54 issues. 22 were blockers or majors, every one confirmed
by a second agent and none rejected. All 22 are fixed, plus the minors listed in the commit messages (d3311d8 and later).

| Finding | Fix | Re-checked |
|---|---|---|
| Arriving on /#consultation could land past the form (gate scroll fix + browser anchoring) | correction by the measured movement of the next element after the live commit | deep links land at 92 to 96 px for #consultation, #results, #how-it-works |
| Reload / Back put the visitor 705 px off | saved offset restored on reload and back_forward | reload at y 7600: same y, #results top unchanged (-107 before and after) |
| Peak reset to its opening beat when entered from below | removed the mount reset | |
| Clock numerals unreadable (1.05 to 2.3:1) | screen dims to 0.6 while a numeral shows, whole screen darkens | contact sheets at 1366x768, EN and SQ |
| Booking card clipped on 768 px laptops | thread clips at the top like a real chat, reminder as a banner, smaller type under 860 px | card bottom 697 vs screen bottom 713 at 1366x768 |
| Typed text white on ivory in the form | paper surface tokens on the close | input colour rgb(31,31,31), caret crimson, border 0.3 alpha |
| Desktop nav wrapped in every language | inline links from 1280 px, compact language code | no item over the bar edge at 1280, 1366, 1536 in en, sq, de, fr, es, it |
| Step 03 blank when reached from the nav | wipes finish while the band is low | all three steps clip-path inset 0 at 1366x768 via the nav link |
| Focused CTA vanished in the peak | focus scrolls to the visible end state | |
| Crimson on non-CTA labels | neutral eyebrow and step label | |
| de/es/it voice and broken fragments | tu/tú, recomposed headings, form step 2 strings | 0 i18n misses in de/fr/es/it at 1440 and 390, form step 2 included |

## Checks after the fixes
- `tsc --noEmit`: pass. `vite build`: pass.
- No horizontal overflow at 360, 390, 1440 (EN and SQ); no page errors.
- Reduced motion and JavaScript off: 0 visible-text nodes hidden on /sq; the peak falls back to the stacked layout.
- Owner's Lovable edits merged (13a6f46): five revenue options (his test's assertion holds), his lead counts and cost
  per lead under every result screenshot in all six languages.

## Hero (sandbox renders)
- Plate WEB-HERO-D@v2: G-VIS PASS (zero defects) on the standard crop packet, after an earlier PASS on an ad-hoc packet.
- Composite at rest equals the master inside the window (mean absolute difference 0.0), so the poster-to-planes swap is
  invisible.
- Notification laid in the screen plane reads at 1440x900; copy column clear of the phone at 1024x768, 1280x720 and
  1366x768 (SQ, the longest headline).
- Cup: WEB-CUP@v1 failed G-VIS (key light reversed, specks, glint). v2 regenerated with a corrected prompt.

## Feel check
Written cold from the contact sheets (desktop 1366x768 and 1440x900, phone 390x844, both languages) before re-reading
the brief, one word per act:

| Act | Felt | Brief's curve | Match |
|---|---|---|---|
| 1 Hero | Recognised (my table, my evening, a message arrives) | Recognition | yes (was "Confident" before the scene existed) |
| 2 Ledger | Steady | Orientation | yes |
| 3 Peak | Uneasy, then stung, then relieved | Unease to relief | yes (the numerals now land the waiting; the booked end fits on laptops) |
| 4 Steps | Clear | Clarity | yes (was "Withheld" before the wipe timing fix) |
| 5 Equation | Emphatic | Conviction | yes |
| 6 Session | Reassured | Reassurance | yes |
| 7 Results | Convinced (numbers under every frame) | Confidence | yes, judged from the sandbox renders and the captions |
| 8 Close | Personal, in control | Resolve | yes (was "Blind" while the typed text was invisible) |

The peak is the largest visual change on the page (the hard cut to charcoal) and holds the most scroll (3.4 viewport
heights against 1.8 for the next act). The page ends on the form beside the phone that has just written the visitor's
own message, not on a fade.

## Not verified
- A real phone and a real Safari (Playwright Chromium only).
- The live Lovable preview and the published site (preview needs a login; publishing is the owner's call).
- The Albanian strings in the peak and the close need a native read before publishing (BRIEF.md).
