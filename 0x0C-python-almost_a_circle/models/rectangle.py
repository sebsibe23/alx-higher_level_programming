#!/usr/bin/python3
'''
Module for Rectangle class.
This module contains the Rectangle
class that inherits from the Base class.
'''


from models.base import Base


class Rectangle(Base):
    '''
    A Rectangle class that inherits from the
    Base class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle.
        Default is 0.
        y (int): The y-coordinate of the rectangle.
        Default is 0.
        id (int): The id of the rectangle.
        Default is None.
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Constructor for the Rectangle class.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            Default is 0.
            y (int): The y-coordinate of the rectangle.
            Default is 0.
            id (int): The id of the rectangle.
            Default is None.
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Getter for the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Setter for the width of the rectangle.

        Parameters:
            value (int): The new width of the rectangle.
        '''
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        '''
        Getter for the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for the height of the rectangle.

        Parameters:
            value (int): The new height of the rectangle.
        '''
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        '''
        Getter for the x-coordinate of the rectangle.

        Returns:
            int: The x-coordinate of the rectangle.
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter for the x-coordinate of the rectangle.

        Parameters:
            value (int): The new x-coordinate
            of the rectangle.
        '''
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        '''
        Getter for the y-coordinate of the rectangle.

        Returns:
            int: The y-coordinate of the rectangle.
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter for the y-coordinate of the rectangle.

        Parameters:
            value (int): The new y-coordinate
            of the rectangle.
        '''
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''
        Method for validating the value.

        Parameters:
            name (str): The name of the attribute.
            value (int): The value of the attribute.
            eq (bool): A flag to determine if the
            value can be equal to zero. Default is True.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less
            than (or equal to, depending on eq) zero.
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        '''
        Computes the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        '''
        return self.width * self.height

    def display(self):
        '''
        Prints the string representation of the rectangle.

        The rectangle is represented by '#'
        characters for its width and height,
        ' ' characters for its x-coordinate, and '\n'
        characters for its y-coordinate.
        '''
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        '''
        Returns the string info about the rectangle.

        Returns:
            str: A string in the format
            '[Rectangle] (id) x/y - width/height'.
        '''
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''
        Internal method that updates instance
        attributes via */**args.

        Parameters:
            id (int): The new id of the rectangle. Default is None.
            width (int): The new width of the rectangle.
            Default is None.
            height (int): The new height of the rectangle.
            Default is None.
            x (int): The new x-coordinate of the rectangle.
            Default is None.
            y (int): The new y-coordinate of the rectangle.
            Default is None.
        '''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''
        Updates instance attributes via no-keyword
        & keyword args.

        Parameters:
            *args: Non-keyword arguments.
            **kwargs: Keyword arguments.
        '''
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''
        Returns the dictionary representation of this class.

        Returns:
            dict: A dictionary with keys "id", "width",
            "height", "x", and "y", and their corresponding
            values from the instance.
        '''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
