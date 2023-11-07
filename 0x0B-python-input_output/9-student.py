#!/usr/bin/python3
"""the Student module 1"""


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

    def to_json(self):
        """
        Function to return the dictionary representation of a Student object.
        Returns:
        dict: The dictionary representation of the Student's attributes.
        """
        return self.__dict__.copy()
