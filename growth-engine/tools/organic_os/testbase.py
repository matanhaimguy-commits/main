"""Shared fixtures for the organic_os tests: a minimal brain, content map, demand map and Post Card."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

BRAIN = {
    "client": "acme", "updated": "2026-10-15",
    "business_model": {"sells": "audits", "sales_process": "call", "capacity": "unknown"},
    "offer": {"main_offer": "free audit", "next_step": "comment AUDIT", "keyword": "AUDIT", "delivers": "a 30-minute audit"},
    "avatars": [{"id": "AV-01", "name": "Ana", "role": "owner", "situation": "busy", "words": ["x"], "fears": ["y"], "desires": ["z"]}],
    "awareness": {"stage": "problem_aware", "sophistication": "3"},
    "mechanism": {"ump": "Patchwork", "ums": "System", "steps": ["Find", "Own"]},
    "belief_ladder": [{"id": f"B{i}", "statement": "s", "state": "unknown"} for i in range(1, 9)],
    "contrarian_vault": [{"id": "C1", "position": "p", "source": "owner"}],
    "proof_bank": [{"id": "P1", "type": "result", "text": "t", "source": "s", "permission": "yes"},
                   {"id": "P2", "type": "result", "text": "t", "source": "s", "permission": "pending"}],
    "lead_magnets": [{"keyword": "AUDIT", "resource": "audit", "delivers": "30 min", "live": True},
                     {"keyword": "TEST", "resource": "quiz", "live": False}],
    "voice": {"adjectives": ["calm"], "samples": [], "banned": ["hype"], "language": "sq", "register": "ti"},
    "visual": {"colors": {}, "fonts": [], "logo_files": [], "face": "ai_character", "ai_label": "unknown", "real_footage": False},
    "market": {"language": "sq", "country": "AL"},
    "constraints": {"cannot_say": ["prices"]},
    "baseline": {"followers": None, "as_of": None},
    "package": {"posts_per_week": 7, "account_stage": "new", "monthly_usd_cap": 60},
}
MAP = {"pillars": [{"name": "Find"}, {"name": "Convert"}], "series": [{"name": "The Build", "pillar": "Convert"}, {"name": "One Step", "pillar": "Find"}],
       "buyer_formats": []}
DEMAND = [{"phrase": "na shkruajne po nuk blejne", "tag": "direct"}, {"phrase": "off topic", "tag": "off_map"}]


def card(**kw):
    c = {"post_id": "AC-2026-10-W3-01", "client": "acme", "account_language": "sq", "slot": "2026-10-19 19:30",
         "pillar": "Find", "series": None, "episode": None, "job": "reach", "belief": "B1", "avatar": "AV-01",
         "awareness": "problem_aware", "demand_phrase": "na shkruajne po nuk blejne", "idea_source": "outlier",
         "source_ref": "@x 3.4x", "narrow_product": "the exact first reply to send", "format": "reel_quote_broll",
         "format_tier": "C", "angle_proven": False, "credit_budget": 30, "length_target_s": 30, "hook_type": "contrarian",
         "emotion": "surprise", "cta_type": "send", "cta_keyword": None, "lead_magnet": None, "proof_used": [],
         "hypothesis": "contrarian line gets more sends", "success_metric": "sends_per_reach", "target": ">= median x1.5",
         "status": "planned"}
    c.update(kw)
    return c


def codes(issues, level=None):
    return [i["code"] for i in issues if level is None or i["level"] == level]


def week_cards():
    days = ["2026-10-19", "2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25"]
    spec = [("reel_quote_broll", "reach", "B1", "send", "contrarian"), ("carousel_framework", "trust", "B4", "save", "teaching"),
            ("reel_quote_broll", "reach", "B2", "comment", "hidden_cause"), ("carousel_self_check", "convert", "B3", "keyword", "self_check"),
            ("reel_strategist_prop", "reach", "B1", "send", "myth"), ("image_question", "trust", "B7", "comment", "question"),
            ("carousel_mistakes", "reach", "B1", "save", "list")]
    return [card(slot=f"{d} 19:30", format=f, job=j, belief=b, cta_type=cta, hook_type=h, cta_keyword="AUDIT" if cta == "keyword" else None)
            for d, (f, j, b, cta, h) in zip(days, spec)]
