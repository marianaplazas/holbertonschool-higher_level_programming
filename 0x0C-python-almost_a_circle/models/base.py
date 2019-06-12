#!/usr/bin/python3
"""
this module is for create a base class
"""


import json
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        'return JSNO'
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        'save the file'
        dict_objs = []
        filename = cls.__name__ + ".jsno"
        if list_objs is not None:
            for obj in list_objs:
                dict_objs.append(cls.to_dictionary(obj))
        json_str = Base.to_json_string(dict_objs)
        with open(filename, 'w+', encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        'returns the list of the JSON string'
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        'returns an instance with all attributes'
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = cls.__name__ + ".json"
        load = []
        try:
            with open(filename) as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                load.append(cls.create(**instances[i]))
            return(load)
        except FileNotFoundError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        'use the turtle'
         for m in list_rectangles:
            turtle.penup()
            turtle.home()
            turtle.color("yellow")
            turtle.setpos(m.x, m.y)
            turtle.pendown()
            turtle.forward(m.width)
            turtle.left(90)
            turtle.forward(m.height)
            turtle.left(90)
            turtle.forward(m.width)
            turtle.left(90)
            turtle.forward(m.height)
           
        for m in list_squares:
            turtle.penup()
            turtle.home()
            turtle.color("blue")
            turtle.setpos(m.x, m.y)
            turtle.pendown()
            turtle.forward(m.size)
            turtle.left(90)
            turtle.forward(m.size)
            turtle.right(90)
            turtle.forward(m.size)
            turtle.right(90)
            turtle.forward(m.size)
        turtle.exitonclick()
