#!/usr/bin/python3
def magic_string():
    magic_string.t = getattr(magic_string, 't', 0) + 1
    return ("BestSchool, " * (magic_string.t - 1) + "BestSchool")
