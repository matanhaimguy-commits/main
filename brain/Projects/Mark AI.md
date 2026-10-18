---
type: project
updated: 2026-10-18
tags: [project, research, e-commerce, archive]
---

# Mark AI

The `Mark AI/` folder holds the output of one e-commerce product-research run, not client or video work.
"Discovery Engine v16" run 848955 (dated 28 Aug 2026, UK mode) drew a random set of research lenses, product
families and countries, checked candidate products against live Meta ad counts, killed eight on named rules
(price band, competition, legal claims) and kept two for full dossiers: a TMJ jaw-tension relief pen and a
cordless handheld vacuum sealer, both marked conditional on the operator verifying suppliers. The folder has
`discovery-log.md` (the run summary; `global-discovery-log.md` is an identical copy), `runs/848955/report.html`
(the full dossier), `small-winners.html` (a later sweep of small UK advertisers, filtered by website traffic),
and the Python helpers used for the draw, UK VAT profit maths, scoring and ad-format routing. A follow-up commit
(f276153) retracted ad counts and brand ids that had been invented in an earlier version of the small-winners
list and added a traffic check. There are no runs after August in the repo. What it is useful for now: the
evidence habits (every number has a retrieved source, conditional claims are labelled, mistakes get a correction
log), which [[Motion Studio]] and the [[Standing rules]] on never inventing numbers follow. Who or what "Mark"
refers to is not recorded in the repo. Back to [[00 Index]].

Source: Mark AI/discovery-log.md, Mark AI/global-discovery-log.md, Mark AI/runs/848955/, motion-studio/knowledge/our-pipeline.md (section 6), CLAUDE.md, git commits 6c8e700, 1543214, f276153
