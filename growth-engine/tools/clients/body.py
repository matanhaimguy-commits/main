"""The body POSTed to the hub's /api/clients/sync: the one place its shape is defined. It follows C1's contract,
docs/client-os.md in matanhaimguy-commits/agent-start-spark (branch claude/client-os-c1):

  {brand: {slug, name, status, business, language, account_stage, timezone, cadence, monthly_usd_cap},
   snapshots: {brain, plan, spend},   (onboarding is the hub's own)
   pieces: [{post_id, status, slot, funnel_stage, job, belief, format, format_family, title, hook_text, hook_grades,
             script_score, gates, project, studio_post_id, content_external_key, usd_spent, notes}]}

Pieces are always sent whole (the hub marks the brand's other pieces removed). Snapshot data holds no timestamp, so
an unchanged brain, plan or spend adds no row on the hub."""
from organic_os.card_title import title_of

from . import hook_grades

BRAND_KEYS = ("slug", "name", "status", "business", "language", "account_stage", "timezone", "cadence", "monthly_usd_cap")
PIECE_KEYS = ("post_id", "status", "slot", "funnel_stage", "job", "belief", "format", "format_family", "title",
              "hook_text", "hook_grades", "script_score", "gates", "project", "studio_post_id", "content_external_key",
              "usd_spent", "notes")


def brand_block(entry: dict) -> dict:
    b = {k: entry.get(k) for k in BRAND_KEYS if k != "business"}
    b["business"] = entry.get("hub_business")
    return {k: b[k] for k in BRAND_KEYS}


def studio_block(entry: dict) -> dict:
    """Registry facts the hub's brand row has no column for; they ride in the brain snapshot."""
    return {k: entry[k] for k in ("vault_folder", "status_note") if entry.get(k)}


def card_gates(card: dict) -> list[dict]:
    return [{"gate": f"card:{g}", "status": str(s).upper(), "by": "Post Card"} for g, s in (card.get("gates") or {}).items()]


def script_score(run: dict | None, proj: dict):
    scores = [g["score"] for g in (run or {}).get("gates", []) if g["gate"] == "G-SCRIPT" and "score" in g]
    return scores[-1] if scores else proj.get("gate_score")


def notes_of(entry: dict) -> str | None:
    note = entry["card"].get("notes")
    if entry["bank"]:
        return "Bank card (spare): no slot until it replaces a piece. " + (note or "")
    return note


def piece_block(entry: dict, slot_at: str | None, stage: str | None, family: str | None, run: dict | None,
                proj: dict, usd_spent: float | None) -> dict:
    card, hook = entry["card"], proj.get("hook") or {}
    run_post = (run or {}).get("post_id")
    p = {"post_id": card["post_id"], "status": card.get("status"), "slot": None if entry["bank"] else slot_at,
         "funnel_stage": stage, "job": card.get("job"), "belief": card.get("belief"), "format": card.get("format"),
         "format_family": (run or {}).get("family") or family, "title": title_of(card),
         "hook_text": hook.get("text") or hook.get("spoken"), "hook_grades": hook_grades.of(proj.get("hook")), "script_score": script_score(run, proj),
         "gates": card_gates(card) + (run or {}).get("gates", []), "project": proj.get("project"),
         "studio_post_id": run_post if run_post and run_post != card["post_id"] else None,
         "content_external_key": proj.get("content_external_key"), "usd_spent": usd_spent, "notes": notes_of(entry)}
    return {k: p[k] for k in PIECE_KEYS}


def snapshot(entry: dict, brain: dict, plan: dict, spend: dict, pieces: list[dict]) -> dict:
    return {"brand": brand_block(entry),
            "snapshots": {"brain": {**brain, "studio": studio_block(entry)}, "plan": plan, "spend": spend},
            "pieces": pieces}
