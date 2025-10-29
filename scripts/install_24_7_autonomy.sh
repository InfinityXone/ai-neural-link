#!/usr/bin/env bash
set -euo pipefail
PROJECT_ID="infinity-x-one-swarm-system"
REGION="us-east1"

echo "🚀 Installing 24/7 autonomous mode..."

# Refresh and keep services warm
gcloud scheduler jobs create http ai-swarm-autonomy --schedule="*/5 * * * *" \
  --uri="https://memory-gateway-938446344277.us-east1.run.app/hydrate" \
  --oidc-service-account-email="scheduler-autopilot@${PROJECT_ID}.iam.gserviceaccount.com" \
  --http-method=POST --location="${REGION}" || echo "⚠️ autonomy job already exists"

echo "✅ 24/7 autonomy scheduler active."
