#!/usr/bin/python3
"""
Rectangle
"""


class Rectangle:

    """Definition of an empty cls Rectangle"""

    def __init__(self, width=0, height=0):
        """build init"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get width"""
        return(self.__width)

    @property
    def height(self):
        """gets height"""
        return(self.__height)

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
