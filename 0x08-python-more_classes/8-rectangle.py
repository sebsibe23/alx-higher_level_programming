#!/usr/bin/python3
"""Rectangle Class, built for a Python project.
"""

class Rectangle:
    """Class for creating, computing dimensions, and visualizing a rectangle.

    This class accepts arguments for the width and height of a rectangle, and contains methods
    for calculating the area or perimeter. It also includes methods for string representation,
    instance recreation, and instance deletion.

    Attributes:
        instance_count (int): Counter that increments for every new instance and decrements for every deleted instance.
        symbol (str): Character used in visualizing the rectangle.
        color (str): Color of the rectangle, defaults to 'white'.
        material (str): Material of the rectangle, defaults to 'wood'.

    """
    instance_count = 0
    symbol = '#'
    color = 'white'
    material = 'wood'

    def __init__(self, width=0, height=0, color='white', material='wood'):
        """Initializes a new Rectangle instance and increments `instance_count`.

        Args:
            width (int): Width of the rectangle, defaults to 0.
            height (int): Height of the rectangle, defaults to 0.
            color (str): Color of the rectangle, defaults to 'white'.
            material (str): Material of the rectangle, defaults to 'wood'.

        """
        type(self).instance_count += 1
        self.width = width
        self.height = height
        self.color = color
        self.material = material

    @property
    def width(self):
        """Getter for `width`.

        Returns:
            width (int): Width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for `width`.

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
        self.__width = value

    @property
    def height(self):
        """Getter for `height`.

        Returns:
            height (int): Height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for `height`.

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
        self.__height = value
    def area(self):
        """Calculates and returns the area of the rectangle.

    Returns:
        Area of the rectangle: width * height

    """
    return self.__width * self.__height

   def perimeter(self):
    """Calculates and returns the perimeter of the rectangle.

       Returns:
           Perimeter of the rectangle: (width * 2) + (height * 2), or 0 if either attribute is 0.

       """

       if self.__width is 0 or self.__height is 0:
           return 0
       else:
           return (self.__width * 2) + (self.__height * 2)

   def _draw_rectangle(self):
       """Creates a string representation of the rectangle using '#' characters.

       Returns:
           String representation of the rectangle suitable for printing.

       """

      str = ""
      for row in range(self.__height):
          for col in range(self.__width):
              str += "{}".format(self.symbol)
          if self.__width != 0 and row < (self.__height - 1):
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

      return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

  @classmethod
   def __del__(cls):
       """Decrements `instance_count` and prints a message upon deletion of an instance.

       """

      cls.instance_count -= 1
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

