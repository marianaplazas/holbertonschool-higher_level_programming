#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx in range(0, len(my_list)):
        cp_list = my_list[:]
        cp_list[idx] = element
        return(cp_list)
    else:
        return(my_list)
