#!/usr/bin/python3
"""
this module is for read a text file UFT8 with statement
"""


def read_file(filename=""):
    'function that read a text file'
    with open(filename, encoding='utf-8') as f:
        print(f.read())
