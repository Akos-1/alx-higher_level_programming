#!/usr/bin/python3
if __name__ == "__main__":
import sys

def add_arguments(arguments):
    total = 0
    for arg in arguments:
        total += int(arg)
    return total

    arguments = sys.argv[1:]
    result = add_arguments(arguments)
    print(result)
