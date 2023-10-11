#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmat = matrix.copy()

    for h in range(len(matrix)):
        newmat[h] = list(map(lambda x: x**2, matrix[h]))

    return (newmat)
