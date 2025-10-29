#!/usr/bin/env bash
set -euo pipefail

# CI checks: unit tests, lint, security and image scan placeholders
# Python
if command -v pip &>/dev/null; then
  pip install -q -r requirements.txt || true
  if command -v pytest &>/dev/null; then pytest -q || true; fi
  if command -v ruff &>/dev/null; then ruff . || true; fi
  if command -v bandit &>/dev/null; then bandit -q -r . || true; fi
fi
# Node
if [ -f package.json ]; then
  npm ci || true
  npx eslint . || true
fi
# Trivy container scan (optional)
if command -v trivy &>/dev/null; then
  trivy fs --exit-code 0 --severity HIGH,CRITICAL . || true
fi
