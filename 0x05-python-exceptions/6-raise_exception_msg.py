#!/usr/bin/python3
def raise_exception_msg(message=""):
    """
    raise_exception_msg
    a function raises a NameError exception with a specified message.
    Parameters:
    - message (str): a message to be included in the NameError exception.
    Returns:
    None
    """
    ex_type = NameError
    raise ex_type(message)
