#!/usr/bin/python3
"""
this module contains the function text_identitation
"""
def text_indentation(text):
    """
    separate a text 
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")
    text = text.replace("?", "?\n\n")
    text = text.split("\n")
    print('\n\n'.join(t.strip()
