#!/usr/bin/python3
def subtract_func(varint_list):
    strsubtract_val = 0
    max_val = max(varint_list)

    for num in varint_list:
        if max_val > num:
            strsubtract_val += num

    return (max_val - strsubtract_val)


def roman_to_integer(varroman_str):
    if not varroman_str:
        return 0

    if not isinstance(varroman_str, str):
        return 0

    varroman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dict_keys = list(varroman_dict.keys())

    int_val = 0
    strl_roman = 0
    varint_list = [0]

    for char in varroman_str:
        for roman_num in dict_keys:
            if roman_num == char:
                if varroman_dict.get(char) <= strl_roman:
                    int_val += subtract_func(varint_list)
                    varint_list = [varroman_dict.get(char)]
                else:
                    varint_list.append(varroman_dict.get(char))

                strl_roman = varroman_dict.get(char)

    int_val += subtract_func(varint_list)

    return (int_val)
