#!/usr/bin/env bash
set -e

source .venv/bin/activate

pip install flake8
flake8 hello.py