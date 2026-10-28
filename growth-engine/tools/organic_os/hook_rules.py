"""Form checks on one hook stack (organic-engine rules/hook-spec.md, STANDARDS 6, hook-lab-organic.md)."""
from __future__ import annotations

from .hook_plain import plain_issues, words

SPOKEN_MAX = 11          # hook-spec 1; the EN library's topic winners have a median of 11 words, losers 13
TEXT_MIN, TEXT_MAX = 4, 10  # STANDARDS 6
BANNED_IN_HOOK = ("patchwork", "agency", "done-for-you", "funnel", "qualified", "guaranteed", "growth partner")
CONTRAST = {"but", "not", "no", "never", "zero", "nothing", "same", "still", "instead", "actually", "yet",
            "without", "only", "vs"}
PAYOFF = {"here's", "how", "why", "ranked", "fix", "check", "step", "first", "test", "spot", "what"}


def form_issues(stack: dict, buyer_words: set[str]) -> list[str]:
    spoken, text = stack.get("spoken", ""), stack.get("text", "")
    sw, tw = words(spoken), words(text)
    out = []
    if not sw:
        out.append("no spoken line")
    elif len(sw) > SPOKEN_MAX:
        out.append(f"spoken line is {len(sw)} words (max {SPOKEN_MAX})")
    if not TEXT_MIN <= len(tw) <= TEXT_MAX:
        out.append(f"text hook is {len(tw)} words ({TEXT_MIN} to {TEXT_MAX})")
    if not stack.get("story") and not {"you", "your", "you're"} & set(sw):
        out.append("no you/your in the spoken line (or mark it story: true)")
    flips = (CONTRAST | PAYOFF) & set(sw + tw) or any(w.endswith("n't") for w in sw + tw)
    if not flips:
        out.append("no contrast or payoff word: the hook flips nothing and promises nothing")
    low = (spoken + " " + text).lower()
    out += [f"banned in a hook: '{b}'" for b in BANNED_IN_HOOK if b in low]
    out += [f"spoken: {p}" for p in plain_issues(spoken, buyer_words)]
    out += [f"text: {p}" for p in plain_issues(text, buyer_words)]
    return out
