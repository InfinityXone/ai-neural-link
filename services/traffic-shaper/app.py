from fastapi import FastAPI
import os
PORT = int(os.getenv("PORT","8080"))
app = FastAPI()

@app.get("/health")
def health(): return {"ok": True}

# Minimal contract endpoints (expand per-service)
@app.post("/run")
def run(): return {"status": "accepted"}
