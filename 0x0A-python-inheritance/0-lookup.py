#!/usr/bin/python3
""" returns the list of available attributes and methods of an object"""
def lookup(obj):
    attributes_and_methods = []
    
    for name in dir(obj):
        attribute = getattr(obj, name)
        
        if not name.startswith('_'):
            if callable(attribute):
                attributes_and_methods.append(f"method: {name}")
            else:
                attributes_and_methods.append(f"attribute: {name}")
    
    return attributes_and_methods
