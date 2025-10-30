# Deploy Plan (Clean Rebuild)

## Repo layout
```
services/
  api-gateway/
  memory-gateway/
  shadow-agent/
  codex-agent/
  guardian/
  picky-bot/
  finsynapse/
.github/workflows/
  deploy.yaml
ops/
  runbooks/
  dashboards/
```

## Build & ship
- GitHub OIDC → GCP Workload Identity Federation.
- Workflow: build Docker → push Artifact Registry → deploy Cloud Run (private).
- Post-deploy: create/refresh warmers (OIDC audience = service URL).

## One-time bootstrap
1. Create WIF pool & provider; bind `roles/run.admin`, `roles/artifactregistry.writer`.
2. Create deployer SA and bind to OIDC subject.
3. Artifact Registry repo `services` (region `us-east1`).

## Day-2 guardrails
- Budgets + alerts.
- Error budget policies; roll back on burn.
- SBOM + vuln scanning; pinned bases.

## Cutover plan
1. Stand up new services with canonical stubs (FastAPI).
2. Point Scheduler jobs to new URLs.
3. Decommission old services (`ai-gateway`, `autonomy-api`, `infinity-agent`, orphaned `orchestrator`).
