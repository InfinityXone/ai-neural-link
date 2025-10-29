import os, logging
from fastapi import FastAPI
from pythonjsonlogger import jsonlogger
app=FastAPI(title="AI Neural Link — API")
h=logging.StreamHandler(); h.setFormatter(jsonlogger.JsonFormatter())
log=logging.getLogger("api"); log.addHandler(h); log.setLevel(logging.INFO)
@app.get("/health")
def health(): return {"ok": True, "port": int(os.environ.get("PORT","8080"))}
