from fastapi import APIRouter
from app.db import ping

router = APIRouter()

@router.get('/db/health')
def db_health():
    ok = ping()
    return { 'ok': ok }
