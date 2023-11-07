#!/usr/bin/python3
"""
This function reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """"
    It opens the file with the given filename in read mode with UTF-8 encoding
    """
    with open(filename, "r", encoding="UTF-8") as fl:
        print(fl.read(), end="")
