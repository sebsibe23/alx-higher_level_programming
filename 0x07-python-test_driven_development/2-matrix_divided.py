#!/usr/bin/python3
"""Module for task 2 of project 0x07.
"""
def matrix_divided(matrix, div):
    """
    This function performs element-wise division of a matrix by a number.

    Parameters:
        matrix (list): A 2D list (matrix) consisting of integers or floats.
        div (int/float): The number by which each element of the matrix will be divided.

    The function validates the following:
        - The matrix is a list of lists and each element is an integer or float.
        - All rows in the matrix are of equal length.
        - The divisor is an integer or float.
        - The divisor is not zero.

    If any of these conditions are not met, the function raises an appropriate exception.

    The function returns a new matrix where each element is the result of dividing the 
    corresponding element in the original matrix by the divisor. Each element in the 
    returned matrix is rounded to 2 decimal places.

    Returns:
        list: A new 2D list (matrix) with the divided values.
    """
    if not isinstance(matrix, list) or not matrix or \
       not all(isinstance(sublist, list) for sublist in matrix) or \
       not all(isinstance(item, (int, float)) for sublist in matrix for item in sublist):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(sublist) == len(matrix[0]) for sublist in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in sublist] for sublist in matrix]



