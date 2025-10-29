#!/usr/bin/env bash
set -euo pipefail
REGION=us-east1
PROJECT_ID=infinity-x-one-swarm-system
AR=us-east1-docker.pkg.dev/$PROJECT_ID/ai-swarm

services=(ai-gateway orchestrator strategy-planner signals-scout price-intel proposal-sniper lead-fabric finops-agent traffic-shaper codex-prime shadow-agent)

for svc in "${services[@]}"; do
  dir=services/$svc
  if [ -f $dir/Dockerfile ]; then
    img=$AR/$svc:$(git rev-parse --short HEAD)
    docker build -t $img $dir
  fi
done
