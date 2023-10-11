#!/usr/bin/python3
def number_keys(a_dictionary):
    intnum = 0
    intlist_keys = list(a_dictionary.keys())

    for i in intlist_keys:
        intnum += 1

    return (intnum)
