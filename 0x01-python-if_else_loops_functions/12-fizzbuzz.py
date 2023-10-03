#!/usr/bin/python3
# 12-fizzbuzz.py
def fizzbuzz():
    for numstr in range(1, 101):
        if numstr % 3 == 0 and numstr % 5 == 0:
            print("FizzBuzz ", end="")
        elif numstr % 3 == 0:
            print("Fizz ", end="")
        elif numstr % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numstr), end="")
