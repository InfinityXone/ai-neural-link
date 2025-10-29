from fastapi import FastAPI, Request
import time
from app.routes.db_health import router as db_router

app = FastAPI()
DIRECTIVES = []

@app.get('/health')
def health():
    return {'ok': True, 'ts': time.time()}

@app.post('/handshake')
async def handshake(req: Request):
    body = await req.json()
    return {'status': 'ok', 'received': body}

@app.get('/directive')
def directive(agent: str = 'Echo'):
    return DIRECTIVES[-1] if DIRECTIVES else {'command': 'noop'}

@app.post('/complete')
async def complete(req: Request):
    body = await req.json()
    return {'status': 'logged', 'received': body}

app.include_router(db_router)
