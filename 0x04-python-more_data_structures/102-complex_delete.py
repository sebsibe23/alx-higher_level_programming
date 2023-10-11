#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete keys in the dictionary with the specific value."""
    varkeys_to_d = [var_key for var_key, str_val in a_dictionary.items() if str_val == value]
    for var_key in varkeys_to_d:
        del a_dictionary[var_key]
    return a_dictionary
