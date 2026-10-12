"""Write research_brief, proposal_packet and script checkpoints for why-the-sky-is-blue."""
import json
import sys
from pathlib import Path

ROOT = Path("/home/user/main/OpenMontage")
sys.path.insert(0, str(ROOT))
from lib.checkpoint import write_checkpoint, PROJECTS_DIR  # noqa: E402

PID = "why-the-sky-is-blue"
PIPE = "animated-explainer"
ART = PROJECTS_DIR / PID / "artifacts"
ART.mkdir(parents=True, exist_ok=True)

TWENTE = "https://ltb.itc.utwente.nl/518/concept/92592"
BAEZ = "https://math.ucr.edu/home/baez/physics/General/BlueSky/blue_sky.html"
BIGTHINK = "https://bigthink.com/starts-with-a-bang/why-the-sky-is-blue-according-to-science/"
NASA_RAYMIE = "https://acd-ext.gsfc.nasa.gov/anonftp/acd/daac_ozone/Lecture4/Text/Lecture_4/raymie.html"
CONVO = "https://theconversation.com/why-is-the-sky-blue-246393"
ASTRO = "https://astronomy.com/magazine/ask-astro/2015/02/black-sky"
NBC = "https://www.nbcnews.com/id/wbna3077395"
ILLINOIS = "https://van.physics.illinois.edu/ask/listing/22358"
BRIT = "https://britannica.com/science/Tyndall-effect"
PT = "https://aip.brightspotcdn.com/PTO.v35.i1.42_1.online.pdf"
REDDIT = "https://redlib.ssps.io/r/explainlikeimfive/comments/1iytxes/eli5_why_is_the_sky_blue"
NASA_SNAP = "https://plus.nasa.gov/video/space-place-in-a-snap-why-is-the-sky-blue-2/"
WIKI = "https://en.wikipedia.org/wiki/Rayleigh_scattering"

research_brief = {
    "version": "1.0",
    "topic": "Why is the sky blue?",
    "research_date": "2026-10-12",
    "research_summary": (
        "The textbook answer (Rayleigh scattering: air molecules scatter short wavelengths far more "
        "than long ones, roughly 1/wavelength^4) is well covered, but most short explainers stop "
        "there and leave the obvious follow-up unanswered: if shorter waves scatter more, why isn't "
        "the sky violet? The answer (less violet in sunlight plus eyes far more sensitive to blue) "
        "is the underserved 'aha', and red sunsets are the same physics seen from the other side."
    ),
    "landscape": {
        "existing_content": [
            {"title": "SciShow: Why Is the Sky Blue? (World's Most Asked Questions)", "url": "https://laughingsquid.com/scishow-explains-why-the-sky-is-blue/", "source": "YouTube / SciShow", "angle": "Q&A explainer", "what_it_covers": "Scattering through the atmosphere plus the role of human perception", "what_it_misses": "Long-form; not a tight visual sub-minute piece"},
            {"title": "minutephysics: Why the Sky is Blue explained in ten seconds", "source": "YouTube / minutephysics", "angle": "Ultra-short", "what_it_covers": "One-line Rayleigh scattering answer", "what_it_misses": "No violet puzzle, no sunset link"},
            {"title": "NASA Space Place in a Snap: Why Is the Sky Blue?", "url": NASA_SNAP, "source": "NASA+", "angle": "Kids' science", "what_it_covers": "Why blue and not purple, green or orange", "what_it_misses": "Aimed at children; little visual physics of wavelength"},
            {"title": "IOP / Teachers TV milk-in-water demonstration", "url": "https://www.stem.org.uk/rxx9r", "source": "STEM Learning", "angle": "Classroom experiment", "what_it_covers": "Scattering demo, reddened transmitted light", "what_it_misses": "Classroom format, not shareable short"},
        ],
        "saturated_angles": ["One-line 'Rayleigh scattering' definition with a rainbow graphic"],
        "underserved_gaps": [
            "Short visual explainer that answers 'why not violet?' instead of skipping it",
            "Connecting blue sky and red sunset as one mechanism in under a minute",
        ],
    },
    "trending": {"recent_developments": [], "active_discussions": [{"platform": "reddit r/explainlikeimfive", "topic_or_url": REDDIT, "sentiment": "curious; corrects a teacher's 'ozone mirror reflects the ocean' claim"}], "timeliness_window": "evergreen"},
    "data_points": [
        {"claim": "Rayleigh scattering intensity is inversely proportional to the fourth power of wavelength", "source_url": WIKI, "source_name": "Wikipedia: Rayleigh scattering", "credibility": "secondary_source", "surprise_factor": "notable", "usable_as": "script_anchor"},
        {"claim": "Blue light (~425 nm) is scattered about 5.5x more than red light (~650 nm); the exact ratio depends on wavelengths chosen", "source_url": TWENTE, "source_name": "University of Twente Living Textbook", "credibility": "primary_source", "surprise_factor": "surprising", "usable_as": "stat_card"},
        {"claim": "Violet scatters even more than blue; the sky looks blue because sunlight contains less violet, some is absorbed high up, and human eyes are much less sensitive to violet", "source_url": BAEZ, "source_name": "UCR Physics FAQ", "credibility": "primary_source", "surprise_factor": "counterintuitive", "usable_as": "hook"},
        {"claim": "Clouds are white because droplets 100-1000x the wavelength scatter all colors about equally (Mie scattering)", "source_url": NASA_RAYMIE, "source_name": "NASA GSFC atmospheric optics lecture", "credibility": "primary_source", "surprise_factor": "notable", "usable_as": "script_anchor"},
        {"claim": "At sunrise/sunset light crosses far more atmosphere, so blue is scattered out of the beam, leaving reds and oranges", "source_url": CONVO, "source_name": "The Conversation", "credibility": "secondary_source", "surprise_factor": "expected", "usable_as": "closing_punch"},
        {"claim": "The Moon has no air, so its daytime sky is black; Mars' thin dusty air gives a butterscotch sky and blue sunsets", "source_url": ASTRO, "source_name": "Astronomy magazine", "credibility": "secondary_source", "surprise_factor": "surprising", "usable_as": "hook"},
    ],
    "audience_insights": {
        "common_questions": [
            "Why is the sky blue? (one of the most common children's questions)",
            "Why isn't the sky violet if violet scatters more?",
            "Why are sunsets red and orange?",
            "Is the sky blue because it reflects the ocean?",
            "Why are clouds white if the sky is blue?",
        ],
        "misconceptions": [
            {"myth": "The sky is blue because it reflects the ocean", "reality": "Air scatters blue light; the sky is blue far inland too. (The ocean is mostly blue because water absorbs red.)", "source": ILLINOIS},
            {"myth": "Shorter waves scatter more, so the sky must be the shortest color we can see", "reality": "Violet scatters most, but sunlight has less of it and our eyes favor blue", "source": BAEZ},
        ],
        "knowledge_level": "General public: knows the question, maybe the word 'scattering', rarely the violet puzzle",
        "pain_points": ["Explanations stop at a jargon word without showing the mechanism"],
    },
    "expert_voices": [
        {"name": "John Tyndall", "title_or_affiliation": "Physicist, 1869 experiments", "position": "Showed tiny particles scatter blue light preferentially", "source_url": BRIT},
        {"name": "Lord Rayleigh", "title_or_affiliation": "Physicist, 1871 papers", "position": "Derived the wavelength^-4 dependence; later showed it applies to molecules themselves", "source_url": PT},
    ],
    "angles_discovered": [
        {"name": "The Sky Should Be Violet", "hook": "By the physics, the sky should be violet. So why does it look blue?", "type": "contrarian", "why_now": "The violet puzzle is the most-skipped part of popular explainers", "grounded_in": ["data_points[2]", "audience_insights.misconceptions[1]"]},
        {"name": "Follow One Beam of Sunlight", "hook": "Sunlight is white. Space is black. So why is the sky blue?", "type": "evergreen", "why_now": "Evergreen top question; a journey makes the mechanism visible", "grounded_in": ["data_points[0]", "data_points[1]", "data_points[4]"]},
        {"name": "Three Skies: Moon, Mars, Earth", "hook": "On the Moon the daytime sky is black. On Mars it's butterscotch. Why is ours blue?", "type": "narrative", "why_now": "Comparison makes the role of air obvious", "grounded_in": ["data_points[5]", "data_points[3]"]},
    ],
    "visual_references": [
        {"description": "Milk-in-water beaker demo", "url": "https://www.stem.org.uk/rxx9r", "what_works": "Blue side-scatter vs orange transmitted light in one frame"},
    ],
    "sources": [
        {"url": TWENTE, "title": "Rayleigh Scattering in the Earth's Atmosphere", "used_for": "5.5x ratio", "reliability": "primary"},
        {"url": BAEZ, "title": "Physics FAQ: Why is the sky blue?", "used_for": "violet puzzle", "reliability": "primary"},
        {"url": NASA_RAYMIE, "title": "NASA: Rayleigh and Mie scattering", "used_for": "clouds, sunsets", "reliability": "primary"},
        {"url": BIGTHINK, "title": "Why the sky is blue, according to science", "used_for": "vision", "reliability": "secondary"},
        {"url": CONVO, "title": "Why is the sky blue?", "used_for": "molecules, sunsets", "reliability": "secondary"},
        {"url": ASTRO, "title": "Why is the sky black in space?", "used_for": "Moon/Mars", "reliability": "secondary"},
        {"url": NBC, "title": "What makes skies blue or red?", "used_for": "Mars sunsets", "reliability": "secondary"},
        {"url": ILLINOIS, "title": "Why the ocean is blue", "used_for": "ocean myth", "reliability": "primary"},
        {"url": BRIT, "title": "Tyndall effect", "used_for": "history", "reliability": "secondary"},
        {"url": PT, "title": "Physics Today historical article", "used_for": "history", "reliability": "primary"},
        {"url": REDDIT, "title": "ELI5: Why is the sky blue", "used_for": "audience question", "reliability": "anecdotal"},
    ],
    "metadata": {"searches_executed": 10},
}

# ---------------- proposal ----------------
taste_profile = {
    "design_read": "Curious-science short for a general audience: make invisible light physics feel tactile and luminous; calm wonder, not hype.",
    "visual_variance": 5,
    "motion_intensity": 5,
    "information_density": 3,
    "palette_discipline": "Night-space navy base that warms to daytime cerulean and ends in sunset amber; spectral wave colors (red/orange/yellow/green/blue/violet) are the only saturated accents.",
    "layout_variation": "Alternate wide 'sky world' frames (sun, atmosphere, horizon) with close-up 'molecule scale' frames where single waves hit single molecules.",
    "reference_strategy": "No generated images (no image keys): every visual is hand-drawn vector/SVG animation authored for this piece; one review still per scene at the storyboard gate.",
    "anti_patterns": ["generic AI-purple gradient backgrounds", "text-only slides", "stock rainbow clip-art", "dense labels on physics diagrams"],
    "quality_gates": ["Every scene shows the mechanism (waves, molecules, path length) rather than just stating it", "No more than one short on-screen label per beat"],
}

concepts = [
    {"id": "c1", "title": "The Sky Should Be Violet", "hook": "By the physics, the sky should be violet. So why does it look blue?", "narrative_structure": "myth_busting",
     "visual_approach": "Spectrum bar that 'predicts' violet, then a reveal of sunlight's spectrum and the eye's sensitivity curve.", "suggested_playbook": "custom", "target_audience": "Curious adults who already half-know 'scattering'", "target_platform": "youtube", "target_duration_seconds": 45,
     "key_points": ["Short waves scatter more", "Violet scatters most", "Less violet in sunlight + eyes favor blue"], "core_message": "The blue sky is physics plus biology.", "cta": "Look up at the next clear sky and notice the paler blue near the horizon.", "tone": "playful contrarian",
     "grounded_in": ["data_points[2]", "audience_insights.misconceptions[1]"], "why_this_works": "Answers the follow-up question most explainers skip (UCR Physics FAQ)."},
    {"id": "c2", "title": "Sunlight, Sorted by Color", "hook": "Sunlight is white. Space is black. So why is the sky blue?", "narrative_structure": "journey",
     "visual_approach": "Follow one beam of white sunlight from the Sun into the air: it splits into colored waves, blue ones ping-pong off molecules across the sky, red ones pass straight through; ends on a sunset.", "suggested_playbook": "custom", "target_audience": "General public, teens and up", "target_platform": "youtube", "target_duration_seconds": 45,
     "key_points": ["White light is all colors", "Air molecules scatter short blue waves ~5x more than red", "Blue reaches you from every direction", "Why not violet: less in sunlight, eyes favor blue", "Sunset: long path scatters the blue away"], "core_message": "The blue sky is sunlight sorted by color.", "cta": "Next sunset, remember: same air, same physics.", "tone": "warm, curious wonder",
     "grounded_in": ["data_points[0]", "data_points[1]", "data_points[2]", "data_points[4]"], "why_this_works": "A single followable journey shows the mechanism, folds in the violet twist as a mid-point surprise, and pays off with sunsets everyone has seen."},
    {"id": "c3", "title": "Three Skies", "hook": "On the Moon, the daytime sky is black. On Mars it's butterscotch. Why is ours blue?", "narrative_structure": "comparison",
     "visual_approach": "Three side-by-side worlds; air is added or removed and the sky color changes in each.", "suggested_playbook": "custom", "target_audience": "Space fans", "target_platform": "youtube", "target_duration_seconds": 45,
     "key_points": ["No air = black sky", "Dusty thin air = butterscotch", "Our air scatters blue"], "core_message": "The sky's color is the air's fingerprint.", "cta": "Ask: what color would an alien sky be?", "tone": "adventurous",
     "grounded_in": ["data_points[5]", "data_points[3]"], "why_this_works": "Comparison makes air's role obvious (Astronomy magazine)."},
]

production_plan = {
    "pipeline": PIPE,
    "playbook": "custom",
    "render_runtime": "remotion",
    "composition_mode": "atelier",
    "renderer_family": "explainer-teacher",
    "art_direction": "'Light, sorted': navy space -> cerulean day -> amber sunset. Sun as a soft gold disc; light drawn as glowing sine waves in true spectral colors; air molecules as small pale-blue dots; blue waves ricochet between molecules; on-screen labels minimal, rounded sans-serif.",
    "taste_profile": taste_profile,
    "delivery_promise": {"promise_type": "teacher_explainer", "motion_required": True, "source_required": False, "tone_mode": "warm curious wonder", "quality_floor": "presentable", "approved_fallback": None},
    "stages": [
        {"stage": "script", "tools": [], "approach": "Write ~110-word narration for 45s with voice cues"},
        {"stage": "scene_plan", "tools": [], "approach": "6-7 bespoke animated scenes; storyboard stills for review"},
        {"stage": "assets", "tools": [
            {"tool_name": "piper_tts", "role": "narration", "provider": "piper", "available": True, "estimated_cost_usd": 0.0, "why_this_provider": "Only free, offline voice; no paid API keys by user request. Voice en_US-lessac-medium."},
            {"tool_name": "audio_mixer", "role": "local ambient music bed synthesis/mix", "provider": "ffmpeg", "available": True, "estimated_cost_usd": 0.0, "why_this_provider": "Online music sources are blocked by this network; a soft synthesized pad is free and local."},
        ], "approach": "Narration per section, ambient pad, bespoke Remotion scene components", "fallback_if_unavailable": "None needed: all local"},
        {"stage": "edit", "tools": [], "approach": "Timeline from measured narration durations, subtitles on"},
        {"stage": "compose", "tools": [{"tool_name": "video_compose", "role": "render", "provider": "remotion", "available": True, "estimated_cost_usd": 0.0, "why_this_provider": "Remotion verified working on this machine (demos rendered)"}], "approach": "Atelier Remotion render 1920x1080 30fps"},
    ],
    "quality_tradeoffs": [
        {"tradeoff": "Voice", "recommendation": "Free Piper voice now; a paid voice (e.g. ElevenLabs/OpenAI) can be swapped in later with one key", "quality_impact": "Piper sounds clear but somewhat flat/robotic"},
        {"tradeoff": "Visuals", "recommendation": "Hand-built vector animation (no image generation keys)", "quality_impact": "Clean diagrammatic look; no photoreal skies"},
    ],
    "alternative_paths": [
        {"description": "Free: Piper voice + bespoke Remotion animation + local ambient pad", "total_cost_usd": 0.0, "quality_level": "free", "what_changes": "Recommended; nothing paid"},
        {"description": "Standard: same visuals with a premium cloud voice", "total_cost_usd": 0.05, "quality_level": "standard", "what_changes": "Needs one paid TTS key (not added, per your request)"},
    ],
    "music_source": {"source_type": "user_library", "track_path": "music_library/soft-sky-pad.wav", "provider": "local ffmpeg synthesis", "mood_direction": "soft airy ambient pad, very low under narration", "estimated_cost_usd": 0.0},
    "voice_selection": {"provider": "piper", "voice_id": "en_US-lessac-medium", "rationale": "Only free offline voice available; clear US English", "estimated_cost_usd": 0.0, "delivery_style": "warm, curious, unhurried", "pacing_policy": "~150 wpm; pauses via punctuation and per-section silence", "sample_approval_required": True},
    "decision_log_ref": "decision_log.json",
}

proposal_packet = {
    "version": "1.0",
    "concept_options": concepts,
    "selected_concept": {"concept_id": "c2", "rationale": "Journey structure is the clearest for a 45s general-audience piece and absorbs c1's violet twist as its mid-point surprise.", "modifications": ["Fold in c1's 'why not violet?' beat"]},
    "production_plan": production_plan,
    "cost_estimate": {"total_estimated_usd": 0.0, "line_items": [
        {"tool": "piper_tts", "operation": "narration ~110 words", "quantity": 1, "estimated_usd": 0.0, "notes": "local"},
        {"tool": "audio_mixer", "operation": "ambient pad + mix", "quantity": 1, "estimated_usd": 0.0, "notes": "local"},
        {"tool": "video_compose", "operation": "Remotion render", "quantity": 1, "estimated_usd": 0.0, "notes": "local"},
    ], "budget_cap_usd": 0.0, "budget_verdict": "within_budget", "savings_options": []},
    "approval": {"status": "approved", "approved_budget_usd": 0.0, "user_notes": (
        "Approval policy from the user's own request: 'stop for my approval at the script and the storyboard'; no paid API keys. "
        "The user delegated proposal choices to the agent's recommendations; concept, runtime (Remotion vs HyperFrames), voice and music "
        "are presented to the user for override at the script gate. Storyboard gate = scene_plan + per-scene review stills.")},
    "metadata": {"approval_policy": "user-specified gates: script, storyboard"},
}


def opt(oid, label, score, reason, rej=None):
    o = {"option_id": oid, "label": label, "score": score, "reason": reason}
    if rej:
        o["rejected_because"] = rej
    return o


decision_log = {
    "version": "1.0",
    "project_id": PID,
    "decisions": [
        {"decision_id": "d-pipeline", "stage": "proposal", "category": "pipeline_selection", "subject": "Pipeline",
         "options_considered": [opt("animated-explainer", "animated-explainer", 0.95, "Topic-to-explainer with narration"), opt("animation", "animation", 0.6, "Motion-first, less narration-led", "Brief is a narrated explainer")],
         "selected": "animated-explainer", "reason": "User asked for an animated explainer", "user_visible": True, "user_approved": True},
        {"decision_id": "d-concept", "stage": "proposal", "category": "concept_selection", "subject": "Concept",
         "options_considered": [opt("c1", "The Sky Should Be Violet", 0.75, "Strong twist", "Better as a beat inside c2"), opt("c2", "Sunlight, Sorted by Color", 0.9, "Clearest mechanism + sunset payoff"), opt("c3", "Three Skies", 0.65, "Fun, but spends time off-Earth", "Less focused on the actual mechanism")],
         "selected": "c2", "reason": "Clearest for 45s; includes c1's violet twist. Delegated by user; open to override at script gate.", "user_visible": True, "user_approved": False},
        {"decision_id": "d-runtime", "stage": "proposal", "category": "render_runtime_selection", "subject": "Composition runtime",
         "options_considered": [
             opt("remotion", "Remotion (React/SVG)", 0.85, "Frame-exact SVG wave/molecule animation, word-level captions, verified rendering on this machine"),
             opt("hyperframes", "HyperFrames (HTML/GSAP)", 0.75, "Excellent kinetic HTML/GSAP motion", "Caption burn parity is Remotion-only; Remotion already proven here"),
             opt("ffmpeg", "FFmpeg", 0.2, "Only pans over stills", "No still images to pan; motion is the point")],
         "selected": "remotion", "reason": "Recommended; presented to user at script gate for override", "user_visible": True, "user_approved": False},
        {"decision_id": "d-mode", "stage": "proposal", "category": "composition_mode", "subject": "Composition authoring mode",
         "options_considered": [opt("atelier", "Atelier (bespoke scenes)", 0.85, "Physics needs custom diagrams: waves hitting molecules"), opt("templated", "Templated stock cards", 0.5, "Fast", "Text/stat cards can't show scattering")],
         "selected": "atelier", "reason": "Hero single explainer; mechanism must be drawn", "user_visible": True, "user_approved": False},
        {"decision_id": "d-voice", "stage": "proposal", "category": "voice_selection", "subject": "Narration TTS provider",
         "options_considered": [opt("piper", "Piper en_US-lessac-medium (free, offline)", 0.7, "Only free option available"), opt("paid", "Cloud voices (ElevenLabs, OpenAI, Google...)", 0.9, "More natural", "User asked for no paid API keys")],
         "selected": "piper", "reason": "No paid keys", "user_visible": True, "user_approved": False},
        {"decision_id": "d-music", "stage": "proposal", "category": "music_source", "subject": "Background music",
         "options_considered": [opt("pad", "Locally synthesized soft ambient pad", 0.7, "Free, local, unobtrusive"), opt("pixabay", "Pixabay royalty-free search", 0.8, "Real produced track", "pixabay.com blocked by this machine's network policy (403)"), opt("none", "No music", 0.5, "Simplest", "Video feels emptier"), opt("byo", "User-provided track in music_library/", 0.9, "Best if user has one", "None provided yet")],
         "selected": "pad", "reason": "Only working music source; user can drop in a track anytime", "user_visible": True, "user_approved": False},
        {"decision_id": "d-playbook", "stage": "proposal", "category": "playbook_selection", "subject": "Visual identity",
         "options_considered": [opt("custom", "Custom 'Light, sorted' art direction", 0.85, "Subject has its own visual world: sky colors"), opt("flat-motion-graphics", "flat-motion-graphics preset", 0.5, "Generic", "Doesn't use the sky's own palette")],
         "selected": "custom", "reason": "Palette taken directly from the subject (space, day sky, sunset)", "user_visible": True, "user_approved": False},
    ],
}

# ---------------- script ----------------
sections = [
    ("s1", "Hook", "Sunlight is white. Space is black. So why is the sky blue?",
     "measured", "curious", ["white", "black", "blue"], 0.5, "Three short beats; slight lift on the question.",
     [("animation", "Black space, a white Sun; a white beam travels toward a small Earth; the sky over Earth glows blue as the question lands", 1)]),
    ("s2", "White light is every color", "That white light is really every color mixed together, each one a wave of a different length.",
     "conversational", "warm", ["every", "length"], 0.3, "Unfold the idea gently.",
     [("animation", "The white beam fans out into six colored sine waves; red long and lazy, violet short and tight", 1), ("overlay", "Tiny label: 'long wave' (red) / 'short wave' (blue)", 4)]),
    ("s3", "Molecules are picky", "When sunlight hits our air, tiny nitrogen and oxygen molecules scatter it. But they're picky: short blue waves scatter about five times more than long red ones.",
     "measured", "intrigued", ["picky", "five times"], 0.4, "Pause after 'picky' to set up the reveal.",
     [("animation", "Zoom to molecule scale: N2/O2 dots; a red wave passes straight through, a blue wave hits a molecule and splashes outward", 1), ("stat_card", "'Blue scatters ~5x more than red'", 7)]),
    ("s4", "Blue from everywhere", "So blue gets bounced all across the sky, and reaches your eyes from every direction.",
     "conversational", "satisfied", ["every direction"], 0.4, "Land the payoff, slightly brighter.",
     [("animation", "Pull back: blue waves ricochet between molecules, filling the sky; a little person looks up, blue arrows arrive from all around", 1)]),
    ("s5", "Why not violet?", "Violet is even shorter, so why not a purple sky? The Sun sends less violet, and your eyes are tuned to blue.",
     "measured", "playful", ["even shorter", "tuned to blue"], 0.4, "Pose the question with a smile, then answer plainly.",
     [("animation", "The sky briefly tints violet with a question mark; sunlight spectrum bars show less violet; an eye icon with a sensitivity curve peaking toward blue/green; the sky settles back to blue", 1)]),
    ("s6", "Sunset and landing", "At sunset, light crosses so much air that the blue is scattered away, leaving reds and oranges. Same air. Same physics. Just sunlight, sorted by color.",
     "slow", "calm wonder", ["sunset", "sorted by color"], 0.8, "Slow down for the final three short sentences.",
     [("animation", "Sun sinks to the horizon; its beam crosses a long slab of air; blue peels off along the way and only red/orange arrive; sky turns amber", 1), ("overlay", "Final title: 'Sunlight, sorted by color.'", 7)]),
]

wpm = 150.0
# Measured Piper en_US-lessac-medium durations at length_scale 1.0, scaled by 1.08.
MEASURED = {"s1": 3.81, "s2": 4.77, "s3": 9.12, "s4": 4.67, "s5": 6.24, "s6": 9.44}
LENGTH_SCALE = 1.08
t = 0.0
script_sections = []
for sid, label, text, pace, energy, emph, pause, note, cues in sections:
    words = len(text.split())
    dur = round(MEASURED[sid] * LENGTH_SCALE + pause, 1)
    start = round(t, 1)
    end = round(t + dur, 1)
    script_sections.append({
        "id": sid, "label": label, "text": text, "start_seconds": start, "end_seconds": end,
        "speaker_directions": f"{pace} pace, {energy}; emphasize {', '.join(emph)}. {note}",
        "delivery_cues": {"pace": pace, "energy": energy, "emphasis_words": emph, "pause_after_seconds": pause, "delivery_note": note, "provider_text": text},
        "enhancement_cues": [{"type": c, "description": d, "timestamp_seconds": round(start + ts, 1)} for c, d, ts in cues],
        "pronunciation_guides": [],
        "source_ref": "research_brief",
    })
    t = end

total_words = sum(len(s[2].split()) for s in sections)
script = {
    "version": "1.0",
    "title": "Sunlight, Sorted by Color: Why Is the Sky Blue?",
    "total_duration_seconds": round(t, 1),
    "voice_performance": {
        "performance_intent": "Warm, curious science narrator: unhurried, a friend pointing at the sky.",
        "pacing_profile": "conversational",
        "energy_curve": "Curious hook -> steady build -> playful twist -> slow, calm landing",
        "pause_policy": "Short pause after each section; longer pause before the final three short sentences.",
        "sample_section_id": "s3",
        "provider_notes": {"piper": "No emotion controls: rely on punctuation, per-section synthesis, length_scale 1.08 (measured), and inserted silences (pause_after_seconds) between sections."},
    },
    "sections": script_sections,
    "metadata": {"word_count": total_words, "estimated_seconds_at_150wpm": round(total_words / wpm * 60, 1), "measured_seconds_piper": round(t, 1), "piper_length_scale": LENGTH_SCALE},
}

if __name__ == "__main__":
    stage = sys.argv[1]
    common = dict(pipeline_type=PIPE)
    if stage == "research":
        (ART / "research_brief.json").write_text(json.dumps(research_brief, indent=2))
        write_checkpoint(PROJECTS_DIR, PID, "research", "completed", {"research_brief": research_brief}, **common,
                         review={"summary": "G1 pass: 6 data points, 3 angles, 11 sources"})
    elif stage == "proposal":
        (ART / "proposal_packet.json").write_text(json.dumps(proposal_packet, indent=2))
        write_checkpoint(PROJECTS_DIR, PID, "proposal", "completed", {"proposal_packet": proposal_packet, "decision_log": decision_log}, **common,
                         human_approval_required=True, human_approved=True,
                         metadata={"approval_basis": "User instruction: approval stops only at script and storyboard; proposal choices delegated and shown for override at script gate."},
                         cost_snapshot={"spent_usd": 0.0, "budget_usd": 0.0})
    elif stage == "script":
        (ART / "script.json").write_text(json.dumps(script, indent=2))
        write_checkpoint(PROJECTS_DIR, PID, "script", "awaiting_human", {"script": script}, **common,
                         human_approval_required=True, cost_snapshot={"spent_usd": 0.0, "budget_usd": 0.0},
                         review={"summary": f"{total_words} words, est {script['metadata']['estimated_seconds_at_150wpm']}s at 150 wpm"})
    print(stage, "ok", "words=", total_words, [(s['id'], s['start_seconds'], s['end_seconds']) for s in script_sections] if stage == "script" else "")
