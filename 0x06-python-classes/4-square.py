#!/usr/bin/python3
"""Defines a class Square"""


class Square:
  """
  Class that represents a square shape.

  Attributes:
    size: The length of one side of the square.
  """
  def __init__(self, size=0):
    """
    Creates a new square object.

    Args:
      size: The length of one side of the square.
    """
    self.size = size

  def area(self):
    """
    Calculates the area of the square.

    Returns:
      The area of the square, in square units.
    """
    return self.size ** 2

  @property
  def size(self):
    """
    Gets the length of one side of the square.

    Returns:
      The length of one side of the square, in units.
    """
    return self.__size

  @size.setter
  def size(self, value):
    """
    Sets the length of one side of the square.

    Args:
      value: The new length of one side of the square, in units.

    Raises:
      TypeError: If the new size is not an integer.
      ValueError: If the new size is negative.
    """
    if not isinstance(value, int):
      raise TypeError("size must be an integer")
    elif value < 0:
      raise ValueError("size must be >= 0")
    else:
      self.__size = value
