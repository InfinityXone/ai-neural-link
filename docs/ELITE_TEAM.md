# Elite Money Team – Contracts & Wiring

Data contracts (Supabase tables or equivalent):
- plan_slots (by slot, campaign, EV_floor, budget)
- jobs_queue (eta, scope, payload, status)
- traffic_caps (provider,key,endpoint → capacity/refill)
- backpressure_caps (endpoint → target_concurrency)
- ev_floors (campaign → floor, last_update)
- signals_buffer (raw signals, source, score)
- leads (enriched contacts, intent)
- proposals (status, link to artifact)
- incidents / anomaly_flags (type, scope, action)
- usage_events (p50/p95, 429%, cost)
The Orchestrator is the only writer of future jobs. Others update their tables; Orchestrator reads them. (No direct GPT→GPT calls.)
