#!/usr/bin/env bash
set -euo pipefail

curl --fail --silent http://localhost:8000/health
