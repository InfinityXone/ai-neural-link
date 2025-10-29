# 22 • Testing, QA & Release Checklist
- Unit: pytest -q; coverage gate.
- Lint: ruff/flake8 + eslint.
- Security: bandit + trivy scan.
- Canary: 10% traffic for 10m; auto-rollback on 5xx>2%.
- Docs: update `docs/` and `gpt/memory_seed.json`.
- Release: tag, changelog, SBOM attach.