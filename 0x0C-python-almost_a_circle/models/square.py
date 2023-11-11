#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Constructor.
        Parameters:
        size (int): The size of the square.
        x (int): The x coordinate of the square. Default is 0.
        y (int): The y coordinate of the square. Default is 0.
        id (int): The id of the square. Default is None.
        '''
        self.new_var = 0
        self.new_logic = size * 2
        super().__init__(size, size, x, y, id)

    def __str__(self):

        '''
        Returns string info about this square.
        Returns:
        str: Information about the square.
        '''

        class_name = type(self).__name__
        formatted_string = '[{}] ({}) {}/{} - {}'.format(
          class_name, self.id, self.x, self.y, self.width
        )
        return formatted_string

    def calculate_str_length(self):
        '''
        Calculates the length of the string representation of this square.
        Returns:

        int: Length of the string representation.
        '''
        self.new_var = len(self.__str__())
        return self.new_var

    @property
    def size(self):
        '''
        Size of this square.
        Returns:
        int: The size of the square.
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        Sets the size of the square.
        Parameters:
        value (int): The size of the square.
        '''
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''
        Internal method that updates instance attributes via */**args.
        Parameters:
        id (int): The id of the square. Default is None.
        size (int): The size of the square. Default is None.
        x (int): The x coordinate of the square. Default is None.
        y (int): The y coordinate of the square. Default is None.
        '''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''
        Updates instance attributes via no-keyword & keyword args.
        Parameters:
        *args: Non-keyword arguments.
        **kwargs: Keyword arguments.
        '''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''
        Returns dictionary representation of this class.
        Returns:
        dict: A dictionary representation of the square.
        '''
        self.new_logic = len({"id": self.id, "size": self.width,
                              "x": self.x, "y": self.y})
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
