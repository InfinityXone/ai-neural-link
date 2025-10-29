#!/usr/bin/env bash
set -euo pipefail
PROJECT_ID="${PROJECT_ID:-infinity-x-one-swarm-system}"
REGION="${REGION:-us-east1}"
probe(){ local u="$1"; for p in /health /healthz; do c="$(curl -s -o /dev/null -w "%{http_code}" "$u$p" || true)"; [[ "$c" == 2* ]] && return 0; done; return 1; }
heal(){ gcloud run services update-traffic "$1" --to-latest --region "$REGION" --project "$PROJECT_ID" --quiet || true; }
warm(){ local s="$1" u="$2"; gcloud scheduler jobs describe "warm-$s" --location "$REGION" >/dev/null 2>&1 && \
  gcloud scheduler jobs update http "warm-$s" --location "$REGION" --http-method GET --uri "$u/health" \
   --oidc-service-account-email "scheduler-autopilot@${PROJECT_ID}.iam.gserviceaccount.com" --oidc-token-audience "$u" \
   --schedule "*/5 * * * *" --max-retry-attempts 3 --attempt-deadline "30s" >/dev/null || \
  gcloud scheduler jobs create http "warm-$s" --location "$REGION" --http-method GET --uri "$u/health" \
   --oidc-service-account-email "scheduler-autopilot@${PROJECT_ID}.iam.gserviceaccount.com" --oidc-token-audience "$u" \
   --schedule "*/5 * * * *" --max-retry-attempts 3 --attempt-deadline "30s" >/dev/null; }
mapfile -t S < <(gcloud run services list --region "$REGION" --project "$PROJECT_ID" --format='value(metadata.name)')
for s in "${S[@]}"; do
  u="$(gcloud run services describe "$s" --region "$REGION" --project "$PROJECT_ID" --format='value(status.url)' || true)"
  [ -z "$u" ] && continue
  probe "$u" || heal "$s"
  warm "$s" "$u"
done
# Known profit kicks (if present and 2xx)
for svc in injector satellite-consumer; do
  u="$(gcloud run services describe "$svc" --region "$REGION" --project "$PROJECT_ID" --format='value(status.url)' || true)"
  [ -z "$u" ] && continue
  curl -fsS -m 12 -X POST "$u/harvest" >/dev/null 2>&1 || true
done
echo "autopilot-ok"
