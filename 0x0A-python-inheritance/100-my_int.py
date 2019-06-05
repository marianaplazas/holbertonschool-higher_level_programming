#!/usr/bin/python3
"""
MyInt Class rebel class
"""


class MyInt(int):
    """ MyInt Class"""
    def __eq__(self, other):
        """ invert eq to not equal"""
        return False

    def __ne__(self, other):
        'invert not equal to eq'
        return True
