#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print all number of the list in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for p in my_list:
            print("{:d}".format(p))
