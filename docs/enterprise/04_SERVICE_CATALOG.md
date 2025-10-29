# 04 • Service Catalog

- **ai-gateway** — unified headless API for agents & UI.
- **orchestrator** — routes tasks and enforces policies.
- **strategy-planner** — DSL→plan steps.
- **signals-scout** — fetch/clean market & web signals.
- **price-intel** — pricing diffs & margin alerts.
- **proposal-sniper** — draft, price, send proposals.
- **lead-fabric** — prospecting & outreach orchestration.
- **finops-agent** — budgets, spend guards, alerting.
- **traffic-shaper** — rate & spend caps by actor.
- **codex-prime** — codegen + review.
- **shadow-agent** — API façade/proxy.

Each service: FastAPI, `/health`, `/metrics`, minimal Dockerfile, GitHub Action deploy step.