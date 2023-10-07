#!/usr/bin/python3
# 7-add_tuple.py


def add_tuple(fnum=(), snum=()):
    """Add two int num."""
    if len(fnum) < 2:
        if len(fnum) == 0:
            fnum = 0, 0
        else:
            fnum = fnum[0], 0
    if len(snum) < 2:
        if len(snum) == 0:
            snum = 0, 0
        else:
            snum = snum[0], 0

    return (fnum[0] + snum[0], fnum[1] + snum[1])
