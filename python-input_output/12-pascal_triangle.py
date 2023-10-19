#!/usr/bin/python3
"""Start of function Pascal_triangle"""


def pascal_triangle(n):
    new_list = []
    if n <= 0:
        return new_list
    index = 0
    while index < n:
        new_list.append(n)
        index += 1
    return new_list
