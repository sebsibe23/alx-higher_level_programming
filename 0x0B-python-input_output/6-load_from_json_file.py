#!/usr/bin/python3
""""the load_from_json_file module """


import json


def load_from_json_file(filename):
    """ the function that creates an Object from a “JSON file”"""
    with open(filename, "r", encoding='utf-8') as varf:
        return json.load(varf)
