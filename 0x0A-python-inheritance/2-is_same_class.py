#!/usr/bin/python3
"""
This script defines a class-checking function.

Function:
- is_same_class(obj: any, a_class: type) -> bool
    Check if an object is exactly an instance of a given class.

Parameters:
- obj (any): The object to check.
- a_class (type): The class to match the type of obj to.

Returns:
- bool: If obj is exactly an instance of a_class - True. Otherwise - False.
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
