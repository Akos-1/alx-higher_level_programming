#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response.
if [ -z "$1" ]; then echo "Usage: $0 <URL>"; exit 1; fi
curl -s -o response.txt -w "%{http_code}" "$1"
cat response.txt
wc -l < response.txt
rm response.txt
