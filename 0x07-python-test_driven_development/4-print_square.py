#!/usr/bin/python3
"""Module for task 4 of project 0x07.
"""
"""
Module draw_hash_square
This module contains a function that draws a square using the '#' character.
"""

def print_square(size):
    """
    This function draws a square where size is the length and width of the square.
    The square is drawn using the '#' character.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print('#', end='')
        print()



