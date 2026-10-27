"""Format router within the monthly budget, and the credit ledger (ORGANIC-OS 7.7)."""
from __future__ import annotations

import csv

from .config import CONFIG
from .files import client_dir


def ledger_rows(slug: str) -> list[dict]:
    p = client_dir(slug) / "ledger.csv"
    if not p.exists():
        return []
    with p.open(newline="") as f:
        return list(csv.DictReader(f))


def month_spend(rows: list[dict], month: str) -> dict:
    sel = [r for r in rows if r["date"].startswith(month)]
    num = lambda r, k: float(r.get(k) or 0)
    by_fmt: dict[str, dict] = {}
    for r in sel:
        d = by_fmt.setdefault(r["format"], {"pieces": 0, "credits": 0.0, "minutes": 0.0})
        d["pieces"] += 1
        d["credits"] += num(r, "higgsfield_credits")
        d["minutes"] += num(r, "minutes")
    return {"month": month, "credits": sum(num(r, "higgsfield_credits") for r in sel),
            "elevenlabs": sum(num(r, "elevenlabs_credits") for r in sel),
            "minutes": sum(num(r, "minutes") for r in sel), "by_format": by_fmt}


def route(card: dict, brain: dict, cmap: dict, prev_family: str | None = None, spent: float = 0.0) -> list[dict]:
    cap = brain["package"]["monthly_credit_cap"]
    remaining = cap - spent
    permitted_proof = any(p.get("permission") == "yes" for p in brain.get("proof_bank", []))
    buyer_formats = cmap.get("buyer_formats", [])
    out = []
    for fid, f in CONFIG["formats"].items():
        if card["job"] not in f["jobs"] or card["belief"] not in f["beliefs"]:
            continue
        why = []
        if f["tier"] == "A" and not (card.get("angle_proven") or card.get("wildcard")):
            continue
        if f.get("needs_real_human") and not brain["visual"].get("real_footage"):
            continue
        if f.get("needs_proof") and not permitted_proof:
            continue
        if prev_family and f["family"] == prev_family:
            continue
        if f["credits"][1] > remaining:
            continue
        score = 0.0
        if fid in buyer_formats:
            score += 3; why.append("wins with this client's buyers (research)")
        if card["job"] == "reach" and f["family"] == "reel":
            score += 2; why.append("reels lead reach for small accounts")
        if card["job"] == "trust" and f["family"] == "carousel":
            score += 2; why.append("carousels earn saves")
        if card["job"] == "convert" and fid in ("reel_strategist_prop", "reel_podcast", "carousel_comparison"):
            score += 2; why.append("proven convert format")
        st = card.get("story_template")
        if st:
            if st not in f.get("story_templates", []):
                continue
            score += 2; why.append(f"renders the {st} story")
            if f["tier"] == "B" and not (card.get("angle_proven") or card.get("wildcard")):
                score += 1; why.append("story lab: test the angle at tier B before a tier A piece")
        if card.get("animation_style") and card["animation_style"] not in f.get("styles", []):
            continue
        if f["tier"] == "C":
            score += 0.5; why.append("cheap: test the angle first")
        if f["family"] == "image":
            score -= 2
        out.append({"format": fid, "tier": f["tier"], "family": f["family"], "credits": f["credits"], "score": score,
                    "why": "; ".join(why) or "fits job and belief", "skill": f.get("skill")})
    return sorted(out, key=lambda r: -r["score"])
