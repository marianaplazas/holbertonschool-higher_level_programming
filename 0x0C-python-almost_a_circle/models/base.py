#!/usr/bin/python3
"""
this module is for create a base class
"""


import json


class Base:
    'this is the base class'
    __nb_objects = 0

    def __init__(self, id=None):
        'init with id'
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
