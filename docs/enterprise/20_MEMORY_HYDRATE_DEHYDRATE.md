# 20 • Memory Hydrate & Dehydrate

**Hydrate:** Read docs/services, compress decisions & interfaces into `gpt/memory_seed.json` for agent boot.
**Dehydrate:** Upload seed to durable store (e.g., GCS) and refresh on deploy.

### CLI
```bash
python scripts/memory_hydrate.py
python scripts/memory_dehydrate.py --bucket gs://<bucket>/seeds
```

### Contracts
- Input: repo paths, commit SHA, service list
- Output: compact seed matching `gpt/schema/memory.schema.json`

### Policy
- No PII.
- Include only public/allowed external endpoints.
- Keep under 500KB for fast agent boot.