#!/usr/bin/python3
"""
Function to convert an object to a JSON formatted string.
"""
import json


def to_json_string(my_obj):
    """The JSON representation of the object as a string."""
    return json.dumps(my_obj)
