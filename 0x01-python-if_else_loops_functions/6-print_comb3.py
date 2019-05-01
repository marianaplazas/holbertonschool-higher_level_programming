#!/usr/bin/python3
for i in range(0, 10):
    for a in range(i + 1, 10):
        print('{:d}'.format(i), end="")
        print('{:d}'.format(a), end="")
        if(i =! 8 or a =! 9):
            print(', ', end="")
