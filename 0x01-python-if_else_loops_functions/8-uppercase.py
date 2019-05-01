#!/usr/bin/python3
def uppercase(str):
    for c in str:
        a = ord(c)
        if c > '`' and c < '{':
            a = a - 32
        print('{}'.format(chr(a)), end="")
    print(' ')
