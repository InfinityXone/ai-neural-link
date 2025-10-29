# Cloud Scheduler — Gateway Jobs (Script)

Apply/update via CLI with stored payloads.

```bash
PROJECT_ID="infinity-x-one-swarm-system"
REGION="us-east1"
GATEWAY="https://memory-gateway-938446344277.us-east1.run.app"
SA="scheduler-autopilot@$PROJECT_ID.iam.gserviceaccount.com"

# Create or update Finsynapse job
if ! gcloud scheduler jobs describe plan-finsynapse --project $PROJECT_ID --location $REGION >/dev/null 2>&1; then
  gcloud scheduler jobs create http plan-finsynapse \
    --project $PROJECT_ID --location $REGION \
    --schedule "*/30 * * * *" --time-zone "UTC" \
    --uri "$GATEWAY/plan" --http-method POST \
    --oidc-service-account-email "$SA" \
    --oidc-token-audience "$GATEWAY" \
    --headers "Content-Type=application/json" \
    --message-body '@infra/scheduler/payloads/plan-finsynapse.json'
else
  gcloud scheduler jobs update http plan-finsynapse \
    --project $PROJECT_ID --location $REGION \
    --schedule "*/30 * * * *" --time-zone "UTC" \
    --uri "$GATEWAY/plan" --http-method POST \
    --oidc-service-account-email "$SA" \
    --oidc-token-audience "$GATEWAY" \
    --update-headers "Content-Type=application/json" \
    --message-body '@infra/scheduler/payloads/plan-finsynapse.json'
fi

# Create or update Guardian job
if ! gcloud scheduler jobs describe guardian-health --project $PROJECT_ID --location $REGION >/dev/null 2>&1; then
  gcloud scheduler jobs create http guardian-health \
    --project $PROJECT_ID --location $REGION \
    --schedule "*/5 * * * *" --time-zone "UTC" \
    --uri "$GATEWAY/plan" --http-method POST \
    --oidc-service-account-email "$SA" \
    --oidc-token-audience "$GATEWAY" \
    --headers "Content-Type=application/json" \
    --message-body '@infra/scheduler/payloads/guardian-health.json'
else
  gcloud scheduler jobs update http guardian-health \
    --project $PROJECT_ID --location $REGION \
    --schedule "*/5 * * * *" --time-zone "UTC" \
    --uri "$GATEWAY/plan" --http-method POST \
    --oidc-service-account-email "$SA" \
    --oidc-token-audience "$GATEWAY" \
    --update-headers "Content-Type=application/json" \
    --message-body '@infra/scheduler/payloads/guardian-health.json'
fi
```
