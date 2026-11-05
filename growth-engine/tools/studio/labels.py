"""Human names for gate codes, and the step each asset type's own gates show under.

Step names come from production/standards.json (pipeline.STANDARDS["steps"]), the 16 steps of
AI-VIDEO-PIPELINE.md section 1; gate codes from STANDARDS.md and VISUAL-QA.md. Unknown codes show as they are.
"""

GATE_LABELS = {
    "G-BRIEF": "Brief", "G-IDEA": "Idea and picture", "G-HOOK": "Hook Lab", "G-SCRIPT": "Script Lab",
    "G-HUMAN-SPINE": "Spine pick (you)", "G-AUDIO-MASTER": "Audio master", "G-HUMAN-VOICE": "Voice listen (you)",
    "G-HUMAN-SONG": "Song listen (you)", "G-TIMELINE": "Timeline", "G-PLAN": "Visual plan", "G-SPEC": "Shot Specs",
    "G-HUMAN-LOOK": "Look bible (you)", "G-CONTINUITY": "Continuity", "G-HUMAN-HOOKBOARD": "Hook board (you)",
    "G-BUDGET": "Budget", "G-ASSETS": "Every take passed", "G-FINAL": "Final QA", "G-DIRECTOR": "Director",
    "G-HUMAN-FINAL": "Final approval (you)", "G-LEARN": "Learn", "G-SET": "Carousel set", "G-MOTION-TEXT": "Motion text",
    "G-MOTION-FRAMES": "Motion frames", "G-PROMPT-IMG": "Image prompt review", "G-PROMPT-VID": "Video prompt review",
    "G-VIS": "Visual review", "G-VIS-SHEET": "Sheet review", "G-VIS-BOARD": "Storyboard review",
    "G-VIS-SLIDE": "Slide review", "G-TAKE": "Take review", "G-AUDIO": "Audio take check",
    "G-HUMAN-TEST": "Test approval (you)", "G-HUMAN-ESCALATE": "Escalation (you)", "G-EXCEPTION": "Model exception (you)",
    "G-FALLBACK": "Fallback (Director)",
}

# Which step an asset's own gates show under (AI-VIDEO-PIPELINE.md section 1, VISUAL-QA.md section 3).
STEP_OF_TYPE = {
    "voice": 4, "song": 4, "music": 4, "sfx": 4, "audio_slice": 5,
    "character_sheet": 7, "prop_sheet": 7, "set_sheet": 7, "style_ref": 7, "storyboard": 8, "start_frame": 8,
    "still": 10, "slide": 10, "cover": 10, "static": 10, "video_clip": 10, "motion_render": 10, "final": 12,
}

# The gate states the page knows.
GATE_STATES = ("PASS", "FAIL", "OVERRIDE", "PENDING")


def gate_label(gate: str) -> str:
    return GATE_LABELS.get(gate, gate)
