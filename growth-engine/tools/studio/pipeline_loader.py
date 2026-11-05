"""pipeline.py, for a run's ledger and its step and gate rules. Imported only when a command needs it."""
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent


def load_pipeline():
    if str(TOOLS) not in sys.path:
        sys.path.insert(0, str(TOOLS))
    try:
        import pipeline
    except ImportError as e:
        sys.exit(f"NO_PIPELINE: {e}. studio-push needs pipeline.py's packages (pip install jsonschema pyyaml).")
    return pipeline
