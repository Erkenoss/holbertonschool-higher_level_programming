#!/usr/bin/python3
"""class matrix_divided"""


def matrix_divided(matrix, div):
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        num_col = len(matrix[0])
        for col in row:
            if len(row) != num_col:
                raise TypeError("Each row of the matrix must\
                    have the same size")

    new_matrix = [[round(col / div, 2) for col in row] for row in matrix]
    return new_matrix
