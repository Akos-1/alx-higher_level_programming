#!/bin/bash
# This script takes a URL as an argument, sends a GET request with a specific header, and displays the body of the response.
curl -s -H "X-School-User-Id: 98" "$1"
