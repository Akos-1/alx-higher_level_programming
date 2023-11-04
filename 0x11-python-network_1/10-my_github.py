#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <username> <access_token>")
    sys.exit(1)

username = sys.argv[1]
access_token = sys.argv[2]

url = "https://api.github.com/user"

headers = {
    'Authorization': 'token {}'.format(access_token),
}

response = requests.get(url, headers=headers)

try:
    data = response.json()
    print("Your GitHub id:", data['id'])
except ValueError:
    print("Not a valid JSON")
