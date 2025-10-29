#!/usr/bin/env bash
set -euo pipefail
REGION="${REGION:?}"; PROJECT_ID="${PROJECT_ID:?}"
mapfile -t LINES < <(gcloud run services list --region "$REGION" --format='value(METADATA.name,STATUS.url)')
for row in "${LINES[@]}"; do
  SVC="$(awk '{print $1}' <<<"$row")"; URL="$(awk '{print $2}' <<<"$row")"
  [[ -z "$SVC" || -z "$URL" ]] && continue
  curl -fsS -m 6 "$URL/health" >/dev/null 2>&1 || gcloud run services update-traffic "$SVC" --region "$REGION" --to-latest --quiet || true
  JOB="warm-${SVC}"
  if gcloud scheduler jobs describe "$JOB" --location "$REGION" >/dev/null 2>&1; then
    gcloud scheduler jobs update http "$JOB" --location "$REGION" --schedule "*/5 * * * *" --http-method GET --uri "${URL}/health" \
      --oidc-service-account-email "run-ciq@${PROJECT_ID}.iam.gserviceaccount.com" --oidc-token-audience "$URL" --quiet
  else
    gcloud scheduler jobs create http "$JOB" --location "$REGION" --schedule "*/5 * * * *" --http-method GET --uri "${URL}/health" \
      --oidc-service-account-email "run-ciq@${PROJECT_ID}.iam.gserviceaccount.com" --oidc-token-audience "$URL" --quiet
  fi
  [[ "$SVC" == "injector" || "$SVC" == "satellite-consumer" ]] && curl -fsS -m 12 -X POST "${URL}/harvest" >/dev/null 2>&1 || true
done
