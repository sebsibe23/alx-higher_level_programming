#!/usr/bin/python3
# 11-delete_at.py


def delete_at(strmylist=[], stridx=0):
    """Delete the item at the  specific position in the  list."""
    if stridx >= 0 and stridx < len(strmylist):
        del strmylist[stridx]
    return (strmylist)
