#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    all_div = []
    for a in range(list_length):
        try:
            div = my_list_1[a] / my_list_2[a]
        except(ZeroDivisionError):
            print("division by 0")
            div = 0
        except(IndexError):
            print("out of range")
            div = 0
        except(TypeError):
            print("wrong type")
            div = 0
        finally:
            all_div.append(div)
    return(all_div)
