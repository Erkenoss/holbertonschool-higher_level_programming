#!/usr/bin/python3
"""class matrix_divided"""


# def matrix_divided(matrix, div):
#     if (not isinstance(matrix, list) or matrix == [] or
#             not all(isinstance(row, list) for row in matrix) or
#             not all((isinstance(ele, int) or isinstance(ele, float))
#                     for ele in [num for row in matrix for num in row])):
#         raise TypeError("matrix must be a matrix (list of lists) of "
#                         "integers/floats")

#     if not isinstance(div, (int, float)):
#         raise TypeError("div must be a number")
#     if div == 0:
#         raise ZeroDivisionError("division by zero")

#     # for row in matrix:
#     #     num_col = len(matrix[0])
#     #     for col in row:
#     #         if len(row) != num_col:
#     #             raise TypeError("Each row of the matrix must\
#     #                 have the same size")
#     if not all(len(row) == len(matrix[0]) for row in matrix):
#         raise TypeError("Each row of the matrix must \
#             have the same size")

#     new_matrix = [[round(col / div, 2) for col in row] for row in matrix]
#     return new_matrix

def matrix_divided(matrix, div):
    """a function that divide the member of a matrix

    returns a new matrix with the divided numbers

    raises:
        TypeError: if the matrix is not a list of lists
        TypeError: if the rows in the matrix are not the same size
        TypeError: if div is neither a float or en int
        ZeroDivisionError: if div is equal to zero
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix