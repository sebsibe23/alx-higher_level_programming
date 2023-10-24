#!/usr/bin/python3
"""Module that defines a class Square"""


class Square:
    """
    Class that encapsulates properties of square by: (based on 3-square.py).

    Attributes:
        size: The length of one side of the square.
    """
    def __init__(self, size=0):
        """Constructor for the Square class.

        Args:
            size: The length of one side of the square. Defaults to 0.
        """
        self.__size = size

    def area(self):
        """Method to compute the area of the square.

        Returns: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Getter for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
