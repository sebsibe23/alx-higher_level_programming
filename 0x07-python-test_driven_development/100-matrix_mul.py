#!/usr/bin/python3

def matrix_mul(mat_a, mat_b):
    """
    Multiplies two matrices.

    Parameters:
    mat_a (list of list of int/float): The first matrix.
    mat_b (list of list of int/float): The second matrix.

    Returns:
    list of list of int/float: The product of the two matrices.

    This function takes two matrices, mat_a and mat_b, as input and returns their product.
    Both matrices should be non-empty and contain only integers or floats. Each row in each matrix should be of the same size.
    The number of columns in the first matrix should be equal to the number of rows in the second matrix.
    If these conditions are not met, the function raises an appropriate error.
    """

    # Check if mat_a and mat_b are lists
    if not isinstance(mat_a, list):
        raise TypeError("mat_a must be a list")
    if not isinstance(mat_b, list):
        raise TypeError("mat_b must be a list")

    # Check if mat_a and mat_b are lists of lists
    if not all(isinstance(row, list) for row in mat_a):
        raise TypeError("mat_a must be a list of lists")
    if not all(isinstance(row, list) for row in mat_b):
        raise TypeError("mat_b must be a list of lists")

    # Check if mat_a and mat_b are not empty
    if mat_a == [] or mat_a == [[]]:
        raise ValueError("mat_a can't be empty")
    if mat_b == [] or mat_b == [[]]:
        raise ValueError("mat_b can't be empty")

    # Check if all elements in the matrices are integers or floats
    if not all(isinstance(element, (int, float)) for row in mat_a for element in row):
        raise TypeError("mat_a should contain only integers or floats")
    if not all(isinstance(element, (int, float)) for row in mat_b for element in row):
        raise TypeError("mat_b should contain only integers or floats")

    # Check if all rows in each matrix are of the same size
    if not len(set(len(row) for row in mat_a)) <= 1:
        raise TypeError("each row of mat_a must be of the same size")
    if not len(set(len(row) for row in mat_b)) <= 1:
        raise TypeError("each row of mat_b must be of the same size")

    # Check if the number of columns in the first matrix is equal to the number of rows in the second matrix
    if len(mat_a[0]) != len(mat_b):
        raise ValueError("mat_a and mat_b can't be multiplied")

    # Perform matrix multiplication
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*mat_b)] for row_a in mat_a]

