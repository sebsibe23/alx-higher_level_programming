#!/usr/bin/python3
"""Defines a function that performs the multiplication of two matrices.

Attributes:
    m_a (list of lists): The first matrix.
    m_b (list of lists): The second matrix.
"""

def matrix_mul(m_a, m_b):
    """Performs multiplication of two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists.
        TypeError: If an element of the matrices is not an integer or a float.
        ValueError: If m_a or m_b is empty.
        TypeError: If m_a or m_b is not rectangular (all rows must be of the same size).
        ValueError: If m_a and m_b can't be multiplied.

    Returns:
        list of lists: The product of the two matrices.
    """
    error_messages = {
        "lists": "{} must be a list of lists",
        "empty": "{} can't be empty",
        "type": "{} should contain only integers or floats",
        "size": "each row of {} must be of the same size",
        "value": "{} and {} can't be multiplied"
    }

    def check_matrix(matrix, name):
        if not isinstance(matrix, list):
            raise TypeError("{} must be a list".format(name))
        
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError(error_messages["lists"].format(name))
            
            for item in row:
                if not isinstance(item, (int, float)):
                    raise TypeError(error_messages["type"].format(name))
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            raise ValueError(error_messages["empty"].format(name))
        
        if len(set(len(row) for row in matrix)) > 1:
            raise TypeError(error_messages["size"].format(name))

    check_matrix(m_a, 'm_a')
    check_matrix(m_b, 'm_b')

    if len(m_a[0]) != len(m_b):
        raise ValueError(error_messages["value"].format('m_a', 'm_b'))

    new_matrix = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return new_matrix

