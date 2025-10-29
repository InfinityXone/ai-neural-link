#!/usr/bin/env python3
import os, json, requests

GATEWAY = os.getenv('MEMORY_GATEWAY_URL', '').rstrip('/')
TOKEN = os.getenv('MEMORY_GATEWAY_TOKEN', '')
SEED_PATH = os.getenv('MEMORY_SEED_PATH', 'memory/core_brain/Etherverse_Core_AI.json')

if not GATEWAY:
    raise SystemExit('MEMORY_GATEWAY_URL not set')

with open(SEED_PATH, 'r') as f:
    seed = json.load(f)

headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
r = requests.post(f"{GATEWAY}/memory/hydrate", json=seed, headers=headers, timeout=60)
print('Hydrate status:', r.status_code, r.text[:400])
