#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    """Prints an integer, followed by a new line.

    Args:
        value: Any type of value.

    Returns:
        True if the value has been correctly printed
        (it means the value is an integer).
        Otherwise, returns False and prints
        in stderr the error preceded by Exception:
    """

    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return False
