#!/usr/bin/python3
"""Define class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create a rectangle"""
    def __init__(self, width, height):
        """Define the start of creation of an object"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
 
    def area(self):
        """define the area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
