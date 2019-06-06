#!/usr/bin/python3
"""
write a file
"""


def write_file(filename="", text=""):
    'this function write in a text file'
    with open(filename, mode='w', encoding='utf-8')as f:
        w = f.write(text)
    return(w)
