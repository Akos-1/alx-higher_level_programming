#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size ** 2
