#!/usr/bin/python3
"""Importing functions from other modules"""


import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """
    Main function to read command-line arguments and store them in a JSON file.
    """
    try:
        varjson_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        varjson_list = []

    for f in range(1, len(sys.argv)):
        varjson_list.append(sys.argv[f])
    save_to_json_file(varjson_list, "add_item.json")
