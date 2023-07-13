#!/usr/bin/python3

import sys
count = len(sys.argv) - 1
if count == 0:
    print("0 arguments.")
elif count == 1:
    print("1 argument:")
else:
    print(f"{count} arguments:")
for i, arg in enumerate(sys.argv[1:], start=1):
    print(f"{i}: {arg}")
