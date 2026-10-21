# BUILD SPEC v2: straightscale.com homepage, "Thread" grammar

v2 folds in the plan review (critics: conversion, scroll-craft compliance, engineering; their reports are summarised
in REVIEW-1.md). Read BRIEF.md first. Repo: `/home/user/straight-scale` (Lovable-synced; never force-push, rebase or
amend). App: TanStack Start + React 19 + Tailwind v4. Homepage = `src/components/pages/home.tsx`, sections in
`src/components/sections/*`. Languages: EN and SQ hand-written with `t(en, sq)` from `@/lib/i18n`; de/fr/es/it come
from dictionaries `src/content/i18n/<lang>.json` keyed by the exact English string.

## 0. Non-negotiables
- Keep every existing owner string (EN and SQ) verbatim unless this spec names a new one or removes one. Keep the
  formal "ju".
- No invented numbers, clients, reviews, results, guarantees, prices. The chat in the peak and close is a labelled
  example ("Example" / "Shembull"). No em dashes anywhere visible.
- Real markup only. The form logic in `consult.tsx` (submit1, submit2, field names, honeypot, `submitApplication`,
  `trackPixel`, `/api/public/intake/details`, navigate to /thank-you) must not change behaviour.
- **Eyebrows: exactly one on the page**, act 6 "Free consultation". The hero eyebrow and the tags on acts 2, 3, 4, 5
  and 8 are deleted (their words survive as nav labels).
- **Kinetic (`Lines`) only on the hero H1 and act 5's equation.** Every other heading renders as plain text inside its
  section's flow+in fade (opacity 0 → 1 and a 14px rise over 620ms, ease-out, staggered 60ms, fired once).
- Crimson (#B31217) only on CTAs and at most one heading emphasis per screen. Gold only on charcoal.
- Motion: transform, opacity, clip-path only. Scroll effects write CSS custom properties from one rAF; no React state
  per frame (state only when a discrete index changes). Sections listen only near the viewport.
- **Desktop motion** (the pinned peak, pointer parallax, results column parallax) runs only when
  `(min-width: 1024px) and (pointer: fine) and (prefers-reduced-motion: no-preference)` AND the section's hook has set
  `data-live="1"` (set once on attach, and only if the section is still below the viewport, so nothing jumps). Until
  then, and on every other device, the static/flow layout renders. Nothing essential is ever hidden waiting for JS.
- Accessibility: one h1, headings in order, focus-visible everywhere, 44px targets, alt text EN/SQ, contrast ≥4.5:1
  body / ≥3:1 large, measured on the render. No horizontal overflow at 360, 390, 768, 1024, 1280, 1440.
- No new npm dependencies. No backdrop-blur on fixed chrome.

## 1. Design system (foundation: DONE in the repo)
- Self-hosted Playfair Display (h1, h2; italic for emphasis) and Montserrat (everything else), `public/fonts/`,
  `src/styles/fonts.css`, preloads in `__root.tsx`.
- Tokens in `src/styles.css`: `--paper #f8f6ef`, `--marble #ede4d6`, `--ink-soft #5a5552`, `--charcoal #1f1f1f`,
  `--ink #171415`, `--emerald #b31217` (crimson; legacy name), `--emerald-hi #8f0e13` (hover), `--gold #dd9a10`.
  Sentence case (no capitalize). Case red for the phone only: #BE0F18.
- Radius scale: 12px (buttons, inputs, chips), 24px (raised proof objects, form card, phone screen inner 34px desktop).
  Only proof objects are raised: screenshots, the phone, the form card.
- `src/lib/scroll.ts`: `useStickyProgress`, `usePassProgress` (write `--p`), `usePrefersReducedMotion`. Extend it with
  what the acts need (e.g. a `useLiveGate(ref)` that sets `data-live`), never per-frame React state.
- Per-act CSS files `src/styles/home/{hero,services,difference,steps,why,session,results,close}.css`, already imported.
- `Btn` has no magnet (removed); press feedback scale(0.97).

## 2. Acts (anchors vary on purpose)

### Act 1 Hero — natural flow, layered parallax (`hero.tsx`, `hero.css`)
- `section#top`, height 100svh (min 640px desktop), **not sticky**. Exit progress p = clamp(scrollY / heroHeight).
- **Scene box**: one absolutely positioned box with the master's aspect ratio (16:9 desktop set; 9:16 portrait set
  under `(max-aspect-ratio: 3/4)`), sized to cover the stage around a focal point (desktop focus about x 0.62 y 0.6,
  portrait about x 0.45 y 0.7). Every plane and the poster live inside this box in % coordinates, so poster and planes
  align by construction.
- Layer contract (assets in `src/assets/hero/`, both sets):
  | Plane | Asset | Motion (exit progress p, page scroll = 1x) | Rule |
  |---|---|---|---|
  | Far | `exterior` (separate render of the view outside: clock tower, square lights; no frame, no glass), larger than the window opening by travel + 10% | lags 25% (translateY +0.25·scroll); pointer ±4px | only seen through the keyed window |
  | Mid | `plate` = master with the cup removed and the table rebuilt; the window glass keyed to alpha by polygon. **The phone stays in the plate.** | lags 12%; pointer ±8px | carries the phone and the HTML screen (identical transform) |
  | Screen | HTML phone screen inside the plate's coordinate space, mapped by `matrix3d` from the 4 measured screen corners (manifest) | exactly the plate's transform | real text, lock-screen notification |
  | Near | `cup` alpha cutout, saucer and table contact cut off by the frame's bottom edge | 1x plus a slight extra drift down-right and scale 1 → 1.06 (passes the viewer); pointer ±18px | never shows a contact point |
  | Atmosphere | CSS: warm bloom at the window lights, faint haze | opacity 0.6 → 0.85 | never over the headline |
  | Copy | H1 (kinetic), subline, CTA unit (`#hero-cta`: Btn + place line as its caption) | 1x, no fade | on a sibling scrim (column on desktop, band on portrait) |
- Poster (`poster-desktop.webp`, `poster-portrait.webp`) = a screenshot of the composited planes at p=0 (rendered in
  the Higgsfield sandbox). It is the LCP (`<picture>`, `fetchpriority="high"`, preload with matching `media`). Planes
  replace it only if they all decode while p < 0.05; otherwise the poster stays.
- Below 1024px: load the planes only after `load` + `requestIdleCallback`, and never when `saveData`, `effectiveType`
  is not `4g`, or `deviceMemory` ≤ 4 (the poster plus the live HTML screen remain).
- Phone wake: a CSS animation with `animation-delay: 1.2s` from first paint slides the notification in ("New message"
  / "Mesazh i ri" + the customer line); it also shows at p ≥ 0.08. Reduced motion: shown at once, no slide.
- Hero copy is exactly: H1, subline, CTA unit. The hero eyebrow, the field strip and the industries strip are removed
  (industries move to act 2).
- **Proof ribbon** directly below the hero (not inside it): a static row of the 5 real result frames (480w WebP thumbs,
  ≤25 KB each, `decoding="async"`, `fetchpriority="low"`) with the existing label "See our ad results" / "Shihni
  rezultatet e reklamave tona" visible, each frame linking to `#results`. Desktop: one row. Phones: horizontal
  scroll-snap row. No marquee, no duplicates.

### Act 2 What we do — lead column, flow+in (`services.tsx`, `services.css`)
Silence before the peak. One lead column (no right column): heading (existing strings; the "whole business." emphasis
is this screen's one crimson), sub "Not just the Instagram page.", the industries sentence ("Built for established
businesses in" + Healthcare, Real estate, Finance, Hospitality, B2B as running text), then the 4 items as ledger rows
at the same left edge with hairlines: small lucide icon in ink, title (existing light + bold words, bold in ink not
crimson), description. Existing CTA. No tag, no cards, no red blocks, no badges, no watermark.

### Act 3 The difference: PEAK (`difference.tsx`, `difference.css`, `src/components/thread-phone.tsx`)
**Desktop live (≥1024, fine pointer, motion ok, data-live):** section 340svh, sticky stage 100svh, split: copy left,
CSS phone right. A persistent figcaption "Example" / "Shembull" above the phone (Montserrat 600, ≥13px, ≥4.5:1 on
paper and charcoal), visible in every state, never under the fixed nav (check 1366x768). Chat header carries a pill:
"Without follow-up" / "Pa ndjekje" until the drop, "With the system in place" / "Me sistemin në vend" from the rewind on.
Timeline, a pure function of p (scroll back plays backwards):
- 0.00 greet: heading, caption 1, the customer bubble already present.  0.04 "Seen".
- 0.10 to 0.32: time jumps as large centred numerals on the dimming screen (Montserrat 600 tabular, ≥28px):
  23:52 at 0.12, 08:15 at 0.20, 13:40 at 0.28; the status-bar clock follows. Caption 2. Chain: Ad and Enquiry lit
  (ink), the Follow-up link dashed grey.
- 0.32 to 0.40: the bubble drops away, the screen dims.
- **0.40 hard cut** to a charcoal ground (restate `color` on the subtree). Authored silence to 0.48: dark screen,
  caption 3 "No reply." in ivory + "Gone." in gold italic Playfair (the reel's line).
- **0.48 hard cut** back to paper. Rewind 0.48 to 0.58: the clock counts back 13:40, 08:15, 23:52, 21:04 as large
  numerals, the bubble retraces its drop path, the pill switches. Caption 4 "Build the missing step."; the Follow-up
  link lights crimson (the one emphasis).
- 0.60 business reply; 0.68 customer answer; 0.76 business confirm; 0.82 booking card, Sale lit, caption 5;
  0.88 reminder notification; paragraph + CTA + place line appear and hold to 1.
**Everywhere else (phones, tablets, touch, reduced motion, before data-live):** no pin, height auto, in order:
heading; figcaption "Example"; Card A (CSS phone-card, case border #BE0F18, radius 28px, max 420px, pill "Without
follow-up"): bubble, "Seen", the three time dividers as large tabular numerals, the bubble greyed to 0.45; a charcoal
strip at least 40svh tall with "No reply. Gone." (same treatment); caption "Build the missing step."; Card B (pill "With
the system in place"): reply, answer, confirm, booking card, reminder; chain row; paragraph; CTA + place line. Bubble
text ≥16px. Bubbles appear by IntersectionObserver once (opacity + 8px rise, 350ms stagger); without JS or with reduced
motion all are visible.
- Chat styling is generic: no WhatsApp/Instagram/Messenger colours, logos or chrome; avatar is an initial glyph or a
  lucide User icon. Incoming bubbles white with ink text; outgoing bubbles charcoal with ivory text. No ✓✓ ticks.
- The full conversation exists in the DOM in reading order; no aria-live.

### Act 4 How it works — centred, reveal (`steps.tsx`, `steps.css`)
The one centred act: centred heading (existing strings; emphasis "creates them." = the screen's crimson), then a
full-width band of the three steps (existing text) in three columns (stacked on phones). Each step block (Playfair
numeral 01/02/03, title in ink, text) wipes in from the left with `clip-path` on a wrapper (never on the numeral's own
box) at pass progress about 0.15, 0.35, 0.55. No SVG line, no nodes, no photo, no cards. Existing CTA "Start with step
01". Reduced motion: no wipe.

### Act 5 Why one team — mirrored, kinetic (`why.tsx`, `why.css`)
Charcoal band inside the page margins (radius 24px). Mirrored: the equation at display scale on the LEFT (Playfair,
one word per line, "+" and "=" in Montserrat, "Growth" in gold with a gold underline that draws), heading + the three
patchwork lines (muted ivory) + "StraightScale brings it all together." + CTA (light variant) on the RIGHT. Kinetic:
the equation lines rise from masks in order as the band enters (stagger 90ms), once. No tag, no glass, no watermark.
Phones: equation first, then the copy.

### Act 6 Free session — sticky split, flow+in (`benefits.tsx` renders both lists; remove `<Start />` from home)
Left column CSS-sticky (top 7rem, desktop only): the page's ONE eyebrow "Free consultation", heading "What you get in
your free session", "45 minutes, one-on-one, focused only on your business.", the place line. Right: the 4 points as
a two-column `dl` (bold Montserrat title running into its sentence, no icons), a hairline, "How to start? 3 simple
steps" as a small heading, the 3 steps as three short plain lines ("Leave your details" links to #consultation), then
the CTA "Book a free consultation" and the place line under it. No red cards, no badges.

### Act 7 Results — full width (`proof.tsx`, `results.css`)
`id="results"`. Heading (existing; "We made" emphasis). Each screenshot ONCE. Desktop: asymmetric two columns (frames
1, 3, 5 left; 2, 4 right, offset down about 20% of a frame), frames ≥560px wide, white raised frames, the right column
parallaxes up to 60px slower (desktop live only). Phones: one horizontal scroll-snap row, cards about 84vw, next card
peeking. Every frame is a button opening the existing lightbox Dialog with the 1600w image. Then "Our own ad spend"
(existing strings) as one raised block: the verified figure **$697,494.87** typeset large in Montserrat tabular, a small
caption "Total spent, converted to USD. Source: Meta Ads Manager." / "Shpenzimi total, i konvertuar në USD. Burimi:
Meta Ads Manager.", and the source crop as a small framed image (button → lightbox with the full crop). No count-up.

### Act 8 Close — split (`consult.tsx`, `close.css`, `thread-phone.tsx`)
Form behaviour untouched. Ivory ground. Remove the "You'll get" list (it restates act 6) and the section tag. Desktop:
left = heading, paragraph, the thread phone (CSS, about 420px tall) composing the visitor's message live from `name`
and `business`, caption "This is where your follow-up starts." under it; right = the form card. Phones: a compact
thread strip (case top edge, chat header, the composing bubble, about 150px) directly ABOVE the Name field in step 1;
after step 1 succeeds, the top of step 2 shows "Your message" / "Mesazhi juaj" with the composed bubble and "Sent" /
"U dërgua". Empty fields render muted italic placeholders "your name" / "emri juaj", "your business" / "biznesi juaj".
No ✓✓. The visitor's text is only rendered locally.

### Chrome (`nav.tsx`, `footer.tsx`, `fx.tsx`, `home.tsx`)
Remove the `0{i + 1}` counters in the mobile menu; remove `backdrop-blur` from the nav and StickyCta (solid white).
StickyCta: shown once `#hero-cta` has passed under the fixed nav (IntersectionObserver, rootMargin "-76px 0px 0px 0px")
and hidden while `#consultation` is in view; visible below 1024px (`lg:hidden` instead of `md:hidden`). Remove
`<ScrollBar />` and `<Start />` from home. Footer unchanged.

## 3. Copy: new strings (EN / SQ in "ju"; SQ needs a native read)
| Where | EN | SQ |
|---|---|---|
| Hero notification title | New message | Mesazh i ri |
| Chat header name | New customer | Klient i ri |
| Figcaption / tag | Example | Shembull |
| Pill A / static label A | Without follow-up | Pa ndjekje |
| Pill B / static label B | With the system in place | Me sistemin në vend |
| Customer 1 | Hi! Do you have a free slot this week? | Përshëndetje! A keni vend të lirë këtë javë? |
| Status | Seen | Parë |
| Business reply | Yes! Wednesday at 10:00 or Thursday at 16:00. Which suits you? | Po! E mërkurë në 10:00 ose e enjte në 16:00. Cila ju përshtatet? |
| Customer 2 | Wednesday, please. | E mërkura, ju lutem. |
| Business confirm | Booked. We'll remind you the day before. | U rezervua. Do t'ju kujtojmë një ditë më parë. |
| Booking card | Booked · Wednesday, 10:00 | Rezervuar · E mërkurë, 10:00 |
| Reminder | Reminder: tomorrow at 10:00 | Kujtesë: nesër në 10:00 |
| Caption 1 | The ad worked. A customer writes. | Reklama funksionoi. Një klient shkruan. |
| Caption 2 | Nobody answers in time. | Askush nuk përgjigjet në kohë. |
| Caption 3 | No reply. Gone. ("No reply." + "Gone.") | Pa përgjigje. Iku. ("Pa përgjigje." + "Iku.") |
| Caption 4 | Build the missing step. | Ndërtoni hapin që mungon. |
| Caption 5 | Answered. Followed up. Booked. | Përgjigje. Ndjekje. Rezervim. |
| Ad spend caption | Total spent, converted to USD. Source: Meta Ads Manager. | Shpenzimi total, i konvertuar në USD. Burimi: Meta Ads Manager. |
| Close bubble | Hi, I'm {name} from {business}. I'd like a free consultation. | Përshëndetje, jam {name} nga {business}. Dua një konsultë falas. |
| Close placeholders | your name / your business | emri juaj / biznesi juaj |
| Close sent | Sent | U dërgua |
| Close caption | This is where your follow-up starts. | Këtu fillon ndjekja juaj. |
| Close phone label | Your message | Mesazhi juaj |
Every new English string also goes into the de/fr/es/it dictionaries.

## 4. Performance budget
- First viewport on a 360x640 phone: ≤ 300 KB of images (portrait poster + nothing else above the fold).
- Hero: poster desktop ≤ 180 KB, portrait ≤ 120 KB; exterior ≤ 90 KB; plate ≤ 170 KB (alpha); cup ≤ 50 KB (alpha).
- Results: 480w thumbs ≤ 25 KB (ribbon), 960w ≤ 45 KB (page), 1600w ≤ 75 KB (lightbox only, on tap).
- No PNG screenshots anywhere on the homepage.
