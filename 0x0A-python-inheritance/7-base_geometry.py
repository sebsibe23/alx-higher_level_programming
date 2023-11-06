#!/usr/bin/python3
"""
This module defines the BaseGeometry class.

Classes:
    BaseGeometry: Represents the concept of a geometric object.
"""


class BaseGeometry:
    """
    A class used to represent the concept of a geometric object.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    area(self):
        Raises an Exception with the message "area() is not implemented".

    integer_validator(self, name, value):
        Validates that 'value' is a positive integer.

        Parameters:
            name (str): The name of the parameter.
            value (int): The value of the parameter.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
    """
    def area(self):
        """Raises an Exception with the message "area() is not implemented"."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
