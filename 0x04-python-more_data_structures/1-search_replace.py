#!/usr/bin/python3
def search_replace(my_list, search, replace):
    strnewlist = list(map(lambda d: replace if d == search else d, my_list))
    return (strnewlist)
