#!/usr/bin/env bash
set -euo pipefail
SVC="${1:-autonomy-api}"
URL="$(gcloud run services describe "$SVC" --format='value(status.url)' || true)"
if [ -z "$URL" ]; then echo "No URL yet for $SVC"; exit 2; fi
code="$(curl -s -o /dev/null -w '%{http_code}' "$URL/health")"
echo "GET $URL/health -> $code"
test "$code" = "200" || exit 3
