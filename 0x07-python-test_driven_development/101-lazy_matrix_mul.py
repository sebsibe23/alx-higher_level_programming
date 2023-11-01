#!/usr/bin/python3
"""Defines the function that multiplies 2 matrices by using the module NumPy.

Attributes:
    m_a (matrix)
    m_b (matrix)
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies the two matrices using numpy

    Args:
        m_a (matrix): first matrix
        m_b (matrix): second matrix

    Returns:
        matrix: a product of the two matrices.
    """
    # m_a = ([1, 2], [3, 4])
    # m_b = [[1, 2], [3, 4]]
    return np.matmul(m_a, m_b)
