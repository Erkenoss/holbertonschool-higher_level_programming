#!/usr/bin/python3
"""start of class Square"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """create a square with class Rectangle"""
    def __init__(self, size):
        """define a square base on Rectangle"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return size * size for have an area"""
        return self.__size * self.__size

    def __str__(self):
        """print the size of a square"""
        return f"[Square] {self.__size}/{self.__size}"
