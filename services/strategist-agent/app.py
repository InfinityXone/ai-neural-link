import os, logging, time, json
from fastapi import FastAPI, Body
from pythonjsonlogger import jsonlogger
app=FastAPI(title="strategist-agent")
h=logging.StreamHandler(); h.setFormatter(jsonlogger.JsonFormatter())
log=logging.getLogger("strategist-agent"); log.addHandler(h); log.setLevel(logging.INFO)
@app.get("/health")
def health(): return {"ok": True, "service": "strategist-agent", "port": int(os.environ.get("PORT","8080"))}
@app.post("/run")
def run(payload: dict = Body(default={})):
    ts=int(time.time()); log.info({"event":"run","service":"strategist-agent","ts":ts,"payload":payload})
    return {"ok": True, "service":"strategist-agent","ts":ts}
