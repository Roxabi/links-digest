#!/usr/bin/env bash
# Wrapper for links-digest server — serves $LINKS_DIR on port 8082.
export LINKS_DIR="${LINKS_DIR:-${HOME}/projects/links-digest}"

exec python3 "$LINKS_DIR/serve.py"
