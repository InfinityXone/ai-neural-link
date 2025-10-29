# 05 • API Gateway & Headless API

**Purpose:** Single secure entry for GPT Actions, UI, and partner calls.

## Endpoints
- `GET /health`, `GET /metrics`
- `POST /plan` — submit DSL → steps
- `POST /route` — route a task
- `POST /harvest` — execute revenue action
- `POST /memory/hydrate` — build seed from repo/docs
- `POST /memory/dehydrate` — export seed to storage (GCS/S3)

## Security
- Private Cloud Run; OIDC caller tokens.
- Input schema validation; object-level allow-lists.

## Deploy
- Service: `ai-gateway`
- GHA job builds/pushes/deploys on `main`.

See `services/ai-gateway/`.