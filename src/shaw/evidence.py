from __future__ import annotations

import json
from pathlib import Path


def write_artifacts(run: dict, out_dir: Path) -> tuple[Path, Path]:
    runs_dir = out_dir / "runs"
    runs_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    run_path = runs_dir / f"{run['run_id']}.json"
    run_path.write_text(json.dumps(run, indent=2))

    evidence_path = out_dir / "evidence.jsonl"
    with evidence_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "run_id": run["run_id"],
            "workflow_id": run.get("workflow_id"),
            "success": run.get("success", False),
            "notes": run.get("notes"),
        }) + "\n")

    return run_path, evidence_path
