#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Function Name: safe_division
    Parameters:
    - a (int/float): The dividend in the division operation.
    - b (int/float): The divisor in the division operation.

    Description:
    a safely divides two numbers and prints the result.
    It handles divide by zero exceptions by setting the result to None.

    Returns:
    - div_result (int/float/None): a result of the
    division operation,
    or None if a divide by zero exception occurred.
    """

    div_result = None
    message = "Inside result: {}"

    try:
        div_result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print(message.format(div_result))

    return div_result
