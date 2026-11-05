"""The answers a PreToolUse hook prints: deny with a reason, or a warning that doesn't block."""
import json


def deny(reason: str) -> str:
    return json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
                                              "permissionDecisionReason": reason}})


def warn(message: str) -> str:
    return json.dumps({"systemMessage": message})
