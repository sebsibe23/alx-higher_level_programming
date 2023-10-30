#!/usr/bin/python3
"""Module for task 1 of project 0x08.
"""

class Rectangle:
    """A class that defines a rectangle by its `width` and `height`.

    Args:
        width (int): Width of the rectangle, defaults to 0.
        height (int): Height of the rectangle, defaults to 0.

    """
    def __init__(self, width=0, height=0):
        """
        Constructs a Rectangle instance with optional `width` and `height`.

        Args:
            width (int): Width of the rectangle. Defaults to 0.
            height (int): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the value of `width`.

        Returns:
            int: The value of `width`.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of `width`.

        Args:
            value (int): The new value of `width`.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the value of `height`.

        Returns:
            int: The value of `height`.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of `height`.

        Args:
            value (int): The new value of `height`.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

