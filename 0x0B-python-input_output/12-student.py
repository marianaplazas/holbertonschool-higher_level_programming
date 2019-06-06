#!/usr/bin/python3
"""
class Student
"""


class Student:
    'class student'
    def __init__(self, first_name, last_name, age):
        'define student'
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return (self.__dict__)
        else:
            dict_keys = {}
            for item in attrs:
                if hasattr(self, item):
                    dict_keys[item] = getattr(self, item)
            return (dict_keys)
