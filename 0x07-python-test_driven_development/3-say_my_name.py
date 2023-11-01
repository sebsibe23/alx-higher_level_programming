#!/usr/bin/python3
"""Module for task 3 of project 0x07.
"""
def say_my_name(first_name: str, last_name: str = "") -> None:
  """Prints a name of a person to the console.

  Args:
    first_name: The first name of the person.
    last_name: The last name of a person (optional).
  """

  if not isinstance(first_name, str):
    raise TypeError("first_name must be a string")

  if not isinstance(last_name, str):
    raise TypeError("last_name must be a string")

  print(f"My name is {first_name} {last_name}")
