from fastapi import FastAPI, Request
import os, time

app = FastAPI()

# in-memory directive queue for demo
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
    # return last directive or noop
    return DIRECTIVES[-1] if DIRECTIVES else {'command': 'noop'}

@app.post('/complete')
async def complete(req: Request):
    body = await req.json()
    return {'status': 'logged', 'received': body}
