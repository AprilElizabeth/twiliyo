#!/bin/bash

export TWILIO_SID=$(cat ./secrets/sid.key)
export TWILIO_AUTH=$(cat ./secrets/auth.key)

echo "Starting twilio app..."
python ./bin/twiliyo.py
