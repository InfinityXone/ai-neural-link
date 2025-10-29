#!/usr/bin/env bash
set -euo pipefail
: "${PROJECT_ID:?}"
: "${REGION:=us-east1}"
: "${ORCHESTRATOR_URL:?}"

# Placeholder heuristic: if orchestrator /metrics says 5xx_ratio > 0.02, rollback to previous revision
# Requires: gcloud run services describe <svc> --region=$REGION --format=json

check_failed() {
  curl -fsS $ORCHESTRATOR_URL/metrics | grep -E '5xx_ratio [0-9]+' | awk '{print $2}' | awk '$1 > 0.02 {exit 0} END {exit 1}'
}

rollback_svc() {
  local svc=$1
  echo "[rollback] $svc"
  # Find last two revisions
  REVS=$(gcloud run services describe $svc --region=$REGION --format=json | jq -r '.status.traffic[].revisionName' | head -n 2)
  CUR=$(echo "$REVS" | sed -n '1p')
  PREV=$(echo "$REVS" | sed -n '2p')
  if [ -n "$PREV" ]; then
    gcloud run services update-traffic $svc --region=$REGION --to-revisions $PREV=100
    echo "[rollback] $svc -> $PREV"
  else
    echo "[rollback] no previous revision for $svc"
  fi
}

if check_failed; then
  for svc in ai-gateway orchestrator; do
    rollback_svc $svc || true
  done
else
  echo "[rollback] metrics look healthy; no action"
fi
