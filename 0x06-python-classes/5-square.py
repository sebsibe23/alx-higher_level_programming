i#!/usr/bin/python3
"""Module that defines a class Square"""

class Square:
    """A class that encapsulates the concept of a square.

    Attributes:
        __size (int): The length of one side of the square.
    """

    def __init__(self, size=0):
        """Constructor for the Square class.

        Args:
            size (int): The length of one side of the square. Defaults to 0.
        """
        self.__size = size

    def area(self):
        """Method to compute the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints a visual representation of the square with the '#' character.

        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))
