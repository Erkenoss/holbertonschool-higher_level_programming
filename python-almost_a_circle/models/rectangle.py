#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """A class that create a rectangle.

    instances:
        width: the int value of the width of the rectancle.
        height: the int value of the height of the rectangle.
        x:
        y:
        """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def height(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @width.setter
    def width(self, value):
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value