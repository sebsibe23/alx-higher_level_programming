#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by:
    (based on 2-square.py).

    Attributes:
        side: a size of a square (1 side).
        perimeter: the perimeter of a square.
    """
    def __init__(self, side=0):
        """it Creates new instances of square.

        Args:
            side: the size of the square (1 side).
        """
        self.__side = side

        if not isinstance(side, int):
            raise TypeError("side must be an integer")
        elif side < 0:
            raise ValueError("side must be >= 0")
        else:
            self.__side = side
            self.__perimeter = self.__side * 4

    def area(self):
        """Calculates a area of square.

        Returns: a current square area.
        """
        return self.__side ** 2

    def perimeter(self):
        """Calculates a perimeter of square.

        Returns: a current square perimeter.
        """
        return self.__perimeter
