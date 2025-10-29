# 06 • Orchestration & Task Routing
- Input: { task:
  - actor, goal, constraints, budget }
- Policy gates: allow-list services, rate & spend caps by actor.
- Routing: orchestrator chooses service based on task kind.
- Idempotency: execution_id = sha256(task)[:12].
- Telemetry: append-only execution log, profit events.

**Key endpoints**
- POST /route → {execution_id}
- GET  /metrics → counters by service