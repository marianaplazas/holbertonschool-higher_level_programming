#!/usr/bin/python3
"""
Rectangle
"""


class Rectangle:

    """Definition of an empty cls Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """build init"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """method area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """method perimeter"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """print square"""
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            string += "\n"
        string = string[:-1]
        return string

    def __repr__(self):
        """repr magic to square"""
        return("Rectangle ({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """delete rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare two instances"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    @classmethod
    def square(cls, size=0):
        """new instance"""
        return (cls(size, size))
