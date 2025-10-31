import asyncio, random
from app.store import next_task, complete
from app.guardrails import Budget
from app.tools import http_tool
from app.logger import logger

class Circuit:
    def __init__(self, thresh:int=5, cool:int=30):
        self.fail=0; self.thresh=thresh; self.cool=cool; self.open_until=0
    def allow(self):
        import time
        if time.time()<self.open_until: return False
        return True
    def record(self, ok:bool):
        import time
        if ok: self.fail=0
        else:
            self.fail+=1
            if self.fail>=self.thresh: self.open_until=time.time()+self.cool; self.fail=0

async def process_once():
    if not circuit.allow():
        logger.warning('circuit_open'); return
    item = next_task()
    if not item: return
    id_, kind, payload, tries = item
    backoff = min(60, 2**min(tries,5)) + random.random()*3
    try:
        if kind=='http.fetch':
            res = await http_tool.fetch(payload['url'], Budget(tokens=100, seconds=20))
            logger.info(f'task {id_} ok {res}')
            complete(id_, True, f'ok {res}')
        else:
            complete(id_, True, 'noop')
        circuit.record(True)
    except Exception as e:
        logger.error(f'task {id_} err {e}')
        circuit.record(False)
        await asyncio.sleep(backoff)
        complete(id_, False, f'err {e}')

circuit = Circuit()

async def run_loop(ticks:int=1):
    for _ in range(ticks):
        await process_once()
