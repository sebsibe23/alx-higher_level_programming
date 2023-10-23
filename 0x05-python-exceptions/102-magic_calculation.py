#!/usr/bin/python3
def magic_calculation(a, b):
    """
    magical_computation
        a function performs the "magical" computation on two numbers.
        It first initializes the result variable to 0.
        Then it runs the loop from 1 to 2,
        and for each iteration, if a current index is greater than a,
        it raises an exception.
        If not, it adds a integer division of a power b
        and the current index to the result.
        If an exception occurs, it simply passes
        and continues to the next line.
        Finally, it adds a and b to the
        result and returns it.
    Parameters:
        a: The first integer number.
        b: The second integer number.

    Description:


    Returns:
        The result of the computation.
    """

    var_comp_result = 0
    try:
        for index in range(1, 3):
            if index > a:
                raise Exception("Too far")
            var_comp_result += (a ** b) // index
    except Exception:
        pass
    var_comp_result += b + a
    return var_comp_result
