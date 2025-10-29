# 09 • Data Model & Storage
Entities: Task, Signal, Plan, Proposal, Lead, Execution, ProfitEvent.
Storage: Firestore (append-only logs), optional Postgres (RLS).
Keys: deterministic IDs; sha256(payload)[:12].
Backups: daily export to GCS; 30d retention.