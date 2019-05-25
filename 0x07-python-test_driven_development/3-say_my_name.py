#!/usr/bin/python3
"""
this module is the simple function say_my_name()
To test, run: `python3 -m doctest -v ./tests/3-say_my_name.txt`
"""
def say_my_name(first_name, last_name=""):
    """
    say_my_name print in screen the strings that are given like arguments
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
