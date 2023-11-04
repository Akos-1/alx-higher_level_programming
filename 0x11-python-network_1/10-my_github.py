#!/usr/bin/python3
import requests
import sys
import base64

if len(sys.argv) != 3:
    print("Usage: python script.py <username> <access_token>")
    sys.exit(1)

username = sys.argv[1]
access_token = sys.argv[2]

url = "https://api.github.com/user"

headers = {
    'Authorization': 'Basic {}'.format(base64.b64encode(f"{username}:{access_token}".encode()).decode()),
}

response = requests.get(url, headers=headers)

try:
    data = response.json()
    print("GitHub API response:", data)  # Print the entire response
    print("Your GitHub id:", data.get('id', 'Not available'))
except ValueError:
    print("Not a valid JSON")
