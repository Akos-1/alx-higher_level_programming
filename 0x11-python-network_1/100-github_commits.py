#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <repository_name> <owner_name>")
    sys.exit(1)

repository_name = sys.argv[1]
owner_name = sys.argv[2]

url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

response = requests.get(url)

try:
    commits = response.json()
    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
except ValueError:
    print("Not a valid JSON")
