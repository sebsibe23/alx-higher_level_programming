#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """
    safe_function
        a function executes a given function safely
        with provided parameters.
        If an error occurs during the execution of
        the function, it catches the exception,
        prints an error message to stderr and returns None.
        If the function executes
        successfully, it returns the result of the function.
    Parameters:
        fct: A pointer to the function to be executed.
        args: the Variable length argument list for
        the function to be executed.
    Returns:
        a result of the function if it
        return executes successfully, otherwise None.
    """

    try:
        varfunc_result = fct(*args)
        return varfunc_result
    except Exception as error:
        varerror_message = "Exception: {}".format(sys.exc_info()[1])
        print(varerror_message, file=sys.stderr)
        return None
