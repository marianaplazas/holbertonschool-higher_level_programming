#!/usr/bin/python3
"""
this function count the number of lines
"""


def number_of_lines(filename=""):
    'count the lines of the txt'
    counter = 0
    with open(filename, encoding='utf-8') as text:
        for line in text:
            counter += 1
        return(counter)
