#!/bin/sh
set -e
black --diff --check .
flake8
pytest -vvv .
