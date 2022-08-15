#!/bin/sh

# Script safety flags
set -o errexit
set -o nounset

# Set up environment variables
export FLASK_APP=${FLASK_APP:-"src/main:app"}
export FLASK_DEBUG=${FLASK_DEBUG:-"false"}

# Launches Flask
flask run --host "0.0.0.0" --port 8080
