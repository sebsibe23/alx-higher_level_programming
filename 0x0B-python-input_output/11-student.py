#!/usr/bin/python3
"""
This module defines the Student class.

Functions:
    __init__(self, first_name, last_name, age):
    Constructor for the Student class.
    to_json(self, attrs=None): Returns a dictionary
    representation of a Student instance.
    reload_from_json(self, json): Replaces attributes
    of the Student instance.
"""


class Student:
    """ The Class Student """

    def __init__(self, first_name, last_name, age):
        """
        Constructor for the Student class.

        Parameters:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
            attrs (list): A list of strings representing attribute names.
            If not provided, all attributes are used.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if not isinstance(attrs, list) or \
           not all(isinstance(k, str) for k in attrs):

            strdic = self.__dict__.copy()
        else:

            strdic = {k: self.__dict__[k] for k in attrs if k in self.__dict__}

        return strdic

    def reload_from_json(self, json):
        """
        Replaces attributes of the Student instance.

        Parameters:
            json (dict): A dictionary with attribute names as keys and
            new values for those attributes.
        """
        for k in json:
            self.__dict__[k] = json[k]
