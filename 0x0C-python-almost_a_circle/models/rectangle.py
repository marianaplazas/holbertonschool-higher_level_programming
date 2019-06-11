#!/usr/bin/python3
"""
this module is the class rectangle
"""


from models.base import Base


class Rectangle(Base): 
    'define the rectangle class'
    def __init__(self, width, height, x=0, y=0, id=None):
        'init with width, height, x and y'
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        'return the value od width'
        return(self.__width)

    @property
    def height(self):
        'return the value of height'
        return(self.__height)
    
    @property
    def x(self):
        'rerturn the value of x'
        return(self.__x)

    @property
    def y(self):
        'return the value of y'
        return(self.__y)
    
    @width.setter
    def width(self, value):
        'setter of width'
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        'setter of height'
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        'x setter'
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__x = value

    @y.setter
    def y(self, value):
        'y setter'
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__y = value
    
    def area(self):
        'define the area of a Rectangle'
        return(self.__width * self.__height)

    def display(self):
       'print the rectangle'
       for b in range(self.__y):
           print()
        for a in range(self.__height):
                print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        'print'
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, 
            self.__width,self.__height))

    def update(self, *args, **kwargs):
        'take arguments given by the user'
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                if key == 1:
                    self.width = value
                if key == 2:
                    self.height = value
                if key == 3:
                    self.x = value
                if key == 4:
                    self.y = value
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
