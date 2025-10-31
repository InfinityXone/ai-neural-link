from fastapi import FastAPI
import os, time
app = FastAPI()
start = time.time()

@app.get("/health")
def health():
    return {
        "ok": True,
        "uptime_s": round(time.time()-start,2),
        "service": os.getenv("SERVICE_NAME","autonomy-api")
    }
