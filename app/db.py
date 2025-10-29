from sqlalchemy import create_engine, text
import os

def _socket_engine():
    socket = os.getenv('DB_SOCKET')
    db = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    pwd = os.getenv('DB_PASSWORD')
    return create_engine(f"postgresql+pg8000://{user}:{pwd}@/{db}?unix_sock={socket}/.s.PGSQL.5432")

def _host_engine():
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT','5432')
    db = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    pwd = os.getenv('DB_PASSWORD')
    return create_engine(f"postgresql+pg8000://{user}:{pwd}@{host}:{port}/{db}")

# prefer socket if present
engine = _socket_engine() if os.getenv('DB_SOCKET') else _host_engine()

def ping():
    with engine.connect() as conn:
        return conn.execute(text('select 1')).scalar() == 1
