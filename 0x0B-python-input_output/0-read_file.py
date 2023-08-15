#!/usr/bin/python3
"""Defines a function that reads a text file """


def read_file(filename=""):
    """Prints the contents of a UTF8 text file"""
    with open(filename, encoding='utf-8') as f:
            content = f.read()
            print(content, end ="")
