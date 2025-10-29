import time, logging
from pythonjsonlogger import jsonlogger
log=logging.getLogger("worker"); h=logging.StreamHandler(); h.setFormatter(jsonlogger.JsonFormatter()); log.addHandler(h); log.setLevel(logging.INFO)
def tick(): log.info({"tick":"ok"})
if __name__=="__main__":
  while True:
    try: tick()
    except Exception: log.exception("tick_error")
    time.sleep(300)
