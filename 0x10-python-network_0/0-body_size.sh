#!/bin/bash
# This script takes a URL as an argument
#sends a silent request,
#and displays the size of the response body in bytes.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sI "$1" | grep -iE '^Content-Length:' | awk '{print $2}' | tr -d '\r'
