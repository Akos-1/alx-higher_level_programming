#!/usr/bin/python3


def write_file(filename="", text=""):
    """Write a string to a UTF8text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        num_chars_written = f.write(text)
    return num_chars_written
