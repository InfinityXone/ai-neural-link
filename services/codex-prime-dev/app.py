from fastapi import FastAPI
from pydantic import BaseModel
import os
PORT = int(os.getenv("PORT","8080"))
app = FastAPI(title="codex-prime-dev")

class PlanRequest(BaseModel):
    repo:str; goal:str; outline:list[str]|None=None

class ScaffoldRequest(BaseModel):
    repo:str; path:str; template:str; params:dict|None=None

class DiffRequest(BaseModel):
    repo:str; path:str; target:str; patch_hint:str|None=None

class PRRequest(BaseModel):
    repo:str; branch:str; title:str; body:str|None=None

@app.get("/health")
def health(): return {"ok": True}

@app.post("/plan")
def plan(req: PlanRequest):
    # TODO: generate file tree plan + steps (placeholder)
    return {"status":"ok","repo":req.repo,"goal":req.goal,"files":["/api/main.py","/web/app/page.tsx"]}

@app.post("/scaffold")
def scaffold(req: ScaffoldRequest):
    # TODO: write files from template + params
    return {"status":"ok","path":req.path,"applied_template":bool(req.template)}

@app.post("/diff")
def diff(req: DiffRequest):
    # TODO: compute+persist patch; return preview
    return {"status":"ok","path":req.path,"preview":"--- a\n+++ b\n"}

@app.post("/pr")
def pr(req: PRRequest):
    # TODO: create branch+commit+open PR via GH API (placeholder)
    return {"status":"ok","pr_url":"https://github.com/<owner>/<repo>/pull/123"}
