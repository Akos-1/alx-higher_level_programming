#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of a named class"""

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of obj to.
    Returns:
        if obj is exactly an instance of a_class - True
        if not - False.
    """   

    if type(obj) == a_class:
        return True
    return False
