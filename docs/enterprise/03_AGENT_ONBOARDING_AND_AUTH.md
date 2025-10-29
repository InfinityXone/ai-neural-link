# 03 • Agent Onboarding & Auth
**Goal:** First 10 minutes to contribution and deploy.

## Access
- GitHub: write on repo; branch protection on `main`.
- GCP: deployer via GitHub OIDC → WIF; runtime via SA.

## Local
```bash
git clone git@github.com:InfinityXone/ai-neural-link.git
cd ai-neural-link
```

## Do First
- Read INDEX → this doc, 05, 07, 13, 19, 20.
- Run `make diag` (or scripts/audit_align.py) to self-check.
- Open your first PR from `ciq/<feature>-<date>`.

## Deploy
- Merge to `main` → Actions build & deploy to Cloud Run.