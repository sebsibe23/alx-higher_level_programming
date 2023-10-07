#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for d in row:
            print("{:d}".format(d), end=" " if d != row[-1] else "")
        print()
