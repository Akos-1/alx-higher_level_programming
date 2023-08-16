#!/usr/bin/python3
"""Defines a function that appends a file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to be appended.
        text (str): The string to be appended to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        added_characters = f.write(text)
    return added_characters
