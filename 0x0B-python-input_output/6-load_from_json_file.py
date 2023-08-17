#!/usr/bin/python3
"""Defines a function that reads a JSON file"""
import json


def load_from_json_file(filename):
    """Make a Pyton object from a JSON file"""
    with open(filename) as f:
        data = json.load(f)
    return data
