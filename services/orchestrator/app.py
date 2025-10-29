import os, time, requests
from fastapi import FastAPI
app=FastAPI(title="orchestrator")
PROJECT_ID=os.getenv("PROJECT_ID","infinity-x-one-swarm-system")
REGION=os.getenv("REGION","us-east1")
ENGINES=["strategist-agent","signals-agent","price-intel-agent","proposal-agent","lead-fabric-agent","arbitrage-agent","finops-agent","traffic-shaper","gpt-gateway"]
@app.get("/health")
def health(): return {"ok": True, "service":"orchestrator","project":PROJECT_ID,"region":REGION}
@app.post("/backup")
def backup(): return {"ok": True, "note": "backup stub"}
@app.post("/ignite")
def ignite():
    # Fire-and-forget stubs; in production, drive via Pub/Sub/Tasks
    kicked=[]
    base=f"https://{REGION}-run.googleapis.com"
    for s in ENGINES:
        try:
            # this is a placeholder; the Autopilot job will warm via /health
            kicked.append(s)
        except Exception:
            pass
    return {"ok": True, "kicked": kicked}
