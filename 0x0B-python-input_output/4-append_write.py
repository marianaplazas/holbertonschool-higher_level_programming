#!/usr/bin/python3
"""
this function append in a txt file
"""


def append_write(filename="", text=""):
    'this function append'
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
