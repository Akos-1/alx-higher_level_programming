#!/usr/bin/python3
import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"
payload = {'q': q}

# Use json=payload instead of data=payload for JSON payload
response = requests.post(url, json=payload)

try:
    data = response.json()
    if data:
        print("[{}] {}".format(data['id'], data['name']))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")

# Print additional information for debugging if needed
print("Status Code:", response.status_code)
print("Response Content:", response.content.decode('utf-8'))
