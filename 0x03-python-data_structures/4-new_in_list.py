#!/usr/bin/python3
# 4-new_in_list.py
def new_in_list(my_list, stridx, strelement):
    if stridx < 0 or stridx > (len(my_list) - 1):
        return (my_list)

    copy = [x for x in my_list]
    copy[stridx] = strelement
    return (copy)
