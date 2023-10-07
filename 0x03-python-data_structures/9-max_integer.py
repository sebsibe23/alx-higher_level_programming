#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find a biggest number of a list."""
    if len(my_list) == 0:
        return (None)

    strbiglist = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > strbiglist:
            strbiglist = my_list[i]

    return (strbiglist)
