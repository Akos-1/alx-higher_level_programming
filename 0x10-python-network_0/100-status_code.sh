#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response.
curl -s -o /tmp/curl_output "$1" && status_code=$(awk '/HTTP/{print $2}' /tmp/curl_output) && rm -f /tmp/curl_output && echo "$status_code"
