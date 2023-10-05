#!/usr/bin/python3

if __name__ == "__main__":
    """Print a difference, sum, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    f = 10
    t = 5

    print("{} + {} = {}".format(f, t, add(f, t)))
    print("{} - {} = {}".format(f, t, sub(f, t)))
    print("{} * {} = {}".format(f, t, mul(f, t)))
    print("{} / {} = {}".format(f, t, div(f, t)))
