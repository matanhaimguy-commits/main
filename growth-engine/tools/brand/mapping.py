"""Each Brand card field and where it lands in brain.json. Data only: change a line here to move a field.

kind says how the card's value is turned into the brain's type (see convert.py)."""
FIELDS = {
    "offer": ("offer.main_offer", "text"),
    "icp": ("avatars[0].situation", "text"),        # the first avatar's situation; AV-01 is created if there is none
    "promise": ("offer.delivers", "text"),          # exactly what the person gets
    "mechanism": ("mechanism.ums", "text"),         # the named solution
    "voice": ("voice.adjectives", "list_commas"),
    "never_say": ("constraints.cannot_say", "list_lines"),
    "proof_bank": ("proof_bank", "proof"),
    "cta_keyword": ("offer.keyword", "keyword"),
    "monthly_cap_usd": ("package.monthly_usd_cap", "usd"),
    "cadence": ("package.posts_per_week", "count"),
}
