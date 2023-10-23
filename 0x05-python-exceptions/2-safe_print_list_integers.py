#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    print_list_elements
    a function prints the elements of the given list
    up to a specified range.
    It handles ValueError and TypeError
    exceptions during execution.
    It returns the count of successfully printed elements.
    Parameters:
    - my_list (list): The list of elements to be printed.
    - x (int): The range up to which
    elements are to be printed from the list.
    Returns:
    - num_printed (int): The count of successfully printed elements from the list.
    """

    varindex = 0
    numprinted = 0
    varseparator = ""

    for varindex in range(0, x):
        try:
            print(f"{varseparator}{my_list[varindex]}", end="")
            varseparator = ""
            numprinted += 1
        except (ValueError, TypeError):
            continue

    print()

    return numprinted
