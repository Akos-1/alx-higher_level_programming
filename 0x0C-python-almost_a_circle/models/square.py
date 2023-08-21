#!/usr/bin/python3
"""Defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        """A new square is initialized

        Args:
            id (int): The new square identity
            width (int): the new square width
            height (int): the new square height
            x (int): the new square x-coordinate
            y (int): the new square y-coordinate
        """

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
