#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    varlist_k = list(a_dictionary.keys())

    for val_dic in varlist_k:
        if value == a_dictionary.get(val_dic):
            del a_dictionary[val_dic]

    return (a_dictionary)
