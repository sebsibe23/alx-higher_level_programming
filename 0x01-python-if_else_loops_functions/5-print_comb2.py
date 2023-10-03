#!/usr/bin/python3
for strnum in range(0, 100):
    if strnum == 99:
        print("{}".format(strnum))
    else:
        print("{:02}".format(strnum), end=", ")
