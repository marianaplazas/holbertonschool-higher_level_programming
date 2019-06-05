#!/usr/bin/python3
"""
chechk if is the class
"""


def inherits_from(obj, a_class):
    """ Return True or flase"""
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
