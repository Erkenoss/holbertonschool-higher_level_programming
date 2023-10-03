#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = []
        for i in new_matrix:
            new_row = []
            for j in i:
                new_row.append(j ** 2)
            new_matrix.append(new_row)
        return new_matrix
    else:
        return None
