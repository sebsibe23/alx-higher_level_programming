#!/usr/bin/python3
"""Module that defines a class Square"""

class Square:
    """A class that encapsulates the concept of a square.

    Attributes:
        __size (int): The length of one side of the square.
        __position (tuple): The position of the square in 2D space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Constructor for the Square class.

        Args:
            size (int): The length of one side of the square. Defaults to 0.
            position (tuple): The position of the square in 2D space. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If `value` is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints a visual representation of the square with the '#' character.

        If the size is 0, it prints an empty line. It also takes into account 
        the position attribute to shift the square to the right and downwards.
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#" * self.__size for _ in range(self.__size)))

