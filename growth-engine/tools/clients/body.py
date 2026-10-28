"""The snapshot body POSTed to the hub's /api/clients/sync: the one place its shape is defined, so it can follow the
app's contract (C1's docs/client-os.md in agent-start-spark) by changing this file only.

Contract client-os.snapshot.v0 (studio side, 28 Oct 2026):
  {contract, generated_at, business, brand: {slug, name, language, status, status_note, account_stage, timezone,
   cadence, monthly_usd_cap, vault_folder}, brain: {...}, plan: {...}, pieces: [piece], spend: {...}, counts: {...}}
  piece: {post_id, title, bank, slot: {local, timezone, at}, funnel_stage, job, belief, format, family, format_tier,
   status, series, episode, cta_type, usd_budget, hook: {id, text, spoken, source} | null,
   scores: {card_gates: {name: state}, run_gates: [{gate, label, status, score?, by?, at?, note?}],
            project_gate_score: int | null},
   production: {run, current_step, steps_done, steps_total, waiting_on_owner, project_stage} | null,
   links: {card, project, run, studio_post_id, content_external_key, hub_item_id}}
"""
from organic_os.card_title import title_of

CONTRACT = "client-os.snapshot.v0"
BRAND_KEYS = ("slug", "name", "language", "status", "status_note", "account_stage", "timezone", "cadence",
              "monthly_usd_cap", "vault_folder")


def brand_block(entry: dict) -> dict:
    return {k: entry.get(k) for k in BRAND_KEYS}


def piece_block(entry: dict, slot: dict, stage: str | None, family: str | None, run: dict | None, proj: dict) -> dict:
    card = entry["card"]
    production = None
    if run or proj.get("stage"):
        production = {"run": (run or {}).get("run"), "current_step": (run or {}).get("current_step"),
                      "steps_done": (run or {}).get("steps_done"), "steps_total": (run or {}).get("steps_total"),
                      "waiting_on_owner": (run or {}).get("waiting_on_owner", []), "project_stage": proj.get("stage")}
    return {
        "post_id": card["post_id"], "title": title_of(card), "bank": entry["bank"], "slot": slot,
        "funnel_stage": stage, "job": card.get("job"), "belief": card.get("belief"), "format": card.get("format"),
        "family": (run or {}).get("family") or family, "format_tier": card.get("format_tier"),
        "status": card.get("status"), "series": card.get("series"), "episode": card.get("episode"),
        "cta_type": card.get("cta_type"), "usd_budget": card.get("usd_budget"), "hook": proj.get("hook"),
        "scores": {"card_gates": card.get("gates") or {}, "run_gates": (run or {}).get("gates", []),
                   "project_gate_score": proj.get("gate_score")},
        "production": production,
        "links": {"card": entry["path"], "project": proj.get("project"), "run": (run or {}).get("run"),
                  "studio_post_id": (run or {}).get("post_id"), "content_external_key": proj.get("content_external_key"),
                  "hub_item_id": card.get("hub_item_id")},
    }


def snapshot(entry: dict, generated_at: str, brain: dict, plan: dict, pieces: list[dict], spend: dict,
             counts: dict) -> dict:
    return {"contract": CONTRACT, "generated_at": generated_at, "business": entry["hub_business"],
            "brand": brand_block(entry), "brain": brain, "plan": plan, "pieces": pieces, "spend": spend,
            "counts": counts}
