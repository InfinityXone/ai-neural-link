#!/usr/bin/env bash
set -euo pipefail
SVC="${1:-autonomy-api}"
MODE="${2:-loop}"
probe() { gcloud run services describe "$SVC" --format='value(status.url)' | xargs -I{} curl -s -o /dev/null -w '%{http_code}' "{}/health" || echo 000; }
tick() {
  code="$(probe)"
  echo "[$(date -Is)] $SVC /health -> $code"
  if [ "$code" != "200" ]; then
    echo "restart $SVC"
    gcloud run services update "$SVC" --set-env-vars=LAST_HEAL="$(date +%s)" --quiet || true
  fi
}
if [ "$MODE" = "--one-shot" ]; then tick; else while true; do tick; sleep 60; done; fi
