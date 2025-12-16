from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None


def _read_structured_file(path: Path) -> Dict[str, Any]:
    text = path.read_text()
    if path.suffix.lower() in {".yaml", ".yml"} and yaml is not None:
        return yaml.safe_load(text)  # pragma: no cover
    return json.loads(text)


def load_workflow(path: Path) -> Dict[str, Any]:
    data = _read_structured_file(path)
    if not isinstance(data, dict):
        raise ValueError("Workflow file must contain an object")
    steps: List[dict] = data.get("steps", []) or []
    if not steps:
        raise ValueError("Workflow requires at least one step")
    return {
        "id": data.get("id", "workflow"),
        "name": data.get("name", "Workflow"),
        "steps": steps,
    }
