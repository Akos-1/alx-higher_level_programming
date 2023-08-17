#!/usr/bin/python3
"""Defines a function thaat writes a JSON file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, that uses a JSON representation"""
    with open(filename, 'w') as f:
            json.dump(my_obj, f)
