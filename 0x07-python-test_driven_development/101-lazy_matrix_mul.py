#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    This Python function, lazy_matrix_mul, uses the NumPy module to perform matrix multiplication.
    It includes several checks to ensure that the input matrices, m_a and m_b, are suitable for multiplication.

    1. It verifies if both m_a and m_b are lists of lists. If not, it raises a ValueError.
    2. It checks if m_a and m_b are not empty. If they are, it raises a ValueError.
    3. It ensures that each row of the matrices has the same size. If not, it raises a ValueError.

    After these checks, it attempts to perform matrix multiplication using np.matmul.
    If this operation fails due to the dimensions of the matrices being incompatible for multiplication,
    it raises a ValueError.
    """
    # Check if m_a and m_b are list of lists
    if not isinstance(m_a, list) or not all(isinstance(i, list) for i in m_a):
        raise ValueError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(i, list) for i in m_b):
        raise ValueError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if not any(m_a) or not any(m_b):
        raise ValueError("m_a and m_b can't be empty")

    # Check if each row of the matrices has the same size
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise ValueError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")

