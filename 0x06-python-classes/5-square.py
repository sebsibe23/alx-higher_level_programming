#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines a properties of square by: 
    (based on 4-square.py).

    Attributes:
        size: a size of a square (1 side).
        perimeter: a perimeter of a square.
    """
    def __init__(self, size=0):
        """
        Function name: __init__
        Parameters: 
            size (int): a size of a square (1 side).
        Description: Creates new instances of square.
        """
        self.__size = size
        self.__perimeter = self.__size * 4

    def area(self):
        """
        Function name: area
        Parameters: None.
        Description: Calculates a area of square.
        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Function name: size (getter)
        Parameters: None
        Description: Returns a size of a square.
        Returns: the current size of a square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Function name: size (setter)
        Parameters:
            value (int): a new size of a square (1 side).
        Description: Property setter for size.
        Updates a size and perimeter of the square.
        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            self.__perimeter = self.__size * 4

    @property
    def perimeter(self):
        """
        Function name: perimeter (getter)
        Parameters: None
        Description: Returns the perimeter of a square.
        Returns: the current perimeter of the square.
        """
        return self.__perimeter

    def my_print(self):
        """prints in stdout the square with the character #

         Function name: my_print
         Parameters: None
         Description: Prints in stdout a square with the character #.
         If size is 0, prints an empty line.
         Returns: None
         """

         if self.__size == 0:
             print()
         for i in range(self.__size):
             print("#" * (self.__size))
