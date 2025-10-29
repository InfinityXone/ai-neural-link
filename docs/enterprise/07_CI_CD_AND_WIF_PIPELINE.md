# 07 • CI/CD & WIF Pipeline
- Trigger: push to main (manual dispatch allowed).
- Auth: google-github-actions/auth@v2 via WIF; SA: gha-deployer@…
- Build: Docker images per service → Artifact Registry.
- Deploy: gcloud run deploy per service; private unless explicit.
- Post: schedule warmers for /health every 5m.

**Checks**
- Unit tests, lint, image scan, SBOM attach (Cosign optional).
- Required status checks on branch protection.