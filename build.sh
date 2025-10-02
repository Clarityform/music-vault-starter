#!/usr/bin/env bash

# Exit on error
set -o errexit

# Optional: echo commands for debugging
# set -o xtrace

# Clone riffusion if it's not already in your repo
if [ ! -d "riffusion" ]; then
  git clone https://github.com/hmartiro/riffusion.git
fi

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
