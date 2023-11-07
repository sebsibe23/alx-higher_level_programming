#!/usr/bin/python3
"""
the Student Class module
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
        Constructor to initialize a Student object.

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
        Public method to retrieve a dictionary representation
        of a Student instance.

        Parameters:
        attrs (list): A list of attribute names to include in the dictionary.
                      If not provided or if not a list of strings,
                      all attributes are included.

        Returns:
        dict: A dictionary representation of the Student's attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(w, str) for w in attrs)):
            return {w: getattr(self, w) for w in attrs if hasattr(self, w)}
        return self.__dict__
