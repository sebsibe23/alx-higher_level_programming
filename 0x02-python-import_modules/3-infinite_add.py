#!/usr/bin/python3
if __name__ == "__main__":
    import sys, math
    intstrresult = 0
    for i in sys.argv:
        intstrresult += int(i)
        print("{}".format(intstrresult))
