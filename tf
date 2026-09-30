#!/bin/sh
# Launcher: runs the CLI on Python 3.10+ via uv, from any directory.
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT" && exec uv run --no-project --quiet --python ">=3.10" python -m fundamentals "$@"
