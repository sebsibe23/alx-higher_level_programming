#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    divide_list_elements
    a function takes two lists and creates a new list
    with the result of the division operation
    for each pair of elements.
    It handles TypeErrors, ZeroDivisionErrors,
    and IndexErrors, and prints the corresponding error message to stdout.
    - my_list_1 (list): a first list of numbers.
    - my_list_2 (list): a second list of numbers.
    - list_length (int): a number of elements to consider from the lists.
    Returns:
    - res_list (list): return the  list containing the result of
    the division operation for each pair of elements.
    """
    varindex = 0
    varres_list = []
    vartemp_result = 0
    error_message = ""

    for varindex in range(0, list_length):
        try:
            vartemp_result = (my_list_1[varindex] / my_list_2[varindex])
        except TypeError:
            vartemp_result = 0
            error_message = "wrong type"
        except ZeroDivisionError:
            vartemp_result = 0
            error_message = "division by 0"
        except IndexError:
            vartemp_result = 0
            error_message = "out of range"
        finally:
            if error_message != "":
                print(error_message)
                error_message = ""
            varres_list.append(vartemp_result)

    return varres_list
