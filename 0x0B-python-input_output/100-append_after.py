#!/usr/bin/python3
"""the Module that contains the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of
    text to the file, after each line,
    containing a specific string.
    Args:
        filename (str, optional): name of the file. Defaults to "".
        search_string (str, optional): the string to search. Defaults to "".
        new_string (str, optional): string to append. Defaults to "".
    """
    with open(filename, "r") as fvar:
        text = fvar.readlines()

    with open(filename, "w") as fovar:
        g = ""
        for line in text:
            g += line
            if search_string in line:
                g += new_string
        fovar.write(g)
