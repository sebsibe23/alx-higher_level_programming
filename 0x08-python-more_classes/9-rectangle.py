#!/usr/bin/python3
"""Module for task 9 of project 0x08.
"""

class Rectangle:
    """Defines a rectangle."""

    # Class attributes
    number_of_instances = 0  # Keeps track of the number of Rectangle instances
    print_symbol = "#"  # Symbol used for string representation of the rectangle

    def __init__(self, width=0, height=0):
        """Initializes the rectangle."""
        self.width = width  # Calls the width setter
        self.height = height  # Calls the height setter
        Rectangle.number_of_instances += 1  # Increments the instance count

    @property
    def width(self):
        """Gets the width."""
        return self.__width  # Returns the width

    @width.setter
    def width(self, value):
        """Sets the width."""
        if not isinstance(value, int):  # Checks if value is an integer
            raise TypeError("width must be an integer")
        if value < 0:  # Checks if value is non-negative
            raise ValueError("width must be >= 0")
        self.__width = value  # Sets the width

    @property
    def height(self):
        """Gets the height."""
        return self.__height  # Returns the height

    @height.setter
    def height(self, value):
        """Sets the height."""
        if not isinstance(value, int):  # Checks if value is an integer
            raise TypeError("height must be an integer")
        if value < 0:  # Checks if value is non-negative
            raise ValueError("height must be >= 0")
        self.__height = value  # Sets the height

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height  # Calculates and returns the area

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:  # Checks if width or height is zero
            return 0
        return 2 * (self.__width + self.__height)  # Calculates and returns the perimeter

    def __str__(self):
        """Returns the string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:  # Checks if width or height is zero
            return ""
        return (str(self.print_symbol) * self.__width + "\n") * self.__height  # Returns a string representation of the rectangle

    def __repr__(self):
        """Returns a string representation of the rectangle for reproduction."""
        return "Rectangle({}, {})".format(self.__width, self.__height)  # Returns a string that can recreate the object using eval()

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")  
        Rectangle.number_of_instances -= 1  # Decrements the instance count

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):  
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):  
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() >= rect_2.area():  
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size."""
        return cls(size, size)  

