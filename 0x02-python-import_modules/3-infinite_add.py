#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    size = len(argv) - 1
    total = 0

    for i in range(1, size + 1):
        total += int(argv[i])

    print("{}".format(total))
