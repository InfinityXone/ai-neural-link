# 01 • System Overview & Principles

**Purpose:** 24/7 autonomous, profit-seeking AI swarm that plans, builds, ships, operates, and grows revenue with strict safety, cost, and quality controls.

## Principles
- **Keyless CI/CD:** GitHub → GCP via OIDC (WIF).
- **Health-first:** `/health`, `/metrics` everywhere, warmers every 5m.
- **Label isolation:** `origin=ai-neural-link`, deterministic naming.
- **Observability:** SLOs + alerts; rollback-first incident response.
- **Ethics & Compliance:** whitelisted data sources, audit logs.

## Control Loop
Signals → Plan (DSL) → Route → Execute → Profit events → Telemetry → Adjust.

## Core Services
- **ai-gateway:** headless API for agents & GPT Actions.
- **orchestrator:** routes tasks to services.
- **strategy-planner, signals-scout, price-intel, proposal-sniper, lead-fabric, finops-agent, traffic-shaper, codex-prime, shadow-agent.

## Read Next
03 Agent Onboarding, 07 CI/CD & WIF, 13 Profit Engines, 19 GPT Actions, 20 Memory Hydrate/Dehydrate.