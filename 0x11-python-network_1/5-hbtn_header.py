#!/usr/bin/python3
"""This module takes in a URL"""
import requests
import sys


def get_x_request_id(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
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

        # Dynamically import 'hbtn_header' and print its docstring
        module_name = "hbtn_header"
        try:
            my_module = __import__(module_name)
            print(f'Docstring of {module_name}: {my_module.__doc__}')
        except ImportError:
            print(f"Error: Module '{module_name}' not found.")
