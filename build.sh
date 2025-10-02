#!/usr/bin/env bash

# Exit on error
set -o errexit

# Optional: echo commands for debugging
# set -o xtrace

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# (Optional) If you need to install other tools, do it here.
# e.g., if Riffusion needs FFmpeg or other system deps, install here.
