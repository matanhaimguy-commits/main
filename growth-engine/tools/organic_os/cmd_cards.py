"""organic.py card-check | week-check | route: a slug's cards against its brain and content map."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

from .cards import card_check
from .files import load_brain, load_cards, load_demand, load_map, need
from .issues import has_errors
from .router import ledger_rows, month_spend, route, route_issues, usd_cap
from .show import print_issues
from .week import week_check


def card_check_cmd(a) -> int:
    brain, cmap = load_brain(a.slug), load_map(a.slug)
    demand = load_demand(a.slug, brain)
    bad = False
    for path, card in load_cards(a.paths):
        iss = card_check(card, brain, cmap, demand)
        print_issues(Path(path).name, iss)
        bad |= has_errors(iss)
    return 1 if bad else 0


def week_check_cmd(a) -> int:
    brain, cmap = load_brain(a.slug), load_map(a.slug)
    cards = [c for _, c in load_cards(a.paths)]
    iss, summary = week_check(cards, brain, cmap)
    print(json.dumps(summary))
    print_issues("week", iss)
    return 1 if has_errors(iss) else 0


def route_cmd(a) -> int:
    brain, cmap = load_brain(a.slug), load_map(a.slug)
    card = yaml.safe_load(need(Path(a.card), "no such card").read_text())
    month = card["slot"][:7]
    spent = month_spend(ledger_rows(a.slug), month)["usd"]
    opts = route(card, brain, cmap, a.prev_family, spent)
    cap = usd_cap(brain)
    print(f"budget {month}: ${spent:.2f}" + (f" of ${cap:.2f} Atlas USD spent" if cap is not None else " spent"))
    print_issues("route", route_issues(brain))
    for o_ in opts[:3]:
        print(f"- {o_['format']} (tier {o_['tier']}, ${o_['usd'][0]:.2f}-{o_['usd'][1]:.2f}): {o_['why']} · {o_['skill']}")
    return 0 if opts else 1
