#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represent a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
