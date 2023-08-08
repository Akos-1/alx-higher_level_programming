#!/usr/bin/python3
"""Defines a locked class."""
class LockedClass:
    __slots__ = ("first_name",)

    def __setattr__(self, name, value):
        if hasattr(self, name) or name != "first_name":
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
