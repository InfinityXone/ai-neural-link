#!/usr/bin/env python3
import os, json, requests
from google.cloud import storage

GATEWAY = os.getenv('MEMORY_GATEWAY_URL', '').rstrip('/')
TOKEN = os.getenv('MEMORY_GATEWAY_TOKEN', '')
SEED_PATH = os.getenv('MEMORY_SEED_PATH', 'memory/core_brain/Etherverse_Core_AI.json')
SEED_GCS = os.getenv('MEMORY_SEED_GCS_URI', '')  # gs://bucket/path.json

def load_seed():
    if SEED_GCS.startswith('gs://'):
        _, path = SEED_GCS.split('gs://',1)
        bucket, *rest = path.split('/',1)
        blob_path = rest[0] if rest else ''
        client = storage.Client()
        bucket_obj = client.bucket(bucket)
        blob = bucket_obj.blob(blob_path)
        return json.loads(blob.download_as_text())
    with open(SEED_PATH, 'r') as f:
        return json.load(f)

if not GATEWAY:
    raise SystemExit('MEMORY_GATEWAY_URL not set')

seed = load_seed()
headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
r = requests.post(f"{GATEWAY}/memory/hydrate", json=seed, headers=headers, timeout=60)
print('Hydrate status:', r.status_code, r.text[:400])
