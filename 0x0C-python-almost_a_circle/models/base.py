#!/usr/bin/python3
'''
Module for Base class.
This module contains the Base class which is used
to handle operations related to JSON and CSV files.
    - json_to_csv(json_file: str, csv_file: str) -> None
        Converts a JSON file to a CSV file.
        Parameters:
            json_file (str): The path to the input JSON file.
            csv_file (str): The path to the output CSV file.
        Returns:
            None

    - csv_to_json(csv_file: str, json_file: str) -> None
        Converts a CSV file to a JSON file.
        Parameters:
            csv_file (str): The path to the input CSV file.
            json_file (str): The path to the output JSON file.
        Returns:
            None
'''
from json import dumps, loads
import csv


class Base:
    '''

    A representation of the base of our OOP hierarchy.
    This class serves as the base class in
    our object-oriented program.
    It keeps track of the number of objects created and
    assigns a unique id to each object.
    Attributes:
        __nb_objects (int): A private class attribute that
        keeps track of the number of objects created.
        id (int): A public instance attribute that
        stores the unique id of an object.

    Methods:
        __init__(self, id=None) -> None:
            Constructor method to initialize an object of this class.
            Parameters:
                id (int, optional): The id to assign to the object.
                If not provided, the object is
                assigned a unique id. Defaults to None.
            Returns:
                None
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Constructor method to initialize an object
        of this class.
        Parameters:
        id (int, optional): The id to assign to the object.
        If not provided, the object is assigned a unique id.
        Defaults to None.
        Returns:
        None
        A private class attribute that keeps
        track of the number of objects created.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Jsonifies a dictionary so it's quite
        rightly and longer.

         This static method converts a list of
         dictionaries into
         a JSON string. If the list is empty or None,
         it returns an empty JSON array string.

        Parameters:
        list_dictionaries (list): The list of
        dictionaries to jsonify.
        If the list is empty or None, an empty
        JSON array string is returned.

        Returns:
        str: The JSON string representation of the list
        of dictionaries.
        '''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''
        Jsonifies a dictionary so it's quite
        rightly and longer.

        This static method converts a list of
        dictionaries into
        a JSON string. If the list is empty or
        None, it returns
        an empty JSON array string.

        Parameters:
        list_dictionaries (list): The list of
        dictionaries to jsonify.
        If the list is empty or None,
        an empty JSON array string is returned.

        Returns:
        str: The JSON string representation
        of the list of dictionaries.
        '''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Saves jsonified object to file.

        This method takes a list of objects and a class name,
        converts the objects to a dictionary, jsonifies the dictionary,
        and saves it to a file. The file is named after the class and has a .
        json extension.
        Parameters:
        cls (str): The name of the class. The method creates a file with
        this name and a .json extension.
        list_objs (list): The list of objects to jsonify and save to file.
        If the list is None, an empty list is saved to file.
        Returns:
        None
        '''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        '''
        Loads string from file and unjsonifies.

        This class method reads a JSON string from a file,
        converts it into a list of dictionaries, and then
        creates objects from these dictionaries. The file is
        named after the class and has a .json extension.
        If the file does not exist, an empty list is returned.

        Parameters:
        cls (str): The name of the class.
        The method reads from a file with this name and
        a .json extension.
        Returns:
        list: A list of objects created from the
        dictionaries in the JSON string. If the file
        does not exist, an empty list is returned.
        '''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        '''
        Loads instance from dictionary.

        This class method creates an instance of
        a class from a dictionary. The class is determined
        by the cls parameter. If the class is Rectangle or Square,
        a new instance of that class is created and updated with the
        values from the dictionary. If the class is
        not Rectangle or Square, None is returned.

        Parameters:
        cls (str): The name of the class. The method
        creates an instance of this class.
        dictionary (dict): The dictionary to use for
        updating the instance.

        Returns:
        object: An instance of the class updated with the
        values from the dictionary. If the class is not
        Rectangle or Square, None is returned.
        '''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Saves object to csv file.

        This method takes a list of objects and a class name,
        converts the objects to a list of lists, and saves it to
        a CSV file. The file is named after the class and has a.
        csv extension. If the list is None, an empty list is saved to file.

        Parameters:
        cls (str): The name of the class.The method creates a
        file with this name and a .csv extension.
        list_objs (list): The list of objects to convert to a
        list of lists and save to file. If the list is None,
        an empty list is saved to file.

        Returns:
        None
        '''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''
        Loads object from csv file.

        This method reads a CSV file, converts each row into
        a dictionary, and then creates an object from each dictionary.
        The file is named after the class and has a .csv extension.
        If the file does not exist, an empty list is returned.

        Parameters:
        cls (str): The name of the class. The method reads from
        a file with this name and a .csv extension.

        Returns:
        list: A list of objects created from the dictionaries in the CSV file.
        If the file does not exist, an empty list is returned.
        '''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws rectangles and squares using the turtle graphics library.

        This function takes a list of rectangles and squares,
        and draws them on the screen using the turtle graphics library.
        Each rectangle or square is drawn with a random color.

        Parameters:
        list_rectangles (list): The list of rectangles to draw.
        Each rectangle is an object that has x, y, width,
        and height attributes.
        list_squares (list): The list of squares to draw.
        Each square is an object that has x, y, and size attributes.

        Returns:
        None
        """
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
