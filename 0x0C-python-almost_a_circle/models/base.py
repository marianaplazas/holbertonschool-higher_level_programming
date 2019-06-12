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

    @staticmethod
    def to_json_string(list_dictionaries):
        'return JSNO'
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        'save the file'
        dic_objs = []
        filename = cls.__name__ + ".jsno"
        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(cls.to_dictionary(obj))
        json_str = Base.to_json_string(dict_list)
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
        dummy = cls(6, 6, 6)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filenamee = cls.__name__ + ".json"
        load = []
        try:
            with open(filename) as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                load.append(cls.create(**instances[i]))
            return(load)
        except FileNotFoundError:
            return ([])
