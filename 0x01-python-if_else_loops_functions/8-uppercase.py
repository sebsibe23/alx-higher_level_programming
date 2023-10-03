#!/usr/bin/python3
# 8-uppercase.py
def uppercase(upcstr):
    for strc in upcstr:
        if ord(strc) >= 97 and ord(strc) <= 122:
            strc = chr(ord(strc) - 32)
        print("{}".format(strc), end="")
    print("")
