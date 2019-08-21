#!/usr/bin/python3
def find_peak(list_of_integers):
    """use recusrion to find a peak"""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[0] > list_of_integers[len(list_of_integers) - 1]:
        return find_peak(list_of_integers[:(len(list_of_integers) + 1)//2])
    else:
        return find_peak(list_of_integers[(len(list_of_integers))//2:])
