#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Module for task 1 of project 0x08.
"""


class Rectangle:

    """A class that defines a rectangle by its `side1` and `side2`.

    Args:
        side1 (int): One side of the rectangle, defaults to 0.
        side2 (int): The other side of the rectangle, defaults to 0.

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, side1=0, side2=0):
        """
        Constructs a Rectangle instance with optional `side1` and `side2`.

        Args:
            side1 (int): One side of the rectangle. Defaults to 0.
            side2 (int): The other side of the rectangle. Defaults to 0.
        """

        type(self).number_of_instances += 1
        self.side1 = side1
        self.side2 = side2

    @property
    def side1(self):
        """
        Retrieves the value of `side1`.

        Returns:
            int: The value of `side1`.
        """

        return self.__side1

    @side1.setter
    def side1(self, value):
        """
        Sets the value of `side1`.

        Args:
            value (int): The new value of `side1`.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """

        if type(value) is not int:
            raise TypeError('side1 must be an integer')
        elif value < 0:
            raise ValueError('side1 must be >= 0')
        self.__side1 = value

    @property
    def side2(self):
        """
        Retrieves the value of `side2`.

        Returns:
            int: The value of `side2`.
        """

        return self.__side2

    @side2.setter
    def side2(self, value):
        """
        Sets the value of `side2`.

        Args:
            value (int): The new value of `side2`.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """

        if type(value) is not int:
            raise TypeError('side2 must be an integer')
        if value < 0:
            raise ValueError('side2 must be >= 0')
        self.__side2 = value

    def area(self):
        """
         Returns area of a rectangle of a given `side1` and `side2`.

         Returns:
             Area of rectangle: __width * __height
         """

        return self.__width * self.__height

    def perimeter(self):
        """
          Returns the perimeter of a rectangle of given `width` and `height`

          Returns:
              0 if either attribute is 0, or the perimeter: (__width * 2) +
          (__height * 2).
          """

    if self.__width is 0 or self.__height is 0:
        return 0
    else:
        return self.__width * 2 + self.__height * 2

    def _draw_rectangle(self):
        """Formats a string of '#' and '\n' chars to print the rectangle
         represented by the current instance.

         Attributes:
             __width (int): horizontal dimension of rectangle
             __height (int): vertical dimension of rectangle
             str (str): string to constructed for return

         Returns:
             str (str): string suitable for printing rectangle (final newline
                 omitted)

         """

        str = ''
        for row in range(self.__height):
            for col in range(self.__width):
                str += '{}'.format(self.print_symbol)
            if self.__width != 0 and row < self.__height - 1:
                str += '\n'
        return str

    def __str__(self):
        """Allows direct printing of instances.

         Returns:
             The output of _draw_rectangle, which creates a string
         representation of the rectangle suitable for printing.

         """

        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval().

         Returns:
             A string of the code needed to create the instance.

         """

        return 'Rectangle({:d}, {:d})'.format(self.__width,
                self.__height)

        @classmethod
    def __del__(cls):
        """Decrements `number_of_instances`, then prints message upon
         deletion of instance.

         """

        cls.number_of_instances -= 1
        print ('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two instances and returns the larger of the two.

         Args:
             rect_1 (Rectangle object): first instance to be compared
             rect_2 (Rectangle object): second instance to be compared

         Raises:
             TypeError: if `rect_1` or `rect_2` is not an instance of cls.

         Returns:
             `rect_1` if `rect_1` has an area larger than or equal to `rect_2`,
         or `rect_2` if it has the larger area

         """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

