#!/usr/bin/python3
"""Start of class base_geometry"""


class BaseGeometry:
    """Create a object"""
    def area(self):
        """Define the area of an object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if value is correct"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

"""Define class Rectangle"""
class Rectangle(BaseGeometry):
    """create a rectangle"""
    def __init__(self, width, height):
        """Define the start of creation of an object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
