#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
