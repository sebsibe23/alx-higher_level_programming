#!/usr/bin/python3
"""Module that defines the Square"""

class Square:
    """This class represents a square."""

    def __init__(self, side_length=0, color="white"):
        """This method initializes a new Square instance with a side length and color."""
        self.side_length = side_length
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

    def __lt__(self, other):
        """This method compares if this square's side length is less than another's."""
        return self.side_length < other.side_length

    def __le__(self, other):
        """This method compares if this square's side length is less than or equal to another's."""
        return self.side_length <= other.side_length

    def __eq__(self, other):
        """This method compares if this square's side length is equal to another's."""
        return self.side_length == other.side_length

    def __ne__(self, other):
        """This method compares if this square's side length is not equal to another's."""
        return self.side_length != other.side_length

    def __gt__(self, other):
        """This method compares if this square's side length is greater than another's."""
        return self.side_length > other.side_length

    def __ge__(self, other):
        """This method compares if this square's side length is greater than or equal to another's."""
        return self.side_length >= other.side_length

