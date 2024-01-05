#!/bin/bash
# sends a POST request
curl -s -X POST -d "subject=I will always be here for PLD&email=test@gmail.com" "$1"
