#!/usr/bin/python3
# 102-magic_calculation.py
def magic_calculation(stra, strb, strc):
    if stra < strb:
        return strc
    elif strc > strb:
        return stra + strb
    else:
        return (stra * strb) - strc
