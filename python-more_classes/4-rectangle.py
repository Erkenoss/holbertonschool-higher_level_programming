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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    """Setter of height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """Getter of the area"""
    def area(self):
        return self.__height * self.__width

    """Setter of area"""
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        larg = self.__height * 2
        long = self.__width * 2

        return larg + long

    """print the rectangle"""
    def __str__(self):
        str_rect = ''
        if self.__height != 0 and self.__width != 0:
            for _ in range(self.__height):
                if _ == self.__height - 1:
                    str_rect += '#' * self.__width
                else:
                    str_rect += '#' * self.__width + '\n'
        return str_rect

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
