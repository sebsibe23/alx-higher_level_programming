#!/usr/bin/python3
"""Defines a class MagicClass"""
import math

class MagicClass:
    """Represents a circle."""

    def __init__(self, radius_length=0, color="white"):
        """Initialize a new Circle instance."""
        self.radius_length = radius_length
        self.color = color

    @property
    def radius_length(self):
        """Get or set the radius length of the circle."""
        return self.__radius_length

    @radius_length.setter
    def radius_length(self, value):
        """This setter ensures that the radius length is a number."""
        if not isinstance(value, (int, float)):
            raise TypeError("radius_length must be a number")
        self.__radius_length = value

    @property
    def color(self):
        """Get or set the color of the circle."""
        return self.__color

    @color.setter
    def color(self, value):
        """This setter ensures that the color is a string."""
        if not isinstance(value, str):
            raise TypeError("color must be a string")
        self.__color = value

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius_length ** 2

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.radius_length

