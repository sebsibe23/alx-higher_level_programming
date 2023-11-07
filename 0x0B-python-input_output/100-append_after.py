#!/usr/bin/python3
"""
Module that contains the function append_after
Function:
    append_after(filename: str = "",
    search_string: str = "", new_string: str = "") -> None

Description:
    This function inserts a line of text to a file,
    after each line containing a specific string.

Parameters:
    filename (str, optional): The name of the file
    to be modified. Defaults to "".
    search_string (str, optional): The string to be
    searched in each line of the file. Defaults to "".
    new_string (str, optional): The string to be
    appended after each line that contains the
    search_string. Defaults to "".
Returns:
    None. The function modifies the file in-place.
"""


def append_after(filename="", search_string="", new_string=""):
    with open(filename, "r") as varfilename:
        text = varfilename.readlines()

    with open(filename, "w") as strfilename:
        d = ""
        for varline in text:
            d += varline
            if search_string in varline:
                d += new_string
        strfilename.write(d)
