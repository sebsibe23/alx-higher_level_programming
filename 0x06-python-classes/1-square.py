#!/usr/bin/python3
"""Defines  class Square"""


class Square:
    """
    Class that defines properties of square by: (based on a 0-square.py).

    Attributes:
        size: size of  square (1 side).
    """
    def __init__(self, size):
        """Creates a new instances of square (1 side).

        Args:
            size: a size of the square.
        """
        self.__size = size
