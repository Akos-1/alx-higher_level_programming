#!/bin/bash
# This script takes a URL as an argument, sends a GET request, and displays the body of the response for a 200 status code.
curl -s -o /dev/null -w "%{http_code}\n%{body}" "$1" | awk '/^200/{getline; print}'
