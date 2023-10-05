#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    intstra = 10
    intstrb = 5
    print("{} + {} = {}".format(intstra, intstrb, add(intstra, intstrb)))
    print("{} - {} = {}".format(intstra, intstrb, sub(intstra, intstrb)))
    print("{} * {} = {}".format(intstra, intstrb, mul(intstra, intstrb)))
    print("{} / {} = {}".format(intstra, intstrb, div(intstra, intstrb))
