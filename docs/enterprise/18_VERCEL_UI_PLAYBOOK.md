# 18 • Vercel UI Playbook
- Import repo or CI push from GitHub.
- Env vars synced from GCP Secret Manager via script.
- Auth: Vercel OIDC/GitHub app; no long-lived secrets.
- Edge functions call headless API (ai-gateway).