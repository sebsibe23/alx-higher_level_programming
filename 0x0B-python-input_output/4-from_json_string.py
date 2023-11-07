#!/usr/bin/python3
"""
Function to convert a JSON formatted string to a Python object.
"""


import json


def to_json_string(my_obj):
    """Python object: The Python object represented by the JSON string."""
    return json.dumps(my_obj)

