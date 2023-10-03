#!/usr/bin/python3
# 101-remove_char_at.py
def remove_char_at(chrstr, b):
    if b < 0:
        return (chrstr)
    return (chrstr[:b] + chrstr[b+1:])
