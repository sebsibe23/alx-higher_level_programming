#!/usr/bin/python3
class LockedClass:
    """
    Class Name: LockedClass
    Attribute: 
    first_name: The only instance attribute allowed in this class.

    This class prevents the user from dynamically creating new instance attributes, 
    except if the new instance attribute is called first_name.
    """
    __slots__ = ['first_name']


