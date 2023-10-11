#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    strnew_dir = a_dictionary.copy()
    var_list_keys = list(strnew_dir.keys())
    for h in var_list_keys:
        strnew_dir[h] *= 2
    return (strnew_dir)
