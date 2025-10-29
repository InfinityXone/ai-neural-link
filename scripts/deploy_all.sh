#!/usr/bin/env bash
set -euo pipefail
REGION=us-east1
PROJECT_ID=infinity-x-one-swarm-system
AR=us-east1-docker.pkg.dev/$PROJECT_ID/ai-swarm

# Deploy each service if it has a Dockerfile and a service.yaml
services=(ai-gateway orchestrator strategy-planner signals-scout price-intel proposal-sniper lead-fabric finops-agent traffic-shaper codex-prime shadow-agent)

for svc in "${services[@]}"; do
  dir=services/$svc
  if [ -f $dir/Dockerfile ] && [ -f $dir/service.yaml ]; then
    img=$AR/$svc:$(git rev-parse --short HEAD)
    gcloud run deploy $svc \
      --project=$PROJECT_ID \
      --region=$REGION \
      --image=$img \
      --platform=managed \
      --allow-unauthenticated=false \
      --source=. || true
  fi
done
