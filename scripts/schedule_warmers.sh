#!/usr/bin/env bash
set -euo pipefail
REGION=us-east1
PROJECT_ID=infinity-x-one-swarm-system

# Health pings + functional smoke tests via Cloud Scheduler
declare -A urls=([ai-gateway]="https://ai-gateway-938446344277.us-east1.run.app" [orchestrator]="https://orchestrator-938446344277.us-east1.run.app")

for svc in "${!urls[@]}"; do
  base=${urls[$svc]}
  gcloud scheduler jobs delete ${svc}-health --location=$REGION --quiet || true
  gcloud scheduler jobs create http ${svc}-health \
    --location=$REGION \
    --schedule="*/5 * * * *" \
    --uri="$base/health" \
    --http-method=GET \
    --oidc-service-account-email="scheduler-autopilot@infinity-x-one-swarm-system.iam.gserviceaccount.com" \
    --oidc-token-audience="$base/health"

  if [ "$svc" == "orchestrator" ]; then
    gcloud scheduler jobs delete orchestrator-smoketest --location=$REGION --quiet || true
    gcloud scheduler jobs create http orchestrator-smoketest \
      --location=$REGION \
      --schedule="*/15 * * * *" \
      --uri="$base/route" \
      --http-method=POST \
      --oidc-service-account-email="scheduler-autopilot@infinity-x-one-swarm-system.iam.gserviceaccount.com" \
      --oidc-token-audience="$base/route" \
      --headers="Content-Type=application/json" \
      --message-body="{\"actor\":\"autonomy\",\"goal\":\"noop\",\"constraints\":{},\"budget\":{\"max_usd\":0}}"
  fi
done
