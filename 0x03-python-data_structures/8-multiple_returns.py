#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(strsent):
    """Returns a length of the  string and its first character from strsent."""
    if strsent == "":
        return (0, None)
    return (len(strsent), strsent[0])
