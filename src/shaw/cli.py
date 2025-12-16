from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .evidence import write_artifacts
from .loader import load_workflow
from .runner import execute_workflow


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="shaw", description="Self-Healing Agentic Workflows")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run a workflow with a retry")
    run_parser.add_argument("--workflow", required=True, type=Path, help="Path to workflow YAML/JSON")
    run_parser.add_argument("--out", default=Path("out"), type=Path, help="Output directory (default: out)")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "run":
        workflow = load_workflow(args.workflow)
        run_record = execute_workflow(workflow)
        run_path, evidence_path = write_artifacts(run_record, args.out)
        print(f"Run saved to {run_path}")
        print(f"Evidence appended to {evidence_path}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
