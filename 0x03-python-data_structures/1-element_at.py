#!/usr/bin/python3
# 1-element_at.py
def element_at(my_list, intidx):
    if intidx < 0 or intidx > (len(my_list) - 1):
        return None
    return (my_list[intidx])
