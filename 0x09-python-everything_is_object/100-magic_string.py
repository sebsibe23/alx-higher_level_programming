#!/usr/bin/python3
def magic_string():
    """
    Function Name: magic_string
    Parameters: None

    This function returns a string "BestSchool" repeated n times, where n is the number of times the function has been called. 
    It uses a counter attribute on the function object itself to keep track of the number of times it has been called.
    """
    magic_string.counter = getattr(magic_string, 'counter', -1) + 1
    return ", ".join(["BestSchool"] * (magic_string.counter + 1))

