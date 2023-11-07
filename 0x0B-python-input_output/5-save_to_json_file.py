#!/usr/bin/python3
"""the save to jason module"""


import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file, using a JSON"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
