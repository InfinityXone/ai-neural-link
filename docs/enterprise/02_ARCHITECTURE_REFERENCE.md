# 02 • Architecture Reference

```
[GATEWAY]<-GPT Actions/Agents
   |-- /plan /route /harvest /metrics /health
   v
[ORCHESTRATOR] -> [SERVICES] -> [Profit Endpoints]
                         |-> price-intel
                         |-> lead-fabric
                         |-> proposal-sniper
                         |-> signals-scout

Storage: Firestore (append-only logs), optional Postgres (RLS).
Build: Docker → Artifact Registry → Cloud Run.
Auth: GitHub OIDC → GCP WIF (no static keys).
```

**Networking:** private Cloud Run with OIDC callers; Vercel UI calls gateway via headless API.
**Secrets:** GCP Secret Manager; mount via runtime SA.
**Images:** pinned bases; vulnerability scanning enabled.