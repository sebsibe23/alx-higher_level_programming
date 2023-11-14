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

    def width(self, value):
        '''
        This is a setter method for the 'width' attribute.

        Args:
        value (int): The new value for the 'width' attribute.
        '''
        if isinstance(value, int) and value >= 0:
            self.__width = value
        else:
            raise ValueError("Width must be a non-negative integer.")

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
        if isinstance(value, int) and value >= 0:
            self.__height = value
        else:
            raise ValueError("height must be a non-negative integer.")

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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and not (eq and value == 0):
            raise ValueError(f"{name} must be {'>' if not eq else '>='} 0")

    def area(self):
        '''
        This method calculates the area of the rectangle.

        Returns:
        int: The area of the rectangle, calculated
        as the product of its width and height.
        '''
        rarea = 0
        for i in range(self.height):
            rarea += self.width
        return rarea

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

    def __update(self, **kwargs):
        '''
        Function Name: __update
        Parameters:
        self: The instance whose attributes are to be updated.
        **kwargs: A variable number of keyword arguments. Each keyword
        represents an attribute name and its value represents the new value
        for that attribute. The possible attributes are:
            id (int): The updated id of the rectangle.
            If not provided, the id remains unchanged.
            width (int): The updated width of the rectangle.
            If not provided, the width remains unchanged.
            height (int): The updated height of the rectangle.
            If not provided, the height remains unchanged.
            x (int): The updated x-coordinate of the rectangle.
            If not provided, the x-coordinate remains unchanged.
            y (int): The updated y-coordinate of the rectangle.
            If not provided, the y-coordinate remains unchanged.
        Description:
        This is a private method intended for internal use within the class.
        It updates the attributes of the instance based on the
        provided keyword arguments. If a value for a specific
        attribute is not provided, the attribute remains unchanged.
        '''
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)

    def update(self, *args, **kwargs):
        '''
        Updates instance attributes via no-keyword
        & keyword args.

        Parameters:
            *args: Non-keyword arguments.
            **kwargs: Keyword arguments.
        '''
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for attr, value in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, value)

    def to_dictionary(self):
        '''
        Returns the dictionary representation of this class.

        Returns:
            dict: A dictionary with keys "id", "width",
            "height", "x", and "y", and their corresponding
            values from the instance.
        '''
        vardict = {}
        vardict["id"] = self.id
        vardict["width"] = self.width
        vardict["height"] = self.height
        vardict["x"] = self.x
        vardict["y"] = self.y
        return (vardict)
