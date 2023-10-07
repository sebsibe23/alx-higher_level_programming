#!/usr/bin/python3
# 7-add_tuple.py


def add_tuple(firstelement=(), secondelement=()):
    if len(firstelement) < 2:
        if len(firstelement) == 0:
            firstelement = 0, 0
        else:
            firstelement = firstelement[0], 0
    if len(secondelement) < 2:
        if len(secondelement) == 0:
            secondelement = 0, 0
        else:
            secondelement = secondelement[0], 0

    return (firstelement[0] + secondelement[0], firstelement[1] + secondelement[1])
