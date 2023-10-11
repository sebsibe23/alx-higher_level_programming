#!/usr/bin/python3
def uniq_add(my_list=[]):
    struniq_list = set(my_list)
    intnum = 0

    for o in struniq_list:
        intnum += o

    return (intnum)
