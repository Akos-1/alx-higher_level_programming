#!/usr/bin/python3
def uppercase(string):
    """Print a string in uppercase."""
    for c in string:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
