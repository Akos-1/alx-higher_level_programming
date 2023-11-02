#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | grep -iE '^Allow:' | cut -d ' ' -f 2-
