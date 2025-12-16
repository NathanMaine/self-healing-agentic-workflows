import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
sys.path.append(str(SRC_ROOT))

from shaw.cli import main  # noqa: E402


def test_run_creates_artifacts(tmp_path):
    workflow = Path(__file__).parent / "fixtures" / "workflow.yaml"
    out_dir = tmp_path / "out"

    code = main(["run", "--workflow", str(workflow), "--out", str(out_dir)])
    assert code == 0

    run_files = list((out_dir / "runs").glob("*.json"))
    assert run_files
    assert (out_dir / "evidence.jsonl").exists()
