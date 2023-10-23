#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """start of class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init of Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """getter of the width"""
    @property
    def width(self):
        return self.__width

    """Getter of the height"""
    @property
    def height(self):
        return self.__height

    """getter of the x"""
    @property
    def width(self):
        return self.__x

    """Getter of the y"""
    @property
    def height(self):
        return self.__y

    """Setter of width"""
    @width.setter
    def width(self, value):
        self.__width = value

    """Setter of height"""
    @height.setter
    def height(self, value):
        self.__height = value

    """Setter of x"""
    @x.setter
    def x(self, value):
        self.__x = value

    """Setter of y"""
    @y.setter
    def y(self, value):
        self.__y = value
