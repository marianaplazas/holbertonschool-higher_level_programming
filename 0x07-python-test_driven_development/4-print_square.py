#!/usr/bin/python3
"""
function that print square
"""
def print_square(size):
    """
    argument is the size
    """
    if type(size) is not int:
        raise TypeError ("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError ("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
