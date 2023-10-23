#!/usr/bin/python3

def magic_calculation(a, b):
    '''
    Function Name: magic_calculation
    This function performs calculations between
    two integers 'a' and 'b'.
    It iterates over a range of 1 to 3. If the
    iterator is greater than 'a',
    it raises an exception and sets the result
    as the sum of 'a' and 'b'.
    Otherwise, it adds the result of '(a^b)/i' to the result.
    Parameters:
    a (int): The first integer input to the function.
    b (int): The second integer input to the function.
    Returns:
    varresult (float): If an error occurs, it returns the
    addition of integers 'a' and 'b'.
                    Otherwise, it returns the desired result.
    '''

    varresult = 0
    for f in range(1, 3):
        try:
            if f > a:
                raise Exception('Too far')
            else:
                varresult += a ** b / f
        except Exception:
            varresult = b + a
            break
    return (varresult)
