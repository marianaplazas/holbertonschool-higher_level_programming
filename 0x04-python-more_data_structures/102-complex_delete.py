#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for look in list(a_dictionary.keys()):
        if a_dictionary[look] == value:
            a_dictionary.pop(look, None)
    return (a_dictionary)
