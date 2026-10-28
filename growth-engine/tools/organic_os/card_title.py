"""A Post Card's short title: its narrow product up to the first colon (the post_id when there is none)."""


def title_of(card: dict, cap: int = 80) -> str:
    return str(card.get("narrow_product") or card.get("post_id") or "").split(":")[0].strip()[:cap]
