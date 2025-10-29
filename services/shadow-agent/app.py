from fastapi import FastAPI
from pydantic import BaseModel
import os, asyncio, httpx
PORT = int(os.getenv("PORT","8080"))
app = FastAPI(title="shadow-agent")

class Task(BaseModel):
    kind:str # "crawl"|"post"|"monitor"|"fetch"|"submit"
    url:str|None=None
    payload:dict|None=None
    headers:dict|None=None

@app.get("/health")
def health(): return {"ok": True}

@app.post("/task")
async def run_task(t: Task):
    # NOTE: no browser here (API-only). Add chrome driver in a future rev if needed.
    async with httpx.AsyncClient(timeout=30) as client:
        if t.kind=="fetch" and t.url:
            r = await client.get(t.url, headers=t.headers)
            return {"status":"ok","code":r.status_code,"len":len(r.text)}
        if t.kind=="post" and t.url:
            r = await client.post(t.url, json=t.payload, headers=t.headers)
            return {"status":"ok","code":r.status_code}
    return {"status":"accepted","kind":t.kind}
