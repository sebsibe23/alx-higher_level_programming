#!/usr/bin/python3
"""Rectangle class for a Python project.
"""

class Rectangle:
    """Defines a rectangle with width and height.

    Args:
        width (int): The width of the rectangle, defaults to 0.
        height (int): The height of the rectangle, defaults to 0.

    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Generates a string representation of the rectangle using '#'. """
        
        if self.__width == 0 or self.__height == 0:
            return ""
        
        str_representation = ""
        
        for _ in range(self.__height):
            str_representation += "#" * self.__width + "\n"
        
        return str_representation.rstrip() # remove trailing newline

    def __repr__(self):
        """Generates a string representation of the code needed to create the rectangle instance."""
        
        return "Rectangle({}, {})".format(self.__width, self.__height)

