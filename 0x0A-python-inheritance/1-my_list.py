#!/usr/bin/python3
"""Defines an inherited list called class MyList"""


class MyList(list):
    """Implementing sorted printing for the built-in list class"""

    def print_sorted(self):
        """List printed in ascending order"""
        print(sorted(self))
