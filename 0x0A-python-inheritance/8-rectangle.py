#!/usr/bin/python3
"""
rectangle with import
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ definition of a Rectangle """
    def __init__(self, width, height):
        """ width and height """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
