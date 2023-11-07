#!/usr/bin/python3
"""the class_to_json module"""


def class_to_json(obj):
    """
    Function to return the dictionary description of a simple data structure.
    """
    vardic = {}
    if hasattr(obj, "__dict__"):
        vardic = obj.__dict__.copy()
    return vardic
