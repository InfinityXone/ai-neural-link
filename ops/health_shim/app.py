from fastapi import FastAPI; import os
app=FastAPI()
@app.get("/health")
def health(): return {"ok": True, "port": int(os.environ.get("PORT","8080"))}
