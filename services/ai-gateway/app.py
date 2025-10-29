import os,time,json,asyncio
from collections import defaultdict,deque
from typing import Dict,Any
import httpx,yaml
from fastapi import FastAPI,Request,HTTPException
from google.cloud import storage
ORCH=os.getenv('ORCHESTRATOR_BASE_URL')
GCS=os.getenv('GCS_SEED_BUCKET')
POLICY=yaml.safe_load(open('policy.yaml')) or {}
ALLOW=set(POLICY.get('allow_actors',[]))
MAXTOK=int(POLICY.get('max_tokens_default',1024))
QPS=POLICY.get('rate_limits_qps',{})
class RL:
  def __init__(s): s.l=asyncio.Lock(); s.b=defaultdict(deque)
  async def ok(s,k,m):
    t=time.time(); d=t-1
    async with s.l:
      q=s.b[k]
      while q and q[0]<d: q.popleft()
      if len(q)<m: q.append(t); return True
      return False
rl=RL(); app=FastAPI(title='ai-gateway')
@app.get('/health')
async def health(): return {'ok':True,'orchestrator':bool(ORCH)}
@app.get('/metrics')
async def metrics(): return {'qps_policy':QPS,'allow_actors':sorted(list(ALLOW))}
async def gate(p:Dict[str,Any]):
  a=p.get('actor')
  if not a or a not in ALLOW: raise HTTPException(403,f'actor {a!r} not allowed')
  b=p.get('budget') or {}; mt=int(b.get('max_tokens',MAXTOK))
  if mt>MAXTOK: raise HTTPException(429,f'max_tokens {mt} exceeds policy {MAXTOK}')
  lim=int(QPS.get(a,QPS.get('default',2)))
  if not await rl.ok(a,lim): raise HTTPException(429,f'QPS limit exceeded for {a}')
@app.post('/route')
async def route(req:Request):
  if not ORCH: raise HTTPException(500,'ORCHESTRATOR_BASE_URL not set')
  p=await req.json(); await gate(p)
  async with httpx.AsyncClient(timeout=30.0) as c:
    r=await c.post(f'{ORCH}/route',json=p)
  if r.status_code>=400: raise HTTPException(r.status_code,r.text)
  return r.json()
@app.post('/memory/hydrate')
async def mem_hydrate():
  s={'system_overview':{'mission':'AI gateway seed'},'policy':{'allow_actors':sorted(list(ALLOW)),'max_tokens_default':MAXTOK},'endpoints':{'route':'/route','health':'/health','metrics':'/metrics','memory_hydrate':'/memory/hydrate','memory_dehydrate':'/memory/dehydrate'}}
  b=json.dumps(s).encode()
  if len(b)>512000: raise HTTPException(413,'seed exceeds 500KB policy')
  return s
@app.post('/memory/dehydrate')
async def mem_dehydrate(req:Request):
  if not GCS: raise HTTPException(500,'GCS_SEED_BUCKET not set')
  d=await req.json(); b=json.dumps(d).encode()
  if len(b)>512000: raise HTTPException(413,'seed exceeds 500KB policy')
  ts=time.strftime('%Y%m%d-%H%M%S'); name=f'seeds/seed-{ts}.json'
  cl=storage.Client(); bk=cl.bucket(GCS); bl=bk.blob(name); bl.upload_from_string(b,content_type='application/json')
  return {'ok':True,'bucket':GCS,'object':name}
