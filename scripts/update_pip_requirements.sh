#!/bin/bash

BASE_DIR="$(dirname "$0")/.."

pip freeze > "$BASE_DIR/backend/requirements.txt"
