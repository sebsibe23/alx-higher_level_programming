#!/usr/bin/python3
# 5-no_c.py
def no_c(my_string):
    copy = [k for k in my_string if k != 'c' and k != 'C']
    return ("".join(copy))
