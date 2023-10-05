#!/usr/bin/python3

if __name__ == "__main__":
    """Print a number of and list of arguments."""
    import sys

    strcount = len(sys.argv) - 1
    if strcount == 0:
        print("0 arguments.")
    elif strcount == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(strcount))
    for i in range(strcount):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
