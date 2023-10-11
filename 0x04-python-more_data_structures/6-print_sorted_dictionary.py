#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    strlist_ord = list(a_dictionary.keys())
    strlist_ord.sort()
    for k in strlist_ord:
        print("{}: {}".format(k, a_dictionary.get(k)))
