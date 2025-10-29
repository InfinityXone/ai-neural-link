from fastapi import FastAPI, Request
app = FastAPI(title='orchestrator')

@app.get('/health')
async def health():
    return {'ok': True}

@app.post('/route')
async def route(req: Request):
    body = await req.json()
    # echo back with an execution_id stub
    return {'execution_id': 'stub-0001', 'received': body}
