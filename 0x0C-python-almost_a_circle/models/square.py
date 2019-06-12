#!/usr/bin/python3
"""
this module cotains the defition of a square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    ' a class that is a square'
    def __init__(self, size, x=0, y=0, id=None):
        'init with size, id, x and y'
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        'size getter'
        return self.width

    @size.setter
    def size(self, value):
        'Setter width and height'
        self.width = value
        self.height = value

    def __str__(self):
        'print str'
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, super().x, super().y, self.size))

    def update(self, *args, **kwargs):
        'update with args ad kwargs'
        if args:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                if key == 1:
                    self.size = value
                if key == 2:
                    self.x = value
                if key == 3:
                    self.y = value
            if args is None or len(args) == 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.size = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        'convert to dict'
        new_dic = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return (new_dic)
