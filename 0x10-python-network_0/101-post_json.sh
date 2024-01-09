#!/bin/bash
# sends a json POST request to a url passes as the first argument
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
