#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    This function prints x elements of the list.
    Parameters:
    my_list (list): a list to be printed. Default is an empty list.
    x (int): The number of elements to print. Default is 0.
    Returns:
    int: a real number of elements printed.
    """ 
    varcount = 0
    varo_put = ""
    for g in range(x):
        try:
            varo_put += str(my_list[g])
            varcount += 1
        except IndexError:
            break
    print(varo_put)
    return varcount
