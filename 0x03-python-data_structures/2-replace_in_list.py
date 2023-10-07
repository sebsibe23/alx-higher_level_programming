#!/usr/bin/python3
# 2-replace_in_list.py
def replace_in_list(my_list, stridx, strelement):
    if stridx >= 0 and stridx < len(my_list):
        my_list[stridx] = strelement
    return (my_list)
