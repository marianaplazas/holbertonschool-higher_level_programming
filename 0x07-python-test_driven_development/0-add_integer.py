#!/usr/bin/python3
"""
this function returns the sum of two integers
"""
def add_integer(a, b=98): 
    """
    the arguments are two numbers if are floats cast to an integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError ("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError ("b must be an integer")
    else:
        int_a = int(a)
        int_b = int(b)
        sum = int_a + int_b
    return(sum)
