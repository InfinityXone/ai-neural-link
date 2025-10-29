# 11 • Autopilot Self-heal Runbook
- Detect: alerts fire < 5m.
- Triage: categorize (auth, deploy, perf, data).
- Mitigate: route traffic to last good revision.
- Warmers: ensure `/health` jobs enabled.
- Learn: postmortem < 48h; track actions.