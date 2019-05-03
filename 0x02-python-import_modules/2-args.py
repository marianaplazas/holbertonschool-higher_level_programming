#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count_ar = len(sys.argv)
    if count_ar == 1:
        print("{:d} argument.".format(count_ar - 1))
    else:
        print("{:d} arguments:".format(count_ar - 1))
    for a in range(0, count_ar):
        if a == 0:
            continue
        print("{:d}: {:s}".format(a, sys.argv[a]))
