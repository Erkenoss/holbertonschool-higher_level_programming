#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (map(lambda row: list(map(lambda x: x * x, row)), matrix))
