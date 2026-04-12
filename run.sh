#!/usr/bin/env bash
# Wrapper for roxabi-intel server — serves $INTEL_DIR on port 8082.
export INTEL_DIR="${INTEL_DIR:-${HOME}/roxabi/intel}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$SCRIPT_DIR/serve.py"
