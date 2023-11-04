#!/usr/bin/python3
import requests
import sys

def get_x_request_id(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.headers.get('X-Request-Id', 'Not present')
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
    else:
        url = sys.argv[1]
        x_request_id = get_x_request_id(url)
        print(x_request_id)
