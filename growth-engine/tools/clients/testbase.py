"""Shared by the clients tests: a temporary repo root with one brand (acme), its cards, a run, a project and a ledger."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

SLUG = "acme"
BRAND = {"slug": SLUG, "name": "Acme", "hub_business": "acme-app", "language": "en", "status": "active",
         "account_stage": "new", "timezone": "America/New_York", "cadence": "Mon and Thu 12:00", "monthly_usd_cap": 50,
         "vault_folder": "Agency OS/Clients/Acme"}
BRAIN = {"client": SLUG, "account": "@acme", "updated": "2026-10-28",
         "offer": {"main_offer": "free audit", "next_step": "comment AUDIT", "keyword": "AUDIT", "delivers": "30 min"},
         "avatars": [{"id": "AV-01", "name": "Ana", "role": "owner", "situation": "busy"}],
         "awareness": {"stage": "problem_aware", "sophistication": "S3", "notes": "x"},
         "voice": {"adjectives": ["calm"], "banned": ["hype"], "samples": []},
         "package": {"posts_per_week": 2, "account_stage": "new", "monthly_usd_cap": 50, "monthly_credit_cap": 0},
         "decisions_open": [{"id": "E1", "question": "Name the method?", "interim": "unnamed"},
                            {"id": "E2", "question": "Host?", "decided": {"answer": "no host", "by": "owner"}}]}
CMAP = {"month": "2026-11 (all of November)", "theme": "steady months", "mix": {"reach": 0.5}, "cadence": "2 a week",
        "pillars": [{"name": "Find", "scope": "broad"}], "series": [{"name": "Parts", "kind": "hard", "job": "reach",
                                                                     "target_episodes": 3, "rule": "one step a part"}],
        "approved_by": "owner"}


def card_yaml(post_id, slot, job, status, extra=""):
    return (f"post_id: {post_id}\nslot: {slot}\njob: {job}\nstatus: {status}\nformat: reel_motion\nformat_tier: C\n"
            f"narrow_product: 'Title {post_id}: the rest'\nsource_ref: 'hooks v2 master AC-B'\n{extra}")


class ClientsCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        c = self.root / "clients" / SLUG
        self.write(c / "brain.json", json.dumps(BRAIN))
        self.write(c / "content-map.json", json.dumps(CMAP))
        self.write(c / "cards" / "W1" / "AC-01.yaml", card_yaml(
            "AC-2026-11-W1-01", "2026-11-02 12:00", "reach", "scripted",
            "funnel_stage: TOF\nproject: motion-studio/projects/acme-01\ngates: {idea: pass}\n"))
        self.write(c / "cards" / "W1" / "AC-02.yaml", card_yaml(
            "AC-2026-11-W1-02", "2026-11-05 12:00", "convert", "planned", "notes: \"Spoken hook (draft): 'Here's the one test.' CTA\"\n"))
        self.write(c / "cards" / "bank" / "AC-09.yaml", card_yaml("AC-2026-11-W9-01", "2026-11-30 12:00", "trust", "planned"))
        self.write(c / "ledger.csv", "date,post_id,format,tier,atlas_usd,minutes,note\n"
                                     "2026-10-27,AC-2026-11-W1-01,reel_motion,C,1.25,10,\n"
                                     "2026-09-30,AC-OLD,reel_motion,C,9,0,\n")
        self.write(c / "runs" / "AC-2026-11-W1-01" / "ledger.json", json.dumps({
            "post_id": "AC-2026-11-W1-01", "slug": SLUG, "format": "reel_motion", "family": "motion", "card": None,
            "steps": {"0": {"status": "done"}, "1": {"status": "done"}, "2": {"status": "todo"}, "3": {"status": "na"}},
            "run_gates": {"G-SCRIPT": [{"status": "FAIL", "by": "lab", "score": 70},
                                       {"status": "PASS", "by": "lab", "score": 88}]},
            "queue": [{"checkpoint": "G-HUMAN-SPINE", "status": "PENDING"}]}))
        p = self.root / "motion-studio" / "projects" / "acme-01"
        self.write(p / "PROJECT.md", "# acme-01\n\n## Status\nStage: script (gate 88/100)\n\n## Decisions\nx gate 10/100\n")
        self.write(p / "docs" / "hooks.json", json.dumps([{"id": "AC-A", "text": "first", "spoken": "one"},
                                                          {"id": "AC-B", "text": "second", "spoken": "two"}]))
        self.write(p / "hub" / "item.json", json.dumps({"external_key": "AC-2026-11-W1-01"}))
        self.registry = self.root / "registry.json"
        self.write(self.registry, json.dumps({"brands": [BRAND]}))

    def tearDown(self):
        self.tmp.cleanup()

    @staticmethod
    def write(p: Path, text: str):
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
