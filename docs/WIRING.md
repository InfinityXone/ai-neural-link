# Wiring (Parallel Model)
- Strategy → writes next 24h plan.
- Orchestrator → reads plan + caps → emits jobs (with jitter).
- Traffic Shaper/Backpressure/Telemetry → write caps/flags every 1–5m; Orchestrator and Workers consult at execution time.
- EV/Cost Gate → computes floors; Orchestrator gates enqueue; budget checks mid-day.
- Signals Scout → writes signals_buffer; Lead Fabric → writes leads; Proposal Sniper → writes proposals.
(Ref: your parallel plan & team split.) 
