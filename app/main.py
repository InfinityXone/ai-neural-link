from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
from app.store import enqueue
from app.worker import run_loop
from app.logger import logger

app = FastAPI()
HEALTH = Counter('health_pings','health checks')
TASKS = Counter('tasks_enqueued','tasks enqueued')

@app.get('/health')
def health():
    HEALTH.inc(); return {'ok':True}

@app.get('/metrics')
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.post('/tasks/cron')
def cron(url: str='https://httpbin.org/get'):
    TASKS.inc(); enqueue('http.fetch', {'url': url}); logger.info('enqueued http.fetch'); return {'queued':True}

@app.post('/tasks/run')
async def run(ticks:int=1):
    await run_loop(ticks=ticks); return {'ran':ticks}
