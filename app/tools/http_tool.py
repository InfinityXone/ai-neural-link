import httpx
from app.guardrails import Budget, allow_domain

async def fetch(url:str, budget:Budget):
    if not allow_domain(url):
        raise RuntimeError('domain_not_allowed')
    budget.spend(10)
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(url)
        return {'status': r.status_code, 'len': len(r.content)}
