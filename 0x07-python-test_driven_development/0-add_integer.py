#!/usr/bin/python3
"""Module for task 0 of project 0x07.
"""
def add_integer(a, b=98):
    """
    This function adds two numbers together.
    Args:
        a: The first number. Must be an integer or a float.
        b: The second number. Must be an integer or a float. Defaults to 98.
    Returns:
        The sum of a and b, as an integer.
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
