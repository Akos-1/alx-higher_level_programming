#!/usr/bin/python3
"""Defines a JSON string function"""
import json


def to_json_string(my_obj):
    """Return the JSON representative of a string object"""
    return json.dumps(my_obj)
