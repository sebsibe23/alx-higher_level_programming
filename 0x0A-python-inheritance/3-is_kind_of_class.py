#!/usr/bin/python3
"""
This script defines a class and inherited
class-checking function.

Function:
- is_kind_of_class(obj: any, a_class: type) -> bool
    Check if an object is an instance or inherited instance of a class.

Parameters:
- obj (any): The object to check.
- a_class (type): The class to match the type of obj to.

Returns:
- bool: If obj is an instance or inherited instance
of a_class - True. Otherwise - False.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance
    of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
