#!/usr/bin/env bash
set -euo pipefail

: "${GCP_PROJECT:?set GCP_PROJECT}"
: "${GCP_REGION:=us-east1}"
SERVICE=${SERVICE:-ai-neural-link}

IMAGE="${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/docker/${SERVICE}:$(git rev-parse --short HEAD)"

gcloud builds submit . --tag "$IMAGE"

gcloud run deploy "$SERVICE" \
  --image "$IMAGE" \
  --allow-unauthenticated \
  --cpu=1 --memory=1Gi --min-instances=1 --max-instances=50 \
  --set-env-vars MEMORY_GATEWAY_URL=${MEMORY_GATEWAY_URL:-} \
  --set-env-vars SUPABASE_URL=${SUPABASE_URL:-} \
  --set-env-vars SUPABASE_SERVICE_KEY=${SUPABASE_SERVICE_KEY:-}

URL=$(gcloud run services describe "$SERVICE" --format='value(status.url)')
echo "Deployed: $URL"
