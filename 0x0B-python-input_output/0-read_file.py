#!/bin/bash/python3
"""
this module is for read a text file UFT8
"""


def read_file(filename=""):
    'function that read a text file'
    with open(filename, encoding='utf-8') as text:
        print(text.read())
