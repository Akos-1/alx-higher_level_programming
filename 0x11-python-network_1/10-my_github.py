#!/usr/bin/python3
import requests
import sys


def get_github_id(username, password):
    url = "https://api.github.com/user"

    headers = {
        'Authorization': 'Basic {}:{}'.format(username, password),
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            print("Your GitHub id:", data['id'])
        except ValueError:
            print("Not a valid JSON")
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <access_token>")
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]

    get_github_id(username, access_token)
