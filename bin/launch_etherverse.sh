#!/usr/bin/env bash
set -euo pipefail

# Launch core workers locally (for dev)
python -u agents/echo/echo_worker.py &
python -u agents/prompt_writer/promptwriter_worker.py &
python -u agents/guardian/guardian_worker.py &
python -u agents/picky_bot/pickybot_worker.py &
python -u agents/finsynapse/finsynapse_worker.py &
wait
