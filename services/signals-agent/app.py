import os, logging, time, json
from fastapi import FastAPI, Body
from pythonjsonlogger import jsonlogger
app=FastAPI(title="signals-agent")
h=logging.StreamHandler(); h.setFormatter(jsonlogger.JsonFormatter())
log=logging.getLogger("signals-agent"); log.addHandler(h); log.setLevel(logging.INFO)
@app.get("/health")
def health(): return {"ok": True, "service": "signals-agent", "port": int(os.environ.get("PORT","8080"))}
@app.post("/run")
def run(payload: dict = Body(default={})):
    ts=int(time.time()); log.info({"event":"run","service":"signals-agent","ts":ts,"payload":payload})
    return {"ok": True, "service":"signals-agent","ts":ts}
