#!/usr/bin/python3
"""Defines the locked class."""


class LockedClass:
    """
    This class prevents the user from dynamicallycreating new instance attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
