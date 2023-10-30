#!/usr/bin/python3
"""1-rectangle, built for Python project task 1.
"""


class Rectangle:
    """This class creates private instance attributes by taking in four arguments.

    Args:
        width (int): The horizontal dimension of the rectangle, defaults to 0.
        height (int): The vertical dimension of the rectangle, defaults to 0.
        color (str): The color of the rectangle, defaults to "white".
        name (str): The name of the rectangle, defaults to "Rectangle".

    """
    def __init__(self, width=0, height=0, color="white", name="Rectangle"):
        # Attribute assignment here engages setters defined below
        self.width = width
        self.height = height
        self.color = color
        self.name = name

    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): The horizontal dimension of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): The horizontal dimension of the rectangle.

        Attributes:
            __width (int): The horizontal dimension of the rectangle.

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
        """__height getter.

        Returns:
            __height (int): The vertical dimension of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): The vertical dimension of the rectangle.

        Attributes:
            __height (int): The vertical dimension of the rectangle.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def color(self):
        """__color getter.

        Returns:
            __color (str): The color of the rectangle.

        """
        
        return self.__color

    @color.setter
    def color(self, value):
        
         """Args:
             value (str): The color of the rectangle.

         Attributes:
             __color (str): The color of the rectangle.

         Raises:
             TypeError: If `value` is not a str.

         """
         
         if type(value) is not str:
             raise TypeError('color must be a string')
         
         self.__color = value
    
    @property
    def name(self):
        
         """__name getter.

         Returns:
             __name (str): The name of the rectangle.

         """
        
         return self.__name
    
    @name.setter
    def name(self, value):
        
         """Args:
             value (str): The name of the rectangle.

         Attributes:
             __name (str): The name of the rectangle.

         Raises:
             TypeError: If `value` is not a str.

         """
         
         if type(value) is not str:
             raise TypeError('name must be a string')
         
         self.__name = value

