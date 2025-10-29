# 21 • Data Model & Storage (Advanced)
- Firestore patterns for append-only logs (profit events, executions).
- Idempotent keys: sha256 canonical payload.
- Optional PostgreSQL (RLS) for analytics; default deny policies.
- Exports to GCS for BI; partitioned by date.