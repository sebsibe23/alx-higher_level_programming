#!/usr/bin/python3
"""
Function to write a given text into a file.
"""


def write_file(filename="", text=""):
    """
    int: The number of characters written into the file.
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
