#!/usr/bin/python3


def magic_string():
    """
    This function returns a string "BestSchool" repeated n times,
    """
    magic_string.counter = getattr(magic_string, 'counter', -1) + 1
    return ", ".join(["BestSchool"] * (magic_string.counter + 1))

