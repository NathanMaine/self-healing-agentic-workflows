# Self-Healing Agentic Workflows

Explores agent workflows that can detect failures, attempt recovery,
and escalate when automation should stop.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
python -m shaw.cli run --workflow workflows/example.yaml --out out
```

Outputs: `out/runs/<run_id>.json` and `out/evidence.jsonl`, including a simulated failure + retry recovery event.
