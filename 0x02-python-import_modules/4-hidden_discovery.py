#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    name = dir(hidden_4)
    for a in name:
        if a[0] != '_':
            print("{}".format(a))
