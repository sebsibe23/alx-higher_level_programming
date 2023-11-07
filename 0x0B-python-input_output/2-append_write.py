#!/usr/bin/python3
"""
Function to append a given text into a file.
"""


def append_write(filename="", text=""):
    """
    int: The number of characters appended into the file.
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
