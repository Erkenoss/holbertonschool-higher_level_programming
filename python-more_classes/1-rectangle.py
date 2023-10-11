#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Start of the class"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    """Getter of the width"""
    @property
    def width(self):
        return self.__width

    """Getter of the height"""
    @property
    def height(self):
        return self.__height

    """Setter of width"""
    @width.setter
    def width(self, value):
        self.__width = value

    """Setter of height"""
    @height.setter
    def height(self, value):
        self.__height = value
