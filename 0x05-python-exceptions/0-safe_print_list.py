#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for a in range(x):
        try:
            if x < counter:
                print("{}".format(a), end="")
                counter += 1
        except:
                break
    print("")
    return(counter)
