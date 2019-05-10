#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newd = {}
    for a in a_dictionary.keys():
        newd[a] = (a_dictionary[a] * 2)
    return(newd)
