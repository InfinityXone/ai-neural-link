#!/usr/bin/env bash
set -euo pipefail
: "${REGION:=us-east1}"
: "${PROJECT_ID:=infinity-x-one-swarm-system}"
: "${AI_GATEWAY_URL:?}"
: "${ORCHESTRATOR_URL:?}"

# 1) Health checks
echo '[tick] health: gateway'
curl -fsS $AI_GATEWAY_URL/health >/dev/null || echo 'gateway health failed'
echo '[tick] health: orchestrator'
curl -fsS $ORCHESTRATOR_URL/health >/dev/null || echo 'orchestrator health failed'

# 2) Memory hydrate (lightweight)
echo '[tick] memory hydrate'
curl -fsS -X POST $AI_GATEWAY_URL/memory/hydrate || echo 'hydrate failed (non-fatal)'

# 3) Functional smoke: route a no-op
echo '[tick] route noop'
curl -fsS -H 'Content-Type: application/json' -d '{"actor":"autonomy","goal":"noop","constraints":{},"budget":{"max_usd":0}}' \
  $ORCHESTRATOR_URL/route >/dev/null || echo 'route failed'

# 4) Profit pings (safe budgets)
echo '[tick] harvest: proposal nudges'
curl -fsS -H 'Content-Type: application/json' -d '{"actor":"revenue-bot","goal":"proposal_nudges","budget":{"max_usd":1.00}}' \
  $AI_GATEWAY_URL/harvest >/dev/null || echo 'harvest failed'

# 5) Quick rollback check via metrics (placeholder)
# If your /metrics signals failure, call auto_rollback.sh
# bash scripts/auto_rollback.sh || true
