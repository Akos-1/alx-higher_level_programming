#!/usr/bin/python3
"""Print the alphabet in reverse order alternating upper- and lower-case."""
a = 0
for b in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(b - a)), end="")
    a = 32 if a == 0 else 0
