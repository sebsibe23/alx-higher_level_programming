#!/usr/bin/python3
"""Defines a class Square"""



class Square:
    """This class represents a square."""

    def __init__(self, side_length=0, offset=(0, 0), color="white"):
        """This method initializes a new Square instance with side length, offset position, and color."""
        self.side_length = side_length
        self.offset = offset
        self.color = color

    @property
    def side_length(self):
        """This property gets or sets the side length of the square."""
        return self.__side_length

    @side_length.setter
    def side_length(self, value):
        """This setter ensures that the side length is an integer and is not less than 0."""
        if not isinstance(value, int):
            raise TypeError("side_length must be an integer")
        if value < 0:
            raise ValueError("side_length must be >= 0")
        self.__side_length = value

    @property
    def offset(self):
        """This property gets or sets the offset position of the square."""
        return self.__offset

    @offset.setter
    def offset(self, value):
        """This setter ensures that the offset is a tuple of two positive integers."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(v, int) and v >= 0 for v in value):
                    raise TypeError("offset must be a tuple of 2 positive integers")
        self.__offset = value

    @property
    def color(self):
        """This property gets or sets the color of the square."""
        return self.__color

    @color.setter
    def color(self, value):
        """This setter ensures that the color is a string."""
        if not isinstance(value, str):
            raise TypeError("color must be a string")
        self.__color = value

    def area(self):
        """This method calculates and returns the area of the square."""
        return self.side_length ** 2

    def my_print(self):
        """This method prints the square at its offset position with '#'."""
        print("\n" * self.offset[1], end="")
        print("\n".join(" " * self.offset[0] + "#" * self.side_length for _ in range(self.side_length)))

    def __str__(self):
        """This method returns a string representation of the square."""
        if self.side_length == 0:
            return ""
        lines = [" " * self.offset[0] + "#" * self.side_length for _ in range(self.side_length)]
        return "\n" * self.offset[1] + "\n".join(lines)

