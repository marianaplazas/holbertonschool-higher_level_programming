#!/usr/bin/python3
"""
subclass list
"""


class MyList(list):
    """ public method """
    def print_sorted(self):
        """ print sorted list """
        new_list = self[:]
        new_list.sort()
        print(new_list)
