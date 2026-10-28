"""The studio side of the hub's Client OS: one dashboard per brand (hub.py client-sync <slug> [--dry-run]).

One job per module: registry (registry.json, the brands), brain_summary (brain.json), plan (content-map.json),
cards (the brand's Post Cards), runs (a card's production run and its gates), project (a card's
motion-studio project: stage, hook, hub item), spend (ledger.csv), body (the snapshot's shape, the one place it is
defined), counts (status and funnel totals) and sync (the command). hub.py owns the token and the HTTP call.

Tests: python3 -m unittest discover -s growth-engine/tools/clients -t growth-engine/tools
"""
