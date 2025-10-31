import os, sqlite3, json, time
from typing import Optional, Tuple

DB_PATH = os.getenv('DB_PATH','/tmp/state.db')

def _conn():
    c = sqlite3.connect(DB_PATH)
    c.execute('CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, kind TEXT, payload TEXT, status TEXT, tries INT, created REAL, updated REAL)')
    c.execute('CREATE TABLE IF NOT EXISTS events(ts REAL, level TEXT, msg TEXT)')
    return c

def enqueue(kind:str, payload:dict):
    c=_conn(); now=time.time()
    c.execute('INSERT INTO tasks(kind,payload,status,tries,created,updated) VALUES(?,?,?,?,?,?)',(kind,json.dumps(payload),'queued',0,now,now)); c.commit(); c.close()

def next_task()->Optional[Tuple[int,str,dict,int]]:
    c=_conn(); row=c.execute("SELECT id,kind,payload,tries FROM tasks WHERE status='queued' ORDER BY id ASC LIMIT 1").fetchone()
    if not row: c.close(); return None
    id_,k,p,t = row; c.execute("UPDATE tasks SET status='inflight', updated=? WHERE id=?",(time.time(),id_)); c.commit(); c.close(); import json as _j; return id_,k,_j.loads(p),t

def complete(id_:int, ok:bool, note:str=''):
    c=_conn(); status='done' if ok else 'failed'; c.execute('UPDATE tasks SET status=?, updated=? WHERE id=?',(status,time.time(),id_)); c.execute('INSERT INTO events(ts,level,msg) VALUES(?,?,?)',(time.time(),'INFO' if ok else 'ERROR', note)); c.commit(); c.close()
