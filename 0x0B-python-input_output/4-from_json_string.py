#!/usr/bin/python3

import json


def from_json_string(my_str):
    """ the function that returns an Python data represented by a JSON """
    return json.loads(my_str)
