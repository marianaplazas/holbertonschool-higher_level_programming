#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ln = abs(number) % 10
l = "the last digitf of"
if number < 0:
    ln = ln * -1
if ln > 5:
    print("{:s} {:d} is {:d} and is greater than 5".format(l, number, ln))
elif ln < 6 and ln != 0:
        print("{} {} is {} and is less than 6 and not 0".format(l, number, ln))
else:
    print("{:s} {:d} is {:d} and is zero".format(l, number, ln))
