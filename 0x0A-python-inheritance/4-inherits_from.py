#!/usr/bin/python3
"""
Module: inherits_from
=====================

This module contains a function `inherits_from` that checks
 if an object is an instance of a class that inherited from
 a specified class.

Function:
---------
def inherits_from(obj, a_class):
    '''
    Method to check if an object is an instance of a class
    that inherited from a specified class.

    Parameters:
    -----------
    obj : object
        The object to check.
    a_class : class
        The class to check against.

    Returns:
    --------
    bool
        True if `obj` is an instance of a class that
        inherited from `a_class`, False otherwise.
    '''
    return False if type(obj) is a_class else isinstance(obj, a_class)
"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
