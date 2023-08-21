#!/usr/bin/python3
"""Defines a base model class"""
import json


class Base:
    """The Base model
    This is the "base" for all the classes in this projects"

    Private Class Attributes:
        __nb_object (int):
        Number of instantiated Bases.
    """

    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
