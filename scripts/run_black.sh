#!/bin/sh

# Set up Python environment (assuming Python 3.10 is already installed)
python_version="3.10"

# Optionally create and activate a virtual environment
# python -m venv venv
# source venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install black

# Run black
black $(git ls-files '*.py')
