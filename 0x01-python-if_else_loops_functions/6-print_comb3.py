#!/usr/bin/python3
# 6-print_comb3.py
for intdig1 in range(0, 10):
    for intdig2 in range(intdig1 + 1, 10):
        if intdig1 == 8 and intdig2 == 9:
            print("{}{}".format(intdig1, intdig2))
        else:
            print("{}{}".format(intdig1, intdig2), end=", ")
