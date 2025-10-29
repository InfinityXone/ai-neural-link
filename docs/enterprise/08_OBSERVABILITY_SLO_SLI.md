# 08 • Observability, SLO/SLI
- Availability SLO: 99.5% / 30d.
- p95 latency: /health < 600ms, /harvest < 2s.
- Signals: Cloud Logging, Error Reporting, Uptime, Scheduler success.
- Dashboards: requests/5m, 4xx/5xx, cold starts, cost/1k req.
- Alerts: 5xx > 2% for 5m; cold starts spike; AR push failures; Scheduler errors.