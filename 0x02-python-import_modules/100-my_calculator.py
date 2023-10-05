#!/usr/bin/python3
#tells the system this script is a Python3 script

if __name__ == "__main__":


    import sys


    from calculator_1 import add, sub, mul, div
    # Importing specific functions from a module named calculator_1

    argv = sys.argv[1:]
    # Getting command line arguments excluding the script name itself

    argv_count = len(argv)
    # Counting the number of command line arguments

    operators = ["+", "-", "*", "/"]
    # Defining a list of valid operators

    if argv_count != 3:
        # Checking if the number of arguments is not equal to 3
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        # If not, print usage format and...
        exit(1)
        # ...exit with status code 1

    elif sys.argv[2] not in operators:
        # Checking if the operator provided
        #is not in the list of valid operators
        print("Unknown operator. Available operators: +, -, * and /")
        # If not, print error message and...
        exit(1)
        # ...exit with status code 1

    else:
        # If number of arguments is 3 and operator is valid
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        # Convert arguments to integers

        if sys.argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            # If operator is '+', call add function and print result

        elif sys.argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            # If operator is '-', call sub function and print result

        elif sys.argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            # If operator is '*', call mul function and print result

        elif sys.argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
