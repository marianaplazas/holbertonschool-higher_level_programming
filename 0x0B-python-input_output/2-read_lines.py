#!/usr/bin/python3
"""
this read a determinated number of lines
"""


def read_lines(filename="", nb_lines=0):
    ' Read n lines of a text file'
    counter = 0
    with open(filename, encoding='utf-8') as text:
        if nb_lines <= 0:
            print(text.read(), end='')
        for line in text:
            if counter < nb_lines:
                print(line, end='')
                counter += 1
