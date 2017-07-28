#!/usr/bin/env bash

set -e

for task in lesson*/**/task.py; do
  echo "> Testing " $task
  python3 $task
done
