#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    counter = 0
    all_ar = len(sys.argv)
    for a in range (1, all_ar):
        counter = int(sys.argv[a]) + counter
    print('{:d}'.format(counter))
