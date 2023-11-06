#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""

class MyInt(int):
    """
    Invert int operators == and !=.

    Attributes:
        real (int): The integer value.
    """

    def __eq__(self, value):
        """
        Override == operator with != behavior.

        Args:
            value (int): The value to compare with.

        Returns:
            bool: True if self and value are not equal, False otherwise.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Override != operator with == behavior.

        Args:
            value (int): The value to compare with.

        Returns:
            bool: True if self and value are equal, False otherwise.
        """
        return self.real == value

