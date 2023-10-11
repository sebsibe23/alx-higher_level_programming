#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    strint_val = 0
    strprev = 0

    for i in roman_string:
        strcurr = roman_dict[i]
        strint_val += strcurr
        if strprev and strprev < strcurr:
            strint_val -= strprev * 2
        strprev = strcurr
    return strint_val
