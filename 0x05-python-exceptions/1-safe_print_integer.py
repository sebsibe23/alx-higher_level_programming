def safe_print_integer(value):
    """
    a function prints the value as an integer with "{:d}".format().

    Parameters:
    value: a value to be printed. It can be of any type.

    Returns:
    bool: True if value has been correctly printed
    (it means the value is integer),
    otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
