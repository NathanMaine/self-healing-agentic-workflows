from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Dict, List


def execute_workflow(workflow: Dict[str, any]) -> Dict[str, any]:
    run_id = str(uuid.uuid4())
    started_at = datetime.now(timezone.utc).isoformat()

    events: List[dict] = []
    failure_injected = False

    for idx, step in enumerate(workflow["steps"], start=1):
        step_id = step.get("id", f"step-{idx}")
        step_name = step.get("name", step_id)

        attempts = []
        for attempt in (1, 2):
            if not failure_injected:
                outcome = "failure"
                failure_injected = True
                attempts.append({"attempt": attempt, "outcome": outcome, "detail": "simulated failure"})
                events.append({"step_id": step_id, "status": outcome, "attempt": attempt})
                continue

            outcome = "success"
            attempts.append({"attempt": attempt, "outcome": outcome, "detail": "recovered"})
            events.append({"step_id": step_id, "status": outcome, "attempt": attempt})
            break

    completed_at = datetime.now(timezone.utc).isoformat()
    return {
        "run_id": run_id,
        "workflow_id": workflow.get("id"),
        "workflow_name": workflow.get("name"),
        "started_at": started_at,
        "completed_at": completed_at,
        "events": events,
        "success": True,
        "notes": "First attempt fails, retry succeeds",
    }
