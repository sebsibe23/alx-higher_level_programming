#!/usr/bin/python3
# 100-print_tebahpla.py
f = 0
for strc in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(strc - f)), end="")
    f = 32 if f == 0 else 0
