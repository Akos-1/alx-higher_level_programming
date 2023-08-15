#!/usr/bin/python3


def write_file(filename="", text=""):
    """Write a string to a UTF8text file

    Args:
        filename (str): the file name to be written.
        text (str): the text too be written to the file
    Return: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
