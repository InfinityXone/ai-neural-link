#!/usr/bin/env bash
set -euo pipefail
echo "[bootstrap] ensuring dirs and baseline"
mkdir -p ops infra app docs .github/ISSUE_TEMPLATE .github/workflows
if [ ! -f app/main.py ]; then
python - <<'PY'
from pathlib import Path
p=Path('app'); p.mkdir(exist_ok=True)
(Path('app')/'main.py').write_text("""from fastapi import FastAPI
import os, time
app = FastAPI(); start = time.time()
@app.get('/health')
def health():
    return {'ok': True, 'uptime_s': round(time.time()-start,2), 'service': os.getenv('SERVICE_NAME','autonomy-api')}
""")
PY
fi
echo "[bootstrap] done"
