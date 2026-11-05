"""Where a brand's files are: the repo root (tests pass their own) and the brand's client folder."""
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def client_dir(root: Path, slug: str) -> Path:
    return Path(root) / "clients" / slug


def rel(root: Path, p: Path) -> str:
    """p relative to the repo root, as the snapshot shows paths."""
    return Path(p).resolve().relative_to(Path(root).resolve()).as_posix()
