#!/usr/bin/python3
"""Rectangle Class, built for a Python project.
"""

class Rectangle:
    """Class for creating, computing dimensions, and visualizing a rectangle.

    This class accepts arguments for the width and height of a rectangle, and contains methods
    for calculating the area or perimeter. It also includes methods for string representation,
    instance recreation, and instance deletion.

    Attributes:
        count (int): Counter that increments for every new instance and decrements for every deleted instance.
        symbol (str): Character used in visualizing the rectangle.

    """
    count = 0
    symbol = '#'

    def __init__(self, w=0, h=0):
        """Initializes a new Rectangle instance and increments `count`.

        Args:
            w (int): Width of the rectangle, defaults to 0.
            h (int): Height of the rectangle, defaults to 0.

        """
        type(self).count += 1
        self.w = w
        self.h = h

    @property
    def w(self):
        """Getter for `w`.

        Returns:
            w (int): Width of the rectangle.

        """
        return self.__w

    @w.setter
    def w(self, value):
        """Setter for `w`.

        Args:
            value (int): Width of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__w = value

    @property
    def h(self):
        """Getter for `h`.

        Returns:
            h (int): Height of the rectangle.

        """
        return self.__h

    @h.setter
    def h(self, value):
        """Setter for `h`.

        Args:
            value (int): Height of the rectangle.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__h = value

    def area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            Area of the rectangle: w * h

        """

       return self.__w * self.__h

   def perimeter(self):
       """Calculates and returns the perimeter of the rectangle.

       Returns:
           Perimeter of the rectangle: (w * 2) + (h * 2), or 0 if either attribute is 0.

       """

       if self.__w is 0 or self.__h is 0:
           return 0
       else:
           return (self.__w * 2) + (self.__h * 2)

   def _draw_rectangle(self):
       """Creates a string representation of the rectangle using '#' characters.

       Returns:
           String representation of the rectangle suitable for printing.

       """

      str = ""
      for row in range(self.__h):
          for col in range(self.__w):
              str += "{}".format(self.symbol)
          if self.__w != 0 and row < (self.__h - 1):
              str += '\n'
      return str

  def __str__(self):
      """Allows direct printing of instances by returning a string representation of the rectangle.

       Returns:
           The output of _draw_rectangle().

       """

      return self._draw_rectangle()

  def __repr__(self):
      """Allows use of eval() by returning a string that recreates the instance when evaluated.

       Returns:
           A string that recreates the instance when evaluated.

       """

      return "Rectangle({:d}, {:d})".format(self.__w, self.__h)

  @classmethod
   def __del__(cls):
       """Decrements `count` and prints a message upon deletion of an instance.

       """

      cls.count -= 1
      print('Bye rectangle...')

   @staticmethod
   def bigger_or_equal(rect_1, rect_2):
       """Compares the area of two Rectangle instances and returns the one with the larger area.

       Args:
           rect_1 (Rectangle object): First instance to be compared.
           rect_2 (Rectangle object): Second instance to be compared.

       Raises:
           TypeError: If `rect_1` or `rect_2` is not an instance of Rectangle.

       Returns:
           The Rectangle instance with the larger area, or `rect_1` if the areas are equal.

       """

      if not isinstance(rect_1, Rectangle):
          raise TypeError('rect_1 must be an instance of Rectangle')
      if not isinstance(rect_2, Rectangle):
          raise TypeError('rect_2 must be an instance of Rectangle')
      if rect_1.area() >= rect_2.area():
          return rect_1
      else:
          return rect_2

