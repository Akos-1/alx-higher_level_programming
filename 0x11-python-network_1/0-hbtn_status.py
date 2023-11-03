#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body_bytes = response.read()
    body_utf8 = body_bytes.decode('utf-8')

print("Body response:")
print("\t- type:", type(body_bytes))
print("\t- content:", body_bytes)
print("\t- utf8 content:", body_utf8)
