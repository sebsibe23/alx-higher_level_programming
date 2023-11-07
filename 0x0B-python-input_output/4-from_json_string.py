#!/usr/bin/python3
"""from json string module"""


import json


def from_json_string(my_str):
    """ a function returns an Python data represented by a JSON """
    return json.loads(my_str)
