# Fingerprints

Every site you build with **scroll-craft** gets one row here, appended after it
ships. The registry exists so your next build can prove it is a different page
rather than a re-skin of one you already made.

This file is **yours**. It starts empty on purpose: the gate is about not
repeating *yourself*, so it has nothing to say until you have built something.

The rules and the gate live in the skill's
`references/uniqueness.md`. Short version:

**A new build must differ from EVERY row below on at least 4 of the 6
dimensions.** Four against each row individually, not four on average across the
table. If a planned build fails, change the plan. Never edit a row to make room
for it.

The six dimensions are: **grammar**, **nav treatment**, **hero device**,
**act-sequence shape**, **close pattern**, **signature move**.

Dimension 6 is free, because a signature move is unique by definition. So the
gate really asks for three more out of the remaining five, and a build that
changes only grammar and world will fail it.

---

## The registry

| Build | Grammar | Nav treatment | Hero device | Act-sequence shape | Close pattern | Signature move | World | Port |
|---|---|---|---|---|---|---|---|---|
| straightscale-site (straightscale.com homepage, Oct 2026) | **Thread** (new): one real object, a red-case phone, carries the story act to act; open editorial spreads on ivory with hard-edged charcoal bands | Floating white bar: inline anchor links from 1280px, compact language code, one CTA; below that a full-screen menu, and on phones a sticky bottom CTA that appears once the hero CTA has passed and hides at the form | Layered photoreal plate, natural flow (no pin): far = the plate's own window view (keyed glass), mid = café table with the phone and an HTML lock-screen notification laid in the screen plane, near = defocused cup; exit lag 18/12/1x+ and an eased pointer, desktop only; phones get a 9:16 poster | 8 acts, about 11.5 viewport heights: parallax hero, quiet ledger, ONE pinned peak (3.4 vh, the longest), centred wipe steps, charcoal kinetic equation band, sticky-split session, captioned proof columns (parallax), close | The thread hands over: the form sits beside the phone and the phone composes the visitor's own message from their name and business, then marks it Sent | One enquiry, two endings, under your scroll: a scroll-scrubbed chat where the message goes unanswered and the screen goes black, then the thread rewinds and gets answered, booked and reminded, while the chain Ad, Enquiry, Follow-up, Sale lights | Tirana after dark: photoreal café, warm tungsten, crimson only for action, gold only on charcoal | React (TanStack Start), Lovable-synced |


---

## What is taken

Add a bullet here whenever a build claims something a later build should avoid
reusing: a grammar, a nav treatment, a close pattern, a signature move, an
act-count-and-length band. The shared columns are what the next build inherits
as a constraint, so writing them down is the whole point.

- **Grammar: Thread** (one recurring real object carrying the story, editorial spreads around it).
- **Signature move: a scroll-scrubbed chat with two endings** (unanswered then answered) on a CSS-drawn phone.
- **Close pattern: the form mirrored live into a phone as the visitor's own composed message.**
- **Hero: a photoreal tabletop plate with an HTML notification mapped into a phone screen** (keyed window, own-view far plane).
- **Act-count band: 8 acts at about 11.5 vh with a single 3.4 vh pinned peak.**

---

## Appending a row

After shipping, add one line to the table and one bullet to **What is taken** if
the build claimed something new. Fill every column. Say what the build shares
with existing rows.

Rows are append-only. A build that has been superseded stays in the table,
because the space it occupies is still occupied.

---

## Worked example

The skill's author kept a registry of twelve builds across eight page grammars.
If you want to see what a filled-in table looks like, and which shapes tend to
collide, read `EXAMPLES.md` in the scroll-craft repository. Treat it as
illustration only: those rows are somebody else's builds and they do **not**
constrain yours.
