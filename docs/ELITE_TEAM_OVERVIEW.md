# Elite Agent Team – Overview

This doc is the blueprint for a production-grade agent swarm built around:

**Memory Gateway**, **API Gateway**, **Shadow (Headless) Agent**, **Codex Agent**, **Guardian**, **Picky Bot**, **Finsynapse**.

It defines each agent’s mission, input/output contracts, IAM, health/SLOs, and the end-to-end deploy plan to Cloud Run with GitHub OIDC (Workload Identity Federation).

## Core tenets
- Small, single-purpose services (FastAPI/Node), each exposing `/health` and `/metrics` and listening on `0.0.0.0:$PORT`.
- Private Cloud Run with OIDC callers (Scheduler, Orchestrator, other agents).
- Deterministic IDs + append-only telemetry (Firestore/GCS).
- FinOps-first: spend caps, EV gates, warmers every 5m only on hot paths.

## Agents (short form)
- **Memory Gateway**: hydrate/dehydrate long-term memory; append-only logs.
- **API Gateway**: actor allow-list, rate/spend caps, request ID, routing.
- **Shadow Agent (Headless API)**: the generic “doer”; executes routed plans.
- **Codex Agent**: internal coder; turns tasks→PRs via CI; never holds secrets.
- **Guardian**: guardrails; policy checks; anomaly/circuit-break; kill-switch.
- **Picky Bot**: quality gate; rejects low-EV/low-quality plans before enqueue.
- **Finsynapse**: quant+FinOps brain; EV floors, budgets, profit forecasts.

See `docs/AGENT_CONTRACTS.md` and `docs/DEPLOY_PLAN.md` for full details.
