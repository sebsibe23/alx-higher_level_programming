#!/usr/bin/python3
"""Rectangle Class, built for a Python project.
"""

class Rectangle:
    """Rectangle Class, built for a Python project."""

    instance_count = 0
    symbol = "#"
    color = "white"
    material = "wood"

    def __init__(self, width=0, height=0, color="white", material="wood"):
        """Initializes a new Rectangle instance and increments `instance_count`."""
        type(self).instance_count += 1
        self.width = width
        self.height = height
        self.color = color
        self.material = material

    @property
    def width(self):
        """Getter for `width`."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for `width`."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for `height`."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for `height`."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def _draw_rectangle(self):
        """Creates a string representation of the rectangle using '#' characters."""
        string = ""
        for row in range(self.height):
            for col in range(self.width):
                string += self.symbol
            if self.width != 0 and row < (self.height - 1):
                string += "\n"
        return string

    def __str__(self):
        """Allows direct printing of instances by returning a string representation of the rectangle."""
        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval() by returning a string that recreates the instance when evaluated."""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @classmethod
    def __del__(cls):
        """Decrements `instance_count` and prints a message upon deletion of an instance."""
        cls.instance_count -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two Rectangle instances and returns the one with the larger area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

