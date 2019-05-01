#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        if a % 3 == 0:
            print('Fizz', end="")
        if a % 5 == 0:
            print('Buzz', end="")
        if a % 3 != 0 and a % 5 != 0:
            print('{:d}'.format(a), end='')
        print(' ', end="")
