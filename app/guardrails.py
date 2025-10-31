import time, os
from typing import Optional

class Budget:
    def __init__(self, tokens:int=1000, seconds:int=30):
        self.max_tokens = tokens
        self.deadline = time.time() + seconds
        self.used = 0
    def spend(self, n:int):
        self.used += n
        if self.used > self.max_tokens:
            raise RuntimeError('budget_exceeded')
        if time.time() > self.deadline:
            raise RuntimeError('deadline_exceeded')

ALLOW_DOMAINS = set((os.getenv('ALLOW_DOMAINS','api.github.com,api.openai.com,httpbin.org').split(',')))

def allow_domain(url:str)->bool:
    from urllib.parse import urlparse
    host = urlparse(url).hostname or ''
    return any(host.endswith(d.strip()) for d in ALLOW_DOMAINS)
