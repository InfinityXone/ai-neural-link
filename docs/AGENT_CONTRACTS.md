# Agent Contracts

## Shared HTTP contract
- `GET /health` → `{ ok: true }` (200) within 600ms.
- `GET /metrics` → Prom-style text; at least: `uptime_seconds`, `req_total`, `req_errors_total`, `latency_ms_bucket`.
- `POST /plan` (where relevant) → `{ plan_id, steps:[...] }`.
- `POST /execute` (shadow) → `{ request_id, result, cost_cents }`.
- All requests carry: `X-Actor`, `X-Request-Id` (uuidv7), and JWT/OIDC.

## Memory Gateway
**Mission**: hydrate/dehydrate memory and keep an append-only record.
**Routes**: `/memory/hydrate`, `/memory/dehydrate`, `/events/append`.
**Storage**: Firestore (append-only), daily GCS export.
**IAM**: `roles/datastore.user`, `roles/storage.objectAdmin` (svc only).

## API Gateway
**Mission**: authn/z, request IDs, rate/spend caps, route to Shadow/Orchestrator.
**Routes**: `/route`, `/allow`, `/charge`, `/health`, `/metrics`.
**Policies**: per-actor caps; per-endpoint QPS; per-day spend ceilings.

## Shadow Agent (Headless)
**Mission**: execute plans; idempotent with `X-Request-Id`.
**Routes**: `/execute`, `/status/{id}`.
**IAM**: minimal; outbound to providers via API keys in GSM.

## Codex Agent
**Mission**: generate PRs from tasks; run tests; open deployments.
**Routes**: `/tickets`, `/patch`, `/rollout`.
**IAM**: GitHub OIDC only; *no* cloud secrets.

## Guardian
**Mission**: guardrails & reliability.
**Routes**: `/policy/check`, `/anomaly/scan`, `/kill-switch`.
**Actions**: open incidents, slash rates, flip kill-switch.

## Picky Bot
**Mission**: quality gate.
**Route**: `/gate` → returns `accept/reject` with reason and EV delta.

## Finsynapse
**Mission**: EV floors, budget caps, daily profit target.
**Routes**: `/ev/floor`, `/budget/plan`, `/forecast/noon`, `/forecast/eod`.
**Inputs**: success rates, rewards, gas/API COGS.

---
**SLOs**: 99.5% avail; p95<600ms; error budget alarms; /health warm every 5m.
