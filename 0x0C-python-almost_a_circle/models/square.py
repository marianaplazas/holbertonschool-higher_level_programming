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
