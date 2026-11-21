#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files

python3 manage.py collectstatic --no-input --clear

# Create Vercel-compatible output vercel directory
mkdir -p .vercel/output/static
cp -r staticfiles/ .vercel/output/static/

python3 manage.py makemigrations
python3 manage.py migrate

