"""Funnel stage of a Post Card: TOF, MOF or BOF. The default comes from the job (reach TOF, trust MOF, convert BOF);
card-check warns when a card's funnel_stage disagrees with its job."""
from __future__ import annotations

from .issues import WARN, issue

JOB_STAGE = {"reach": "TOF", "trust": "MOF", "convert": "BOF"}


def default_stage(job: str | None) -> str | None:
    return JOB_STAGE.get(job or "")


def stage_of(card: dict) -> str | None:
    """The card's funnel_stage, else the default from its job."""
    return card.get("funnel_stage") or default_stage(card.get("job"))


def funnel_issues(card: dict) -> list[dict]:
    want, got = default_stage(card.get("job")), card.get("funnel_stage")
    if not got:
        return [issue(WARN, "funnel", f"no funnel_stage: defaults to {want} from job {card.get('job')}; write it on the card")]
    if want and got != want:
        return [issue(WARN, "funnel", f"funnel_stage {got} but job {card['job']} is usually {want}")]
    return []
