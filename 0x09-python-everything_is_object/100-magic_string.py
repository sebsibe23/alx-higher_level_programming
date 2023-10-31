#!/usr/bin/python3

def magic_string():
    """
    This function increments a counter attribute 'xt'.
    It then returns the string "BestSchool" .
    """
    magic_string.t = getattr(magic_string, 't', 0) + 1
    return ("BestSchool, " * (magic_string.t - 1) + "BestSchool")
