#!/usr/bin/env bash

set -e

# Let the stub be imported
export PYTHONPATH=${PWD}:${PYTHONPATH}

for task in lesson*/**/task.py; do
  echo "> Testing " $task
  python3 $task
done
