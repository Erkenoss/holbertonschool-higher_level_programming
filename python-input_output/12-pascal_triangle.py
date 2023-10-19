#!/usr/bin/python3
"""Start of function Pascal_triangle"""

def pascal_triangle(n):
    """Return a matrix with pascal triangle"""
    if n <= 0:
        return []

    pascal_matrix = []
    for i in range(n):
        row = [1]
        if pascal_matrix:
            last_row = pascal_matrix[-1]
            for j in range(len(last_row) - 1):
                row.extend([last_row[j] + last_row[j + 1]])
            row.append(1)
        pascal_matrix.append(row)

    return pascal_matrix
