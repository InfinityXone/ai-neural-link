# Memory Gateway – Endpoint Probe

Use this script to discover which endpoints your Memory Gateway exposes (paths often vary across deployments).

```bash
GATEWAY="https://memory-gateway-938446344277.us-east1.run.app"

# Core
curl -sS $GATEWAY/health | jq . || true
curl -sS $GATEWAY/ | head -n 50 || true
curl -sS $GATEWAY/openapi.json | jq .paths || true

# Common plan endpoints tried across versions
for p in \n  /plan \n  /v1/plan \n  /api/plan \n  /router/plan \n  /tasks/plan \n  /workflow/plan \n; do
  echo "== Testing $p =="
  curl -sS -X POST "$GATEWAY$p" \n    -H "Content-Type: application/json" \n    -d '{"actor":"echo","goal":"hello_world","constraints":{},"budget":{"requests":1}}' | head -n 80
  echo
  echo
done

# Memory hydrate endpoints
for p in \n  /memory/hydrate \n  /v1/memory/hydrate \n  /api/memory/hydrate \n  /memory/hydrate-seed \n; do
  echo "== Testing $p =="
  curl -sS -X POST "$GATEWAY$p" -H "Content-Type: application/json" -d '{"seed":"test"}' | head -n 80
  echo
  echo
done
```

> If your service requires authentication, use an Identity Token:

```bash
GATEWAY="https://memory-gateway-938446344277.us-east1.run.app"
SCHEDULER_SA="scheduler-autopilot@infinity-x-one-swarm-system.iam.gserviceaccount.com"
ID_TOKEN=$(gcloud auth print-identity-token \n  --audiences="$GATEWAY" \n  --impersonate-service-account="$SCHEDULER_SA")

curl -sS -X POST "$GATEWAY/plan" \n  -H "Authorization: Bearer $ID_TOKEN" \n  -H "Content-Type: application/json" \n  -d '{"actor":"echo","goal":"hello_world"}'
```
