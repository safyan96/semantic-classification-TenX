#!/bin/sh

echo "running with debugger"
uvicorn app:app --reload --host 0.0.0.0 --port 8002