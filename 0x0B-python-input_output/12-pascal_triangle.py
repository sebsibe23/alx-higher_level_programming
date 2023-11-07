#!/usr/bin/python3
"""
This module defines the pascal_triangle function.

Functions:
    pascal_triangle(n): Generates the first
    n rows of Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generates the first n rows of Pascal's Triangle.

    Parameters:
        n (int): The number of rows of Pascal's
        Triangle to generate.

    Returns:
        list: A list of lists representing the first
        n rows of Pascal's Triangle.
    """
    var_li = []
    if n <= 0:
        return var_li
    for r in range(n):
        for s in range(r + 1):
            if s == 0:
                var_li.append([1])
            elif s == r:
                var_li[r].append(1)
            else:
                var_li[r].append(var_li[r - 1][s] + var_li[r - 1][s - 1])
    return var_li
