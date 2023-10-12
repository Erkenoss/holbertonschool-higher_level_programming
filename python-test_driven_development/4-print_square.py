#!/usr/bin/python3
"""start methode"""


def print_square(size):
    """function for print a square"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)