#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        """Initialize a new Student.


        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return
    {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
    }
