from fastapi import FastAPI, Request, Response, status
import os, time

APP_NAME = os.getenv('APP_NAME','api-gateway')
app = FastAPI(title=APP_NAME)

@app.get('/health')
async def health():
    return {'ok': True, 'service': APP_NAME}

@app.get('/metrics')
async def metrics():
    # minimal prom text; real metrics exported via OTEL in prod
    uptime = int(time.time() - START)
    return Response(f'uptime_seconds {uptime}
', media_type='text/plain')

@app.post('/route')
async def route(req: Request):
    body = await req.json()
    # placeholder routes to orchestrator; actual logic in MAX build
    return {'ok': True, 'gateway_received': body}

START = time.time()
