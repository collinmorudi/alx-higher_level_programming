#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    size = len(argv) - 1

    if size == 1:
        print("{} argument:".format(size))
        print("{}: {}".format(1, argv[1]))
    elif size > 1:
        print("{} arguments:".format(size))

        for i in range(1, size + 1):
            print("{}: {}".format(i, argv[i]))
    else:
        print("{} arguments.".format(size))
