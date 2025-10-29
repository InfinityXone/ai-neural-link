# Elite Agents (24/7 Autonomous Revenue)
- strategist-agent — sets daily Financial Goal, EV floors, campaign mix.
- signals-agent — harvests public deal signals (rfqs, permits, pricing, hiring).
- price-intel-agent — tracks competitor price & catalog deltas.
- proposal-agent — RFP ingest → compliance matrix → draft → PDF.
- lead-fabric-agent — intent + contact stitching; outreach hooks.
- arbitrage-agent — executes safe, policy-checked opportunities.
- finops-agent — EV/cost guardrails; budgets and caps.
- traffic-shaper — token buckets; politeness and rate limits.
- gpt-gateway — LLM routing with budget metering.
- orchestrator — warms, routes, schedules; /backup endpoint for housekeeping.
Each service exposes: GET /health, POST /run (stub). Autopilot warms/heals every 10m.
